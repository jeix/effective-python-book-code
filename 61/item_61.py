########################################
import logging
########################################
class EOFError(Exception):
    pass
########################################
class ConnectionBase:
    def __init__(self, connection):
        self.connection = connection
        self.file = connection.makefile('rb')

    def send(self, command):
        line = command + '\n'
        data = line.encode()
        self.connection.send(data)

    def receive(self):
        line = self.file.readline()
        if not line:
            raise EOFError('Connection closed')
        return line[:-1].decode()
########################################
import random
########################################
WARMER = 'Warmer'
COLDER = 'Colder'
UNSURE = 'Unsure'
CORRECT = 'Correct'
########################################
class UnknownCommandError(Exception):
    pass
########################################
class Session(ConnectionBase):
    def __init__(self, *args):
        super().__init__(*args)
        self._clear_state(None, None)

    def _clear_state(self, lower, upper):
        self.lower = lower
        self.upper = upper
        self.secret = None
        self.guesses = []

    def loop(self):
        while command := self.receive():
            parts = command.split(' ')
            if parts[0] == 'PARAMS':
                self.set_params(parts)
            elif parts[0] == 'NUMBER':
                self.send_number()
            elif parts[0] == 'REPORT':
                self.receive_report(parts)
            else:
                raise UnknownCommandError(command)

    def set_params(self, parts):
        assert len(parts) == 3
        lower = int(parts[1])
        upper = int(parts[2])
        self._clear_state(lower, upper)

    def next_guess(self):
        if self.secret is not None:
            return self.secret

        while True:
            guess = random.randint(self.lower, self.upper)
            if guess not in self.guesses:
                return guess

    def send_number(self):
        guess = self.next_guess()
        self.guesses.append(guess)
        self.send(format(guess))

    def receive_report(self, parts):
        assert len(parts) == 2
        decision = parts[1]

        last = self.guesses[-1]
        if decision == CORRECT:
            self.secret = last

        print(f'Server: {last} is {decision}')
########################################
import contextlib
########################################
import math
########################################
class Client(ConnectionBase):
    def __init__(self, *args):
        super().__init__(*args)
        self._clear_state()

    def _clear_state(self):
        self.secret = None
        self.last_distance = None

    @contextlib.contextmanager
    def session(self, lower, upper, secret):
        print(f'Guess a number between {lower} and {upper}!'
              f' Shhhhh, it\'s {secret}.')
        self.secret = secret
        self.send(f'PARAMS {lower} {upper}')
        try:
            yield
        finally:
            self._clear_state()
            self.send('PARAMS 0 -1')

    def request_numbers(self, count):
        for _ in range(count):
            self.send('NUMBER')
            data = self.receive()
            yield int(data)
            if self.last_distance == 0:
                return

    def report_outcome(self, number):
        new_distance = math.fabs(number - self.secret)
        decision = UNSURE

        if new_distance == 0:
            decision = CORRECT
        elif self.last_distance is None:
            pass
        elif new_distance < self.last_distance:
            decision = WARMER
        elif new_distance > self.last_distance:
            decision = COLDER

        self.last_distance = new_distance

        self.send(f'REPORT {decision}')
        return decision
########################################
import socket
########################################
from threading import Thread
########################################
def handle_connection(connection):
    with connection:
        session = Session(connection)
        try:
            session.loop()
        except EOFError:
            pass
########################################
def run_server(address):
    with socket.socket() as listener:
        # Allow the port to be reused
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind(address)
        listener.listen()
        while True:
            connection, _ = listener.accept()
            thread = Thread(target=handle_connection,
                            args=(connection,),
                            daemon=True)
            thread.start()
########################################
def run_client(address):
    with socket.create_connection(address) as connection:
        client = Client(connection)

        with client.session(1, 5, 3):
            results = [(x, client.report_outcome(x))
                       for x in client.request_numbers(5)]

        with client.session(10, 15, 12):
            for number in client.request_numbers(5):
                outcome = client.report_outcome(number)
                results.append((number, outcome))

    return results
########################################
def main():
    address = ('127.0.0.1', 1234)
    server_thread = Thread(
        target=run_server, args=(address,), daemon=True)
    server_thread.start()

    results = run_client(address)
    for number, outcome in results:
        print(f'Client: {number} is {outcome}')

main()

# Guess a number between 1 and 5! Shhhhh, it's 3.
# Server: 2 is Unsure
# Server: 4 is Unsure
# Server: 3 is Correct
# Guess a number between 10 and 15! Shhhhh, it's 12.
# Server: 10 is Unsure
# Server: 14 is Unsure
# Server: 12 is Correct
# Client: 2 is Unsure
# Client: 4 is Unsure
# Client: 3 is Correct
# Client: 10 is Unsure
# Client: 14 is Unsure
# Client: 12 is Correct
########################################
class AsyncConnectionBase:
    def __init__(self, reader, writer):             # Changed
        self.reader = reader                        # Changed
        self.writer = writer                        # Changed

    async def send(self, command):
        line = command + '\n'
        data = line.encode()
        self.writer.write(data)                     # Changed
        await self.writer.drain()                   # Changed

    async def receive(self):
        line = await self.reader.readline()         # Changed
        if not line:
            raise EOFError('Connection closed')
        return line[:-1].decode()
