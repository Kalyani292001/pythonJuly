# Lists methods

fruits = ["apple","mango","banana"]
marks = [2,3,4,5]
info = ["Kalyani","Hadole",12,False]

z = "Kalyani"
print(type(z))
print(type(info))


# program 1
vegetables = ["carrot","cauliflower","cabbage"]
print(vegetables[0])
print(vegetables[2])
q1 = len(vegetables)
print(q1)


# program2

vegetables = ["carrot","brinjal","cauliflower","waterMelon","cabbage"]
q2 = vegetables.append("Potato")
print(q2)
print(vegetables)


# program 3
vegetables = ["carrot","Soyabeen","cauliflower","Potato","carrot"]
q3 = vegetables.count("carrot")
q4 = vegetables.count("Carrot")
print(q3)
print(q4)

# program 4

vegetables = ["carrot","brinjal","cauliflower","cabbage","carrot"]
q5 = vegetables.index("carrot",1)
q6 = vegetables.index("cabbage",1,4)
print(q5)
print(q6)


# program 5

fruits = ["apple","banana","orange","soyabeen","ladiesFinger","papaya"]
# q8 = fruits.pop()
# print(fruits)
# print(q8)

# Program 6

cities=["pune","mumbai","thane","kalkatta","ahemdabad"]
a1=cities.append("nagpur")
print(a1)
print(cities)

# program 7
#clear
cities.clear()
print(cities)

# program 8

"""names=cities
names[0]="mumbai"
print(cities)
print(names)
"""

# program 9
#copy

numbers=[1,2,3,4,5]
numA=numbers.copy()
numA[1] = 6
print(numA)
print(numbers)


# program 10
# count

numberA= [12,23,34,45,56,67]
a2 = numberA.count(45)
print(a2)

# program 11
# extend
numberB=[1,3,5,7]
numberC=[2,4,6,8]
numberB.extend(numberC)
print(numberB)

# program 12
# index
a3 = numberB.index(5)
print(a3)

# program 13
# insert
country = ["india","Japan","pakistan"]
country.insert(1,"Afganisthan")
print(country)

#program 14
#pop
a4= country.pop()
print(a4)

#program 15
# remove ===> remove the specific element
country = ["india","Japan","pakistan"]
country.remove("pakistan")
print(country)

#program 16
num=[1,2,3,4,5]
num.reverse()
print(num)

# program 17
# sort
cities.sort()
print(cities)