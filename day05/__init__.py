def day05_1(data):
    steps, currpos = 0, 0

    mutable_data = data.copy()

    while currpos < len(mutable_data):
        oldpos = currpos
        currpos += mutable_data[currpos]
        mutable_data[oldpos] += 1
        steps += 1

    return steps


def day05_2(data):
    steps, currpos = 0, 0

    mutable_data = data.copy()

    while currpos < len(mutable_data):
        oldpos = currpos
        currpos += mutable_data[currpos]
        if mutable_data[oldpos] >= 3:
            mutable_data[oldpos] -= 1
        else:
            mutable_data[oldpos] += 1
        steps += 1

    return steps
