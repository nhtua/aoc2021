#!/usr/bin/env python

import helper

commands = helper.lines2command('input/day02.txt', debug=True)


def command_v1():
    dimension = {
        "x": 0,
        "z": 0
    }

    for cmd in commands:
        if cmd[0] == 'forward':
            dimension['x'] += int(cmd[1])
        elif cmd[0] == 'up':
            dimension['z'] -= int(cmd[1])
        else:
            dimension['z'] += int(cmd[1])

    return (dimension['x']*dimension['z'])


def command_v2():
    dimension = {
        "x": 0,
        "z": 0,
        "a": 0
    }

    for cmd in commands:
        if cmd[0] == 'forward':
            dimension['x'] += int(cmd[1])
            dimension['z'] += dimension['a'] * int(cmd[1])
        elif cmd[0] == 'up':
            dimension['a'] -= int(cmd[1])
        else:
            dimension['a'] += int(cmd[1])

    return (dimension['x']*dimension['z'])


print(f"V1 {command_v1()}")
print(f"V2 {command_v2()}")
