#Tuples
numbers = (1, 2, 3) # similar to a list execpt you use () instead of []
print(numbers[0])
# Tuples are immutable, you can not change a tuples once its been created and assigned values


# unpacking

coordinates = (1,2,3)
coordinates[0] * coordinates[1] * coordinates[2]
# how do we make this line above look cleaner? with the below
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

# but this can be reduced even more using unpacking
x,y,z = coordinates

# this applies to lists aswell
names = ["John", "Alvin", "Rob"]
first, second, third = names


# DICTIONARIES

patient = {
    "name": "John Smith",
    "age": 20,
    "sex": "Male",
    "birthdate": "09/19/1999"
}
print(patient["birthdate"]) # print the birthdate key

#python is case sensitive so you will get an error with BirthDate
#We use .get() to avoid this. If you call a key that doesnt exist you will get "none"


print(patient.get("dob")) # dob doesnt exist so return None
print(patient.get("dob", "September 19 1999")) # if dob doesnt exist, create dob and set it to September 19 1999
# Doing this is like setting the default. Each time a patient doesnt have a birthday the default is september 19 1999

# to add to a dictionary
patient["name"] = "Alvin Rob" 
print(patient["name"])

#You can also add new key values
patient["is_alive"] = True
print(patient["is_alive"])