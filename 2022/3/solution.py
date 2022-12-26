is_part_1 = False

def get_priority(char):
    o = ord(char)
    if o >= ord('a'):
        return o - ord('a') + 1
    else:
        return o - ord('A') + 1 + 26

priorities = 0

with open('input.txt') as f:
    potential_badge = None
    compared = 0
    for l in f:
        l = l.strip()
        if is_part_1:
            first = set(l[:len(l) // 2])
            second = set(l[len(l) // 2:])
            compartment_overlap = (first & second).pop()
            priorities += get_priority(compartment_overlap)
        else:
            cur_bag = set(l)
            potential_badge = potential_badge & cur_bag if potential_badge else cur_bag
            compared += 1
            if compared == 3:
                compared = 0
                priorities += get_priority(potential_badge.pop())
                potential_badge = None

print(priorities)