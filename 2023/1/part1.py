from pathlib import Path
from typing import Iterable


def read_calibrations(input: str) -> Iterable[int]:

    for line in input.splitlines():

        value = None
        last = None

        for c in line:
            if c.isdigit():
                last = int(c)

                if value is None:
                    value = int(c) * 10

        yield value + last


input = Path('test.txt').read_text()
calibration_numbers = list(read_calibrations(input))
print(sum(calibration_numbers))

input = Path('input.txt').read_text()
calibration_numbers = list(read_calibrations(input))
print(sum(calibration_numbers))
