def always_increasing(number: int):
    digits = list(str(number))
    always_increasing = True
    for i in range(1, 6):
        if digits[i] < digits[i - 1]:
            always_increasing = False
    return always_increasing


def check_for_repeating(number: int):
    digits = list(str(number))
    digits_dict = {}
    repeats_twice = False
    for item in digits:
        if item in digits_dict:
            digits_dict[item] += 1
        else:
            digits_dict[item] = 1
    for item in digits_dict:
        if digits_dict[item] == 2:
            repeats_twice = True
    return repeats_twice


def check_password(number: int):
    if len(list(str(number))) == 6 and check_for_repeating(number) and always_increasing(number):
        return True
    else:
        return False


def password(start: int, end: int):
    total_count = 0
    for number in range(start, end + 1):
        if check_password(number):
            total_count += 1
    return total_count


def main() -> None:
    print(password(254032, 789860))


if __name__ == "__main__":
    main()
