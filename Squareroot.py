import math

try:
    # Input from user
    n = float(input("Write the number to proceed with finding the square root: "))

    # Checking if the number is negative
    if n < 0:
        print("Can't proceed with a negative number.")
    else:
        # Calculate square root
        square_root = math.sqrt(n)
        print(f"The square root of {n} is {square_root:.2f} 😎")

except ValueError:
    print("Invalid input. Please enter a numeric value.")


