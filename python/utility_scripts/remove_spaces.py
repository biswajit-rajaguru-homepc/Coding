import subprocess as sp 
import re
sp.run(["sh", "-c", "ls > ls_file"])
with open("ls_file","r") as f:
    data = f.readlines()
    
    for line in data:
        
        #test_line = "hi there here i am.pdf"
        words = re.findall(r'[#+\w]+', line.strip())
        name = ""
        if len(words)>1:
        
            for word in words[:-2]:
                name += word + '_'
        
            name += words[-2]  

        name += '.' + words[-1]
        #print(line.strip())
        #print(name)
        cmd = "mv " + "\'" + line.strip() + "\'" + " " + name
        #print(cmd)
        sp.run(["sh", "-c", cmd])




        

