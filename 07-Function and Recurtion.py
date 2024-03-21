marks1=[55, 56, 78, 99]
percentage1=((marks1[0] + marks1[1] + marks1[2] + marks1[3] )/400)*100

marks2=[67, 99, 87, 35]
percentage2=((marks2[0] + marks2[1] + marks2[2] + marks2[3] )/400)*100
print(percentage1, percentage2)


# you can also write this by (sum(marks)/400)*100


def percent(marks):
    p=((marks[0] + marks[1] + marks[2] + marks[3] )/400)*100
    return p
marks1=[55, 56, 78, 99]
percentage1=percent(marks1)

marks2=[67, 99, 87, 99]
percentage2=percent(marks2)

print(percentage1, percentage2)

# defult prament value 
def greet(name):
    print("Good Day,"+name)
greet("Mustafa")

# recartion

