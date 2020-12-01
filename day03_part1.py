def right(wire: set, position: list, length: int) -> None:
    for number in range(length):
        wire.add((position[0] + (number + 1), position[1]))
    position[0] += length


def left(wire: set, position: list, length: int) -> None:
    for number in range(length):
        wire.add((position[0] - (number + 1), position[1]))
    position[0] -= length


def up(wire: set, position: list, length: int) -> None:
    for number in range(length):
        wire.add((position[0], position[1] + (number + 1)))
    position[1] += length


def down(wire: set, position: list, length: int) -> None:
    for number in range(length):
        wire.add((position[0], position[1] - (number + 1)))
    position[1] -= length


def execute(wire: set, position: list, code: str) -> None:
    if code.startswith("R"):
        right(wire, position, int(code[1:]))
    elif code.startswith("L"):
        left(wire, position, int(code[1:]))
    elif code.startswith("U"):
        up(wire, position, int(code[1:]))
    elif code.startswith("D"):
        down(wire, position, int(code[1:]))


def manhattan_distance(point: tuple) -> int:
    distance = 0
    for item in point:
        distance += abs(item)
    return distance


def find_closest_intersection(wire_list: list) -> int:
    closest_intersection = None
    intersections = set.intersection(*wire_list)
    for intersection in intersections:
        if closest_intersection is None:
            closest_intersection = intersection
        elif manhattan_distance(intersection) < manhattan_distance(closest_intersection):
            closest_intersection = intersection
    return closest_intersection


def main() -> None:
    with open("day03_input.txt", "r") as inp:
        wire_list = []
        for counter, line in enumerate(inp, 0):
            position = [0, 0]
            wire_list.append(set())
            for instruction in line.split(","):
                execute(wire_list[counter], position, instruction)
        print(find_closest_intersection(wire_list))
        print(manhattan_distance(find_closest_intersection(wire_list)))


if __name__ == "__main__":
    main()
