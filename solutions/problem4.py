# Rectangle Area Calculator
try:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    if length <= 0 or width <= 0:
        print("Dimensions must be greater than zero.")
    else:
        area = length * width
        print(f"Rectangle Area is: {area}")
except ValueError:
    print("Error! Please enter valid numbers.")