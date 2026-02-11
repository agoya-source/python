first = int(input("Enter first number:"))
second = int(input("Enter second number:"))
third = int(input("Enter third number:"))

if first > second and first > third:
    print(first,"is the largest number")
if second > first and second > third:
    print(second,"is the largest number")
    if third > second and third > first:
        print(third,"is the largest number")


