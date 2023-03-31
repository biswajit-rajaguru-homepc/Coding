with open('puzzle_2_data', 'r') as f:
    data = f.readlines()
    scorecard = { 
                 'AX' : 3,
                 'AY' : 4,
                 'AZ' : 8,
                 'BX' : 1,
                 'BY' : 5,
                 'BZ' : 9,
                 'CX' : 2,
                 'CY' : 6,
                 'CZ' : 7
                 }
    total_score = 0
    for line in data:
        [p1, p2] = line.strip().split()
        score = scorecard[p1+p2]
        total_score += score
        print(p1, p2, score)
    
    print(f"\n\nTotal score is: {total_score} ")
        
        

