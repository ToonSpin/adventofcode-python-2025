import functools
import sys

def joltage_from_list(t: list[int]) -> int:
    def combine(a: int, b: int) -> int:
        return a * 10 + b
    return functools.reduce(combine, t, 0)

def get_max_combination(l: list[int], n: int) -> list[int]:
    if n == 1:
        return [max(l)]
    
    if n == len(l):
        return l

    max_element = max(l[:-(n-1)])
    index = l.index(max_element)
    return [max_element] + get_max_combination(l[index+1:], n - 1)

total_part_one = 0
total_part_two = 0

for line in sys.stdin.read().strip().splitlines():
    bank = [int(c) for c in line]
    total_part_one += joltage_from_list(get_max_combination(bank[:], 2))
    total_part_two += joltage_from_list(get_max_combination(bank[:], 12))

print(total_part_one)
print(total_part_two)
