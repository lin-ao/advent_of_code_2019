def count_orbit(orbits: dict, key: str, total=0) -> int:
    try:
        orbits[key]
        total += 1
        return count_orbit(orbits, orbits[key], total)
    except KeyError:
        return total


def main() -> None:
    orbits = {}
    keys = []

    with open("day6_input.txt", "r") as inp:
        for line in inp:
            orbits[line.split(")")[1].rstrip()] = line.split(")")[0]
            keys.append(line.split(")")[1].rstrip())

    total_orbits = 0

    for item in keys:
        total_orbits += count_orbit(orbits, item)

    print(total_orbits)


if __name__ == "__main__":
    main()
