# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

person = {
    'fn' : 'biswajit',
    'ln' : 'rajaguru',
    'age' : 37
}

person1 = dict(fn = 'gorachand', ln='rajaguru', age=47)
person2 = person.copy()
person3 = person
person2['location'] = 'Kolkata'
person3['color'] = 'black'
print(person)
print(person2)
print(person3)
# print(person1.get('age'))

