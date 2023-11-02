#using tuple
numbers = ("Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine")
phone_number = input("Phone: ")
output = ""

for x in phone_number:
    output += (numbers[int(x)] + " ")
   
print(output)

#using dictionary
phone = input("Phone: ")
digits = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""
for number in phone:
    output += digits.get(number, "!") + " "

print(output)