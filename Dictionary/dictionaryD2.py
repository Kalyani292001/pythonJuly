# string booelan int float list

listK = ["kalyani","sonali","shweta","pradnya"]
# add
listK.append("Isha")
print(listK)
# retrive
print(listK[1])
# remove
listK.pop(1)
# update
listK[0] = "Santosh"
print(listK)

# program 2
dictA = {
    "firstName":"Kalyani",
    "lastName":"Hadole",
    "age":23
 }
print(type(dictA))

# retrive
print(dictA['firstName'])

# update
dictA['firstName'] = "Nilesh"
print(dictA)

# add
dictA['city'] ="Mumbai"
print(dictA)

# delete
del dictA['lastName']
print(dictA)


# loop
country  = ["india","pakistan","china","australia","cuba"]

for city in country:
    print(city)

for city in range(len(country)):
    print(country[city])


# dict

info1 = {
    "fullName":"Aryan Pawar",
    "skills":["Javascript","java"],
    "age":23,
    "city":"pune",
    "canDrive":True,
    "city":"Mumbai"
}

print(info1)
print(info1)

for prop in  info1:
    print(prop,info1[prop])


l = [11,22,33]
k = l
k[0] = 111
print(k) # [111,22,33]
print(l) # [111,22,33]

vehicle = {
        "color":"black",
        "city":"Sambhajinagar",
        "regNo":1418
}
vehicle2  = vehicle
vehicle2['color'] = "blue"
print(vehicle)
print(vehicle2)