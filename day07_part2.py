from itertools import permutations


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


def step(thruster_intcodes: list, thruster: int, position: int, phase_setting: tuple, thruster_uninitialized: list, previous_output: int, temporary_output: int, thruster_position: list) -> int:
    if read_opcode(pad_input(str(thruster_intcodes[thruster][position]))) == "01":
        thruster_intcodes[thruster][thruster_intcodes[thruster][position + 3]] = int(get_parameter_1(thruster_intcodes[thruster], position)) + int(
            get_parameter_2(thruster_intcodes[thruster], position))
        return step(thruster_intcodes, thruster, position + 4, phase_setting, thruster_uninitialized, previous_output, temporary_output, thruster_position)
    elif read_opcode(pad_input(str(thruster_intcodes[thruster][position]))) == "02":
        thruster_intcodes[thruster][thruster_intcodes[thruster][position + 3]] = int(get_parameter_1(thruster_intcodes[thruster], position)) * int(
            get_parameter_2(thruster_intcodes[thruster], position))
        return step(thruster_intcodes, thruster, position + 4, phase_setting, thruster_uninitialized, previous_output, temporary_output, thruster_position)
    elif read_opcode(pad_input(str(thruster_intcodes[thruster][position]))) == "03":
        if thruster_uninitialized[thruster]:
            thruster_intcodes[thruster][thruster_intcodes[thruster][position + 1]] = phase_setting[thruster]
            thruster_uninitialized[thruster] = False
        else:
            thruster_intcodes[thruster][thruster_intcodes[thruster][position + 1]] = previous_output
        return step(thruster_intcodes, thruster, position + 2, phase_setting, thruster_uninitialized, previous_output, temporary_output, thruster_position)
    elif read_opcode(pad_input(str(thruster_intcodes[thruster][position]))) == "04":
        previous_output = get_parameter_1(thruster_intcodes[thruster], position)
        thruster_position[thruster] = position + 2
        if thruster < 4:
            return step(thruster_intcodes, thruster + 1, thruster_position[thruster +1], phase_setting, thruster_uninitialized, previous_output, temporary_output, thruster_position)
        else:
            temporary_output = previous_output
            return step(thruster_intcodes, 0, thruster_position[0], phase_setting, thruster_uninitialized, previous_output, temporary_output, thruster_position)
    elif read_opcode(pad_input(str(thruster_intcodes[thruster][position]))) == "05":
        if get_parameter_1(thruster_intcodes[thruster], position) != 0:
            return step(thruster_intcodes, thruster, get_parameter_2(thruster_intcodes[thruster], position), phase_setting, thruster_uninitialized, previous_output,
                        temporary_output, thruster_position)
        else:
            return step(thruster_intcodes, thruster, position + 3, phase_setting, thruster_uninitialized, previous_output, temporary_output, thruster_position)
    elif read_opcode(pad_input(str(thruster_intcodes[thruster][position]))) == "06":
        if get_parameter_1(thruster_intcodes[thruster], position) == 0:
            return step(thruster_intcodes, thruster, get_parameter_2(thruster_intcodes[thruster], position), phase_setting, thruster_uninitialized, previous_output,
                        temporary_output, thruster_position)
        else:
            return step(thruster_intcodes, thruster, position + 3, phase_setting, thruster_uninitialized, previous_output, temporary_output, thruster_position)
    elif read_opcode(pad_input(str(thruster_intcodes[thruster][position]))) == "07":
        if get_parameter_1(thruster_intcodes[thruster], position) < get_parameter_2(thruster_intcodes[thruster], position):
            thruster_intcodes[thruster][thruster_intcodes[thruster][position + 3]] = 1
        else:
            thruster_intcodes[thruster][thruster_intcodes[thruster][position + 3]] = 0
        return step(thruster_intcodes, thruster, position + 4, phase_setting, thruster_uninitialized, previous_output, temporary_output, thruster_position)
    elif read_opcode(pad_input(str(thruster_intcodes[thruster][position]))) == "08":
        if get_parameter_1(thruster_intcodes[thruster], position) == get_parameter_2(thruster_intcodes[thruster], position):
            thruster_intcodes[thruster][thruster_intcodes[thruster][position + 3]] = 1
        else:
            thruster_intcodes[thruster][thruster_intcodes[thruster][position + 3]] = 0
        return step(thruster_intcodes, thruster, position + 4, phase_setting, thruster_uninitialized, previous_output, temporary_output, thruster_position)
    elif read_opcode(pad_input(str(thruster_intcodes[thruster][position]))) == "99":
        return temporary_output
    else:
        print("Error!")


def main() -> None:
    code_list = [*permutations(range(5, 10), 5)]
    last_output = []
    for code in code_list:
        thruster_intcodes = []
        thruster_position = [0] * 5
        with open("day07_input.txt", "r") as file:
            for line in file:
                for i in range(0, 5):
                    thruster_intcodes.append([int(item) for item in line.split(",")])
        thruster_uninitialized = [True] * 5
        previous_output = 0
        temporary_output = 0
        last_output.append(step(thruster_intcodes, 0, 0, code, thruster_uninitialized, previous_output, temporary_output, thruster_position))

    print("Answer: " + str(max(last_output)))


if __name__ == "__main__":
    main()
