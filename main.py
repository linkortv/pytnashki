import keyboard
import numpy as np
import PyQt5
import random

def random_permutation(array):
    length = len(array)
    for i in range(0, length):
        rnd = random.randint(0, length - 1)
        # обмен элементов массива
        temp = array[i]
        array[i] = array[rnd]
        array[rnd] = temp
    return array

def generate(a):
    a=random_permutation(a)
    if validate(a):
        a=to2mer(a)
        return  a 
    else:
        generate(a)

def validate(a):
    #print(a)
    s=0
    for i in range(len(a)):
        if a[i] != 'x' and i!=len(a):
            for j in range(i+1,len(a)):
                if a[j] != 'x':
                    if a[i]>a[j]:
                        s+=1
                        
            #print(s) 
    # if 0<=a.index('x')<=3:
    #     k=1
    # elif 4<=a.index('x')<=7:
    #     k=2
    # elif 8<=a.index('x')<=11:
    #     k=3
    # elif 12<=a.index('x')<=15:
    #     k=4
    # s+=k
    #print(s)
    if s%2 == 0:
        return True
    else:
        return False


def print_pressed_keys(e):
    #print(e, e.event_type, e.name)
    if e.event_type=="down":
        if e.name=="up":
            for i in range(len(a)):
                for j in range(len(a[i])):
                    #print(a[i][j])
                    if a[i][j]=="x":
                        k1=i 
                        k2=j
                        #print(k1,k2)
            if k1!=0:
                a[k1-1][k2],a[k1][k2]=a[k1][k2],a[k1-1][k2]
            print(a)
            print("-----------------------------------")
        elif e.name=="down":
            for i in range(len(a)):
                for j in range(len(a[i])):
                    #print(a[i][j])
                    if a[i][j]=="x":
                        k1=i 
                        k2=j
                        #print(k1,k2)
            if k1!=3:
                a[k1+1][k2],a[k1][k2]=a[k1][k2],a[k1+1][k2]
            print(a)
            print("-----------------------------------")
            
        elif e.name=="right":
            for i in range(len(a)):
                for j in range(len(a[i])):
                    #print(a[i][j])
                    if a[i][j]=="x":
                        k1=i 
                        k2=j
                        #print(k1,k2)
            if k2!=3:
                a[k1][k2+1],a[k1][k2]=a[k1][k2],a[k1][k2+1]
            print(a)
            print("-----------------------------------")
            
        elif e.name=="left":
            for i in range(len(a)):
                for j in range(len(a[i])):
                    #print(a[i][j])
                    if a[i][j]=="x":
                        k1=i 
                        k2=j
                        #print(k1,k2)
            if k2!=0:
                a[k1][k2-1],a[k1][k2]=a[k1][k2],a[k1][k2-1]
            print(a)
            print("-----------------------------------")

def to2mer(a):
    b=[]
    k1=[a[0],a[1],a[2],a[3]]
    k2=[a[4],a[5],a[6],a[7]]
    k3=[a[8],a[9],a[10],a[11]]
    k4=[a[12],a[13],a[14],a[15]]
    b.append(k1)
    b.append(k2)
    b.append(k3)
    b.append(k4)
    return b

a=[1,2,3,4,
5,6,7,8,
9,10,11,12,
13,14,15,'x']
a=generate(a)
a=np.array(a)
print(a)
print("-----------------------------------")
keyboard.hook(print_pressed_keys)
keyboard.wait()