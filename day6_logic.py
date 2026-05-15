# -------------------------------
# Smallest Digit in a Number
# -------------------------------
n = int(input("Enter a number to find smallest digit: "))

smallest = 9

temp = n
while temp > 0:
    digit = temp % 10

    if digit < smallest:
        smallest = digit

    temp = temp // 10

print("Smallest digit is:", smallest)


# -------------------------------
# Largest and Smallest Digit
# -------------------------------
n = int(input("\nEnter a number to find largest and smallest digit: "))

smallest = 9
largest = 0

temp = n
while temp > 0:
    digit = temp % 10

    if digit < smallest:
        smallest = digit

    if digit > largest:
        largest = digit

    temp = temp // 10

print("Smallest digit is:", smallest)
print("Largest digit is:", largest)


# -------------------------------
# Digit Frequency
# -------------------------------
number = input("\nEnter a number to check digit frequency: ")

for digit in number:
    count = number.count(digit)
    print(digit, "appears", count, "times")


# -------------------------------
# Harshad Number
# -------------------------------
n = int(input("\nEnter a number to check Harshad number: "))

original = n
total = 0

temp = n
while temp > 0:
    digit = temp % 10
    total += digit
    temp = temp // 10

if original % total == 0:
    print("It is a Harshad number")
else:
    print("It is not a Harshad number")


# -------------------------------
# Duck Number
# -------------------------------
n = input("\nEnter a number to check Duck number: ")

if "0" in n:
    if n[0] == "0":
        print("It is not a Duck number")
    else:
        print("It is a Duck number")
else:
    print("It is not a Duck number")


# -------------------------------
# Spy Number
# -------------------------------
n = int(input("\nEnter a number to check Spy number: "))

total = 0
product = 1

temp = n
while temp > 0:
    digit = temp % 10

    total += digit
    product *= digit

    temp = temp // 10

if total == product:
    print("It is a Spy number")
else:
    print("It is not a Spy number")