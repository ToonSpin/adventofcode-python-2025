import re
import sys

raw_input = sys.stdin.read().rstrip().split(',')
raw_split = map(lambda s: tuple(s.split('-')), raw_input)
input: list[tuple[int, int]] = list(map(lambda t: (int(t[0]), int(t[1])), raw_split))

regex_part_one = re.compile(r'^(.*)\1$')
regex_part_two = re.compile(r'^(.*)\1+$')

total_part_one = 0
total_part_two = 0

for start, end in input:
    for n in range(start, end + 1):
        if regex_part_one.match(str(n)) is not None:
            total_part_one += n
        if regex_part_two.match(str(n)) is not None:
            total_part_two += n

print(total_part_one)
print(total_part_two)