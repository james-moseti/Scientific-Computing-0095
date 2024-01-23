def area_of_triangle(side1, side2, side3):
    semi_p = (side1 + side2 + side3) / 2
    area = (semi_p*(semi_p - side1)*(semi_p - side2)*(semi_p - side3)) ** 0.5
    return area

num1 = float(input("Enter the length of side 1: "))
num2 = float(input("Enter the length of side 2: "))
num3 = float(input("Enter the length of side 3: "))

print(f"The area of the triangle with the given dimensions is: {round(area_of_triangle(num1, num2, num3), 4)}")