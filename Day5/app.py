#dictionary example
numbers = ("Zero","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine")
phone_number = input("Phone: ")
output = ""

for x in phone_number:
    output += (numbers[int(x)] + " ")
   
print(output)

