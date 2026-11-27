import functools
import itertools
import sys

def csv_to_list(s: str) -> list[int]:
    return list(map(int, s.split(',')))

class Machine:
    def __init__(self, line: str) -> None:
        self.line = line

        lights, rest = line[1:].split(']')
        rest, joltages = rest[:-1].split('{')

        buttons = rest.strip()[1:-1].split(') (')
        buttons = list(map(csv_to_list, buttons))

        joltages = csv_to_list(joltages)

        self.lights = list(map(lambda c: 1 if c == '#' else 0, lights))
        self.buttons = buttons
        self.joltages = joltages

    def generate_part_one(self, lights_val, buttons_vals):
        configuration = [0 for _ in buttons_vals]

        while True:
            digit = 0
            while configuration[digit] == 1:
                configuration[digit] = 0
                digit += 1
                if digit == len(buttons_vals):
                    break
            if digit == len(buttons_vals):
                break
            configuration[digit] = 1
            val = 0
            for button in itertools.compress(buttons_vals, configuration):
                val ^= button
            if val == lights_val:
                yield sum(configuration)

    def part_one(self) -> int:
        lights_val = functools.reduce(lambda a, e: a * 2 + e, reversed(self.lights))
        buttons_vals = [sum(map(lambda x: 2 ** x, b)) for b in self.buttons]
        return min(self.generate_part_one(lights_val, buttons_vals))


input = [Machine(line) for line in sys.stdin.read().strip().splitlines()]

print(sum(machine.part_one() for machine in input))