a= 25 
b= 12
print("The sum of a and b is", a+b)
# The above programing is called (PROCEGURE ORENTATED PROGRAMING)

class Number : 
    def sum(self):
        return self.a+ self.b
    
num= Number()
num.a=12
num.b=34
s= num.sum()
print(s)


# RAILWAY FORM 
class RailwayForm:
    formType="RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

mustafasApplication= RailwayForm()
mustafasApplication.name="Mustafa"
mustafasApplication.train="Green line"
mustafasApplication.printData()

# GAME FORM 
class Remote():
    pass

class Player:
    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def moveUp(self):
        pass

remote1=Remote()
player1= Player()

if(remote1.isLeftPressed()):
    player1.moveLeft()


# OFFICE TALK
class Employee:
    company="Google"
    salary=1000


Mustafa=Employee()
Saad=Employee()

# Creating isinstance Attribute salary for both the objects
Mustafa.salary=300
Mustafa.company="Youtube"
# Saad.salary=500
print(Mustafa.salary)
print(Saad.salary)
print(Mustafa.company)
print(Saad.company) 
# print(Saad.adrees)


# SALARY PROGRAM
class Employee:
    company="Google"
    def getsalary(self, signature ):
        print(f"The Salary of this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

harry=Employee()
harry.salary=100000
harry.getsalary("Happy")
# harry.getsalary() # Employee.getsalary(harry)
harry.greet() # Employee.greet()
 

# CONSTRUCTOR 
class Employee:
    company="Google"
    salary=100000

    def __init__(self,name,salary,subunit):
       self.name=name
       self.salary=salary
       self.subunit=subunit
       print("Employee is created!")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    def getsalary(self, signature ):
        print(f"The Salary of this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

harry =Employee("Mustafa",100,"Youtube")
harry.getsalary("HELLO")
harry.getDetails()

#  ME USING MY BRAIN TO MESS WITH OOPS BUT OPPS IT DIDNT WORK OUT

class Employee:
    company="Google"
    salary=100000

    def __init__(self,name,salary,subunit):
       self.name=name
       self.salary=salary
       self.subunit=subunit
       print(f"Employee is created!\nThe name of the employee is {self.name}\nThe salary of the employee is {self.salary}\nThe subunit of the employee is {self.subunit}")

    # def getDetails(self):
        # print(f"The name of the employee is {self.name}")
        # print(f"The salary of the employee is {self.salary}")
        # print(f"The subunit of the employee is {self.subunit}")

    # def getsalary(self, signature ):
        # print(f"The Salary of this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

harry =Employee("Mustafa",100,"Youtube")
# harry.getsalary("HELLO")
# harry.getDetails()


# Practic set problem 1
class Programmer:
    company="Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product

    def getInfo(self):
        print(f"The name of the programmer is {self.name} and the product is {self.product}")

mustafa=Programmer("Mustafa","Skype")        
laiba=Programmer("Laiba","GitHub")
mustafa.getInfo()
laiba.getInfo()

# Problem 2
class Calculator:
   def __init__(self,num):
      self.number= num

   def square(self):
       print(f"The value of {self.number} square is {self.number**2}")
   
   def squaRoot(self):
       print(f"The value of {self.number} squareRoot is {self.number**5.5}")
       
   
   def cube(self):
       print(f"The value of {self.number} cube is {self.number**4}")
       
   
a=Calculator(3)
a.square()
a.squaRoot()
a.cube()

# Problem 3creating a train info 

class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getStatus(self):
         print("***************")
         print(f"The name of the train is {self.name}")
         print(f"The number of avalible seats in the train are {self.seats}")
         print("**********")
        
    def getFare(self):
        print(f"The fare of the train is Rs.{self.fare}") 

    def bookTicket(self):
        if(self.seats>0):
           print(f"Your ticket has been booked! Your seat number is {self.seats}")
           self.seats=self.seats -1 
        else:
            print("Sorry this train is full!")

    def cancelTickect(self):
        print(f"Your tickect {self.seats} has been cancled! ")
        self.seats=self.seats +1

intercity = Train("Intercity Express :14007 ", 800 , 5)
intercity.getFare()
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.cancelTickect()
intercity.getStatus()

# DRY=DONT USE YOUESELF