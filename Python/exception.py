import sys
try:
    X = int(input("add a number X: "))
    Y = int(input("add a number Y: "))
except ValueError:
    print("Error: Invalid input! Please enter a number.")
    sys.exit(1) 

try:
    result = X / Y
except ZeroDivisionError:
   print("Error: Cannot divide by 0!")
   sys.exit(1) 

print(f"{X} divided by {Y} is {result}")