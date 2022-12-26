# READ ON FOR UGLY CODE
import re
from collections import defaultdict

is_part_1 = False
stacks = defaultdict(list)
with open('input.txt') as f:
    is_init = True
    for l in f:
        if is_init:
            l = l.strip("\n\r")
            if re.search('\d', l):
                is_init = False
                continue
            for i, x in enumerate(l):
                if re.match('[^ \[\]]', x):
                    stack_i = ((i - 1) // 4) + 1
                    stacks[stack_i] = [x] + stacks[stack_i]
        else:
            match = re.match('move (\d+) from (\d+) to (\d+)', l.strip())
            if match:
                to_move, start, end = [int(x) for x in match.groups()]
                if is_part_1:
                    crates = [stacks[start].pop() for x in range(to_move)]
                else:
                    crates = stacks[start][-1 * to_move:]
                    del stacks[start][-1 * to_move:]
                stacks[end] += crates

print(''.join([stacks[i][-1] if stacks[i] else ' ' for i in range(1, max(stacks.keys()) + 1)]))
