# A List is a collection which is ordered and changeable. Allows duplicate members.
numbers = [1, 2, 3, 4, 5, 6]
numberss = list('My name is Biswajit Rajaguru'.split())
numbers.append('hello')
print(numbers, len(numbers))
numbers.remove(3)
print(numbers, len(numbers))
numbers.insert(0, 'Namaskar')
print(numbers)
numbers.pop(0)
print(numbers)
numbers.reverse()
print(numbers)