with open('puzzle_4_data', 'r') as f:
    data = f.readlines()
    assignment_pairs = [line.strip() for line in data]
    # print(assignment_pairs)
    num_contains,num_any_overlap = 0, 0
    def get_set_from_range(num_range):
        bounds = [int(x) for x in num_range.strip().split('-')]
        return set(range(bounds[0], bounds[1]+1))
        
    for (index,pair) in enumerate(assignment_pairs):
        ranges = [get_set_from_range(x) for x in pair.split(',')]
        if ranges[0].issubset(ranges[1]) or ranges[0].issuperset(ranges[1]):
            print(f"{index}: {pair}")
            num_contains += 1
        if ranges[0].intersection(ranges[1]):
            num_any_overlap += 1
    
    print(f"the total no of pairs in which one range contains the other is {num_contains}\nthe total no of pairs in which the two ranges have non empty intersection is {num_any_overlap}")
            
    