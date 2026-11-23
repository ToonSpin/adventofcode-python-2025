import sys

type Graph = dict[str, list[str]]
type RouteCounts = dict[str, int]

input: Graph = {}

for line in sys.stdin.read().strip().splitlines():
    name, outputs = line.split(': ')
    input[name] = outputs.split()

def count_routes(start: str, end: str, graph: Graph) -> int:
    route_counts: RouteCounts = {start: 1}
    total_count = 0
    while len(route_counts) > 0:
        new_counts: RouteCounts = {}
        for node, count in route_counts.items():
            if node == end:
                total_count += count
            if node not in input:
                continue
            for next_node in input[node]:
                new_counts.setdefault(next_node, 0)
                new_counts[next_node] += count
        route_counts = new_counts
    return total_count

print(count_routes('you', 'out', input))

fft_dac = count_routes('svr', 'fft', input) * count_routes('fft', 'dac', input) * count_routes('dac', 'out', input)
dac_fft = count_routes('svr', 'dac', input) * count_routes('dac', 'fft', input) * count_routes('fft', 'out', input)

print(fft_dac + dac_fft)
