import textwrap


def count_occurence(image: str, number: int) -> int:
    counter = 0
    for pixel in image:
        if int(pixel) == number:
            counter += 1
    return counter


def main() -> None:
    width = 25
    height = 6
    with open("day08_input.txt", "r") as input_file:
        for line in input_file:
            pixels = line
    images = textwrap.wrap(pixels, width * height)
    number_of_zeroes = [count_occurence(image, 0) for image in images]
    number_of_ones = count_occurence(images[number_of_zeroes.index(min(number_of_zeroes))], 1)
    number_of_twos = count_occurence(images[number_of_zeroes.index(min(number_of_zeroes))], 2)
    print("Answer: " + str(number_of_ones * number_of_twos))


if __name__ == "__main__":
    main()
