with open('puzzle_3_data','r') as f:
    data = f.readlines()
    repeat = []
    total = 0
    cntr = 0
    for line in data:
        line = line.strip()
        l = len(line)
        # print(line, l)
        half = int(l/2)
        w1, w2 = line[0:half], line[half:l]
        # print(line,w1, w2)
        cnt = [0]*200
        repeat_c = 0
        for c in w1:
            cnt[ord(c)] += 1
        for c in w2:
            if cnt[ord(c)] != 0:
                repeat_c = ord(c)
                break
        repeat.insert(cntr,chr(repeat_c))
        total += repeat_c - 38 if repeat_c < 91 else repeat_c - 96
        # print(line, w1, w2, repeat[cntr] )
        cntr += 1
    
    # print(f"Total priority of misplaced is {total}")
   
    # ------------------ second part
   
    no_of_groups = int(len(data)/3)
    total_badges = 0
   
    for i in range(no_of_groups):
        
        l0, l1, l2 = data[i*3].strip(), data[i*3 + 1].strip(), data[i*3 + 2].strip()
        print(f"Group {i}:\n{l0},\n{l1},\n{l2}\n\n")
        
        cnt = [0]*200
        dummy=[]
        badge = 0
        
        for c in l0:
            cnt[ord(c)]=1
            dummy.append(chr(ord(c)))
        
        # print(dummy)
        dummy = []
        
        for i in range(200):
            if cnt[i]==1:
                dummy.append(chr(i))
        # print(dummy)
        # print([chr(index) for (index,x) in enumerate(cnt) if x == 1])
        
        
        for c in l1:
            if cnt[ord(c)]==1:
                    cnt[ord(c)] = 2 
            else:
                cnt[ord(c)] = 0 
        # print([chr(index) for (index,x) in enumerate(cnt) if x == 1])
        dummy = []
        for c in range(200):
            if cnt(c) == 2:
                dummy.append(chr(c))
        print(dummy)
        
        
        
        # for c in l2:
        #     if cnt[ord(c)] == 2:
        #         badge = ord(c) 
        #         break
        
        for c in l2:
            cnt[ord(c)] = 3 if cnt[ord(c)] == 2 else cnt[ord(c)]
        
        badge = [chr(index) for (index,value) in enumerate(cnt) if value == 3] 
                
        print(badge,"\n")
        if badge !=[]:
            total_badges += ord(badge[0]) - ord('A') + 27 if ord(badge[0]) < 91 else ord(badge[0]) - ord('a') + 1
    
    print(f"The total of the badge priorities is {total_badges}")               
    

