class Student:
    def __init__(self,name,gpa,major):
        self.name=name
        self.gpa=gpa
        self.major=major

    def on_honor_roll(self):
        if self.gpa <= 3.5:
            return True     
        else:
            return False
        
Student1=Student("Joffrey",3.6,"Accounts")
student2=Student("Mave",2.5,"AI")

print(Student1.on_honor_roll()) 




