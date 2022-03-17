import sys

for line in sys.stdin:
    line = int(line)
    if line == 0:
        print("Y")
    elif line % 6 == 0:
        print("Y")
    else:
        print("N")


