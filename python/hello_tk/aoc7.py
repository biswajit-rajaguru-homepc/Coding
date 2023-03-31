from util import *
class myfile:
    def __init__(self, name):
        self.name = name
        self.size = 0
    
        
    def set_size(self, size):
        self.size = size

class cmd:
    def __init__(self, cmd, output):
        self.cmd = cmd
        self.output = output

class directory_entry:
    def __init__(self,name,mytype):
        self.name = name
        self.type = mytype
        self.element = directory(name)  if mytype == "dir" else myfile(name)


def get_next_cmd_output(list):
        new_cmd = ""
        output = []
        while(len(list) > 0):
            line = list[0]
            # print(line)
            if line[0] == '$' and new_cmd == "":
                new_cmd = line[2:].strip()
                # print(new_cmd)
                output = []
            elif line[0] =='$' and new_cmd != "":
                # print(new_cmd,'\n',output)
                New_cmd = cmd(new_cmd, output)
                return [list, New_cmd]
            else:
                output.append(line.strip())
                # print(output)
            if len(list) > 1:
                list = list[1:]
                # print(len(list))
            else:
                list = []
        
        if new_cmd=="":
            return [[],None]
        else:
            New_cmd = cmd(new_cmd, output)
            return [[], New_cmd]




class directory:
    def __init__(self, name):
        self.entries = []
        self.name = name
        
    def create_directory_from_ls_and_cd_output(self, list):
        while(len(list) > 0):
            [list, cmd_output] = get_next_cmd_output(list)
            cmdline = cmd_output.cmd.strip().split()
            if cmdline[0] == 'ls':
                # print("LS:  ", cmd_output.cmd, "\n", cmd_output.output) 
                for line in cmd_output.output:
                    [entry_type_or_size,entry_name] = line.strip().split()
                    if entry_type_or_size == 'dir':
                        newentry = directory_entry(entry_name, 'dir')
                        self.entries.append(newentry)
                    else:
                        entry_size = int(entry_type_or_size.strip())
                        newentry = directory_entry(entry_name, 'file')
                        newentry.element.set_size(entry_size)
                        self.entries.append(newentry)
                        
                
                              
            
            elif cmdline[0] == 'cd' and cmdline[1] != "..":
                # print("CD:  ", cmd_output.cmd, "\n", cmd_output.output)               
                dirname = cmdline[1]
                dirlist = [entry.name for entry in self.entries if entry.type == 'dir']
                if dirname not in dirlist:
                    newentry = directory_entry(dirname,'dir')
                    self.entries.append(newentry)
                for entry in self.entries:
                    if entry.type == 'dir' and entry.name == dirname:
                        list = entry.element.create_directory_from_ls_and_cd_output(list)
                                                
                    
                
            elif cmdline[0] == 'cd' and cmdline[1] == '..':
                return list
        return []
       
                

with open('puzzle_7_data', 'r') as f:
    list = [line.strip() for line in f.readlines()]

# for line in list:
#     print(line)
def test_get_next_cmd_output():
    while (len(list) > 0):
        len1 = len(list)
        [list,next_cmd] = get_next_cmd_output(list)
        # len2 =len(list)
        # print(len1, len2)
        Output = ""
        for line in next_cmd.output:
            Output += line+'\n'
        print(f"{'.'*80}\n{len1}{' '*30+next_cmd.cmd}\n\n{Output}\n")
    

def create_filesystem():
    file_system = directory("file_system")
    file_system.create_directory_from_ls_and_cd_output(list)
    return file_system


def display_directory_structure(directory, offset):
    for entry in directory.entries:
        if entry.type == 'dir':
            node_str = "d: " + bcolors.OKGREEN + entry.name + bcolors.ENDC
            print(" "*offset + node_str)
            
            display_directory_structure(entry.element, offset + len("d: "))
        else:
            node_str = "f: " + entry.name + ' '*5 + bcolors.OKBLUE + str(entry.element.size) + bcolors.ENDC
            print(" "*offset + node_str)

          
def find_small_directories(directory, total_num_till_now, total_size_till_now):
    self_size = 0
    for entry in directory.entries:
        if entry.type == 'dir':
            [entry_size, total_num_till_now,total_size_till_now] = find_small_directories(entry.element, total_num_till_now, total_size_till_now)
            self_size += entry_size
        else:
            self_size += entry.element.size
    if self_size <= 100000:
        total_num_till_now += 1
        total_size_till_now += self_size
    
    return [self_size, total_num_till_now, total_size_till_now]

def find_size_of_directory(directory):
    self_size = 0
    for entry in directory.entries:
        if entry.type == 'dir':
            entry_size = find_size_of_directory(entry.element)
            self_size += entry_size
        else:
            self_size += entry.element.size
    
    return self_size

def find_smallest_directory_which_exceeds_target(directory, target):
    
    smallest_size = 100000000
    smallests = None
    for entry in directory.entries:
        
        if entry.type == 'dir':
            [smallest_size_in_entry, smallests_in_entry] = find_smallest_directory_which_exceeds_target(entry.element, target)
            if smallests_in_entry != None and smallest_size_in_entry < smallest_size:
                smallest_size = smallest_size_in_entry
                smallests = smallests_in_entry
    
    if smallests != None and smallest_size >= target:
        return [smallest_size, smallests]
    else:
        this_size = find_size_of_directory(directory)
        if this_size >= target:
            return [this_size, directory]
        else:
            return [0, None]


    
    
    
    


file_system = create_filesystem()
display_directory_structure(file_system,0)
[total_size, total_num_of_small_directories, total_size_of_small_directories] = find_small_directories(file_system, 0, 0)
print(f"Total size of file system: {total_size}")
print(f"Total number of directories whose size is less than 100000: {total_num_of_small_directories}")
print(f"Total size of the directories whose size is less than 100000: {total_size_of_small_directories}")
target = total_size - 40000000
print("Target: ",target)

[smallest_size, d] = find_smallest_directory_which_exceeds_target(file_system, target)
if smallest_size != find_size_of_directory(d):
    print("ERROR")
print(f"The directory: {d.name}, is the smallest directory with size {smallest_size} whose size exceeds target: {target}")

                       