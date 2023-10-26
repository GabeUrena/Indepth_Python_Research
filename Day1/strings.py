#string
print('This is a use for the single quotes')
print("You use the double quotes when you need to use single quotes,It's there's Gabriel's.")
# Python can capture strings thats span multiple lines, you can incapsulate them using tripe single quotes

email = '''
Hello John,

This is an email to you.

Best Regards,
Gabriel Urena
'''
print(email)
print("*" * 60)

name = "Shylin"
print(name)
print(name[2]) #using square brackets let you return the char at a specified index 
print(name[-1]) # using negative index will return the last element and move towards the front.
print(name[0:3]) # return all the char from index 0-2 it does not go to the number you give it, only righ before it.
print(name[0:]) # print the string starting at index 0
print(name[1:]) # print everything starting at index 1
print(name[:3]) # python interpreter will assume your starting index is 0
print(name[:]) # python interpreter will assume the start index is 0 and the end index is the end of the string

#using [:] is perfect for cloning
temp = name[:]
print(temp)

print(name[1:-1]) # print the string but exclude the first and last index
print("*" * 60)

#FORMATTED STRING
first_name = "Gabriel"
last_name = "Urena"
message = f"{first_name} {last_name} is a coder" 
#the curly bracket acts as holes where the variables fill.

print(message)
print("*" * 60)

#String methods
name = "Angel Smith"
print(len(name)) #tells us how many char are in the string
print(name.upper()) #returns string all uppercase
print(name.lower()) #return string all lowercase
print(name.find('g')) #return the index of the first occurance of the specified char
    # python is case sensitive, if you put a lower case it will look for the lowercase
print(name.replace("Smith", "Wood")) # replaces a specifed string (Smith) with another (Wood)
print(name.replace("A", "I"))

#using 'in' you can return a boolean value checking if a char or string occures in a specified string
print("ith" in name) #print True if 'ith' is found in the string variable name
    
    
#Strings
len(name) # return number of chars
name.upper() # uppercase
name.lower() # lowercase
print(name.title()) #
name.find("")
name.replace("","")
"..." in name
