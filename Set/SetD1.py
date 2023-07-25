# SET
# set doesn't store the value by index
# set doesnt't store the value by key value pair

q1={11,22,33,44,55,66,77,88,99}
print(q1)
print(type(q1))  #<class 'set'>

# retrive

for item in q1:
    print(q1)

print(2 in q1)

# add

cities={"pune","mumbai","Delhi","manmad"}
print(cities)
q2=cities.add("Nagpur")  # add element at first
print(q2)  # none
print(cities)


# remove (specific element remove)
cities.remove("mumbai")
print(cities)

# discard
cities.discard("Delhi")
print(cities)

#pop  remove first element
cities.pop()
print(cities)

# clear

cities.clear()
print(cities)

# del cities
print(cities)
