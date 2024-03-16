'''
def catAndMouse(x, y, z):
    dist_cat_a = abs(z - x)
    dist_cat_b = abs(z - y)
    if dist_cat_a == dist_cat_b:
        return "Mouse C"
    elif dist_cat_a < dist_cat_b:
        return "Cat A"
    else:
        return "Cat B"
# Example usage
print(catAndMouse(1, 2, 3))  # Output: Cat B

num = 8
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is:", factorial)

sum_even = 0
sum_odd = 0
for num in range(12, 38):
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)

n1 = 123
total = 0
while n1 > 0:
    digit = n1 % 10
    total += digit
    n1 //= 10
print("Sum of digits of the number:", total)

n1 = 234
reverse = 0
while n1 > 0:
    digit = n1 % 10
    reverse = reverse * 10 + digit
    n1 //= 10
print("Reverse of the given number:", reverse)


# ----> while loop
# ----> break using while loop

# eg:1
# 1.)iterate from 20 to 30 and break the loop in 27

i = 20
while i<31:
    if i ==27:
        break
    print(1)
    i+=1

# 2.)
i = 20
while i<31:
    print(i)
    if 1==27:
        break
    i+=1

# 3.)
i = 20
while i<31:
    print(i)
    if i==27:
        break
    i+=1

# ! ------> continue
# ----> eg:1
i = 20
while i<31:
    if 1==27:
        continue
    print(i)
    i=i+1

# ! eg:5
# while to iterate from 12 to 22
# find the sum of all numbers

i = 12
while i<22+1:
     print(i)
     i+=1

i = 12
sum=0
while i<23:
    sum+=i
    i+=1
    if i == 23:
        print(sum)

# ! eg:6
# find the avrage of value from 20 to 25

i=20
sum=0
while i<=25:
    sum=sum+i
    avg=sum/6
    i+=1
print(avg)


# ! --------> nested for loop
eg:1
for row in range(1, 3+1):
    for col in range(1, 4+1):
        print(row, col)


# eg:2
# * * * * *
# * * * * *
# * * * * *
# * * * * *


for row in range(4):
    for col in range(4):
        print("*" , end=" ")
        print()

print(1,end=" ")
print(2)


s1 = "hello world to all"

rows = int(input("enter the rows: "))
cols = int(input("enter the cols: "))

for row in range(rows):
    for col in range(col):
        print("*", end=" ")
    print()


# ! to print stars in right angle triangle

for row in range(0, 6):
    for col in range(0, row+1):
        print("*", end=" ")
    print()

for row in range(5):
    for col in range(5):
        if col==0 or col==5 or row==0 or row==5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for row in range(0, 5):
    for col in range (0, 6):
        if((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# *
# * *
# *   *
# *     *
# *       *
# * * * * * *

for row in range(6):
    for col in range(6):
            if(col==0 or (row==0 and col==0) or (row==1 and col==1))or (row==2 and col==2) or (row==3 and col==3) or (row==4 and col==4) or (row==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

# Number ----> int, float complex
# String
# Boolean
# None

# collection
# List
# tuple
# set
# dictionary


# ? ---> List

# 1.) if the collection of elements are surrounded by Square brackets, it is considered to be list.
# ! ---> Eg:
# l1 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]


# Characteristics of list
# 1.) List have to be surrounded []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every elements inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous


#--> Indexing
# In the collection datatypes like list, tuple, string, the elements will be alloted
# with predefined unique value called index value
# We have 2 types of indexing
# Positive indexing --> starts with @ from left hand side
# Negative indexing --> starts with -1 from right hand side
'''





















