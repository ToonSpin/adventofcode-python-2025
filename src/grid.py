from enum import auto, Enum
from collections.abc import Generator
import re

class OutOfBoundsException(Exception):
    pass

class Direction(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

    def forward(self, x: int, y: int) -> tuple[int, int]:
        match self:
            case Direction.NORTH:
                return (x, y - 1)
            case Direction.EAST:
                return (x + 1, y)
            case Direction.SOUTH:
                return (x, y + 1)
            case Direction.WEST:
                return (x - 1, y)
            case _:
                raise Exception("Invalid direction")

    def turn_left(self) -> 'Direction':
        match self:
            case Direction.NORTH:
                return Direction.WEST
            case Direction.EAST:
                return Direction.NORTH
            case Direction.SOUTH:
                return Direction.EAST
            case Direction.WEST:
                return Direction.SOUTH
            case _:
                raise Exception("Invalid direction")

    def turn_right(self) -> 'Direction':
        match self:
            case Direction.WEST:
                return Direction.NORTH
            case Direction.NORTH:
                return Direction.EAST
            case Direction.EAST:
                return Direction.SOUTH
            case Direction.SOUTH:
                return Direction.WEST
            case _:
                raise Exception("Invalid direction")

def all_directions() -> Generator[Direction]:
    yield Direction.NORTH
    yield Direction.EAST
    yield Direction.SOUTH
    yield Direction.WEST

class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Pos<{self.x}, {self.y}>"

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other: object) -> bool:
        if other.__class__ != self.__class__:
            return False
        return self.x == other.x and self.y == other.y # pyright: ignore

    def move(self, dir: Direction) -> None:
        self.x, self.y = dir.forward(self.x, self.y)

    def peek(self, dir: Direction) -> "Position":
        x, y = dir.forward(self.x, self.y)
        return Position(x, y)

class Grid:
    def __init__(self, input: str) -> None:
        self.grid = [list(line.strip()) for line in input.strip().split('\n')]
        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.grid])

    def get(self, pos: Position) -> str:
        return self.grid[pos.y][pos.x]

    def set(self, pos: Position, char: str) -> None:
        if self.out_of_bounds(pos):
            raise(OutOfBoundsException(f"{pos.x}, {pos.y} is out of bounds"))
        self.grid[pos.y][pos.x] = char

    def find(self, char: str) -> Generator[Position]:
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == char:
                    yield Position(x, y)

    def find_re(self, regex: str) -> Generator[Position]:
        expr = re.compile(regex)
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if expr.match(cell):
                    yield Position(x, y)

    def in_bounds(self, pos: Position) -> bool:
        return pos.x >= 0 and pos.y >= 0 and pos.x < self.width and pos.y < self.height

    def out_of_bounds(self, pos: Position) -> bool:
        return not self.in_bounds(pos)

    def neighbors(self, pos: Position, diagonal: bool = False) -> Generator[Position]:
        for q in [-1, 0, 1]:
            for p in [-1, 0, 1]:
                if p == 0 and q == 0: continue
                if not diagonal and p != 0 and q != 0: continue
                n = Position(pos.x + p, pos.y + q)
                if self.in_bounds(n):
                    yield n
