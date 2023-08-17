
info = [
    {
        'name': 'Alice',
        'age': 30 ,
        'city':"pune",
        "skills":["python","java","javascript"]
    },
    {
        'name': 'Bob',
        'age': 22,
        'city':"sangamner",
        "skills":["css3","sql","powerBI"]

    },
    {
        'name': 'Charlie',
        'age': 28,
        'city':"pune",
        "skills":["css3","sql","powerBI"]
    },
    {
        'name': 'David',
        'age': 26,
        'city':"nagpur",
        "skills":["css3","flutter","c#"]
    },
    {
        'name': 'Eve',
        'age': 19,
        'city':"jaipur",
        "skills":["css3","flutter","c#"]
    }
]

# program 1

listA = [11,22,33,44,55,66]
print(list(map(lambda x:x+1,listA)))

# program 1
print(list(map(lambda person:person.get('city'),info)))

#program 2
# add  git as skill to every people
print(list(map(lambda person:person['skills'].append("git"),info)))
print(info)
for x in info:
    x['skills'].append("Accountant")
print(info)

# people belong to pune city
# program3
q1 = list(filter(lambda person: person['city'] == "pune",info))
for a in q1:
    print(a['name'])

# program 4
# alice:3
q2 = list(map(lambda person:person['name']+":" + str(len(person['skills'])),info))
print(q2)

# program 5
j = [11,22,33]

from functools import *
print(reduce(lambda acc,y:acc+y,j,5))
print(reduce(lambda acc,person:acc+person['age'],info,0)/len(info))