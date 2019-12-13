def pad_input(intcode: str) -> str:
    return intcode.rjust(4, '0')


def read_opcode(intcode: str) -> str:
    return intcode[2:]


def get_parameter_1(intcodes: list, position: int) -> int:
    if pad_input(str(intcodes[position]))[1] == "0":
        return (intcodes[intcodes[position + 1]])
    else:
        return (intcodes[position + 1])


def get_parameter_2(intcodes: list, position: int) -> int:
    if pad_input(str(intcodes[position]))[0] == "0":
        return (intcodes[intcodes[position + 2]])
    else:
        return (intcodes[position + 2])


def step(intcodes: list, position: int) -> None:
    if read_opcode(pad_input(str(intcodes[position]))) == "01":
        intcodes[intcodes[position + 3]] = int(get_parameter_1(intcodes, position)) + int(
            get_parameter_2(intcodes, position))
        step(intcodes, position + 4)
    elif read_opcode(pad_input(str(intcodes[position]))) == "02":
        intcodes[intcodes[position + 3]] = int(get_parameter_1(intcodes, position)) * int(
            get_parameter_2(intcodes, position))
        step(intcodes, position + 4)
    elif read_opcode(pad_input(str(intcodes[position]))) == "03":
        number = input("Please enter your input: ")
        intcodes[intcodes[position + 1]] = number
        step(intcodes, position + 2)
    elif read_opcode(pad_input(str(intcodes[position]))) == "04":
        print(get_parameter_1(intcodes, position))
        step(intcodes, position + 2)
    elif read_opcode(pad_input(str(intcodes[position]))) == "05":
        if get_parameter_1(intcodes, position) != 0:
            step(intcodes, get_parameter_2(intcodes, position))
        else:
            step(intcodes, position + 3)
    elif read_opcode(pad_input(str(intcodes[position]))) == "06":
        if get_parameter_1(intcodes, position) == 0:
            step(intcodes, get_parameter_2(intcodes, position))
        else:
            step(intcodes, position + 3)
    elif read_opcode(pad_input(str(intcodes[position]))) == "07":
        if get_parameter_1(intcodes, position) < get_parameter_2(intcodes, position):
            intcodes[intcodes[position + 3]] = 1
        else:
            intcodes[intcodes[position + 3]] = 0
        step(intcodes, position + 4)
    elif read_opcode(pad_input(str(intcodes[position]))) == "08":
        if get_parameter_1(intcodes, position) == get_parameter_2(intcodes, position):
            intcodes[intcodes[position + 3]] = 1
        else:
            intcodes[intcodes[position + 3]] = 0
        step(intcodes, position + 4)
    elif read_opcode(pad_input(str(intcodes[position]))) == "99":
        print("Finished!")
    else:
        print("Error!")


def main() -> None:
    with open("day05_input.txt", "r") as file:
        for line in file:
            intcodes = [int(item) for item in line.split(",")]
    step(intcodes, 0)


if __name__ == "__main__":
    main()
