def step(intcodes: list, pointer: int) -> None:
    if intcodes[pointer] == 1:
        intcodes[intcodes[pointer + 3]] = intcodes[intcodes[pointer + 1]] + intcodes[intcodes[pointer + 2]]
        step(intcodes, pointer + 4)
    elif intcodes[pointer] == 2:
        intcodes[intcodes[pointer + 3]] = intcodes[intcodes[pointer + 1]] * intcodes[intcodes[pointer + 2]]
        step(intcodes, pointer + 4)
    elif intcodes[pointer] == 99:
        pass
    else:
        print("Error!")


def main() -> None:
    with open("day2_input.txt", "r") as file:
        for line in file:
            intcodes = [int(item) for item in line.split(",")]

    intcodes[1] = 12
    intcodes[2] = 2

    step(intcodes, 0)

    print("Answer: " + str(intcodes[0]))


if __name__ == "__main__":
    main()
