num1 = int(input("Enter the number :\n"))
num2 = int(input("Enter the number :\n"))
num3 = int(input("Enter the number :\n"))

result = num1 if (num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)
print(f"The maximum of {num1},{num2},{num3} is : {result}")

