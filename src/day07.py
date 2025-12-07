from grid import Grid, Position as Pos
import sys


def count_splits(manifold: Grid) -> tuple[int, int]:
    start = next(manifold.find('S'))
    beams: dict[Pos, int] = {start: 1}
    y = start.y
    splits_found: set[Pos] = set()

    while y < manifold.height:
        new_beams: dict[Pos, int] = {}

        for beam, count in beams.items():
            new_positions: list[Pos] = []

            if manifold.get(beam) == '^':
                splits_found.add(beam)
                new_positions.append(Pos(beam.x - 1, y + 1))
                new_positions.append(Pos(beam.x + 1, y + 1))
            else:
                new_positions.append(Pos(beam.x, y + 1))

            for p in new_positions:
                existing_count: int = new_beams.get(p, 0)
                new_beams[p] = existing_count + count

        beams = new_beams
        y += 1

    return len(splits_found), sum(beams.values())


manifold = Grid(sys.stdin.read().strip())

split_count, timeline_count = count_splits(manifold)
print(split_count)
print(timeline_count)
