#Empty List
empty_list = []

#Numbers with Numbers
numbers = [1, 4, 2, 0, 50]

mixedData = [1, "Hello", 'A', 6.67]

nested = [[1,3], [2,4], [5,6]]

#Accessing the list elements
print(mixedData[2])
print(mixedData[0])

#Mutating the data
mixedData[2] = 3
print(mixedData)

#Appending will be done at end
mixedData.append("Stand")
print(mixedData)

#Inserting will be done with particular index
mixedData.insert(0, "start")
print(mixedData)

#Removing the elements in the list
mixedData.remove("Hello")
print(mixedData)

print(numbers.sort())
print(numbers.sort(reverse = True))
print(numbers.reverse())
print(numbers.count(50))
print(numbers.index(4))
numbers.extend([10,20])
print(numbers)
numbers.pop()
#Creating the Duplicate Lists
new_list = numbers.copy()
print(new_list)

print(len(numbers))

print(max(numbers))
print(min(numbers))

print(sum(numbers))

#Checks whether ele is present
print(10 in numbers)

#list Slicing
print(numbers[1:4])

#Slicing and sorting
numbers[5:10] = sorted(numbers[5:10])
print(numbers)

