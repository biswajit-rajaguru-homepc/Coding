# Python has functions for creating, reading, updating, and deleting files.

# myfile = open('myfile.txt', 'w')

# print(f'file name :{myfile.name}, \nis_closed {myfile.closed} \nmode {myfile.mode}')
# myfile.write('Biswajit : Hello World\n')
# myfile.write('Bye')
# myfile.close()

myfile = open('myfile.txt', 'r+')
file_text = myfile.read(100)

myfile.close()

print(file_text)


