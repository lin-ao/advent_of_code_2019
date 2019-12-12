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


def find_answer() -> int:
    for i in range(100):
        noun = i
        for j in range(100):
            verb = j
            with open("day2_input.txt", "r") as file:
                for line in file:
                    intcodes = [int(item) for item in line.split(",")]
            intcodes[1] = noun
            intcodes[2] = verb
            step(intcodes, 0)
            if intcodes[0] == 19690720:
                return noun * 100 + verb


def main() -> None:
    print("Answer: " + str(find_answer()))


if __name__ == "__main__":
    main()
