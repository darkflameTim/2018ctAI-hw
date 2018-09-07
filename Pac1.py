#1. 
fruits = ['apple', 'pear', 'orange', 'pinapple', 'mandarin']
 
# 2.
def i_found_it(fruit):
    if  fruit == "apple":
        return "I found it !"     
for i in range(len(fruits)):
    print(i_found_it(fruits[i]))
     
#3.
fruits.append('bannana')
fruits.append('kiwi')
 
# 4.
letters = list()
for i in range(len(fruits)):
    if fruits[i] == 'apple':
        letters.append(5)
    elif fruits[i] == 'pear':
        letters.append(4)
    elif fruits[i] == 'orange':
        letters.append(6)
    elif fruits[i] == 'pinapple':
        letters.append(8)
    elif fruits[i] == 'mandarin':
        letters.append(8)
    elif fruits[i] == 'bannana':
        letters.append(7)
    else:   
        letters.append(4)
for i in range(len(fruits)):
    print(str(fruits[i])+" has "+str(letters[i])+" letters ")

#5.
original = list()
square = list()
def half_squared(original):
    for i in range(len(original)):
        square.append((original[i]**2)/2)
    return square
print(half_squared([3,3]))

#6.
a = float(input("Please input the score: "))
if(a>=90):
    if(a<=100):
        print("Grade A")
    else:
        print("Error")
elif(a>=60):
    print("Grade B")
elif(a<60):
    if(a>=0):
        print("Grade C")
    else:
        print("Error")

#7.
def reSort(a,b,c):
    if(a>b):
        if(a>c):
            if(b>c):
                a,b,c = a,b,c
            else:
                a,b,c = a,c,b
        else:
            a,b,c = c,a,b
    else:
        if(b>c):
            if(a>c):
                a,b,c = b,a,c
            else:
                a,b,c = b,c,a
        else:
            a,b,c = c,b,a
    return a,b,c 

#8.
list1 = [1,2,3]
list2 = [4,5,6]
array = [list1,list2]
for i in range(0,len(list1)):
    print(list1[i])
for i in range(len(list2)):
    print(list2[i])
       
    
#9
def count(x):
    y = x
    n = 0
    while y != 0:
        y = y//10
        n = n+1
    return n
import math
def sum(x):
    c = count(x)
    if x<10:
        return x 
    else:
        h = int(x//math.pow(10,c-1))
        l = int(x-h*math.pow(10,c-1))
        x = h+sum(l)
        return x
def result(x):
    y = math.pow(x, 3)
    if x == sum(y):
        return x        
a = list()
for i in range(1,100):
    a.append(i)
for i in map(result,a):
    print(i)

#10.
import random
x = random.randint(1,10)
y = random.randint(1,10)
print(x,y)
x,y = y,x
print(x,y)

#11.
for i in range(1,8,2):
    t = (7-i)//2
    print(' '*t + '*'*i + ' '*t)
for i in range(1,4):
    t = 7-2*i
    print(' '*i + '*'*t + ' '*i) 
    

#12.
for i in range(1,7):
    for j in range(i,7):
        print(j,end="")
    for k in range(1,i):
        print(k,end="")
    print()
   
    
#13.
players = ['charles','martina','michael','florence','eli']
players1 = list()
for i in range(0,5):
    players1.append(players[i].title()) 
for i in range(0,5):
    for j in range(i+1,6):
        print(players1[i:j])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    