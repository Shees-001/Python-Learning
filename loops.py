# count = 1

# while count <= 5:
#     print("Hello")
#     count += 1

# i = 1 
# while i <= 5:
#     print(i)
#     i += 1

# i = 5 
# while i >= 1:
#     print(i)
#     i -= 1

#Practice Questions 

#1. print multiplication of number n 

# range = 1
# n = 3

# while range <= 10:
#     print(f"3 x {range} = {n*range}" )
#     range += 1


#qs 4

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0
# while idx < len(num):
#     print(num[idx])
#     idx += 1


#qs 5
# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# i = 0
# x = 49

# while i < len(num):
#     if(num[i] == x):
#         print(x, "FOUND at index : ", i)
#         break
#     else:
#         print("Finding")    
#     i += 1    

#Continue Example

# i = 1 
# while(i <= 10):
#     if(i % 2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1    


# For loops 
# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for i in num:
#     print(i)


# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
# x = 36 
# idx = 0

# for i in num:
#     if(i == 36):
#         print(x, "Found at index", idx)
#         break
#     idx += 1   


# for i in range(101):
#     print(i)

# for i in range(100, 0, -1):   
#     print(i)

# num = int(input("Enter a number : "))

# for i in range(1, 11):
#     print(num*i)


# n = 5
# sum = 0

# for i in range(1, n+1):
#     sum += i

# print(sum)

# n =5 
# sum = 0 
# i = 1 
# while i <= 5 :
#     sum += i
#     i += 1

# print(sum)    


# n = 8
# factorial = 1

# for i in range(1, n+1):
#     factorial *= i

# print(factorial)