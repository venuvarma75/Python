#a = 10 
#b = 15
#if a == b:
 #print('you can get value')
#else:
 #print('you cannot get value')

# Q-1.write a program to check if a given number is positive, negative, or zero. 

num=-1
if num>0:
    print('positive number')
else:
    if num==0:
        print('zero is not a posive or negative number')
    
    else:
        print('negative number')
   
# number is even or odd
num1=55
if num1%2==0:
    print('it is even number')
else:
    print('it is an odd number')

#check ifa person is eligible for vote or not 
age=18
if age<18:
    print('you cannot vote')
else:
    print('you can vote')
# Q-. Write a program to find the greatest of two numbers. 
num4=22
num5=32
if num4>num5:
    print('num4 is Greatest number')
else:
    print('num5 is Greatest number')  
    

# Q-. Print "Pass" if a student scores more than 40 marks otherwise, print "Fail."
Marks=20
if Marks<40:
    print('Pass')
elif Marks>40:
    print('fail')
else:
    print('Pass') 
 

# Q-. Print "Pass" if a student scores more than 40 marks otherwise, print "Fail."
marks = 50
if marks<=40:
    print('fail')
else:
    print('pass')    
    
#write a program to display the day of the week based on a 
Day =input('enter a day')
if Day=="1":
    print('Monday')
elif Day=="2":
    print('Tuesday')
elif Day=="3":
    print('Wenesday')
elif Day=="4":
    print('Thursday')
elif Day=="5":
    print('friday')    
elif Day=="6":
    print('Saturday')
elif Day=="7":
    print('Sunday')
else:
    print('enter the day ')                        
        



# Q-7.Implement a simple calculator to perform addition, subtraction, multiplication, and division.
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operator= input('enter +,-,*,/ any onething')

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print("Result:", result)
  
# Q-.Write a program to display the name of a month based on the month number (1 for January, 2 for February, etc.)  '''
month=(input('Enter the month:'))
if month=="1":
    print('January')
elif month=="2":
    print('Feburary')
elif month=="3":
    print('March')
elif month=="4":
    print('April')
elif month=="5":
    print('May')
elif month=="6":
    print('June')
elif month=="7":
    print('July') 
elif month=="8":
    print('August')
elif month=="9":
    print('September')
elif month=="10":
    print('October')
elif month=="11":
    print('November')   
elif month=="12":
    print('December')       
else:
    print('enter the month')
#Q.Write a program to find the greatest of three numbers 
number1= input('enter the first greatest number') 
number2= input('enter the second greatest number')
number3= input('enter the third greatest number')   
if number1>number2:
    print('11')
elif number2>number3:
    print('22')        
else:
    print('88')


# Q-.Check if a year is a leap year. 
z = int(input("Enter the year: "))
if (z % 4 == 0 and z % 100 != 0 or z % 400 == 0):
    print("it is not a leap year")
else:
    print("leap year")       
 
    
# Q-3.Write a program to classify a character entered by the user as a vowel, consonant, or neither. 
text=input("enter a character:")
if text=="a" or text=="e" or text=="i" or text=="o" or text=="u":
    print("it is an vowel")
elif text.isdigit():
    print('it is an number')
else:
    print('it is an consonent')
    
    
# Q-4.Calculate the grade of a student based on the marks they 
# score: 
# 1.  90-100  : Grade A 
# 2.  80-89  : Grade B 
# 3.  70-79  : Grade C 
# 4.  <70  : Fail. 

                   

grade=77
if grade>90:
    print('GradeA')
elif grade>80:
    print('GradeB')
elif grade>70:
    print('GradeC')
elif grade>60:
    print('Fail')
else:
    print('enter the valid  Grade')
    
 #Write a program to check if three sides length form a valid
# triangle.
a = float(input("enter the first side: "))
b = float(input("enter the second side: "))
c = float(input("enter the third side: "))

if a + b> c and a + c > b and b + c  > a:
    print("The side of a traingle is a valid")
else:
    print("The side of a traingle is not valid")
            
           
    