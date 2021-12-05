
def lines2list(filePath, debug=False):
    f = open(filePath, "r")
    lines = f.readlines()

    for i, line in enumerate(lines):
        if debug:
            print(line)
        lines[i] = line.strip().replace('\n', '')
    return lines


def lines2command(filePath, debug=False):
    f = open(filePath, "r")
    lines = f.readlines()
    for i, line in enumerate(lines):
        if debug:
            print(line)
        lines[i] = line.strip().replace('\n', '')
    return [x.split(' ') for x in lines]
