from importlib import resources


def read_digits_from_line(line: str) -> int:
    all_digits = [char for char in line if char.isdigit()]
    return int(all_digits[0] + all_digits[-1])


def main():
    with (resources.files("input_data") / "day_01.txt").open() as input_data:
        return sum(read_digits_from_line(line) for line in input_data)


if __name__ == "__main__":
    print(main())
