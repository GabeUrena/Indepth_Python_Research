#print
print("Hello world")
print("*" * 60) # printing a string '*' 60 times

#variables
first_name = "Gabriel"
last_name = "Urena"
age = 22
is_new = True

#input
name = input("Hello there! What's your name? : ")
color = input("It's nice to meet you " + name + ". Whats your favorite color? : ")
print("You like " + color + " that's my favorite as well!") # take input and print
print("*" * 60) # printing a string '*' 60 times

#type conversion
birth_year = int(input("Enter your birth year: ")) # turn string input into int
age = 2023 - birth_year 
print(age)
print("*" * 60) # printing a string '*' 60 times

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