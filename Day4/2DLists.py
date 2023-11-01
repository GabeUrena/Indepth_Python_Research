#2D List

Matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]    # this matrix has 3 rows and 3 colomns, with elements 

print(Matrix[0][1]) # print 2

for row in Matrix:
    for x in row:
        print(x)
print("done") 
#List methods

numbers = [7, 3, 4, 1, 8, 9]
numbers.append(20) #adding number to the end of a list
print(numbers)

numbers.insert(2,21) # add the number 21 in index 2
print(numbers)

numbers.remove(1) #remove the first instance of the given element
print(numbers)

numbers.pop() # removes the last element in a list
print(numbers)


print(numbers.index(3)) #returns the index of the first occurance of that element

numbers.clear() # clears the entire list
print(numbers)

# to check for the existance of an element in a list you use ' in ' 
numbers = [7, 3, 4, 1, 8, 9]
print(20 in numbers) # check if the number 50 exists in this list

numbers.sort() # sort in ascending order
print(numbers)

numbers.reverse() # sort in descending order
print(numbers)

clone_numbers = numbers.copy() # copy a list to another list
print(clone_numbers.append(21))
print(numbers)
