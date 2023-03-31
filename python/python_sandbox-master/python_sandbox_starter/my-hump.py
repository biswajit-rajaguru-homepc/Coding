# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules




def myHump(s):
    cs=''
    if s[0].isalpha() : cs = s[0].upper()
    for index in range(1,len(s)):
        if  s[index-1] == ' ':
            cs += s[index].upper()
        else : cs += s[index]
    
    return cs
    


    



# print(date.today(), time.time())