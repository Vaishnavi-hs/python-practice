# -------------------------------
# Prime Check
# -------------------------------
n = int(input("Enter a number to check prime: "))

if n <= 1:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")


# -------------------------------
# Prime Numbers from 1 to N
# -------------------------------
n = int(input("Enter range to print primes: "))

for num in range(1, n+1):
    if num <= 1:
        continue

    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
print()


# -------------------------------
# Factorial (Recursion)
# -------------------------------
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

n = int(input("Enter number for factorial: "))
print("Factorial is:", fact(n))


# -------------------------------
# Reverse a Number
# -------------------------------
n = int(input("Enter number to reverse: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reversed number is:", rev)


# -------------------------------
# Palindrome Check
# -------------------------------
n = int(input("Enter number to check palindrome: "))
original = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if original == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")