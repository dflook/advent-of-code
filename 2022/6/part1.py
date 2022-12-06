from pathlib import Path

def start_of_packet(datastream: str) -> int:
    for i in range(len(datastream)):
        unique = set(datastream[i:i + 4])
        if len(unique) == 4:
            return i + 4


print(start_of_packet(Path('input.txt').read_text()))
