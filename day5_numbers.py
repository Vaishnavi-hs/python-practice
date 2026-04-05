# -------------------------------
# Strong Number
# -------------------------------
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

num = int(input("Enter number to check Strong number: "))
original = num
total = 0

temp = num
while temp > 0:
    digit = temp % 10
    total = total + fact(digit)
    temp = temp // 10

if total == original:
    print("It is a Strong number")
else:
    print("It is not a Strong number")


# -------------------------------
# Perfect Number
# -------------------------------
num = int(input("\nEnter number to check Perfect number: "))
total = 0

for i in range(1, num):
    if num % i == 0:
        total = total + i

if total == num:
    print("It is a Perfect number")
else:
    print("It is not a Perfect number")


# -------------------------------
# Fibonacci Series
# -------------------------------
n = int(input("\nEnter number of terms for Fibonacci: "))

f1 = 0
f2 = 1

print("Fibonacci series:")

if n == 1:
    print(f1)
elif n >= 2:
    print(f1, f2, end=" ")
    
    for i in range(2, n):
        f3 = f1 + f2
        print(f3, end=" ")
        f1 = f2
        f2 = f3