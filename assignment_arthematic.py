#write python program to calculate simple interest
'''
p=float(input("ENTER THE PRINCIPAL AMOUNT"))
t=float(input("ENTER THE TIME PERIOD"))
r=float(input("ENTER THE RATE OF INTEREST"))
i=((p*r)*t)/100
print(i)
'''

#write a python program to calculate speed using s=ut+1/2at^2
'''
u=float(input("Enter the initial velocity :"))
a=float(input("Enter the acceleration at time T :"))
t=float(input("Enter the time period :"))
s= (u*t)+(0.5*a*t*t)
print(s)
'''

#write pyhton program to find area and perimeter of a rectangle
'''
l=float(input("ENTER THE LENGTH :"))
b=float(input("ENTER THE BREADTH :"))
area=l*b
perimeter=2*(l+b)
print("area=",area)
print("perimeter=",perimeter)
'''

#write a python program to convert celsius to farheniet
'''
t=float(input("Enter the temperature in celsius"))
f=float((9/5)*t+32)
print(f)
'''

#write to find bmi
'''
w=float(input("enter the weight in kg :"))
h=float(input("enter the height in cm:"))
bmi=w/h
print("your BMI is : ",bmi)
'''

#write a program to calculate total price based on
#price,qunatity,subtotal,tax,total
'''
p=float(input("Enter the price of the product :"))
q=float(input("Enter the quantity of the product :"))
st=float(p*q)
tax=float(st*0.18)
total=float(st+tax)
print("TAX is : ",tax)
print("Total Bill  : ",total)
'''

#write a python program to calculate EMI for given loan amount?
'''
p=float(input("ENTER THE PRINCIPAL AMOUNT :"))
r=float(input("ENTER THE RATE OF INTEREST :"))
n=float(input("ENTER NUMBER OF DAYS"))
emi=((p*r*(1+r)**n)/((1+r)**n)-1)
print(emi)
'''

#write a python program to calculate distance between two points
'''
import math
x1=float(input("Enter X1 :"))
y1=float(input("Enter Y1 :"))
x2=float(input("Enter X2 :"))
y2=float(input("Enter Y2 :"))
distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(distance)
'''

#write calculator using tkinter
from tkinter import*
from tkinter import messagebox

window=Tk()
window.config(bg="black")
window.geometry("300x300")
window.title("LOGIN")