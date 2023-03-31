import subprocess as sp

class stack:
    def __init__(self):
        self.stk = []
    
    def pushm(self, data):
        self.stk += data
        return data
    
    def push(self, data):
        self.stk.append(data)
        return data
    
    def pop(self):
        if len(self.stk) < 1:
            return None
        data = self.stk[-1]
        self.stk = self.stk[:-1]
        return data
    
    def popm(self, n=1):
        if len(self.stk) < n:
            return None
        
        data = self.stk[-n:]
        self.stk = self.stk[:-n]
        return data
    def len(self):
        return len(self.stk)
    
    def __str__(self):
        s = ""
        for item in list(reversed(self.stk)):
            s += item+"\n"
        return s
    def get(self, index):
        if index >= len(self.stk):
            return None
        return self.stk[index]
    
  

def display_stacks(stacks):
    display = []
    level = 0
    # print(len(stacks))
    while(True):
        remaining = len(stacks)
        # print(remaining)
        line = ""
        for stk in stacks:
            # print(stk.len())
            if level>= stk.len():
                remaining -= 1
                line += " " + "  "
            else:
                line += ""+stk.get(level) + "  "
            
        if remaining == 0:
            break
        level += 1
        display.append(line)
    
    # print(len(display))
    display.reverse()
    for line in display:
        print(line)
    
  

# class test:
    
#     def __init__(self):
#         self.name = []
        
#     def push(self, name):
#         self.name.append(name)
    
#     def __str__(self):
#         s = ""
#         for item in self.name:
#             s += item + " "
#         return s
    

# names = [test() for _ in range(3)]
# for idx, item in enumerate(names):
#     item.push(str(idx))
#     item.push("  ")
#     item.push(str(idx)*5)

# for item in names:
#     print(item)

# exit(0)


with open('puzzle_5_data', 'r') as f:
    file = f.readlines()
    stack_ids = file[8].split()
    # print(stack_ids, file[7][1])
    stacks = [stack() for _ in stack_ids]
    # print(stacks[0])
    for (index, stk) in enumerate(stacks):
        # if index != 0:
        #     print(stacks[index - 1])
        stk.push(stack_ids[index])
        ROW = 8
        COL = 1 + 4*index
        while(ROW > 0):
            ROW -= 1
            item = file[ROW][COL]
            if item == " ":
                break
            stk.push(item)
        
    
    # display_stacks(stacks)
    
    for step in file[10:]:
        tokens = step.strip().split()
        n, frm, to = int(tokens[1]), int(tokens[3]), int(tokens[5])
        frm -= 1
        to -= 1
        
        #---- Move 1 crate at a time
        # for _ in range(n):
        #     v = stacks[frm].pop()
        #     stacks[to].push(v)
        
        #---- Move mutiple crates at a time
        
        v = stacks[frm].popm(n)
        stacks[to].pushm(v)
        
        sp.run(["bash","-c", "sleep .1 && clear"])
        
        display_stacks(stacks)
        
        
    display_stacks(stacks)    
    
    
                
                
            
            
   
    
    # stacks[0].push("hello")
    # stacks[1].push("world")
    # print(stacks[0], stacks[1])    
    # a = stack()
    # b = stack()
    # print("---", a, b)
    # print(stacks[0])
    
            
    


            
    
    
    
    
