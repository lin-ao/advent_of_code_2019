from itertools import permutations


def pad_input(intcode: str) -> str:
    return intcode.rjust(4, '0')


def read_opcode(intcode: str) -> str:
    return intcode[2:]


def get_parameter_1(intcodes: list, position: int) -> int:
    if pad_input(str(intcodes[position]))[1] == "0":
        return intcodes[intcodes[position + 1]]
    else:
        return intcodes[position + 1]


def get_parameter_2(intcodes: list, position: int) -> int:
    if pad_input(str(intcodes[position]))[0] == "0":
        return intcodes[intcodes[position + 2]]
    else:
        return intcodes[position + 2]


def step(intcodes: list, position: int, phase_setting: int, first_time: bool, previous_output: int, temporary_output: int) -> int:
    if read_opcode(pad_input(str(intcodes[position]))) == "01":
        intcodes[intcodes[position + 3]] = int(get_parameter_1(intcodes, position)) + int(get_parameter_2(intcodes, position))
        return step(intcodes, position + 4, phase_setting, first_time, previous_output, temporary_output)
    elif read_opcode(pad_input(str(intcodes[position]))) == "02":
        intcodes[intcodes[position + 3]] = int(get_parameter_1(intcodes, position)) * int(get_parameter_2(intcodes, position))
        return step(intcodes, position + 4, phase_setting, first_time, previous_output, temporary_output)
    elif read_opcode(pad_input(str(intcodes[position]))) == "03":
        if first_time:
            intcodes[intcodes[position + 1]] = phase_setting
            first_time = False
        else:
            intcodes[intcodes[position + 1]] = previous_output
        return step(intcodes, position + 2, phase_setting, first_time, previous_output, temporary_output)
    elif read_opcode(pad_input(str(intcodes[position]))) == "04":
        temporary_output = get_parameter_1(intcodes, position)
        return step(intcodes, position + 2, phase_setting, first_time, previous_output, temporary_output)
    elif read_opcode(pad_input(str(intcodes[position]))) == "05":
        if get_parameter_1(intcodes, position) != 0:
            return step(intcodes, get_parameter_2(intcodes, position), phase_setting, first_time, previous_output, temporary_output)
        else:
            return step(intcodes, position + 3, phase_setting, first_time, previous_output, temporary_output)
    elif read_opcode(pad_input(str(intcodes[position]))) == "06":
        if get_parameter_1(intcodes, position) == 0:
            return step(intcodes, get_parameter_2(intcodes, position), phase_setting, first_time, previous_output, temporary_output)
        else:
            return step(intcodes, position + 3, phase_setting, first_time, previous_output, temporary_output)
    elif read_opcode(pad_input(str(intcodes[position]))) == "07":
        if get_parameter_1(intcodes, position) < get_parameter_2(intcodes, position):
            intcodes[intcodes[position + 3]] = 1
        else:
            intcodes[intcodes[position + 3]] = 0
        return step(intcodes, position + 4, phase_setting, first_time, previous_output, temporary_output)
    elif read_opcode(pad_input(str(intcodes[position]))) == "08":
        if get_parameter_1(intcodes, position) == get_parameter_2(intcodes, position):
            intcodes[intcodes[position + 3]] = 1
        else:
            intcodes[intcodes[position + 3]] = 0
        return step(intcodes, position + 4, phase_setting, first_time, previous_output, temporary_output)
    elif read_opcode(pad_input(str(intcodes[position]))) == "99":
        return temporary_output
    else:
        print("Error!")


def main() -> None:
    code_list = [*permutations(range(0, 5), 5)]
    thrusters = range(0, 5)
    output_list = []
    for code in code_list:
        previous_output = 0
        for thruster in thrusters:
            temporary_output = 0
            first_time = True
            with open("day07_input.txt", "r") as file:
                for line in file:
                    intcodes = [int(item) for item in line.split(",")]
            if thruster < 4:
                previous_output = step(intcodes, 0, code[thruster], first_time, previous_output, temporary_output)
            else:
                output_list.append(step(intcodes, 0, code[thruster], first_time, previous_output, temporary_output))
    print("Answer: " + str(max(output_list)))


if __name__ == "__main__":
    main()
