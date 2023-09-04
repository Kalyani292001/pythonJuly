class Student:
    def __init__(self,firstName, lastName , adharNo):
        self.firstName = firstName
        self.lastName = lastName
        self.adharNo = adharNo

    def displayName(self):
        print(self.firstName+self.lastName)


class Teacher(Student):
    def __init__(self,firstName, lastName , adharNo,salary):
        super().__init__(firstName, lastName , adharNo)
        self.salary = salary

    def displaySalary(self):
        print(self.salary)

amol = Teacher("amol","hadole",23,10000)
print(amol.firstName)
print(amol.lastName)
print(amol.adharNo)
print(amol.salary)
amol.displaySalary()
amol.displayName()

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

amol = Son("savliram","hadole","navnath","amol")
print(amol.firstName)
print(amol.lastName)
print(amol.ffirstName)
print(amol.sname)
amol.displayGN()
amol.displayFN()
amol.displaySN()


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

#kanchan = Mother("kanchan","deshpande")

amol = Son("kusum","hadole","amol")
kalyani = Daughter("kusum","hadole","kalyani")


print(amol.sname)
print(amol.firstName)
print(amol.lastName)
amol.displayMName()
amol.displaySName()

print(kalyani.dname)
print(kalyani.firstName)
print(kalyani.lastName)
kalyani.displayMName()
kalyani.displayDName()