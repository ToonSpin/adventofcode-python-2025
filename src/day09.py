import itertools
import sys

type Pt = tuple[int, int]
type Edge = tuple[Pt, Pt]

def area(p: Pt, q: Pt) -> int:
    return (abs(p[0] - q[0]) + 1) * (abs(p[1] - q[1]) + 1)

def hor(edge: Edge) -> bool:
    return edge[0][1] == edge[1][1]

def ver(edge: Edge) -> bool:
    return not hor(edge)

def sort_edge(edge: Edge) -> Edge:
    p = (min(edge[0][0], edge[1][0]), min(edge[0][1], edge[1][1]))
    q = (max(edge[0][0], edge[1][0]), max(edge[0][1], edge[1][1]))
    return (p, q)

def valid_part_two(a: Pt, b: Pt, edges: list[Edge]) -> bool:
    if a[0] == b[0] or a[1] == b[1]:
        return True

    min_x = min(a[0], b[0])
    max_x = max(a[0], b[0])
    min_y = min(a[1], b[1])
    max_y = max(a[1], b[1])

    for p, q in filter(lambda e: hor(e) and min_y < e[0][1] < max_y, edges):
        if p[0] >= max_x: continue
        if q[0] <= min_x: continue
        return False

    for p, q in filter(lambda e: ver(e) and min_x < e[0][0] < max_x, edges):
        if p[1] >= max_y: continue
        if q[1] <= min_y: continue
        return False

    return True

input = map(lambda l: l.split(','), sys.stdin.read().strip().splitlines())
tiles: list[Pt] = list(map(lambda l: tuple(map(int, l)), input)) # type: ignore
edges: list[Edge] = list(map(sort_edge, itertools.pairwise(tiles))) + [(tiles[-1], tiles[0])]

areas_part_one: list[int] = []
max_area_part_two = 0

for t, u in itertools.combinations(tiles, 2):
    areas_part_one.append(area(t, u))
    if area(t, u) > max_area_part_two and valid_part_two(t, u, edges):
        max_area_part_two = area(t, u)

print(max(areas_part_one))
print(max_area_part_two)
