print("hello world") 
name="hey I am learning python"
print(name)
# age=input("what is your age")
# name=input("what is your name")
# Piyush bhatt
# print(age)
print(name)
print(name.find('a'))
# 9
print(name.find("Bhatt"))
# -1
print('t' in name)
# False
print(5 ** 4)
# 25
print(5 // 2)
# 2 double / removes the digits after the point
print(3<2)
# False
print(3>2 and 2>1)
# True      
print(not 2>3)
# True
age =60
if age>=18:
    print("you are adult")
# print("thankyou")
elif age<18 and age>100:
    print("not adult")
# elif se ye hoga ke iske upar wale condition false ha tabhi ye chalege iske niche elif ha to vo bhi tabhi chalege
else:
    print("you are in school")
print(range(5))
# 0,1,2,3,4
i=1
while i<=5:
    print(i * '*')
    i=i+1
for j in range(10):
    print(j)
marks=[1,4,64,33,87]
# list
print(marks[3])
# 33
print(marks[-1])
# 87
print(marks[-2])
# 33
print(marks[0:3])
# [1,4,64]
marks.append(99)
print(marks)
# it will add 99 to its end
marks.insert(0,77)
print(marks)
print(len(marks))
# prints the size of list
marks.clear
print(marks)
# clear all the elements
list=[23,94,64.45,63.12,23.06]
del list[1:4]
print("hello",list)
# [23,23.06]
list.pop()
# last se element ko delet krdega
# del list[:]
# print(list)
#  [] 
print(list)
alphabet=['a','t','w','o','m']
for item in alphabet:
    if item == 'w':
        break
    print(item)
# jb w ke equal hoga to break krega a or t he print honge
print("next command")
for char in alphabet:
    if char =='w':
        continue
    print(char)    
# w ko chod ke sb print honge
tupple=(34,65,73,35,73)
print(tupple[1])
# 65
# tupple[3]=77
# shows error it is immutable
print(tupple.count(73))
# 2 times
print(tupple.index(65))
# 1
tupple2=(123,4565,'helloo tupple')
print(tupple2[2])
# helloo tupple
# tupple can also hold string
sets={23,56,37,97,56}
print(sets)
# {56,97,37,23} sets include only unique values
# sets ka koi index nhi hota isse for loops se he access kr skta ha
dictionary={"piyush" :18 , "bhatt" : 20}
dictionary2={
    'name' :['piyush','bhatt','ramji','hanumanji'],
    'marks':[13,38,39,12],
}
age=(dictionary["piyush"])
print(age)
# you can also add elements to the dictionary
dictionary["ramji"]=1000
print(dictionary)
# tino ko dikha de ga
print(dictionary2)


       