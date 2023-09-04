class Person:
    # class level variable
    country = "india"
    def __init__(self,fn,ln,age):
        self.firstName = fn
        self.lastName = ln
        self.age = age

    def displayName(self):
        print(self.firstName + self.lastName)

    def displayCountry(self):
        print(self.country)

    @classmethod
    def changeCourty(cls,newC):
        cls.country = newC

Person.changeCourty("USA")
kalyani  =  Person("kalyani","hadole",23)
kalyani.displayCountry()

dhanvi  =  Person("dhanvi","bangal",8)
dhanvi.displayCountry()

aryan = Person("aryan","pawar",12)
aryan.displayCountry()

dhanvi.country = "UK seattle"
dhanvi.displayCountry()


# program 2
class PersonB:
    def __init__(self,firstName,lasName):
        self.firstName = firstName
        self.lastName = lasName

    # getter()
    def getFirst(self):
        return self.firstName

    # setter()
    def setFirstName(self,fn):
        self.firstName = fn
        return self.firstName

    # setter
    # setcountry
    def setCountry(self,cntry):
        self.country = cntry
        return self.country

amol  = PersonB("amol","hadole")
amruta = PersonB("amruta","pawar")
amruta.setFirstName("rekha pawar")
amruta.setCountry("india")

print(amruta.firstName)
print(amruta.lastName)
print(amruta.country)

#############################################################


class MathUtils:
    @staticmethod
    def add(x,y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y


cal1 = MathUtils()
print(cal1.add(12,4))
print(cal1.sub(12,4))
print(MathUtils.add(12,3))
print(MathUtils.sub(12,3))

# program 2 count number of objects created from class
class MyClass:
    count = 0
    def __init__(self):
        MyClass.count =  MyClass.count + 1

    @staticmethod
    def get_object_count():
        return MyClass.count

a = MyClass()
b = MyClass()
c = MyClass()
d = MyClass()

print(MyClass.get_object_count())

# program 3


class Person:
    count = 0
    country = 'INDIA'
    def __init__(self):
        Person.count += 1

    @classmethod
    def getObjCount(cls):
        return Person.count

    @classmethod
    def updateCountry(cls,cn):
        cls.country = "india"

    @staticmethod
    def displayCoutry():
        return Person.country


a  = Person()
b  = Person()
print(b.getObjCount())
print(Person.getObjCount())