import textwrap


def find_non_transparent(pixels: list) -> str:
    for pixel in pixels:
        if int(pixel) != 2:
            return pixel


def main() -> None:
    width = 25
    height = 6
    with open("day08_input.txt", "r") as input_file:
        for line in input_file:
            pixels = line
    images = textwrap.wrap(pixels, width * height)
    overlay_image = [*zip(*images)]
    final_image = "".join([find_non_transparent(pixels) for pixels in overlay_image])
    lines = textwrap.wrap(final_image, width)
    print("Answer:\n" + "\n".join(lines))


if __name__ == "__main__":
    main()
