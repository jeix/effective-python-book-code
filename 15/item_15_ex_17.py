# page 115-116

# python3 -m mypy item_15_ex_17.py

from typing import Dict, MutableMapping

def populate_ranks(votes: Dict[str, int],
                   ranks: Dict[str, int]) -> None:
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i

def get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))

from typing import Iterator, MutableMapping

class SortedDict(MutableMapping[str, int]):
    def __init__(self) -> None:
        self.data: Dict[str, int] = {}

    def __getitem__(self, key: str) -> int:
        return self.data[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.data[key] = value

    def __delitem__(self, key: str) -> None:
        del self.data[key]

    def __iter__(self) -> Iterator[str]:
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self) -> int:
        return len(self.data)

votes = {
    'otter': 1281,
    'polar bear': 587,
    'fox': 863,
}

sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)

# item_15_ex_17.py:10: error: Argument "key" to "sort" of "list" has incompatible type overloaded function; expected "Callable[[str], _SupportsLessThan]"
# item_15_ex_17.py:48: error: Argument 2 to "populate_ranks" has incompatible type "SortedDict"; expected "Dict[str, int]"
# item_15_ex_17.py:50: error: Argument 1 to "get_winner" has incompatible type "SortedDict"; expected "Dict[str, int]"
# Found 3 errors in 1 file (checked 1 source file)
