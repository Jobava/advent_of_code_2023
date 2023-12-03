import re

DIGITS = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
ALL_DIGITS = {**DIGITS, **dict((str(n),n) for n in range(10))}

NUMBER_PATTERN = r"(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))"


def get_digits(in_str):
    matches = re.findall(NUMBER_PATTERN, in_str)
    return [ALL_DIGITS[m] for m in matches]


def get_number_from_line(in_line):
    digits = get_digits(in_line)
    first_digit = int(digits[0])
    last_digit = int(digits[-1])
    return first_digit * 10 + last_digit


def get_number():
    with open("data.txt") as f:
        for line in f:
            if not line:
                continue
            yield get_number_from_line(line)


if __name__ == "__main__":
    solution = sum(get_number())
    print(solution)
