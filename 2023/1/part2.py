from pathlib import Path
from typing import Iterable


def read_calibrations(input: str) -> Iterable[int]:

    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def to_int(number: str) -> int:
        if number.isdigit():
            return int(number)
        return numbers.index(number) + 1

    for line in input.splitlines():

        first_index = None
        value = None

        last_index = None
        last_value = None

        for candidate in numbers:
            if (index := line.find(candidate)) != -1:
                if first_index is None or index < first_index:
                    first_index = index
                    value = to_int(candidate) * 10

            if (index := line.rfind(candidate)) != -1:
                if last_index is None or index > last_index:
                    last_index = index
                    last_value = to_int(candidate)

        yield value + last_value



input = Path('test2.txt').read_text()
calibration_numbers = list(read_calibrations(input))
print(sum(calibration_numbers))

input = Path('input.txt').read_text()
calibration_numbers = list(read_calibrations(input))
print(sum(calibration_numbers))
