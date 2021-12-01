#!/usr/bin/python
import helper
import sys
sys.setrecursionlimit(999999)


def detect_v1(scans: list, count=0):
    if len(scans) <= 1:
        return count

    if scans[0] < scans[1]:
        return detect_v1(scans[1:], count=count+1)
    return detect_v1(scans[1:], count)


def detect_v2(scans: list, count=0):
    if len(scans) <= 3:
        return count
    if sum(scans[0:3]) < sum(scans[1:4]):
        return detect_v2(scans[1:], count=count+1)
    return detect_v2(scans[1:], count)


if __name__ == '__main__':
    sonar_scans = helper.lines2list('input/day01.txt', debug=False)
    sonar_scans = [int(x) for x in sonar_scans]
    count1 = detect_v1(sonar_scans, 0)
    print("V1: Sea floor inceased %d times" % count1)
    count2 = detect_v2(sonar_scans, 0)
    print("V2: Sea floor inceased %d times" % count2)
