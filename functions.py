# #function definition
# def calc_sum(a, b): 
#     return a +b

# #function call
# sum = calc_sum(45,67)
# print(sum)

# def helloPrint():
#     print("Hello")

# helloPrint()

# def averageNum(a, b, c):
#     return (a + b + c )/3

# average = averageNum(1,2,)
# print(average)

#default Paramerts 

# def calc_prod(a =1,b = 1):
#     print(a * b)
#     return a * b

# calc_prod()


# list = [2,34,56,78,45,78,34]

# def listLength(listValue):
#     print(len(listValue))


# listLength(list)

# def listElemets(listValues):
#     for i in listValues:
#         print(i, end= " ")

# listElemets(list)


# def factorial(value):
#     fact = 1
#     for i in range(1, value+1):
#         fact *= i
#     print(fact)

# factorial(6)        


# def currencyConverter(value):
#     res = value * 283.91
#     print(res)

# currencyConverter(1000)


# def check_Even_or_Odd(num):
#     if(num % 2 == 0):
#         print("Even")
#     else:
#         print("Odd")

# check_Even_or_Odd(99) 

#Recursion

# def show(n):
#     if(n == 0): #base case
#         return           
#     print(n, end=" ")
#     show(n-1)

# show(10)

# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n

# print(fact(10))

# def calc(n):
#     if(n == 0):
#         return 0
#     return calc(n-1) + n

# print(calc(5))

fruits = ["Apple", "Banana", "Mango"]

def print_list(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

print_list(fruits)    