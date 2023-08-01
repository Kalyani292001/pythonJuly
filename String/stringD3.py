##############################
# program 1
a=10
b=20

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

# program 2

k=2
s=5

print(k+s)
print(k-s)
print(k*s)
print(k/s)
print(k%s)

# string as a parameter and string as return

def greet(str):
    print("welcome" +" "+ str)
    return "welcome" + " " + str

q1=greet("python")
print(q1)

# boolean as a parameter and boolean as return type

def canDrive(vehicle,vehhicleAvl):
    if(vehhicleAvl and vehicle>=18):
        return  True
    else:
        return False

q2=canDrive(21,True)
print(q2)

# list as parameter and list as return type

cities=["pune","mumbai","nagpur","goa"]

def avlCities(cty):
    cty.remove('nagpur')
    return cty

q3=avlCities(cities)
print(q3)
print(cities)

# dictionary as parameter and dictionary as return type

info={
    "firstName":"Kalyani",
    "LastName":"Hadole",
    "age":23,
    "rollNumber":12
}

def infrmtion(cty):
    cityAdd={"city":"Pune"}
    cty.update(cityAdd)
    return cty

q5=infrmtion(info)
print(q5)


def addinfo(cty):
    cityadd={"city":"pune"}
    cty.update(cityadd)
    return cty
q6=addinfo(info)
print(q6)

# tuple as a parameter and tuple as return type
# program 1
numbers=(11,22,33,44)
def tpl(num):
   num= list(num)
   num.append(55)
   num=tuple(num)
   print(num)
   return num

q7=tpl(numbers)
print(q7)

# program 2

tupA=(9,8,7,6,5,4)
def addNum(tpl):
    tpl=list(tpl)
    tpl.append(3)
    tpl=tuple(tpl)
    return tpl

q8=addNum(tupA)
print(q8)

# set as a parameter and set as return type

setA={1,2,3,4}
setB={5,6,7,8}

def combn(setA,setB):
    return setA.union(setB)

q9=combn(setA,setB)
print(q9)