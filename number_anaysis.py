numbers=[]
n=int(input("enter the number of elements :"))
if n==0:
    print("invalid input!!")
    exit()
for i in range(n):
    num=float(input("enter the element:"))
    numbers.append(num)
a = numbers[0]
b = float('-inf')
c = numbers[0]
d = float('inf')
for x in numbers:
    if x > a:
        b = a
        a = x
    elif x > b and x != a:
        b = x
for z in numbers:
    if z < c:
        d = c
        c = z
    elif z < d and z != c:
        d = z
total=0
for y in numbers:
    total=total+y
average=total/n
print("total number of elements entered is:",n)
print("sum of elements entered is:",total)
print("average of elements is:",average)
print("the largest number is:",a)
print("the smallest number is:",c)
if b == float('-inf'):
    print("no second largest element")
else:
    print("the second largest number is:", b)

if d == float('inf'):
    print("no second smallest element")
else:
    print("the second smallest number is:", d)