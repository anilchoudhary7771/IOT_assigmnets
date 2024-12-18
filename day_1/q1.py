#Write a Python Program find an area of a rectangle and perimeter of the rectangle.

length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

def rectangle_properties(length: float, breadth: float):
    print(f"area = {length * breadth}")
    print(f"perimeter = {2 * (length + breadth)}")

rectangle_properties(length, breadth)