"""print("Enter first number : ")
a=input()
print("Enter first number : ")
b=input()
print("sum of",int(a),"and",int(b),"is",int(a)+int(b),".")
z= "767+893j"
f = z.isdecimal()
print(f)
num = []
print("Enter first number : ")
a=input()
print("Enter first number : ")
b=input()
num.append(a)
num.append(b)
print(num)
a=5
b=6
c=7
a,c,b = c,b,a
print(a,b,c)
d = {"ahmad":123,"hmad":1233}
print(d.)
dictionary = {"set":"Matlab set","map":"Matlab maap","array":"matlab array","list":"matlab list"}
word = input("Enter the word ")
print(dictionary.get(word))
s = set()
s1 = set([1,2,3])
print(s1.union([2,3,4,5]))
if 1>2:
    print("true")
elif 2>4:
   print("false")
   print("Yes")
else :
    print("else")
list = ["a","b","c"]
if 2 in list:
    print("found")
if 2 not in list:
    print("not found")
if "a" in list:
    print("found")
age = int(input("enter age"))
if age>18:
    print("you can drive")
elif age<18:
    print("You can't drive")
elif age==18:
    print("We can't decide")
operate = input("operator ")
num1 = int(input("number 1 "))
num2 = int(input("number 2 "))
if operate == "*" and num1 == 47 and num2 == 3 :
    print("faulty answer")
else :
    print(num1*num2)
list = ["a",4,8972,2,78,"hswa",("sjah"),]
for item in list:
    if str(item).isnumeric() and item < 100:
        print(item)

inpu = int(input("Enter the number "))
while(inpu <=100):
    inpu = int(input("Enter the number "))
    if inpu >100:
        print("Congratulate you enter the number greater than 100")
n = 67
tries = 5
print("Guess the number ")
while (True):
   if tries != 0:
    tries = tries - 1
    inp = int(input())
    if inp == n:
        print("Congratulations You won!!")
        print(" total number of tries ", int(5-tries))
        break
    if tries != 0:
         if inp > n:
           print("Your input is large Try again (Tries left",tries,")")
           continue
         else:
           print("Yout input is small Try again (Tries left",tries,")")
           continue
   else:
       print("You have lost")
       break
#Bitwise operator
print (1 | 11)
a = int(input("Enter a "))
b = int(input("Enter b "))
print("a is greater than b") if a>b else print("b is greater than a")
a = 5
b = 6
def AverageFunction(a,b):
    ""This functions return the average of two numbers""
    return (a+b)/2
average = AverageFunction(a,b)
print(average)
print(AverageFunction.__doc__)  #Print the DocStrings
print(AverageFunction(a,b))"""
import pandas as pd

# create a simple DataFrame with three columns
data = {'ID': ['A', 'A', 'B', 'B', 'B', 'C'],
        'Gender': ['M', 'F', 'F', 'F', 'M', 'M'],
        'Height': [175, 163, 170, 162, 180, 167]}
df = pd.DataFrame(data)

# create a pivot table to summarize the data by Gender
pt = pd.pivot_table(df, values='Height', index='Gender', aggfunc=['max'])

print(pt)
print(pt.shape)


