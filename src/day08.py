import functools
import heapq
import itertools
import sys

type JunctionBox = tuple[int, int, int]
type CircuitSet = list[set[int]]

def distance(p: JunctionBox, q: JunctionBox) -> int:
    x, y, z = p
    m, n, o = q
    return (x - m) * (x - m) + (y - n) * (y - n) + (z - o) * (z - o)

def add_edge(cs: CircuitSet, i: int, j: int) -> CircuitSet:
    i_index = None
    j_index = None

    for set_index, s in enumerate(cs):
        if i in s:
            i_index = set_index
        if j in s:
            j_index = set_index
        if i_index is not None and j_index is not None:
            break

    if i_index is not None and j_index is not None:
        if i_index == j_index:
            return cs

        s = cs[j_index]
        cs[i_index] |= s
        cs = cs[:j_index] + cs[j_index + 1:]
        return cs

    if i_index is None and j_index is None:
        cs.append(set([i, j]))
        return cs

    if j_index is None:
        cs[i_index].add(j) # pyright: ignore
    else:
        cs[j_index].add(i)

    return cs

raw_input = sys.stdin.read().strip().splitlines()
input: list[JunctionBox] = list(map(lambda s: tuple(map(int, s.split(','))), raw_input)) # pyright: ignore[reportAssignmentType]
edge_count = 10 if len(input) < 100 else 1000

cs: CircuitSet = []

distances: list[tuple[int, int, int]] = []
for (i, p), (j, q) in itertools.combinations(enumerate(input), 2):
    distances.append((distance(p, q), i, j))
heapq.heapify(distances)

for counter in itertools.count(1):
    d, i, j = heapq.heappop(distances)

    cs = add_edge(cs, i, j)

    if counter == edge_count:
        sizes = sorted([len(s) for s in cs])
        print(functools.reduce(lambda a, b: a * b, sizes[-3:], 1))

    if len(cs) == 1 and len(cs[0]) == len(input):
        print(input[i][0] * input[j][0])
        break
