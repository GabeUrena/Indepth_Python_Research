class Point:
    # Assigning x and y coords without .x and .y
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
   
point3 = Point(45, 123)
print(point3.x)

   
   
   
   
        
# Assigning x and y coordinates using .x and .y
"""
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()


point2 = Point()
point2.x = 50

print(point2.x)

"""


