filename = "day1/input.txt"

curr = 50
bound = 100
count_zero = 0

with open(filename, "r") as f:

    for line in f:
        line = line.strip()
        if not line:
            continue
    
        dir = line[0]
        moves = int(line[1:])

        rotations = moves // bound
        count_zero += rotations
        
        rem = moves % bound
        if dir == "L":
            if (curr - rem) < 0 and curr != 0:
                count_zero += 1
            curr -= rem
        elif dir == "R":
            if (curr + rem) > bound:
                count_zero += 1
            curr += rem
        else:
            raise ValueError("Invalid input")

        curr %= bound
        if curr == 0:
            count_zero += 1


    print(count_zero)