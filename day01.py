#!/usr/bin/python
import helper
import sys
sys.setrecursionlimit(999999)


def detect_increasing_depth(scans: list, count=0):
    try:
        current_depth = scans.pop(0)
        scans[0]
    except IndexError:
        return count

    if int(current_depth) < int(scans[0]):
        return detect_increasing_depth(scans, count=count+1)
    return detect_increasing_depth(scans, count)


if __name__ == '__main__':
    sonar_scans = helper.lines2list('input/day01.txt', debug=False)
    count = detect_increasing_depth(sonar_scans, 0)
    print("Sea floor inceased %d times" % count)
