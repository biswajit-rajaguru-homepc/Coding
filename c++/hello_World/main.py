
with open('text.txt','r') as f:
    data = f.read()


from ast import pattern
import re

pat = re.compile(r'(https?://)?(w{3}\.)?(\w+\.)[a-z]{3}')

matches = pat.finditer(data)

for match in matches:
    print(match)
    
