#!/usr/bin/env python
GAME_MODE = 'noob'
import helper

results = helper.lines2list('input/day01.txt', debug=False)
results = [int(x) for x in results]


def detect(results, steps=1):
    count = 0
    for i, item in enumerate(results):
        if len(results[i:i+steps]) >= steps:
            if sum(results[i:i+steps]) < sum(results[i+1:i+steps+1]):
                count += 1
    return count


print(f"Part 1 {detect(results, 1)}")
print(f"Part 2 {detect(results, 3)}")
