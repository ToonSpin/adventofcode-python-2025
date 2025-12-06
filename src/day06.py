import functools
import operator
import sys

def line_to_numbers(line: str) -> list[int]:
    return list(map(int, line.strip().split()))

def get_grand_total(operators: list[str], numbers: list[list[int]]) -> int:
    grand_total = 0
    for operation, operands in zip(operators, numbers):
        if operation == '+':
            grand_total += sum(operands)
        if operation == '*':
            grand_total += functools.reduce(operator.mul, operands, 1)
    return grand_total

input = sys.stdin.read().strip().splitlines()
max_len = max(len(l) for l in input)
input = [(l + max_len * ' ')[:max_len] for l in input]
operators = input[-1].split()

numbers_part_one_raw = [line_to_numbers(line) for line in input[:-1]]
numbers_part_one = [
    [numbers_part_one_raw[j][i] for j in range(len(numbers_part_one_raw))]
    for i in range(len(numbers_part_one_raw[0]))
]

input_transposed = "\n".join([
    ''.join(input[j][i] for j in range(len(input[:-1]))).strip()
    for i in range(len(input[0]))
])
numbers_part_two = [line_to_numbers(chunk) for chunk in input_transposed.split('\n\n')]

print(get_grand_total(operators, numbers_part_one))
print(get_grand_total(operators, numbers_part_two))
