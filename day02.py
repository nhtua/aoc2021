#!/usr/bin/env python

import helper

commands = helper.lines2command('input/day02.txt', debug=True)


def command_v1():
    horizon = 0
    depth = 0

    for cmd in commands:
        if cmd[0] == 'forward':
            horizon += int(cmd[1])
        elif cmd[0] == 'up':
            depth -= int(cmd[1])
        else:
            depth += int(cmd[1])

    return (horizon*depth)


def command_v2():
    horizon = 0
    depth = 0
    aim = 0

    for cmd in commands:
        if cmd[0] == 'forward':
            horizon += int(cmd[1])
            depth += aim * int(cmd[1])
        elif cmd[0] == 'up':
            aim -= int(cmd[1])
        else:
            aim += int(cmd[1])

    return (horizon*depth)


print(f"V1 {command_v1()}")
print(f"V2 {command_v2()}")
