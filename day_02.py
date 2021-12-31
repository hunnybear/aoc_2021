import lib
import re



def run():
    print(part_01())
    print(part_02())


def parse_input():
    for line in lib.get_input().splitlines():
        match = re.match(r'^(up|down|forward|back(?:ward)?)\s+(\d+)$', line)
        direction, amp = match.groups()
        yield (direction, int(amp))


def part_01():
    pos = depth = 0

    for direction, velocity in parse_input():

        if direction == 'up':
            depth -= velocity
        elif direction == 'down':
            depth += velocity
        elif direction == 'forward':
            pos += velocity
        # back is speculative, not used on first problem
        elif direction.startswith('back'):
            pos -= velocity

    return pos * depth


def part_02():
    pos = depth = aim = 0
    for direction, value in parse_input():
        if direction == 'up':
            aim -= value
        elif direction == 'down':
            aim += value
        elif direction == 'forward':
            pos += value
            depth += (aim * value)
        else:
            raise ValueError(direction)

    return pos * depth
run()
