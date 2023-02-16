print("==========================CALCULATOR==========================")
print('=======================Attention Please=======================')
print('================We have only this operations==================')
print("(+) is Plus")
print('(-) is Minus')
print('(/) is Divide')
print('(//) is Divide, but result will be concrete')
print('(*) is Multiply')
print('(%) is Mod')
print('(^) is Exponent')
print('($) is Square Root ')
print('(!) is Factorial')
from math import sqrt
import math
try:
   result=0
   while result==False:
    num1=int(input('First number:'))
    operation=(input('What do you want (operation):'))
    if operation !='+' and operation !='-' and operation !='*'and operation !='/'and operation !='//'and operation !='%' and operation !='!'and operation !='$' and operation !='^':
        print("===========Please use true operations===========")
    else:
        if operation=='$':
            result=sqrt(num1)
            print(f'Your result:{result}')
        elif operation=='!':
            result=math.factorial(num1)
            print(f'Your result:{result}')
        else:
            num2=int(input('Second number:'))
            if operation == '+':
                 result=num1+num2
            elif operation == '-':
                result=num1-num2
            elif operation == '/':
                result=num1/num2
            elif operation == '//':
               result=num1//num2   
            elif operation == '*':
                result=num1*num2
            elif operation == '^':
                result=num1**num2
            elif operation == '%':
                result=num1%num2
            print(f'Your result:{result}')
except ValueError:
   print("You don't input number ")
except ZeroDivisionError:
   print("MathError you can't devide 0")





