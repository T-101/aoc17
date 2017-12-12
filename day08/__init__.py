import re
import operator

ops = {
    '==': operator.eq,
    '>': operator.gt,
    '<': operator.lt,
    '>=': operator.ge,
    '<=': operator.le,
    '!=': operator.ne,
}


def oper(op):
    operator, value = op.split(" ")
    if operator.lower() == "inc":
        return int(value)
    else:
        return int(value) * -1


def compare(comp, cond):
    conditional, value = cond.split(" ")
    return ops[conditional](comp, int(value))


def day_08_1(data):
    registers = {}
    for row in data:
        try:
            r = re.search(r'^\w+', row).group(0)
        except AttributeError:
            continue
        registers[r] = 0

    for row in data:
        try:
            reg, inc, comp, cond = re.search(r'(\w+)\s(\w+\s-?\d+)\sif\s(\w+)\s(\S+\s-?\d+)', row).groups()
        except AttributeError:
            continue

        registers[reg] = registers[reg] + oper(inc) if compare(registers[comp], cond) else registers[reg]

    return max(registers.items(), key=operator.itemgetter(1))[1]


def day_08_2(data):
    max_val = 0
    registers = {}
    for row in data:
        try:
            r = re.search(r'^\w+', row).group(0)
        except AttributeError:
            continue
        registers[r] = 0

    for row in data:
        try:
            reg, inc, comp, cond = re.search(r'(\w+)\s(\w+\s-?\d+)\sif\s(\w+)\s(\S+\s-?\d+)', row).groups()
        except AttributeError:
            continue

        registers[reg] = registers[reg] + oper(inc) if compare(registers[comp], cond) else registers[reg]
        value = max(registers.items(), key=operator.itemgetter(1))[1]
        if value > max_val:
            max_val = value

    return max_val
