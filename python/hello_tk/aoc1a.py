with open('data', 'r') as f:
    data = f.readlines()
    # for i in range(20):
    #     print(f"{data[i].strip()}")
    elf_index = 0
    item_cnt_for_elf, calorie_cnt_for_elf = [],[]
    item_cnt, calorie_cnt = 0,0
    max_index0, max_index1, max_index2 = 0, 0, 0
    
    for line in data:
        line = line.strip()
        if line == '':
            item_cnt_for_elf.insert(elf_index, item_cnt)
            calorie_cnt_for_elf.insert(elf_index, calorie_cnt)
            
            
            if calorie_cnt > calorie_cnt_for_elf[max_index2]:
                max_index2 = elf_index
                if calorie_cnt_for_elf[max_index2] > calorie_cnt_for_elf[max_index1]:
                    temp = max_index2
                    max_index2 = max_index1
                    max_index1 = temp
                    
                    if calorie_cnt_for_elf[max_index1] > calorie_cnt_for_elf[max_index0]:
                        temp = max_index1
                        max_index1 = max_index0
                        max_index0 = temp
            
            item_cnt, calorie_cnt = 0, 0
            elf_index += 1
            continue
        item_cnt += 1
        calorie_cnt += int(line.strip())
    
    item_cnt_for_elf.insert(elf_index, item_cnt)
    calorie_cnt_for_elf.insert(elf_index, calorie_cnt)
    if calorie_cnt > calorie_cnt_for_elf[max_index2]:
                max_index2 = elf_index
                if calorie_cnt_for_elf[max_index2] > calorie_cnt_for_elf[max_index1]:
                    temp = max_index2
                    max_index2 = max_index1
                    max_index1 = temp
                    
                    if calorie_cnt_for_elf[max_index1] > calorie_cnt_for_elf[max_index0]:
                        temp = max_index1
                        max_index1 = max_index0
                        max_index0 = temp
    item_cnt, calorie_cnt = 0, 0
    elf_index += 1

    print(f"Elf no\t\t Item count\t\t Total Calories")    
    for index in range(elf_index):
        print(f"{index}\t\t{item_cnt_for_elf[index]}\t\t{calorie_cnt_for_elf[index]}\n")
    
    print(f"elf {max_index0} with {item_cnt_for_elf[max_index0]} items and {calorie_cnt_for_elf[max_index0]} calories has the maximum calories")
    print(f"elf {max_index1} with {item_cnt_for_elf[max_index1]} item and {calorie_cnt_for_elf[max_index1]} calories has the 2nd largest calories")
    print(f"elf {max_index2} with {item_cnt_for_elf[max_index2]} item and {calorie_cnt_for_elf[max_index2]} calories has the 3rd largest calories")
    total = calorie_cnt_for_elf[max_index0] + calorie_cnt_for_elf[max_index1] + calorie_cnt_for_elf[max_index2]
    
    print(f"the sum of the three calories is {total}")