########################################
class AsyncSession(AsyncConnectionBase):            # Changed
    def __init__(self, *args):
        super().__init__(*args)
        self._clear_values(None, None)

    def _clear_values(self, lower, upper):
        self.lower = lower
        self.upper = upper
        self.secret = None
        self.guesses = []

    async def loop(self):                           # Changed
        while command := await self.receive():      # Changed
            parts = command.split(' ')
            if parts[0] == 'PARAMS':
                self.set_params(parts)
            elif parts[0] == 'NUMBER':
                await self.send_number()            # Changed
            elif parts[0] == 'REPORT':
                self.receive_report(parts)
            else:
                raise UnknownCommandError(command)

    def set_params(self, parts):
        assert len(parts) == 3
        lower = int(parts[1])
        upper = int(parts[2])
        self._clear_values(lower, upper)

    def next_guess(self):
        if self.secret is not None:
            return self.secret

        while True:
            guess = random.randint(self.lower, self.upper)
            if guess not in self.guesses:
                return guess

    async def send_number(self):                    # Changed
        guess = self.next_guess()
        self.guesses.append(guess)
        await self.send(format(guess))              # Changed

    def receive_report(self, parts):
        assert len(parts) == 2
        decision = parts[1]

        last = self.guesses[-1]
        if decision == CORRECT:
            self.secret = last

        print(f'Server: {last} is {decision}')
########################################
class AsyncClient(AsyncConnectionBase):             # Changed
    def __init__(self, *args):
        super().__init__(*args)
        self._clear_state()

    def _clear_state(self):
        self.secret = None
        self.last_distance = None

    @contextlib.asynccontextmanager                 # Changed
    async def session(self, lower, upper, secret):  # Changed
        print(f'Guess a number between {lower} and {upper}!'
              f' Shhhhh, it\'s {secret}.')
        self.secret = secret
        await self.send(f'PARAMS {lower} {upper}')  # Changed
        try:
            yield
        finally:
            self._clear_state()
            await self.send('PARAMS 0 -1')          # Changed

    async def request_numbers(self, count):         # Changed
        for _ in range(count):
            await self.send('NUMBER')               # Changed
            data = await self.receive()             # Changed
            yield int(data)
            if self.last_distance == 0:
                return

    async def report_outcome(self, number):         # Changed
        new_distance = math.fabs(number - self.secret)
        decision = UNSURE

        if new_distance == 0:
            decision = CORRECT
        elif self.last_distance is None:
            pass
        elif new_distance < self.last_distance:
            decision = WARMER
        elif new_distance > self.last_distance:
            decision = COLDER

        self.last_distance = new_distance

        await self.send(f'REPORT {decision}')       # Changed
        # Make it so the output printing is in
        # the same order as the threaded version.
        await asyncio.sleep(0.01)
        return decision
########################################
import asyncio
########################################
async def handle_async_connection(reader, writer):
    session = AsyncSession(reader, writer)
    try:
        await session.loop()
    except EOFError:
        pass
########################################
async def run_async_server(address):
    server = await asyncio.start_server(
        handle_async_connection, *address)
    async with server:
        await server.serve_forever()
########################################
async def run_async_client(address):
    # Wait for the server to listen before trying to connect
    await asyncio.sleep(0.1)

    streams = await asyncio.open_connection(*address)   # New
    client = AsyncClient(*streams)                      # New

    async with client.session(1, 5, 3):
        results = [(x, await client.report_outcome(x))
                   async for x in client.request_numbers(5)]

    async with client.session(10, 15, 12):
        async for number in client.request_numbers(5):
            outcome = await client.report_outcome(number)
            results.append((number, outcome))

    _, writer = streams                                 # New
    writer.close()                                      # New
    await writer.wait_closed()                          # New

    return results
########################################
async def main_async():
    address = ('127.0.0.1', 4321)

    server = run_async_server(address)
    asyncio.create_task(server)

    results = await run_async_client(address)
    for number, outcome in results:
        print(f'Client: {number} is {outcome}')

logging.getLogger().setLevel(logging.ERROR)

asyncio.run(main_async())

logging.getLogger().setLevel(logging.DEBUG)

# Guess a number between 1 and 5! Shhhhh, it's 3.
# Server: 3 is Correct
# Guess a number between 10 and 15! Shhhhh, it's 12.
# Server: 11 is Unsure
# Server: 14 is Colder
# Server: 10 is Unsure
# Server: 15 is Colder
# Server: 12 is Correct
# Client: 3 is Correct
# Client: 11 is Unsure
# Client: 14 is Colder
# Client: 10 is Unsure
# Client: 15 is Colder
# Client: 12 is Correct
########################################
