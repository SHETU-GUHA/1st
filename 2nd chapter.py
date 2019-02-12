'''name = 'Shetu'
password = 'abcde'
if name == 'Shetu':
    print('Hello shetu')
    if password == 'abcde':
        print('Access accepted')
    else:
        print('Wrong password')



###

name = 'Bob'
if name == 'Alice':
    print('Hi, Alice')
else:
    print ('Hello,stranger.')
    
###
name = 'Bob'
age = 7
if name =='Alice':
    print('Hi,alice')
elif age < 11 :
    print('This is not Alice,it is kiddo')
###
name = 'Bob'
age = 250
if name == 'Alice':
    print('Hi, Alice')
elif age<10 :
    print('You are not Alice. kiddo')
elif age< 130:
    print ( 'Alice is not happy:')
elif age>95:
    print('You are not Alice, you are robert')

###
spam = 1
while spam<4:
    print('Hello,World.')
    spam = spam +1 
###
name = ''
while name != 'your name':
    print ('please enter your name')
    name= input()
    print('Thank you')
###
while True:
    print('please enter your name')
    name=input()
    if name=='your name':
        break
print('Thank you')
###
while True:
    print('Who are you?')
    name=input()
    if name != 'jon':
        continue
        print('Hello ,  jon. what is your name')
        password=input()
        if password==abcde:
            break
print('Acess accepeted')
###
total=0
for num in range(101):
    total = total+num
print(total)
###
print('My Name is')
i=0
while i<3:
    print('jon five timea('+str(i)+')')
    i=i+1
###
for i in range(0,14,2):
    print(i)'''
###
import random
for i in range(5):
    print(random.randint(1,10))

1. true, false (T, F)
2. and ,not ,or
3. T and T= T
T and F=F
F and T =F
F and F =F
T or T = T
T OR F =T
F OR T =T
F OR F =F
4. F,F,T,F,F,T
5.==,!=,<,>,<=, and >=
6.== is the equal to operator that compares two values , the assignment operator that stores a value in a variable
7. Acondition is expression is used in flow control and evaluates bollean value.
8.print('bacon') and print('ham').


print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
print('spam')
9.if spam == 1:
    print('Hello')
elif spam == 2
    print('Howdy')
else:
    print('Greetings!')
11. The break statement will move the execution outside after a loop. The continue statement will move the execution to the start of the loop.
12.The range(10) call ranges from 0 up to (but not including) 10, range(0, 10)tells the loop to start at 0, and range(0, 10, 1) tells the loop to increase the variable by 1 on each iteration
13. for i in range(1, 11):
    print(i)
and:


i = 1
while i <= 10:
    print(i)
    i = i + 1


        
