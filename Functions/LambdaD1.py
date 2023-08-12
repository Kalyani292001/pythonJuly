# Program 1

x=lambda a,b:a+b
print(x(11,22))

# program 2

a=lambda x,y:x*y
print(a(3,5))

#Program 3
b=lambda a:a+20
print(b(43))

# Program 4

x=lambda a,b:a+b

def funA(n):
    print(n(12,32))
funA(x)

# prgram 5

a=lambda x,y:x*y

def mulFun(b):
    print(b(23,3))
mulFun(a)

# Program 6

num=[1,2,3,4,5,6,7,8,9,10,11,12,13]
addA=[]

for x in num:
    addA.append(x*2)
print(addA)

# map()

numA=[1,2,3,4,5,6]

q1=list(map(lambda x:x*2,numA))
print(q1)

#==================>

numB=[1,2,3,4,5,6]
q2=list(map(lambda x:x+2,numB))
print(q2)

# Filter()

listA=[12,23,54,64,11,34,45,22,32]
greater=[]

for x in listA:
    if(x>30):
       greater.append(x)
print(greater)

q3=list(filter(lambda x:x>30,greater))
print(q3)


