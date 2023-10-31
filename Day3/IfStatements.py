#if statements
# comparison Operators
#temperature = float(input("What's the temperature?: "))
temperature = 80

if temperature > 80:
    print("It's a hot day, drink plenty of water!")
elif temperature < 60:
    print("It's a cold day, wear warm clothes.")
else:
    print("It's a lovely day.")
    
# You can also rewrite this using boolean!

print("Using Boolean Value")

is_cold = True
is_hot = False

if is_hot:
    print("It's a hot day, drink plenty of water!")
elif is_cold:
    print("It's a cold day, wear warm clothes.")
else:
    print("It's a lovely day.")
print("*************************************************")

#price downpayment if statement example
price = 1_000_000
good_credit = False

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"With your good credit: {good_credit}   You need you put down: ${down_payment}")
print("*************************************************")
#Logical Operators

has_high_income = True
has_good_credit = True
has_criminal_record = True

if (has_high_income and has_good_credit) and not has_criminal_record:
    print("You are eligible for a loan!")
else:
    print("No loan :(")
# AND: both, OR: one, NOT
print("*************************************************")
# example

name = input("What's your name?: ")
name_length = len(name)

if name_length < 3:
    print("Name must be at least 3 characters.")
elif name_length > 50:
    print("Name can be a maximum of 50 characters.")
else:
    print("Name looks good!")


