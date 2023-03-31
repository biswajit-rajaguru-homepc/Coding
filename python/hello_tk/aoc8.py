
def display_visibility(visibility):
    display_string = ""
    for row in visibility:
        for cell in row:
            if cell == 1:
                col = "\u001b[38;2;255;255;255m"
            else:
                col = "\u001b[38;2;100;100;100m"
            display_string += col + str(cell) + "\u001b[0m"
        display_string += '\n'
    return display_string

def display_forest(grid, visibility):
    display_string = ""
    for i,row in enumerate(grid):
        for j,elt in enumerate(row):
            if visibility[i][j] == 1:
                cell = "\u001b[38;2;150;150;255m"
            else:
                cell = "\u001b[38;2;0;0;100m"#"\u001b[38;5;20m"
            display_string += cell + elt + "\u001b[0m"
            
        display_string += '\n'
    
    return display_string



with open('puzzle_8_data','r') as f:
    data = f.readlines()
    grid = []
    visibility = []
    for line in data:
        row = line.strip()
        grid.append([x for x in row])
        visibility.append([0 for _ in range(len(row))])
        
                
num_visible_trees = 0


def find_visibility(i,j,grid):
    ht = int(grid[i][j])
    rv, lv, tv, bv = True, True, True, True
    
    for tree in grid[i][j+1:]:
        if int(tree) >= ht:
            rv = False
            break
    
    for tree in grid[i][:j]:
        if int(tree) >= ht:
            lv = False
            break
    
    for r in grid[:i]:
        if int(r[j]) >= ht:
            tv = False
            break
    for r in grid[i+1:]:
        if int(r[j]) >= ht:
            bv = False
            break
    
    return int(rv or lv or tv or bv)
    
    


def find_scenic_score(i, j, grid):
    
    score = 1
    distance_r = 0
    for tree in grid[i][j+1:]:
        distance_r += 1
        if int(tree) >= int(grid[i][j]):
            break
    score *= distance_r
    
    distance_l = 0
    for tree in list(reversed(grid[i][:j])):
        distance_l += 1
        if int(tree) >= int(grid[i][j]):
            break
    score *= distance_l
    
        

    distance_t = 0
    for row in list(reversed(grid[:i])):
        distance_t += 1
        if int(row[j]) >= int(grid[i][j]):
            break
    score *= distance_t
    
    
        
    distance_b = 0
    for row in grid[i+1:]:
        distance_b += 1
        if int(row[j]) >= int(grid[i][j]):
            break
    score *= distance_b
    
    
    return score
    

top_scenic_score, ii, jj = 0, 0, 0;
for (i,row) in enumerate(grid):
    for (j,col) in enumerate(row):
        
        #---- part (a)
        visibility[i][j] = find_visibility(i, j, grid)
        num_visible_trees += visibility[i][j]
        
        #---- part (b)
        scenic_score = find_scenic_score(i, j, grid)
        if scenic_score > top_scenic_score:
            top_scenic_score = scenic_score
            ii, jj = i, j


        
        




            

print(f"the no of visible trees is {num_visible_trees}")
print(f"Top Scenic score: {top_scenic_score} for tree with coordinates: ({ii},{jj})")
print(display_forest(grid, visibility))
print(display_visibility(visibility))



