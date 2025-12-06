import math
import sys

raw_input = sys.stdin.read().rstrip().split(',')
raw_split = map(lambda s: tuple(s.split('-')), raw_input)
input: list[tuple[int, int]] = list(map(lambda t: (int(t[0]), int(t[1])), raw_split))

def count_digits(n: int) -> int:
    return math.floor(math.log10(n)) + 1

def min_max_factors(range: tuple[int, int], dividend: int) -> tuple[int, int]:
    range_min, range_max = range
    # allow for using math.ceil without illegible "if" stuff
    if range_min % dividend == 0:
        range_min -= 1
    return (math.ceil(range_min / dividend), range_max // dividend)

def validity_factor(n: int) -> int:
    validity_digit_count = math.floor(count_digits(n) / 2)
    return 10 ** validity_digit_count + 1

def min_max_for_vf(vf: int) -> tuple[int, int]:
    digits = count_digits(vf) - 1
    return (10 ** (digits * 2 - 1), 10 ** (digits * 2) - 1)


def add_valid_ids(range: tuple[int, int]) -> int:
    min_id, max_id = range

    min_vf = validity_factor(min_id)
    max_vf = validity_factor(max_id)

    vfs = [min_vf, max_vf] if min_vf != max_vf else [min_vf]
    total = 0

    for vf in vfs:
        min_for_vf, max_for_vf = min_max_for_vf(vf)
        actual_range = (max(min_for_vf, min_id), min(max_for_vf, max_id))
        if max_for_vf < min_id or min_for_vf > max_id:
            continue
        min_f, max_f = min_max_factors(actual_range, vf)
        triangle = (max_f - min_f + 1) * (max_f + min_f) // 2
        total += triangle * vf

    return total

assert(min_max_factors((11, 22), 11) == (1, 2))
assert(min_max_factors((10, 23), 11) == (1, 2))
assert(min_max_factors((11, 21), 11) == (1, 1))
assert(count_digits(99) == 2)
assert(count_digits(100) == 3)
assert(count_digits(101) == 3)
assert(validity_factor(22) == 11)
assert(min_max_for_vf(101) == (1000, 9999))

print(sum(map(add_valid_ids, input)))
