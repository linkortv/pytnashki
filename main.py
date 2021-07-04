import keyboard
import numpy as np
import PyQt5
import random
#x=symbols('x',real=True)


def generate(a):
    a=sorted(a, key=lambda a: random.random())
    if validate(a):
        return  a 
    else:
        generate(a)

def validate(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            k=1
            n=0
    if k>n:
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
            if k1!=2:
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
            if k2!=2:
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

x="x"
a=[[1,2,3],
[4,5,6],
[7,8,x]]

a=generate(a)
a=np.array(a)
print(a)
print("-----------------------------------")
keyboard.hook(print_pressed_keys)
keyboard.wait()