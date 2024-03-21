# This is a parent class programing
class Employee:
    company="Google"
    
    def showDetails(self):
        print("This is an Employee")
# This is a Child class programing
class Programmer(Employee):
    language="Python"
    company="Youtube"
    def getLanguage(self):
        print(f"The language is {self.language}")
    def showDetails(self):
        print("This is a Programmer")

        
e=Employee()
e.showDetails()
p=Programmer()
print(p.company)
p.getLanguage()
p.showDetails()


# MULTIPUL classing

class Employee:
    company = "Visa"
    def printData(self):
        print(f"The eCode of this employee is {self.eCode}")
   
class Freelancer:
    company="Fiverr"
    level=0

    def upgradeLevel(self):
        self.level=self.level+1

class Programmer(Employee,Freelancer):
    name="Murtasim"

p=Programmer()
p.upgradeLevel()
print(p.company)
print(p.level)
Employee.eCode=2100
p.printData()


# multilevel class 
class Person:
    company="Pakistan"
    def takeBreath(self):
        print("I am breathing....")

class Employee(Person):
    company="Honda"
    def takeBreath(self):
        print("I am also breathing..By the help of Person")

class Programmer(Employee):
     company="Apple"
     def takeBreath(self):
        print("I am a programmer and I am working on C++..")


p= Person()
p.takeBreath()
print(p.company)
# .......
e=Employee()
e.takeBreath()
print(e.company)
# ......
pr=Programmer()
pr.takeBreath()
print(pr.company)


# SUPER class
class Person:
    company="Pakistan"
    def __init__(self):
        super().__init__()
        print("Initializing Person...\n")

    def takeBreath(self):
        print("I am breathing....")

class Employee(Person):
    company="Honda"
    def __init__(self):
        super().__init__()
        print("Initializing Employee...\n")

    def takeBreath(self):
        print("I am also breathing..By the help of Person")

class Programmer(Employee):
    company="Apple"
    def __init__(self):
        # super().__init__()
        print("Initializing Programmer...\n") 

    def takeBreath(self):
        super().takeBreath
        print("I am a programmer and I am working on C++..")


p= Person()
p.takeBreath()

# .......
e=Employee()
e.takeBreath()

# ......
pr=Programmer()
pr.takeBreath()

# PROPERTY-DECORATER
class Employee:
    company="SUI GAS"
    salary=550000
    salarybouns=1000
    # totalsalary=55800

    @property
    def totalsalary(self):
        return self.salary + self.salarybouns
    
    @totalsalary.setter
    def totalSalary(self,val):
        self.salarybouns=val-self.salary
        
e=Employee()
print(e.totalsalary)
e.totalSalary=580000
print(e.salary)
print(e.salarybouns)

# PRACTICE set

class C2dVec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j

    def __str__(self):
        return f"{self.icap}i+{self.jcap}j"
    
class C3dVec(C2dVec):
    def __init__(self, i, j,k):
        super().__init__(i, j,)
        self.kcap=k
    def __str__(self):
         return f"{self.icap}i+{self.jcap}j+{self.kcap}k"
    
v2d=C2dVec(1,5)
v3d=C3dVec(5,9,6)
print(v2d)
print(v3d)

# PROBLEM NUMB 2
class Animlas:
    animalType="Mammal"
class Pets:
    color = "White"
class Dog:
    @staticmethod
    def bark():
        print("BOW BOW!!")
d= Dog()
d.bark()
# THIS IS CALLED MULTI LEVEL INHERITANCE

# PROBLEM NUMB 3
class Employee:
    salary=1000
    increment=1.5
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
        self.increment=sai/self.salary
e=Employee()
print(e.increment)
e.salaryAfterIncrement=2000
print(e.increment)
print(e.salaryAfterIncrement)

# PROBLEM NUMBER 4
class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,c):
        return Complex(self.real + c.real, self.imaginary +c.imaginary)

    def __mul__(self,c):
        mulReal= self.real*c.real - self.imaginary + c.imaginary
        return Complex(self.real + c.real, self.imaginary + c.imaginary)
    
    def __str__(self):
        return f"{self.real}r+ {self.imaginary}i"

c1= Complex(1,5)
c2=Complex(8,5)
print(c1+c2)

