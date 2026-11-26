import sys
    
input = sys.stdin.read().strip().splitlines()

valid_count = 0
for line in input[30:]:
    w = int(line[0:2])
    h = int(line[3:5])
    counts = list(map(int, line[7:].split()))
    if w * h >= 9 * sum(counts):
        valid_count += 1
print(valid_count)
