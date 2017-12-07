import re


def day07_1(arr):
    node_arr, support_arr = [], []

    for row in arr:
        node_arr.append(re.match(r'[\w]+', row).group(0))
        if re.search(r'->', row):
                nodes = re.search(r'->\s(?P<nodes>[\w,\s]+)', row).group('nodes').replace(' ', '').split(',')
                for node in nodes:
                    support_arr.append(node)

    for node in node_arr:
        if node not in support_arr:
            return node
