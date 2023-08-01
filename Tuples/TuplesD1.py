# TUPLES

# Lists

fruits=["apple","Banana","Mango","Papaya"]
print(type(fruits))
print(fruits)
fruits[2]="Orange"
print(fruits)

# tuples

fruits=("apple","mango","papaya")
print(type(fruits))
print(fruits)
'''fruits[2]="banana"
print(fruits)  '''        #'tuple' object does not support item assignment(convert into lists)


cities=("pune","mumbai","nagpur","nashik","pune")
print(type(cities))
print(cities)
print(cities[0])
print(cities[1])
print(cities[2])
print(cities[3])
print(cities[4])

# type of tuples

canDrive = (False , False ,True ,True)
numberTuple = (11,22,33,44,55)
listTuple = ([11,22],[22,33],[44,55])
dictTuple = (
    {"firstName":"kalyani","lastName":"hadole"},
    {"firstName":"amruta", "lastName":"pawar"}
)



# tupleName[startIndex:endIndex (not inclusive)]

vegetables=("brinjal","carrot","cauliflower","cabbage","ladyfinger")
print(vegetables)
print(vegetables[0:4])
print(vegetables[1:-1])
print(vegetables[3:-1])
print(vegetables[1:3])
print(vegetables[-4:-1])
print(vegetables[4])

print("ladyfinger" in vegetables)

print("ladyfinger" not in vegetables)

if("cabbage" in vegetables):
    print('vegetables is available')
else:
    print('vegetables is not available')

# update tuples

names=("kalyani","nilesh","dhanvi","aryan")
print(names)
print(type(names))

names=list(names) # convert tuple to list
print(names)
print(type(names))

names[2]="shivnaya"
print(names)

names=tuple(names) # convert list intoo tuple
print(names)

# unpacking

cities=("pune","mumbai","nashik","nagpur")
print(cities)

a=cities[0]
a1=cities[1]
a2=cities[2]
a3=cities[3]

print(a,a1,a2,a3)

(q,q1,q2,q3)=cities
print(q,q1,q2,q3)
print(q,q1,*q2)

#####################################
tupleA = (11,22)
tupleB = (33,44)
tupleC = tupleA + tupleB
print(tupleC)

tupleD = tupleA * 2
print(tupleD)

# count and index

flowers=("rose","lotus","lilly","jasmine","rose")

e=flowers.count("rose")
print(e)    # int
print(type(e))

e2=flowers.index("rose",1)
print(e2)  # int
print(type(e2))

name="Kalyani"
rev=""

for items in range(len(name)):
    rev=name[items]+rev
print(rev)
