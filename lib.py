import pathlib
import re
import sys

# Todo would be fun to see if I can do something to traverse up the stack to
# calling code and get `__file__`

def get_input(day=None):
    if day is None:
        frame = sys._getframe(0)
        caller_fn = frame.f_back.f_globals['__file__']
        day = int(re.match(r'day_(\d+)\.py', caller_fn).groups()[0])

    in_file = pathlib.Path('input').joinpath(f'{day:02}')
    return in_file.read_text()
