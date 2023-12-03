import re
from copy import deepcopy

with open("data.txt") as f:
    data_lines = [line.strip() for line in f.readlines() if line.strip()]

digits = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
all_digits = {**digits, **dict((str(n),n) for n in range(10))}

number_pattern = r"(?=(0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))"
def get_digits(in_str):
    matches = re.findall(number_pattern, in_str)
    for m in matches:
        yield all_digits[m]

lines_sum = 0
for line in data_lines:
    digits = list(get_digits(line))
    print(line, digits)
    first_digit = int(digits[0])
    last_digit = int(digits[-1])
    lines_sum += first_digit * 10 + last_digit

print(lines_sum)
