with open('puzzle_3_data', 'r') as f:
    data = f.readlines()
    rucksacks = [line.strip() for line in data]
    
    total_priorities_of_misplaced_items = 0
    for rucksack in rucksacks:
        left_half = set(rucksack[:len(rucksack)//2])
        right_half = set(rucksack[len(rucksack)//2:])
        misplaced_item = left_half.intersection(right_half).pop()
        if misplaced_item.isupper():
            total_priorities_of_misplaced_items += ord(misplaced_item) - ord('A') + 27
        elif misplaced_item.islower():
            total_priorities_of_misplaced_items += ord(misplaced_item) - ord('a') + 1
    
    
    print("total priorities of misplaced items", total_priorities_of_misplaced_items)

# --------------- part 2

with open('puzzle_3_data', 'r') as f:
    data = f.readlines()
    rucksacks = [line.strip() for line in data]
    
    total_priorities_of_badges = 0
    while len(rucksacks) > 0:
        first = set(rucksacks.pop())
        second = set(rucksacks.pop())
        third = set(rucksacks.pop())
        
        badge = first.intersection(second).intersection(third).pop()
        print(badge)
        if badge.isupper():
            total_priorities_of_badges += ord(badge) - ord('A') + 27
        elif badge.islower():
            total_priorities_of_badges += ord(badge) - ord('a') + 1
    
    
    print("total priorities of badges: ", total_priorities_of_badges)
