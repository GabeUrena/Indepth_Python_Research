#Writing program that will remove duplicates in a list
list = [1,2,3,3,4,4,5,5]
temp = []

for number in list: # For each number in the list
    if number not in temp: # if that element doesnt appear in the temp list
        temp.append(number) # add that element 
print(temp) # print the new list


       
