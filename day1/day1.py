filename = "day1/input.txt"

curr = 50
count_zero = 0

with open(filename, "r") as f:

    for line in f:
        line = line.strip()
        if not line:
            continue

        if line[0] == "L":
            curr -= int(line[1:])
        elif line[0] == "R":
            curr += int(line[1:])
        else:
            raise ValueError("Invalid input")

        curr %= 100
        if curr == 0:
            count_zero += 1

    print(count_zero)