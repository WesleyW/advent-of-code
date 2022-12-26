def is_within_range(x, range):
    return range[0] <= x <= range[1] 


fully_contained = 0
overlaps = 0
with open('input.txt') as f:
    for l in f:
        l = l.strip()
        first, second = l.split(",")
        first_range = [int(i) for i in first.split("-")]
        second_range = [int(i) for i in second.split("-")]
        if (first_range[0] - second_range[0]) * (first_range[1] - second_range[1]) <= 0:
            fully_contained += 1
        if is_within_range(first_range[0], second_range) or \
            is_within_range(first_range[1], second_range) or \
            is_within_range(second_range[0], first_range) or \
            is_within_range(second_range[1], first_range):
            overlaps += 1
            
    
print(overlaps)