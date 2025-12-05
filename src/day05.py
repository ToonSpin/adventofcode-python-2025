import itertools
import sys

def remove_overlap(im: list[tuple[int, bool]]) -> list[tuple[int, bool]]:
    counter = 0
    result: list[tuple[int, bool]] = [(0, False)]
    for id, fresh in im:
        if fresh:
            if counter == 0:
                result.append((id, True))
            counter += 1
        else:
            counter -= 1
            if counter == 0:
                result.append((id, False))
    return result

class IngredientMap:
    def __init__(self, ranges: list[tuple[int, int]]) -> None:
        im: list[tuple[int, bool]] = []
        for left, right in ranges:
            im.append((left, True))
            im.append((right + 1, False))
        im.sort()

        self.ingredient_map = remove_overlap(im)

    def is_fresh(self, ingredient: int) -> bool:
        is_it_fresh = False
        for id_found, fresh in self.ingredient_map:
            if id_found > ingredient:
                break
            is_it_fresh = fresh
        return is_it_fresh

    def count_fresh_ingredients(self) -> int:
        count = 0
        for left, right in itertools.pairwise(self.ingredient_map):
            if left[1] == True and right[1] == False:
                count += right[0] - left[0]
        return count

input = sys.stdin.read().strip()

ranges_raw, ids_raw = input.split('\n\n')
ranges: list[tuple[int, int]] = []
for line in ranges_raw.splitlines():
    l, r = line.split('-')
    ranges.append((int(l), int(r)))
ids = list(map(int, ids_raw.splitlines()))

m = IngredientMap(ranges)

print(sum(1 for id in ids if m.is_fresh(id)))
print(m.count_fresh_ingredients())
