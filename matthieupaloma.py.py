import math
x1 = float(input("Enter x1:"))
y1 = float(input("Enter y1:"))
x2 = float(input("Enter x2:"))
y2 = float(input("Enter y2:"))
distance = math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2))
print(f" the distance of the two points is:{ distance : }")


"""REFLECTION
Using the math library is more practical because it already has prompts like sqrt() and pow(), making the program shorter and easier to understand. 
Without these functions, I would need to write complex calculations which could lead to more errors.
"""

import math

def get_coordinate(label):
    return float(input(f"Enter {label}: "))

def calculate_distance(point_a, point_b):
    x1, y1 = point_a
    x2, y2 = point_b
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
    print("=== Distance Calculator ===")

    x1 = get_coordinate("x1")
    y1 = get_coordinate("y1")
    x2 = get_coordinate("x2")
    y2 = get_coordinate("y2")

    distance = calculate_distance((x1, y1), (x2, y2))
    print(f"Distance: {distance:.2f} miles")

main()

