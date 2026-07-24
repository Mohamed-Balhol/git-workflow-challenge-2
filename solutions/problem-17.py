num = int (input("Enter any positive integer number: "))

if num < 0:
    print("Sorry, not positive integer number !! Try again!")
elif num ==0:
    print("The Factorial of Zero = 1")
else:
    factorial = 1
    i= num
    while i >1:
        factorial*= i
        i -= 1

    print("The Factorial of the number : ",num ," is ", factorial )
