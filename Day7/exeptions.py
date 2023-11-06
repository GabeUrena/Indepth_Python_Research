try:
    age = int(input("What is your age? : "))
    income = 25000
    risk = income / age
    print(f"Age: {age}")
except ValueError:
    print("invalid value")
except ZeroDivisionError:
    print("Age can't be 0")