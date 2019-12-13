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


def calculate_intersections(wire_list: list) -> int:
    intersections = set.intersection(*wire_list)
    return intersections


def count_steps(wire: str, point: tuple) -> int:
    position = [0, 0]
    total_count = 0
    for code in wire.split(","):
        if code.startswith("R"):
            counter = 0
            while tuple(position) != point and counter < int(code[1:]):
                position[0] += 1
                counter += 1
                total_count += 1
        elif code.startswith("L"):
            counter = 0
            while tuple(position) != point and counter < int(code[1:]):
                position[0] -= 1
                counter += 1
                total_count += 1
        elif code.startswith("U"):
            counter = 0
            while tuple(position) != point and counter < int(code[1:]):
                position[1] += 1
                counter += 1
                total_count += 1
        elif code.startswith("D"):
            counter = 0
            while tuple(position) != point and counter < int(code[1:]):
                position[1] -= 1
                counter += 1
                total_count += 1
    return total_count


def main() -> None:
    with open("day03_input.txt", "r") as inp:
        wire_list = []
        for counter, line in enumerate(inp, 0):
            position = [0, 0]
            wire_list.append(set())
            for instruction in line.split(","):
                execute(wire_list[counter], position, instruction)
        intersections = calculate_intersections(wire_list)
        intersection_distances = {}
        for intersection in intersections:
            distance = 0
            with open("day03_input.txt", "r") as inp:
                for line in inp:
                    distance += count_steps(line, intersection)
                intersection_distances[intersection] = distance

        sorted_intersection_distances = sorted(intersection_distances.items(), key=lambda kv: kv[1])
        print(sorted_intersection_distances[0])


if __name__ == "__main__":
    main()
