import lib


def _helper(lines):
    vals = [0] * len(lines[0])

    for line in lines:
        for i, bit in enumerate(line):
            if int(bit):
                vals[i] += 1
            else:
                vals[i] -= 1
    return vals


def get_gamma_raw(lines):
    """most common bit"""
    return ''.join('1' if v > 0 else '0' for v in _helper(lines))


def get_epsilon(lines):
    """least common bit """
    return int(''.join('0' if c == '1' else '1' for c in get_gamma_raw(lines)),2)


def get_gamma(lines):
    return int(get_gamma_raw(lines), 2)


def run():
    in_lines = lib.get_input().splitlines()

    gamma = get_gamma(in_lines)
    epsilon = get_epsilon(in_lines)

    print((gamma, epsilon, gamma * epsilon))

run()
