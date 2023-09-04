#################################

# Program 1

class Person:
    def __init__(self,fullName,Age,Skills,rollNo):
        self.fullName=fullName
        self.Age=Age
        self.Skills=Skills
        self.rollNo=rollNo

    def noOfSkills(self):
        print(self.Skills)

    def displayName(self):
        print(self.fullName)

Kalyani=Person("Kalyani",23,["javaScript","Java","typeScript"],25)
print(Kalyani.Skills)
print(Kalyani.fullName)
print(Kalyani.Age)
print(Kalyani.rollNo)

Kalyani.displayName()
Kalyani.noOfSkills()

# Program 2

students=[
    Person("Kalyani",23,["javaScript","Java","typeScript"],25),
    Person("Kalyani",23,["javaScript","Java","typeScript"],25),
    Person("Kalyani",23,["javaScript","Java","typeScript"],25),
    Person("Kalyani",23,["javaScript","Java","typeScript"],25),
    Person("Kalyani",23,["javaScript","Java","typeScript"],25)
]

# program 3


studentsA={
   "studentsA" :Person("Kalyani",23,["javaScript","Java","typeScript"],25),
    "studentsA" :Person("Kalyani",23,["javaScript","Java","typeScript"],25),
    "studentsA" :Person("Kalyani",23,["javaScript","Java","typeScript"],25),
    "studentsA" :Person("Kalyani",23,["javaScript","Java","typeScript"],25),
    "studentsA" :Person("Kalyani",23,["javaScript","Java","typeScript"],25)
}

# get methods(keys) using loop
for k in studentsA:
    studentsA[k].noOfSkills()
    studentsA[k].displayName()

#get keys and values
for k,v in studentsA.items():
    # print(k,v)
    v.noOfSkills()
    v.displayName()

# get values

for v in studentsA.values():
    v.noOfSkills()
    v.displayName()

# get keys
for k in studentsA.keys():
    studentsA.get(k).noOfSkills()
    
    studentsA.get(k).displayName()

for item in range(len(students)):
    students[item].displayName()
    students[item].noOfSkills()
