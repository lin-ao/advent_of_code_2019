def always_increasing(number: int) -> bool:
    digits = list(str(number))
    always_increasing = True
    for i in range(1, 6):
        if digits[i] < digits[i - 1]:
            always_increasing = False
    return always_increasing


def check_password(number: int) -> bool:
    if len(list(str(number))) == 6 and len(set(list(str(number)))) < 6 and always_increasing(number):
        return True
    else:
        return False


def password(start: int, end: int) -> int:
    total_count = 0
    for number in range(start, end + 1):
        if check_password(number):
            total_count += 1
    return total_count


def main() -> None:
    print(password(254032, 789860))


if __name__ == "__main__":
    main()
