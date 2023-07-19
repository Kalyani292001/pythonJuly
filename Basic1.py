# Data Types
#program 1
a="Kalyani"
print(a)
print(type(a))

#profram 2
b=10
print(b)
print(type(b))

# program 3
c=True
print(c)
print(type(c))

#program 4

# comparison
# entity < entity -----> boolean --- type
# < , > ,<=, >= ,!= ,==

print(2 >3)  # False
print(2 < 3) # True
print(2 <=3) # True
print(3 >= 2) # True
print(2 != 3) # True
print(2 == 3) # False
print(3 == 3) # True

# logical operators

# and

# True  and  True  ====> True
# False  and  True  ====> False
# True   and  False ====> False
# False  and  False ====> False

print( 3 == 3 and 7 != 6)
print( 3 != 3 and 7 != 6)
print( 3 == 3 and 7 == 6)
print( 3 != 3 and 7 == 6)

# or

# True  or  True  ====> True
# False  or  True  ====> True
# True   or  False ====> True
# False  or  False ====> False

print( 3 == 3 or 7 != 6)
print( 3 != 3 or 7 != 6)
print( 3 == 3 or 7 == 6)
print( 3 != 3 or 7 == 6)


# not
print(not (7==7))
print(not (7!=7))

# if statement
# check all the condition

num=92
if(num>90):
    print("Grade A")
if(num>75):
    print("Grade B")
if(num>65):
    print("Grade C")

#if else
# check first condition then check second condition

num=92
if(num>90):
    print("Grade A")
elif(num>75):
    print("Grade B")
elif(num>65):
    print("Grade C")

