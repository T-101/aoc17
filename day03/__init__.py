def day03_1(value):
    ring, max_value = 0, 1

    if max_value == value:
        return 0

    while max_value < value:
        ring += 1
        max_value += 8 * ring

    step_index = (value - 1) % (2 * ring)
    steps = abs(step_index) - ring
    return steps + ring
