def countdown():
  try:
    num = int(input("Enter a positive integer for countdown: "))
    print(f"--- Starting countdown from {num} to 0 ---")
    while num >= 0:
      print(num)
      num -= 1
    print("Countdown finished!")
  except ValueError:
    print("Error: Please enter a valid integer.")


if __name__ == "__main__":
  countdown()