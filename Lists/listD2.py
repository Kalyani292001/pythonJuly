
cities=["pune","mumbai","benglore","ranchi","kolkata","hydrebad"]
print(cities[1])
print(cities[4])


# slice
#city[startIndex:endIndex:steps]
print(cities[1:])
print(cities[1:4])
print(cities[-3:])
print(cities[0:len(cities):2])
print(cities[0:len(cities):3])

# program 3

'''print("pune" in cities)

a1=input("please enter the valide city name")

if(a1 in cities):
    print("city is available")
else:
    print("city is not available")'''

# program 4

for cities in cities:
    print(cities)

fruits = ["papaya","mango","apple","bananan","grapes"]

for  fruit in fruits:
    print(fruit)

# program 5

# for x in range(startIndex,endIndex,step):

for x in range(10):
    print(x)

for x in range(1,10):
    print(x)

for x in range(3,30,3):
    print(x)


fruits1 = ["papaya","mango","banana","grapes","pineapple"]
for x in range(len(fruits1)):
    #print(x)
    print(fruits1)