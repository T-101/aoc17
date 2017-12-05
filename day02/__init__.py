def day_02_1(input_data):
    result = 0
    for row in input_data:
        result += max(row) - min(row)

    return result


def day_02_2(input_data):
    result = 0
    for row in input_data:
        while len(row):
            test_val = row.pop(0)
            for item in row:
                if max(item, test_val) % min(item, test_val) == 0:
                    result += int(max(item, test_val) / min(item, test_val))

    return result
