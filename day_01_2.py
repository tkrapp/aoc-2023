import re
from importlib import resources

valid_digit_words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}
digit_pattern = re.compile(rf"({'|'.join(valid_digit_words.keys())})", re.IGNORECASE)


def read_digits_from_line(line: str) -> int:
    start_idx = 0
    all_digits: list[str] = []

    while match := digit_pattern.search(line, start_idx):
        all_digits.append(match.group())
        start_idx = match.start() + 1

    return int(valid_digit_words[all_digits[0]] + valid_digit_words[all_digits[-1]])


def main():
    with (resources.files("input_data") / "day_01.txt").open() as input_data:
        return sum(read_digits_from_line(line) for line in input_data)


if __name__ == "__main__":
    print(main())
