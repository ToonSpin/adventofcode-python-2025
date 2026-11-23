import itertools
import sys

type Pt = tuple[int, int]

def area(p: Pt, q: Pt) -> int:
    return (abs(p[0] - q[0]) + 1) * (abs(p[1] - q[1]) + 1)

input = map(lambda l: l.split(','), sys.stdin.read().strip().splitlines())
tiles: list[Pt] = list(map(lambda l: tuple(map(int, l)), input)) # type: ignore
# print(max(map(area, itertools.combinations(tiles, 2))))

edges_h: set[Pt] = set()
edges_v: set[Pt] = set()

for t, u in itertools.pairwise(tiles + [tiles[0]]):
    tx, ty = t
    ux, uy = u

    if ty == uy:
        for x in range(min(tx, ux) + 1, max(tx, ux)):
            edges_h.add((x, ty))
    else:
        for y in range(min(ty, uy) + 1, max(ty, uy)):
            edges_v.add((tx, y))

def min_max(t: Pt, u: Pt) -> tuple[Pt, Pt]:
    tx, ty = t
    ux, uy = u
    p = (min(tx, ux), min(ty, uy))
    q = (max(tx, ux), max(ty, uy))

    return (p, q)

def valid_part_two(p: Pt, q: Pt) -> bool:
    p, q = min_max(p, q)
    x1, y1 = p
    x2, y2 = q
    if any((x, y) in edges_v for x in range(x1+1,x2) for y in [y1, y2]):
        return False
    if any((x, y) in edges_h for x in [x1, x2] for y in range(y1+1,y2)):
        return False
    return True


areas_part_one: list[int] = []
areas_part_two: list[int] = []
for t, u in itertools.combinations(tiles, 2):
    areas_part_one.append(area(t, u))
    if valid_part_two(t, u):
        areas_part_two.append(area(t, u))

# print(valid_part_two((9, 5), (2, 3)))
# print(valid_part_two((7, 1), (2, 3)))

print(max(areas_part_one))
print(max(areas_part_two))

# import grid
# g = grid.Grid((('.' * 15) + '\n') * 15)
# for x, y in tiles:
#     g.set(grid.Position(x, y), '#')
# for x, y in edges_h:
#     g.set(grid.Position(x, y), '-')
# for x, y in edges_v:
#     g.set(grid.Position(x, y), '|')

# print(g)
