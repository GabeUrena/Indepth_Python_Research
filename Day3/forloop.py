#for loops

for x in "Python":
    print(x)
    
for x in ["gabriel, john, angel"]:
    print(x)
    
for x in range(10): # instead of [0,1,2,3,4,5,6,7,8,9] use range()
    print(x)
print("done")

range(10)       # [0,1,2,3,4,5,6,7,8,9]
range(5,10)     # [5,6,7,8,9]
range(5, 10, 2) # [5,7,9]

prices = [10,20,30]
sum = 0

for x in prices:
    sum += x
print(f"Your Total: ${sum}") 

#nested loop

for x in range(5):
    for y in range(5):
        print(f"({x},{y})")
        
for item in [5, 2, 5, 2, 2]:
    output = ""
    for y in range(item):
        output += "x"
    print(output)
    
    
    # Get largest value from list
nums = [4,100,78,5,2]
max = nums[0]

for x in nums:
    if max < x:
        max = x
print(max)