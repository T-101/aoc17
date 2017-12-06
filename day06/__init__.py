def day_06_1(arr):

    temp_arr = arr.copy()
    states = []

    while True:
        max_val = max(temp_arr)
        index = temp_arr.index(max_val)

        for i in range(max_val):
            temp_arr[(i + 1 + index) % len(temp_arr)] += 1
            temp_arr[index] -= 1

        states.append(temp_arr.copy())

        if states.count(temp_arr) == 2:
            return len(states)


def day_06_2(arr):

    temp_arr = arr.copy()
    states = []

    while True:
        max_val = max(temp_arr)
        index = temp_arr.index(max_val)

        for i in range(max_val):
            temp_arr[(i + 1 + index) % len(temp_arr)] += 1
            temp_arr[index] -= 1

        states.append(temp_arr.copy())

        if states.count(temp_arr) == 2:
            positions = []
            for i in range(len(states)):
                if states[i] == temp_arr:
                    positions.append(i)
            return max(positions) - min(positions)
