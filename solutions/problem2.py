# Countdown Timer
try:
    number = int(input("Enter a positive integer: "))
    
    if number < 0:
        print("Please enter a positive number.")
    else:
        while number >= 0:
            print(number)
            number -= 1
except ValueError:
    print("Error! Please enter integers only.")