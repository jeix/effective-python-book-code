# page 161

# python3 -m mypy item_24_ex_09.py

from datetime import datetime
from time import sleep
from typing import Optional

def log_typed(message: str,
              when: Optional[datetime]=None) -> None:
    """Log a message with a timestamp.
    Args:
        message: Message to print.
        when: datetime of when the message occurred.
            Defaults to the present time.
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')

log_typed('Hi there!')
sleep(0.1)
log_typed('Hello again!')

# 
