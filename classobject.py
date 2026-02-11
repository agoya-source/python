#class is a blueprint os an object
#Object is an instance of a class

class Employee:
    #ttributes/Variables
    name = "James"
    age = 45
    gender = "Male"
    salary = 75000.00

    #Behaviour/Function
    def eat(self):
        print("Employee eats")


employee1 = Employee() #creating an object
print(employee1.name)
employee2 = Employee()
employee3 = Employee()