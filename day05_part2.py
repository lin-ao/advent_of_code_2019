def pad_input(input: str) -> str:
    return input.rjust(4, '0')


def read_opcode(input: str) -> str:
    return input[2:]


def get_parameter_1(input_list: list, position: int) -> int:
    if pad_input(str(input_list[position]))[1] == "0":
        return (input_list[input_list[position + 1]])
    else:
        return (input_list[position + 1])


def get_parameter_2(input_list: list, position: int) -> int:
    if pad_input(str(input_list[position]))[0] == "0":
        return (input_list[input_list[position + 2]])
    else:
        return (input_list[position + 2])


def step(input_list: list, position: int) -> None:
    if read_opcode(pad_input(str(input_list[position]))) == "01":
        input_list[input_list[position + 3]] = int(get_parameter_1(input_list, position)) + int(
            get_parameter_2(input_list, position))
        step(input_list, position + 4)
    elif read_opcode(pad_input(str(input_list[position]))) == "02":
        input_list[input_list[position + 3]] = int(get_parameter_1(input_list, position)) * int(
            get_parameter_2(input_list, position))
        step(input_list, position + 4)
    elif read_opcode(pad_input(str(input_list[position]))) == "03":
        number = input("Please enter your input: ")
        input_list[input_list[position + 1]] = number
        step(input_list, position + 2)
    elif read_opcode(pad_input(str(input_list[position]))) == "04":
        print(get_parameter_1(input_list, position))
        step(input_list, position + 2)
    elif read_opcode(pad_input(str(input_list[position]))) == "05":
        if get_parameter_1(input_list, position) != 0:
            step(input_list, get_parameter_2(input_list, position))
        else:
            step(input_list, position + 3)
    elif read_opcode(pad_input(str(input_list[position]))) == "06":
        if get_parameter_1(input_list, position) == 0:
            step(input_list, get_parameter_2(input_list, position))
        else:
            step(input_list, position + 3)
    elif read_opcode(pad_input(str(input_list[position]))) == "07":
        if get_parameter_1(input_list, position) < get_parameter_2(input_list, position):
            input_list[input_list[position + 3]] = 1
        else:
            input_list[input_list[position + 3]] = 0
        step(input_list, position + 4)
    elif read_opcode(pad_input(str(input_list[position]))) == "08":
        if get_parameter_1(input_list, position) == get_parameter_2(input_list, position):
            input_list[input_list[position + 3]] = 1
        else:
            input_list[input_list[position + 3]] = 0
        step(input_list, position + 4)
    elif read_opcode(pad_input(str(input_list[position]))) == "99":
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
