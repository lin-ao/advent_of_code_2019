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

    common_orbits = list(set(you_orbits).intersection(san_orbits))
    target_orbit = you_orbits[min([you_orbits.index(item) for item in common_orbits])]
    transfers = you_orbits.index(target_orbit) + san_orbits.index(target_orbit)

    print(transfers)


if __name__ == "__main__":
    main()
