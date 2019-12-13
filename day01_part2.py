def calculate_fuel(mass: int) -> int:
    total_fuel = 0
    while int(mass / 3) - 2 > 0:
        total_fuel += int(mass / 3) - 2
        mass = int(mass / 3) - 2
    return total_fuel


def main() -> None:
    with open("day01_input.txt", "r") as file:
        total_fuel = 0
        for line in file:
            total_fuel += calculate_fuel(int(line))

    print("Answer: " + str(total_fuel))


if __name__ == "__main__":
    main()
