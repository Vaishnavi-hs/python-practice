# Left aligned pattern
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

print()

# Right aligned pattern
for i in range(1, 5):
    for j in range(4 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

print()

# Pyramid pattern
for i in range(1, 5):
    for j in range(4 - i):
        print(" ", end="")
    for k in range(2*i - 1):
        print("*", end="")
    print()