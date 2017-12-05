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


def day03_2(value):
    # Verbose, but works
    def sum_neighbours(arr, xx, yy):
        result = 0

        result += arr[xx - 1][yy]
        result += arr[xx + 1][yy]

        result += arr[xx][yy - 1]
        result += arr[xx][yy + 1]

        result += arr[xx - 1][yy - 1]
        result += arr[xx - 1][yy + 1]

        result += arr[xx + 1][yy - 1]
        result += arr[xx + 1][yy + 1]

        return result

    # create matrix and zerofill
    m = []
    for x in range(11):
        m.append([])
        for y in range(11):
            m[x].append(0)

    # Position to center and set initial value to 1
    x, y = 4, 4
    m[x][y] = 1

    # Set initial neighbour before automation
    x += 1
    m[x][y] = 1
    largest = 1

    while largest < value:
        if m[x-1][y] != 0 and m[x][y+1] == 0:       # move up
            y += 1
        elif m[x-1][y] == 0 and m[x][y-1] != 0:     # move left
            x -= 1
        elif m[x+1][y] != 0 and m[x][y-1] == 0:     # move down
            y -= 1
        elif m[x+1][y] == 0 and m[x][y+1] != 0:     # move right
            x += 1

        largest = sum_neighbours(m, x, y)
        m[x][y] = largest

    return largest
