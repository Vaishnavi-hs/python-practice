# -------------------------------
# Sum of Digits
# -------------------------------
num = int(input("Enter a number for sum of digits: "))
total = 0

temp = num
while temp > 0:
    digit = temp % 10
    total = total + digit
    temp = temp // 10

print("Sum of digits is:", total)


# -------------------------------
# Largest Digit in a Number
# -------------------------------
num = int(input("Enter a number to find largest digit: "))
largest = 0

temp = num
while temp > 0:
    digit = temp % 10
    if digit > largest:
        largest = digit
    temp = temp // 10

print("Largest digit is:", largest)


# -------------------------------
# Armstrong Number (Generalized)
# -------------------------------
num = int(input("Enter a number to check Armstrong: "))
original = num
total = 0
count = 0

temp = num

# Count digits
while temp > 0:
    temp = temp // 10
    count = count + 1

temp = num

# Calculate Armstrong sum
while temp > 0:
    digit = temp % 10
    total = total + digit ** count
    temp = temp // 10

if original == total:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")