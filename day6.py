

'''
# 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]

s1=input("enter string: ")
fst = s1[-1].upper()
lst = s1[-1].upper()
print(fst+s1[1:len(s1)-1]+fst)

print(s1.replace('h','h'))
print(s1.replace('d',"d"))

n=128
temp = n
f1 = 0
while n!=0:
    rem = n%10
    check = temp % rem
    if check!=0:
        f1 = 1
        n = n//10

if f1==0:
    print("yes")
else:
    print("no")
    
n=128
temp=n
f1=0
while n!=0:
    rem=n%10
    check=temp%rem
    if check!=0:
        f1=1
    n=n//10
        
    if f1==0:
        print("yes")
    else:
        print("no")


l1 = [8, 9, 0, 7]
l2 = [7, 6, 5, 4]

#print(l1[0]+l2[0], l1[1]+l2[1])
l3 = []
for val in range(len(l1)):
    ans = l1[val]+l2[val]
    l3.append(ans)
print(l3)

# ! -----> set
# characteristics of set
1.) set can be created using{}
2.) The element inside set are not indexed
3.) Does not allow duplicate values
4.) it unordered
5.) heterogenous
6.) mutable or changable


# Eg:1
s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
print(s1)


# * Eg:2

# s2 = {5, 8, 98, [9, 0]}
# print(s2) --> error

# Eg: 4
# min(), max(), len()

# * Eg:
# ? to add element inside set

s1 = {8, 78, 67, 'u'}
#add
#s1.add(43)
print(s1)


# ? to delete element inside set
s1 = {8, 78, 67, 'u'}


# pop() # to delete one element randonly
# s1.pop()
# print(s1)

# remove()
s1.remove(78)
print(s1)

# discard()
s1.discard(8967)
print(s1)


# clear()
l1 = {}
print(type(l1)) ---- datatype is dict

s1 = set() # to creat empty set
print(type(s1))

# clear()

l1 = {}
print(type(l1)) 



s1 = set() # --> to create empty set
print(type(s1))


s1 = {8,9,0}
s1.clear()
print(s1)



s1 = {8,9,0}
del s1
print(s1)

# intersection() ---> to get common elements inside set
s1 = {4, 5, 6}
s2 = {5, 6, 7, 8, 9}
print(s1.intersection(s2))

# n1 = {1,2,3} --> s1

for val in s1:
    if val in s2:
        str1 = "its joint set"
print(str)

# ! -----> dictionary
#eg:1
d1 = {1:100, 'a':200, 4.5:"hello"}
print(d1)
print(len(d1))

mech_name =["name1", "name2", "name"]
mech_age = [23,22,24]
mec_mark = [89,78, 60]
mech_email = ["name2@gmail.com", "name3gmail.com"]

mech = {
    "student1":{
        "name":"name1"
        "age":24,
        "mark":89,
  },
   "student2":{
        "name":"name2"
        "age":24,
        "mark":89,

  },
   "student3":{
        "name":"name3"
        "age":24,
        "mark":89,

# ? Char of dictionary
# 1.) Have to be surrounded by{}
# 2.) It have to be in the form of key, value pair
# 3.) It is mutable
# 4.) Duplicate keys are not allowed, duplicate value are allowed
# 5.) It is unindexed
# 6.) It is ordered

d1 = {1:100, 2:200, 3:300, 4:400}
# * to acess element in dictionary

print9d1)
or
to acess the values, have to use key
print(d1[1]0 # o/p --> 100

# ? some common functions
len(), min, max()9
    print(min(d1))
    print(max(d1))

# ? to find min, max based on values
    print(min(d1.values()))
    print(max(d1.values()))

# ? dictionary based fuctions
to add element(key and value) in dict
d1 = {1:100, 2:200, 3:300, 4:400}
d1[5] = 500
print(d1)

# ? to replace a value in dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
d1[2]="mango"
print(d1)

#? to delete a value in dictionary
# d1={1:100,2:200,3:300,4:400}
d1.popitem()
print(d1)
310- RE BHARATH
2:07 PM
# ? delete element from dictionary
d1 = {1:100, 2:200, 3:300,4:400}
#pop item()
d1.popitem()
print(d1)
      
#pop()
#d1.pop(2) # ---> 2 is the key in dictionary
#print(d1)

# clear(),del

# join 2 dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
d2 = {"a":"apple"}



# to print all the values
#print(d1.values())


# to print all the keys
# print(d1.keys())
# print(type(d1.keys()))

# to print all the values
# print(d1.values())


# * Iterating dictionary
# for val in d1: # to Iterate keys alone
#   print(val)


# for val in d1.values(): # iterate values alone
#   print(val)

# to get both keys and values
# for key, val in d1.items():
#   print(key, val)


n=int(input("Enter of times:"))
integer=[]
float_value=[]
string=[]

for val in range(n):
    value=eval(input("Enter of times:"))
    if type(value)==int:
        integer.append(value)
    elif type(value) == float:
        float_value.append(value)
    elif type(value) ==str:
        string.append(value)
    else:
        print("Pls provide data in int, float, string")
print(integer)
print(float_value)
print(string)
        

# Return a set of elements present in Set A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
{20, 70, 10, 60}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

l1=set1 ^ set2
print(l1)

# ! problem:2
# return a set elements present in set A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}



set3 = set()
for val in set1:
    if val not in set2:
        set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)

print(set3)

#! ---> problem 3
l1=[1,2,3,4] # key
l2=["a","b","c","d"]  # value
l3=(l1[0],l2[0]or l1[1],l2[1] or l1[2],l2[2]or l1[3],l2[3])
print(l3)

#!------> problem 3
l1=[1,2,3,4] # key
l2=["a", "b", "c", "d"] # value

#{1:'a'}
d1 = {}
for val in range(len(l1)):
    d1[l1[val]]=l2[val]
print(d1)
'''




















