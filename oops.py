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


class Account():
    def __init__(self, balance, accountno):
        self.balance = balance 
        self.accountno = accountno

    #debit
    def debit(self, amount):
        self.balance -= amount
        print(f"Rs. {amount} Debited")
        print("Total balance = ", self.get_balance())

    #credit
    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} Credited")
        print("Total balance = ", self.get_balance())

    #balance
    def get_balance(self):
        return self.balance

acc1 = Account(5000, 123)
acc1.debit(200)
acc1.credit(2000)
