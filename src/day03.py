import heapq
import functools
import sys

COUNT = 12

def joltage_from_iterable(t) -> int:
    return functools.reduce(lambda a, b: a * 10 + b, t, 0)

def get_max_combination(l: list[int], n: int) -> list[int]:
    queue = [tuple([[], [-i for i in l], n])]

    while len(queue) > 0:
        partial, ll, nn = heapq.heappop(queue)

        if nn == 0:
            return [-i for i in partial]

        for i, e in enumerate(ll):
            if nn < len(ll) - 1:
                if e > min(ll[:-nn]):
                    continue
            heapq.heappush(queue, tuple([partial[:] + [e], ll[i+1:], nn - 1]))

    raise Exception('queue ran out!')

total = 0
perf_comb = 0
perf_max = 0
for line in sys.stdin.read().strip().splitlines():
    bank = [int(c) for c in line]
    total += joltage_from_iterable(get_max_combination(bank, COUNT))

print(total)
