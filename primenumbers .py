#5.A bank rewards its customers who have an account number that is a 'Perfect Number.'
# A perfect number is a number whose sum of divisors 
# (excluding itself) equals the number itself. Write a program to check whether
# a given account number is a perfect number. 
number=input("Enter a Account number:")
number1=0
sumofdivisors=0
for i in range (1,number1):
     if number % i == 0:
         sumofdivisors+=1
if sumofdivisors == 0:
        print("Account number is perfect number")
else:
    print("Account number is not a  perfect number")
 


#2. n=125 print all  the prime numbers in range  using nested loops

num1 = 125
for i in range (2,int(num1 ** 0.5) + 1):
    if i % 2 == 0:
        print(i)
        spy=True
        print("prime number")
        break



#5) A company is organizing a large-scale project and 
# assigning teams sequential numbers (1, 2, 3, ... n). 
# However, due to resource constraints, only even-numbered teams receive funding.
n=20
for i in range (1,n+1):
     if i % 2 == 0:
         print("funding")
     else:
         print("not funding")


#9) Wap to print the sum of odd digits in a number. 
# { input : 2355 output : 13}
num1=15
sum=2+3+5+5
for i in range (1,sum):
    if i % 2!= 0:
        print(i)



//method 1
# num1=34
# count=0


# for i in range (1, num1+1):
#     if num1 % i == 0:
#         count+=1
        
# print("Prime number") if count == 2 else print ("not a prime number")

//method 2
#num1=36
# spy=False
# for i in range (2,num1):
#     if num1 % i == 0:
#         spy=True
#         print("not a prime number")
#         break
#     if spy == False:
#         print("prime number")
#     else:
#         print("not a prime number")
    
//Method 3
 #num1=45
# spy=False
# for i in range (2,num1//2 + 1):
#     if num1 % i == 0:
#         spy=True
#         print("not a prime number")
#         break
#     if spy == False:
#         print("prime number")
#     else:
#         print("not a prime number")   

//Method 4
#num1=40
# spy=True
# for i in range (2,int(num1 ** 0.5) + 1):
#     if num1 % i == 0:
#         spy=True
#         print("prime number")
#         break
#     if spy == False:
#         print("prime number")
#     else:
#         print("not a prime number")            
            
