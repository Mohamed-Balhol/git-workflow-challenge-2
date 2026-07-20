# 12جمع الارقام 
def sum_of_numbers():
  try:
    num = int(
        input("Enter a positive integer to calculate the sum up to it: ")
    )
    if num < 0:
      print("Error: Please enter a positive integer.")
      return

    total_sum = 0
    for i in range(1, num + 1):
      total_sum += i

    print(f"The sum of numbers from 1 to {num} is: {total_sum}")

  except ValueError:
    print("Error: Please enter a valid integer.")


if __name__ == "__main__":
  sum_of_numbers()
