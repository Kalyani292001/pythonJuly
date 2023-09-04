# Program 1
# Using Constructor
class Student:
    def __init__(self,firstName, lastName , adharNo):
        self.firstName = firstName
        self.lastName = lastName
        self.adharNo = adharNo

    def displayName(self):
        print(self.firstName+ " " +self.lastName)


class Teacher(Student):
    def __init__(self,firstName, lastName , adharNo,salary):
        super().__init__(firstName, lastName , adharNo)
        self.salary = salary

    def displaySalary(self):
        print(self.salary)

amol = Teacher("amol","hadole",21,25000)
print(amol.firstName)
print(amol.lastName)
print(amol.adharNo)
print(amol.salary)
amol.displaySalary()
amol.displayName()

# Program 2
class GrandFather:

    def __init__(self,firstName , lastName):
        self.firstName = firstName
        self.lastName = lastName

    def displayGN(self):
        print(self.firstName + self.lastName)


class Father(GrandFather):
    def __init__(self,firstName , lastName, ffirstName):
            super().__init__(firstName , lastName)
            self.ffirstName = ffirstName

    def displayFN(self):
        print(self.ffirstName + self.lastName)


class Son(Father):
    def __init__(self, firstName, lastName, ffirstName, sname):
        super().__init__( firstName, lastName, ffirstName)
        self.sname = sname

    def displaySN(self):
        print(self.sname + self.lastName)

Amol = Son("savliram","hadole","Navnath","Amol")
print(Amol.firstName)
print(Amol.lastName)
print(Amol.ffirstName)
print(Amol.sname)
Amol.displayGN()
Amol.displayFN()
Amol.displaySN()

# Program 3

class Mother:
    def __init__(self,mname,mlastName):
        self.firstName = mname
        self.lastName = mlastName

    def displayMName(self):
        print(self.firstName + self.lastName)

class Son(Mother):
    def __init__(self ,mname,mlastName, sname):
        super().__init__(mname,mlastName)
        self.sname = sname

    def displaySName(self):
        print(self.sname + self.lastName)


class Daughter(Mother):
    def __init__(self, mname, mlastName, dname):
        super().__init__(mname, mlastName)
        self.dname = dname

    def displayDName(self):
        print(self.dname + self.lastName)



Nilesh = Son("Kusum","Hadole","Nilesh")
Kalyani = Daughter("Kusum","Hadole","Kalyani")


print(Nilesh.sname)
print(Nilesh.firstName)
print(Nilesh.lastName)
Nilesh.displayMName()
Nilesh.displaySName()

print(Kalyani.dname)
print(Kalyani.firstName)
print(Kalyani.lastName)
Kalyani.displayMName()
Kalyani.displayDName()