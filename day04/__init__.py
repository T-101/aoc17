def day04_1(arr):
    ret_arr = []

    for row in arr:
        fail = False
        row_temp = row.split()
        while len(row_temp):
            test_val = row_temp.pop(0)
            for item in row_temp:
                if test_val == item:
                    fail = True

        if not fail:
            ret_arr.append(row)
    return ret_arr


def day04_2(arr):
    ret_arr = []
    for row in arr:
        fail = False
        row_temp = row.split()
        while len(row_temp):
            sorted_word = ''.join(sorted([s for s in row_temp.pop(0)]))
            for item in row_temp:
                if sorted_word == ''.join(sorted([s for s in item])):
                    fail = True

        if not fail:
            ret_arr.append(row)
    return ret_arr
