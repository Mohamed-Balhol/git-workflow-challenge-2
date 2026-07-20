def calculate_rectangle_area():
  try:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area}")
  except ValueError:
    print("Error: Please enter valid numbers for length and width.")


if __name__ == "__main__":
  calculate_rectangle_area()