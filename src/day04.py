import grid
import sys
from typing import Self

class Floor(grid.Grid):
    def is_accessible(self: Self, pos: grid.Position) -> bool:
        return self.count_adj_rolls(pos) < 4

    def count_adj_rolls(self: Self, pos: grid.Position) -> int:
        return len([n for n in self.neighbors(pos, diagonal=True) if floor.get(n) == '@'])

    def count_accessible(self: Self) -> int:
        return sum(1 if self.is_accessible(p) else 0 for p in self.find('@'))

    def remove_accessible_rolls(self) -> int:
        count = 0
        for p in self.find('@'):
            if self.is_accessible(p):
                self.set(p, '.')
                count += 1
        return count

floor = Floor(sys.stdin.read().strip())

print(floor.count_accessible())
count_removed = 0
while True:
    removed = floor.remove_accessible_rolls()
    if removed == 0:
        break
    count_removed += removed
print(count_removed)
