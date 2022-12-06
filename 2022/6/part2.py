from pathlib import Path

def start_of_message(datastream: str) -> int:
    for i in range(len(datastream)):
        unique = set(datastream[i:i + 14])
        if len(unique) == 14:
            return i + 14


print(start_of_message(Path('input.txt').read_text()))
