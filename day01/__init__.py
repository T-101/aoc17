def day01_1(input_data):
    result = 0
    for i in range(len(input_data)):
        if int(input_data[i]) == int(input_data[(i + 1) % len(input_data)]):
            result += int(input_data[i])

    return result


def day01_2(input_data):
    result = 0
    for i in range(len(input_data)):
        if int(input_data[i]) == int(input_data[(i + int(len(input_data) / 2)) % len(input_data)]):
            result += int(input_data[i])

    return result
