def greeting(first_name, last_name):  # Define functions with def
    print(f"Hi {first_name} {last_name}!")
    print("Welcome to this program")
    farwell(first_name)

def farwell(first_name):
    print(f"Goodbye {first_name}.")

print("Start")
greeting("Gabriel","Urena")
print("Finish")

# Parameters are the variables attached to the functions like
# def greetings(name): name is the parameter
# An argument is the thing we assign to that for instance
# greeting("Gabriel") the string "Gabriel" is the argument

#Key word arguments

def hello(fname, lname):
    print(f"{fname}: Hello there my name is {fname} {lname}!")
    print("It's nice to meet you.")
    
    #using keyword arguments helps us in some cases, they let us assign arguemtns without worrying about position
hello(lname="Smith", fname="John")
    #positional arguement
hello("John", "Smith")

def square(num):
    return num * num

print(square(10))