#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

args = "{:d} argument"
lenarg = len(sys.argv) - 1
if lenarg == 0:
    args += 's.'
elif lenarg == 1:
    args += ':'
else:
    args += 's:'
print(args.format(lenarg))

i = 0
for arg in sys.argv:
    if i != 0:
        print("{:d}: {:s}".format(i, arg))
    i += 1
