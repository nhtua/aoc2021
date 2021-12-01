
def lines2list(filePath, debug=False):
    f = open(filePath, "r")
    lines = f.readlines()

    for i, line in enumerate(lines):
        if debug:
            print(line)
        lines[i] = line.strip().replace('n', '')
    return lines
