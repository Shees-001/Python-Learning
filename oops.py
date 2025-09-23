# #creating class
# # class Student:

# #     #Default constructor
# #     def __init__(self):
# #         pass

# #     #parameterized constructors    
# #     def __init__(self, fullname):
# #         self.name = fullname 

# #     def hello(self):
# #         print("Welcome ",self.name)      

# # #creating oject(instance)
# # s1 = Student("Shees")
# # print(s1.name)    
# # s1.hello()

# # class Cars:
# #     color = "blue"
# #     brand = "mercedes"


# # car1 = Cars()
# # print(car1.color)

# # Create Student class that takes name & marks of 3 subject as argument in constrctor. Then create a method to print average

# class Student():

#     def __init__(self, name, marks):
#         self.name = name # object attribute
#         self.marks = marks

#     @staticmethod #decorator
#     def hello():
#         print("Hello")

#     def average(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name)    
#         print("Your average marks is: ",  sum/3)
    

# s1 = Student("Shees", [87,77,91])    
# s1.name = "ABC"
# s1.hello()
# s1.average()


# class Car():
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car Started .. ")


# car1 = Car()
# car1.start()


#Create Account Class with 2 attributes - balance & account no.
#Create methods for debit, credit and prinitng the balance


# class Account():
#     def __init__(self, balance, accountno):
#         self.balance = balance 
#         self.accountno = accountno

#     #debit
#     def debit(self, amount):
#         self.balance -= amount
#         print(f"Rs. {amount} Debited")
#         print("Total balance = ", self.get_balance())

#     #credit
#     def credit(self, amount):
#         self.balance += amount
#         print(f"Rs. {amount} Credited")
#         print("Total balance = ", self.get_balance())

#     #balance
#     def get_balance(self):
#         return self.balance

# acc1 = Account(5000, 123)
# acc1.debit(200)
# acc1.credit(2000)


#Inheritance

# class Car:
#     def __init__(self, type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("Start")

#     @staticmethod
#     def stop():
#         print("Stop") 


# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)

# car1 = ToyotaCar("Prius", "Hybrid")

# print(car1.type)



# class A:
#     varA = "Welocme to Class A"

# class B:
#     varB = "Welocme to Class B"


# class C(A,B):
#     varC = "Welocme to Class C"

# c = C()

# print(c.varA)
# print(c.varB)
# print(c.varC)


# class Student:
#     def __init__(self, phy, chem, maths):
#         self.phy = phy
#         self.chem = chem
#         self.maths = maths
#         #self.percentage = str((maths + phy + chem)/3 ) + "%
    
#     @property
#     def percentage(self):
#         return str((self.maths + self.phy + self.chem)/3 ) + "%"


# s1 = Student(67,88,87)
# s1.maths = 76
# print(s1.percentage)        


#Polymorphism

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i +", self.img,"j" )

#     def __add__(self, num2):
#         realNumber = self.real + num2.real 
#         imgNumber = self.img + num2.img
#         return Complex(realNumber, imgNumber)
    
# num1 = Complex(2, 3)
# num1.showNumber()

# num2 = Complex(4,6)
# num2.showNumber()

# num3  = num1 + num2

# num3.showNumber()


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius 

#     def area(self):
#         return (22/7) * self.radius ** 2
    
#     def parameter(self):
#         return 2 * (22/7) * self.radius

# c1 = Circle(41)        
# print(c1.area())
# print(c1.parameter())


# class Employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary

#     def showDetails(self):
#         print(self.role) 
#         print(self.department)
#         print( self.salary)

# class Developers(Employee):
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age
#         super().__init__("Software Developer", "Development", "50,000")
                

# dev1 = Developers("Shees", "19")        
# dev1.showDetails()
        

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price
        


o1 = Order("Laptop", 50_000)        
o2 = Order("iPhone", 500_000)        
o3 = Order("PS5", 175_000)        
    
print(o2 > o1)