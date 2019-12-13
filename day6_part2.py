def find_orbits(orbits: dict, key: str) -> list:
    try:
        orbits[key]
        return [orbits[key]] + find_orbits(orbits, orbits[key])
    except KeyError:
        return []


def main() -> None:
    orbits = {}

    with open("day6_input.txt", "r") as inp:
        for line in inp:
            orbits[line.split(")")[1].rstrip()] = line.split(")")[0]

    you_orbits = find_orbits(orbits, "YOU")
    san_orbits = find_orbits(orbits, "SAN")

    transfers = len(set(you_orbits).symmetric_difference(san_orbits))

    print(transfers)


if __name__ == "__main__":
    main()
