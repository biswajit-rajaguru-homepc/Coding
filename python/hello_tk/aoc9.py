with open('puzzle_9_data', 'r') as f:
    file_input = f.readlines()

head_motions = []
tail_motions = []
for line in file_input:
    line = line.strip().split()
    move_type = line[0]
    move_arg =int(line[1])
    
    head_motions += [move_type] * move_arg

# for x in head_motions:
#     print(x, end="")

# exit(0)

# head_x, head_y, tail_x, tail_y = 0, 0, 0, 0
# head_path, tail_path = set(), set()
# head_path.add((0,0))
# tail_path.add((0,0))

# for head_motion in head_motions:
#     match head_motion:
        
#         case 'R':
#             head_x += 1
#             head_path.add((head_x,head_y))
#             if head_x-tail_x == 2:
#                 tail_x += 1
#                 if tail_y != head_y:
#                     tail_y = head_y
#                 tail_motions.append('R')
#                 tail_path.add((tail_x,tail_y))
        
#         case 'L':
#             head_x -= 1
#             head_path.add((head_x,head_y))
#             if head_x - tail_x == -2:
#                 tail_x -= 1
#                 if tail_y != head_y:
#                     tail_y = head_y
#                 tail_motions.append('L')
#                 tail_path.add((tail_x,tail_y))
                
        
#         case 'U':
#             head_y -= 1
#             head_path.add((head_x,head_y))
#             if head_y - tail_y == -2:
#                 tail_y -= 1
#                 if tail_x != head_x:
#                     tail_x = head_x
#                 tail_motions.append('U')
#                 tail_path.add((tail_x,tail_y))
                
        
#         case 'D':
#             head_y += 1
#             head_path.add((head_x,head_y))
#             if head_y - tail_y == 2:
#                 tail_y += 1
#                 if tail_x != head_x:
#                     tail_x = head_x
#                 tail_motions.append('D')
#                 tail_path.add((tail_x,tail_y))
                
  
# print(len(tail_path))
    
    
#----------------- part 2
import curses
import time

def initialize_curses():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(False)
    if curses.has_colors():
        curses.start_color()
    # Optional - Enable the keypad. This also decodes multi-byte key sequences
    # stdscr.keypad(True)
    return stdscr

def shutdown_curses():
    curses.nocbreak()
    curses.echo()
    curses.curs_set(True)
    # stdscr.keypad(False)
    curses.endwin()



def display_nodes(paths):
    stdscr = initialize_curses()
    caught_Exception = ""
    try:
        
        length = len(paths[0])
        for i in range(length):
            stdscr.erase()
            x_offset = (paths[0][i][0]//50)*50
            y_offset = (paths[0][i][1]//14)*14
            stdscr.addstr(0,0,f"step {i} of {length}, x-off: {x_offset}, y-off: {y_offset}")
            test_str = ""
            for n in range(10):
                x_pos = paths[n][i][0] - x_offset + 70
                y_pos = paths[n][i][1] - y_offset + 25
                stdscr.addstr(n+1,0,f"({x_pos},{y_pos})")
                stdscr.addstr(y_pos, x_pos, str('.'))
            
            # stdscr.addstr(curses.LINES//2,curses.COLS//2,test_str)
            # stdscr.addstr(curses.LINES//5,(curses.COLS-len(test_str))//2,test_str)
            stdscr.refresh()
            time.sleep(0.001)
            # if i > 10:
            #     break
                
        
        
    
    
    except Exception as err:
        caught_Exception = str(err)
    
    stdscr.getch()
    shutdown_curses()
    if caught_Exception != "":
        print(f"Caught Exception from curses try block.\n{caught_Exception}")
    
            
            
        
    
    


origin = (0,0)
nodes_x, nodes_y = [0]*10, [0]*10
paths = [[origin] for _ in range(10)]

def update_nodes_and_paths(nodes_x, nodes_y, paths):
    for i in range(1,10):
        sdx, sdy = 0, 0
        dx = nodes_x[i-1] - nodes_x[i]
        dy = nodes_y[i-1] - nodes_y[i]
        if dx == 2 or dx == -2 or dy == 2 or dy == -2:
            if dx == 0:
                sdx = 0
            elif dx > 0:
                sdx = 1
            else:
                sdx = -1
            
            if dy == 0:
                sdy = 0
            elif dy > 0:
                sdy = 1
            else:
                sdy = -1
        nodes_x[i] += sdx
        nodes_y[i] += sdy
    
    for i in range(10):
        paths[i].append((nodes_x[i], nodes_y[i]))
    
    return [nodes_x,nodes_y,paths]
     
        
        
        

for head_motion in head_motions:
    
    match head_motion:
        case 'R':
            nodes_x[0] += 1
            [nodes_x, nodes_y, paths] = update_nodes_and_paths(nodes_x, nodes_y, paths)
            
        case 'L':
            nodes_x[0] -= 1
            [nodes_x, nodes_y, paths] = update_nodes_and_paths(nodes_x, nodes_y, paths)
        case 'U':
            nodes_y[0] -= 1
            [nodes_x, nodes_y, paths] = update_nodes_and_paths(nodes_x, nodes_y, paths)
        case 'D':
            nodes_y[0] += 1
            [nodes_x, nodes_y, paths] = update_nodes_and_paths(nodes_x, nodes_y, paths)
display_nodes(paths)


traces = [ set(path) for path in paths]

print(f" The no of distinct points traversd by the last node: {len(traces[9])}")

    