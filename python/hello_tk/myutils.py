def myrgb(red,green,blue):
    red %= 255
    blue %= 255
    green %= 255
    hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    code = '#' + hex[int(red/16)] + hex[red%16] + hex[int(green/16)] + hex[green%16] + hex[int(blue/16)] + hex[blue%16]
    return code

# inp = input('<red,green,blue>')
# inp = inp.split(',')
# values =  [int(x) for x in inp]
# print(myrgb(values[0],values[1],values[2]))
# # print(values, "", end="")
