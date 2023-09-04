########################################

class Person:
    firstName="Kalyani"
    lastName="Hadole"
    age=23
    rollNumber=10

    def talk(self):
        print("Talking")

    def walk(self):
        print("Walking")

Kalyani=Person()
print(Kalyani.firstName)
print(Kalyani.lastName)
print(Kalyani.rollNumber)
print(Kalyani.age)

Kalyani.walk()
Kalyani.talk()

##############################

Nilesh=Person()
print(Nilesh.firstName)   #Kalyani
print(Nilesh.lastName)    # Hadole
print(Nilesh.rollNumber)  # 10
print(Nilesh.age)         # 23

Nilesh.firstName="Nilesh"
print(Nilesh.firstName)

Nilesh.age=25
print(Nilesh.age)

Nilesh.talk()
Nilesh.walk()

# Program 2

class PersonA:
    def __init__(self,fn,ln,ag):
        self.fullName=fn
        self.lastName=ln
        self.age=ag

    def display(self):
     print(self.fullName+ " "+ self.lastName)

Aryan=PersonA("Kalyani","Hadole",12)
Aryan.display()

Om=PersonA("Om","Matsagar",9)
Om.display()

# Program 3

class PersonB:
    def __init__(self,fn,ln,ag,rNo):
        self.fn=fn
        self.ln=ln
        self.ag=ag
        self.rNo=rNo

    def display(self):
            print(self.fn + " " + self.ln)

divansh=PersonB("Divansh","Patil",6,13)
divansh.display()

