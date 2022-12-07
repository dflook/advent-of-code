from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Tuple, Iterable


@dataclass
class File:
    name: str
    size: int

    def __str__(self) -> str:
        return f'- {self.name} (file, size={self.size})\n'

    def __repr__(self):
        return f'File(name={self.name!r}, size={self.size!r}'


class Directory(dict):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)

    @property
    def size(self) -> int:
        return sum(entry.size for entry in self.values())

    def __str__(self) -> str:
        s = f'- {self.name} (dir, size={self.size})\n'

        for entry in self.values():
            for line in str(entry).splitlines():
                s += f'  {line}\n'

        return s

    def __repr__(self) -> str:
        return f'Directory(name={self.name!r}, size={self.size!r})'


def read_commands(log: str) -> Iterable[Tuple[str, str]]:
    command = ''
    output = []

    for line in log.splitlines():
        if line.startswith('$ '):
            if command:
                yield command, output
            command = line[2:].split(' ')
            output = []
        else:
            output.append(line)

    yield command, output


def read_filesystem(commands):
    root = Directory('/')
    dir_path = []

    for command, output in commands:

        print(f'{command=}, {output=}')

        def get_cwd():
            cwd = root
            for segment in dir_path:
                cwd = cwd[segment]
            return cwd

        match command:
            case ['cd', '/']:
                dir_path = []
            case ['cd', '..']:
                dir_path.pop()
            case ['cd', dir]:
                dir_path.append(dir)
            case ['ls']:
                for line in output:
                    size, name = line.split(' ')

                    d = get_cwd()

                    if size == 'dir':
                        d[name] = Directory(name)
                    else:
                        d[name] = File(name, int(size))

    return root


def all_directories(d: Directory) -> Iterable[Directory]:
    for entry in d.values():
        if isinstance(entry, Directory):
            yield from all_directories(entry)

    yield d


TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000

commands = read_commands(Path('input.txt').read_text())
fs = read_filesystem(commands)
print(fs)

unused_space = TOTAL_SPACE - fs.size
print(f'{unused_space=}')

still_needed = REQUIRED_SPACE - unused_space
print(f'{still_needed=}')

candidates = []
for d in all_directories(fs):
    if d.size >= still_needed:
        candidates.append(d)
print(candidates)
print(min(candidates, key=lambda d: d.size).size)
