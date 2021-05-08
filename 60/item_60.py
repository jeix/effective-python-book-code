########################################
import logging
########################################
# from 56

ALIVE = '*'
EMPTY = '-'
########################################
#from 56

class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)

    def get(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def set(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state

    def __str__(self):
        output = ''
        for row in self.rows:
            for cell in row:
                output += cell
            output += '\n'
        return output
########################################
# from 56

def count_neighbors(y, x, get):
    n_ = get(y - 1, x + 0)  # North
    ne = get(y - 1, x + 1)  # Northeast
    e_ = get(y + 0, x + 1)  # East
    se = get(y + 1, x + 1)  # Southeast
    s_ = get(y + 1, x + 0)  # South
    sw = get(y + 1, x - 1)  # Southwest
    w_ = get(y + 0, x - 1)  # West
    nw = get(y - 1, x - 1)  # Northwest
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count
########################################
async def game_logic(state, neighbors):
    # Do some input/output in here:
    data = await my_socket.read(50)

# from 56 (async)

async def game_logic(state, neighbors):
    # Do some input/output in here:
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY     # Die: Too few
        elif neighbors > 3:
            return EMPTY     # Die: Too many
    else:
        if neighbors == 3:
            return ALIVE     # Regenerate
    return state
########################################
# from 56 (async, await)

async def step_cell(y, x, get, set):
    state = get(y, x)
    neighbors = count_neighbors(y, x, get)
    next_state = await game_logic(state, neighbors)
    set(y, x, next_state)
########################################
import asyncio
########################################
async def simulate(grid):
    next_grid = Grid(grid.height, grid.width)

    tasks = []
    for y in range(grid.height):
        for x in range(grid.width):
            task = step_cell(
                y, x, grid.get, next_grid.set)      # Fan out
            tasks.append(task)

    await asyncio.gather(*tasks)                    # Fan in

    return next_grid
########################################
# from 56

class ColumnPrinter:
    def __init__(self):
        self.columns = []

    def append(self, data):
        self.columns.append(data)

    def __str__(self):
        row_count = 1
        for data in self.columns:
            row_count = max(
                row_count, len(data.splitlines()) + 1)

        rows = [''] * row_count
        for j in range(row_count):
            for i, data in enumerate(self.columns):
                line = data.splitlines()[max(0, j - 1)]
                if j == 0:
                    padding = ' ' * (len(line) // 2)
                    rows[j] += padding + str(i) + padding
                else:
                    rows[j] += line

                if (i + 1) < len(self.columns):
                    rows[j] += ' | '

        return '\n'.join(rows)
########################################
logging.getLogger().setLevel(logging.ERROR)

grid = Grid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)

columns = ColumnPrinter()
for i in range(5):
    columns.append(str(grid))
    grid = asyncio.run(simulate(grid))   # Run the event loop

print(columns)

logging.getLogger().setLevel(logging.DEBUG)

#     0     |     1     |     2     |     3     |     4
# ---*----- | --------- | --------- | --------- | ---------
# ----*---- | --*-*---- | ----*---- | ---*----- | ----*----
# --***---- | ---**---- | --*-*---- | ----**--- | -----*---
# --------- | ---*----- | ---**---- | ---**---- | ---***---
# --------- | --------- | --------- | --------- | ---------
########################################
try:
    async def game_logic(state, neighbors):
        raise OSError('Problem with I/O')
    
    logging.getLogger().setLevel(logging.ERROR)
    
    asyncio.run(game_logic(ALIVE, 3))
    
    logging.getLogger().setLevel(logging.DEBUG)
except:
    logging.exception('Expected')
else:
    assert False

# ERROR:root:Expected
# Traceback (most recent call last):
#   File "item_60.py", line 147, in <module>
#     asyncio.run(game_logic(ALIVE, 3))
#   File "/usr/local/lib/python3.8/asyncio/runners.py", line 44, in run
#     return loop.run_until_complete(main)
#   File "/usr/local/lib/python3.8/asyncio/base_events.py", line 616, in run_until_complete
#     return future.result()
#   File "item_60.py", line 143, in game_logic
#     raise OSError('Problem with I/O')
# OSError: Problem with I/O
########################################
# restore

async def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY     # Die: Too few
        elif neighbors > 3:
            return EMPTY     # Die: Too many
    else:
        if neighbors == 3:
            return ALIVE     # Regenerate
    return state
########################################
# from 56 (async)

async def count_neighbors(y, x, get):
    n_ = get(y - 1, x + 0)  # North
    ne = get(y - 1, x + 1)  # Northeast
    e_ = get(y + 0, x + 1)  # East
    se = get(y + 1, x + 1)  # Southeast
    s_ = get(y + 1, x + 0)  # South
    sw = get(y + 1, x - 1)  # Southwest
    w_ = get(y + 0, x - 1)  # West
    nw = get(y - 1, x - 1)  # Northwest
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count
########################################
# from 56 (async, await)

async def step_cell(y, x, get, set):
    state = get(y, x)
    neighbors = await count_neighbors(y, x, get)
    next_state = await game_logic(state, neighbors)
    set(y, x, next_state)
########################################
logging.getLogger().setLevel(logging.ERROR)

grid = Grid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)

columns = ColumnPrinter()
for i in range(5):
    columns.append(str(grid))
    grid = asyncio.run(simulate(grid))

print(columns)

logging.getLogger().setLevel(logging.DEBUG)

#     0     |     1     |     2     |     3     |     4
# ---*----- | --------- | --------- | --------- | ---------
# ----*---- | --*-*---- | ----*---- | ---*----- | ----*----
# --***---- | ---**---- | --*-*---- | ----**--- | -----*---
# --------- | ---*----- | ---**---- | ---**---- | ---***---
# --------- | --------- | --------- | --------- | ---------
########################################
