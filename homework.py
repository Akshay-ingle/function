import math

def calculate_circumference(radius):
    # Using the formula C = 2 * pi * r
    circumference = 2 * math.pi * radius
    return circumference

# Example usage
radius = float(input("Enter the radius of the circle: "))
print(f"The circumference of the circle is: {calculate_circumference(radius)}")
