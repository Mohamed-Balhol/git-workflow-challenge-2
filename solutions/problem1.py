def simple_calculator():
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Choose an operator (+, -, *, /): ").strip()

    if operator == "+":
      result = num1 + num2
      print(f"Result: {result}")
    elif operator == "-":
      result = num1 - num2
      print(f"Result: {result}")
    elif operator == "*":
      result = num1 * num2
      print(f"Result: {result}")
    elif operator == "/":
      if num2 == 0:
        print("Warning: Division by zero is not allowed!")
      else:
        result = num1 / num2
        print(f"Result: {result}")
    else:
      print("Error: Invalid operator selected.")
  except ValueError:
    print("Error: Please enter valid numeric inputs.")


if __name__ == "__main__":
  simple_calculator()