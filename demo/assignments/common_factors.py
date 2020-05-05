# Display common factors of two numbers

num1 = int(input("Enter first  number :"))
num2 = int(input('Enter second number :'))
small = num1 if num1 < num2 else num2

for i in range(2, small//2 + 1):
    if num1 % i == 0 and num2 % i == 0:
         print(i)
