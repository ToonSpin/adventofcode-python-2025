import sys

input = sys.stdin.read().rstrip().split()

def get_zeroes_left(pos: int, count: int) -> int:
    if count < pos:
        return 0
    if pos == 0:
        return (count - pos) // 100
    return (count - pos) // 100 + 1

def get_zeroes_right(pos: int, count: int) -> int:
    return get_zeroes_left((100 - pos) % 100, count)

pos = 50
zero_count_part_one = 0
zero_count_part_two = 0

for move in input:
    count = int(move[1:])

    if move[0] == 'L':
        zero_count_part_two += get_zeroes_left(pos, count)
        pos -= count
        pos += 10000
    else:
        zero_count_part_two += get_zeroes_right(pos, count)
        pos += count

    pos %= 100

    if pos == 0:
        zero_count_part_one += 1

print(f'The password: {zero_count_part_one}')
print(f'The password using method 0x434C49434B: {zero_count_part_two}')
