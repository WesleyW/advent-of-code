from collections import deque

highest_three = [0] * 3 # sorted low to high
cur = 0
with open("input_1.txt") as f:
    for l in f:
        l = l.strip()
        if l == '':
            highest_three[0] = max(highest_three[0], cur)
            highest_three = sorted(highest_three)
            cur = 0
        else:
            cur += int(l)
print(sum(highest_three))
