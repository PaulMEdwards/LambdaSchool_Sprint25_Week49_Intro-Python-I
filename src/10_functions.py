# Write a function is_even that will return true if the passed-in number is even.

def is_even(number):
    return (True if number % 2 == 0 else False)

# Read a number from the keyboard
num = int(input("Enter a number: "))

# Print out "Even!" if the number is even. Otherwise print "Odd"

print("Even!" if is_even(num) else "Odd")
