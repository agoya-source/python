# Logic tha indicates whether a number is even or odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
if number == 0:
    print("number is neutral")
elif number % 2 == 0:
    print("number is even")
