#======================
# program 1
def add(x,y):
    return x+y

q1=add(11,22)
print(q1)

# program 2

def addA(x=11,y=12,z=14):
    return x+y+z

q2=addA()
q3=addA(1,2,3)  # take updated arguments
print(q2)
print(q3)

# program 3

def addB(a,b,c,d):
    print(a+b+c+d)

addB(1,2,34,4)
#addB(13,4,56,7,89,9)   #takes 4 positional arguments but 6 were given

# program 4

def addD(*numbers):
    print(numbers)
    sum=0
    for a in numbers:
        sum= sum+ a
    return sum

q4=addD(1,23,4,6,8)
print(q4)

# program 5

def addE(*num):
    sum=0
    for b in num:
        sum= sum + b
    return sum

q5=addE(9,8,7,6,5)
print(q5)

# program 6

tupA=(11,22,33,44,55)
sum=0

for c in tupA:
    sum=sum+c
print(sum)

# program 7

'''def childName(**Name):
    print(Name)

    for prop in Name:
        print(prop,Name[prop])

childName(FirstName="Kalyani",LastName="Hadole",MiddleName="Navnath")'''

def childName(**names):
    print(names)
    for prop in names:
        print(prop,names[prop])

childName(firstName="Kalyani",age=23)


