import keyboard
import numpy as np
import PyQt5
import random

class Logic():
  _a1=[1,2,3,4,5,6,7,8, 9,10,11,12,13,14,15,'x']

  def __init__(self):
    self.a=np.asarray(self.to2mer(self.generate(self._a1)))

  def generate(self,a):
      random.shuffle(a)
      print(a)
      if self.validate(a):
          return a
      else:
          self.generate(a)
      return a
  def validate(self,a):
      #print(a)
      s=0
      for i in range(len(a)):
          if a[i] != 'x' and i!=len(a)-1:
              for j in range(i+1,len(a)):
                  if a[j] != 'x':
                      if a[i]>a[j]:
                          s+=1

      if s%2 == 0:
          return True
      else:
          return False


  def print_pressed_keys(self,e):
      #print(e, e.event_type, e.name)
      a=self.a
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
              print()
              #print(a)
              return a
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
              print()
              #print(a)
              return a
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
              print()
              #print(a)
              return a
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
              print()
              #print(a)
              return a
              print("-----------------------------------")

  def to2mer(self,a):
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


p=Logic()

print(p.a)
print("-----------------------------------")
keyboard.hook(p.print_pressed_keys)
print(p.a)
keyboard.wait()