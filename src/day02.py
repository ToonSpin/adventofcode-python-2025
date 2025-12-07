from collections.abc import Iterable, Callable
import sys


type Factor = tuple[int, int, int]
type FactorFunc = Callable[[int], Iterable[Factor]]


def factors_part_one(max_value: int) -> Iterable[Factor]:
    factor = 11
    while factor <= max_value:
        yield (factor, factor * (factor - 1) // 10, factor * (factor - 2))
        factor = factor * 10 - 9

def factors_part_two(max_value: int) -> Iterable[Factor]:
    repdigit = 11
    while repdigit <= max_value:
        yield (repdigit, repdigit, repdigit * 9)
        repdigit = repdigit * 10 + 1
    p = 1
    while 10 ** (p + 5) <= max_value:
        q = 1
        while True:
            factor = ('1' + p * '0') * q + '1'
            minv = ('1' + p * '0') * (q + 1)
            maxv = ('9' * (p + 1)) * (q + 1)
            yield(int(factor), int(minv), int(maxv))
            q += 1
            if int(minv) > max_value:
                break
        p += 1

def part(max_value: int, gen_func: FactorFunc) -> int:
    found: set[int] = set()

    for start, end in input:
        for factor, minv, maxv in gen_func(max_value):
            minv = max(minv, start)
            maxv = min(maxv, end)
            for n in range(minv, maxv + 1):
                if n % factor == 0:
                    while n <= maxv:
                        found.add(n)
                        n += factor
                        if n > factor * (factor - 2):
                            break

    return sum(found)


raw_input = sys.stdin.read().rstrip().split(',')
raw_split = map(lambda s: tuple(s.split('-')), raw_input)
input: list[tuple[int, int]] = list(map(lambda t: (int(t[0]), int(t[1])), raw_split))

max_value = max(b for _, b in input)
print(part(max_value, factors_part_one))
print(part(max_value, factors_part_two))
