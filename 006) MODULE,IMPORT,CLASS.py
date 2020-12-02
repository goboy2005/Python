# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:39:52 2020

@author: goboy
"""

Day 6 Python Problmes 

■ Q-148 my_cal.py모듈 스크립트안에 곱하기를 하는 아래의 함수를 추가하시오! 

c://Users//std//my_cal.py

def gob_number(n1,n2):
    result=n1*n2
    return result 

And then save it / This will create a module for the above functions 

■ Q-149. 다른 새로운 창에서 my_cal 모듈을 import 하고 gob_number
함수를 실행하시오! 

print(my_cal.add_number(1,2))
print(my_cal.add_number(1,2))

■ Q-150.  이번에는 나누기를 하는 함수를 my_cal.py 에 저장하고 다른 새로운 창에서 
아래와 같이 import 하고 실행 될 수 있도록 하시오 !

import   my_cal 

print ( my_cal.add_number(1,2) ) 
print ( my_cal.gob_number(1,2) )
print ( my_cal.devide( 10, 2 )  )             

■ Q-151 my_loc 더를 site-packages 폴더 밑에 두세요! 

C:\users\goboy2005\anaconda3\lib\site-packages 

my_loc3 는 패키지이고
my_call은 모듈이다 
저기 에 파일에다가 패키지를 넣으면

from my_loc3 import my_call ---이렇게 패키지에서 모듈 불러오기 가능 

■ Q-152 아래의 행렬의 합을 출력하시오! 

import numpy as np 

a=[[1,2],[4,7]]
b=[[3,1],[6,2]] 
a2=np.array(a)
b2=np.array(b)
print(a2+b2)

■ Q-153.아래의 행렬의 합을 출력하시오! 

import numpy as np
a=[[ 6,3,4   ] ,[5,1,7] ] 
a2=np.array(a)
b=[[ 4,5,7 ], [9,20,4 ] ] 
b2=np.array(b)

print(a2+b2)

■ Q-154아래의 행렬의 곱을 먼저 손으로 구하시오

import numpy as np
a=[ [ 1,2] ,[4,3 ]]
b=[[2,1], [3,4 ]]
a2=np.array(a)
b2=np.array(b)
print(np.dot(a2,b2))

■ Q-155 아래의 행렬의 곱을 출력하시오! 

import numpy as np
a=[ [ 3,4,1] ,[2,4,3]]
b=[[2,1], [4,3 ],[6,7]]
a2=np.array(a)
b2=np.array(b)
print(np.dot(a2,b2))

■ Q-156. 폐사진을 파이썬에서 시각화 하시오 !

import  PIL.Image  as  pilimg   
import   numpy  as   np
import   matplotlib.pyplot  as  plt 다.

im = pilimg.open('c:\\data\\1.png') 
pix = np.array(im) 
print(pix)
plt.imshow(pix)

■ Q-157 총설계도를 수정해서 총알을 아래와 같이 충전하면
몇발이 충전되었습니다. 라는 메세지가 출력되게 하시오! 
gun1.charge(10)
10발이 충전되었습니다.

class  Gun(): 
    def  charge( self, num ): 
        self.bullet = num
        print ( num, '발이 충전되었습니다')

    def  shoot( self, num): 
        for  i  in  range(num):
            if  self.bullet > 0:
                print ('탕!')
                self.bullet -= 1
            elif  self.bullet ==0:
                print('총알이 없습니다')
                break

gun1 = Gun()
gun1.charge(10)

■ Q-158 이번에는 총을 쏘면 총알이 탕!탕! 하면서 아래쪽에 몇발 남았습니다.
라는 메세지가 출력되게하시오! 

gun1 = Gun()
gun1.charge(10)

gun1.shoot(3)
 탕!
 탕!
 탕!
7발 남았습니다.

class  Gun():
    def  charge( self, num ): 
        self.bullet = num
        print ( num, '발이 충전되었습니다')

    def  shoot( self, num):  # 총을 쏘는 함수 
        for  i  in  range(num):
            if  self.bullet > 0:
                print ('탕!')
                self.bullet -= 1
            
            elif  self.bullet ==0:
                print('총알이 없습니다')
                break
        print ( '총알이  ', self.bullet, ' 발 남았습니다')

gun1 = Gun()
gun1.charge(10)
gun1.shoot(3)

■ 159. 총을 처음 생산했을때 총알이 반드시 0발 장전되겠금
총설계도를 수정하시오!

class  Gun():
    def __init__(self): 
        self.bullet = 0 
        print ( '총이 만들어졌습니다' , self.bullet, '발 장전 되었습니다')

    def  charge( self, num ): # 총알을 충전하는 함수 
        self.bullet = num
        print ( num, '발이 충전되었습니다')

    def  shoot( self, num):  # 총을 쏘는 함수 
        for  i  in  range(num):
            if  self.bullet > 0:
                print ('탕!')
                self.bullet -= 1
            
            elif  self.bullet ==0:
                print('총알이 없습니다')
                break
        print ( '총알이  ', self.bullet, ' 발 남았습니다')

gun1  = Gun()

■ Q-160. 총 클래스를 이용해서 아래와 같이 카드 클래스를 만들고 아래와 같이
카드를 충전하고 사용하시오! 

class  Card():
    def __init__(self): 
        self.cash = 0  
        print ( '카드가 만들어졌습니다' , self.cash, '원이 충전 되었습니다')

    def  charge( self, num ):
        self.cash = num
        print ( num, '원이 충전되었습니다')

    def  consume( self, num):  
        if  self.cash > 0:
            self.cash -= num
            print (num ,'원 사용되었습니다')
            print ( '잔액이  ', self.cash, ' 원 남았습니다')
           
        elif  self.cash ==0:
            print('잔액이 없습니다')
           
card1  = Card()
card1.charge(10000)
card1.consume(1000)

Q-161. 초등학생 키에 한 모집단을 생성하세요! (천만개로 구성)
키의 평균 값은 140,표준편차 5로 해서 생성하시오 ! 

import numpy as np
avg=140
std=5
N=10000000

height=np.random.randn(N) *std+avg  

■ Q-162 위의 모집단에 표본 100개를 추출해서 표본의 평균값을 출력하시오! 

import numpy as np
avg=140
std=5
N=10000000

height=np.random.randn(N) *std+avg       
result=np.random.choice(height,100).mean()
print(result)  

■ Q-163위에서 표본 100개를 뽑아서 a라는 비어있는 리스트에 담는 작업을 10000번
수행하시오! 

import numpy as np
avg=140
std=5
N=10000000
a=[]
height=np.random.randn(N) *std+avg       
for i in range(1,10001):
    result=np.random.choice(height,100).mean()
    a.append(result)
print(len(a))
        
■ Q-164 위에서 구한 표본 평균값들 10000개의 평균값과 표준편차를 
s_avg와 s_std 변수를 각각 담으시오! 

import numpy as np
avg=140
std=5
N=10000000
a=[]
height=np.random.randn(N) *std+avg       
for i in range(1,10001):
    result=np.random.choice(height,100).mean()
    a.append(result)

s_avg=np.mean(a)
s_std=np.std(a)

print(s_avg,s_std)

■ Q-165 초등학생 키 데이터를 120부터 160까지 0.001 간격으로 생성하시오

import numpy as np
from scipy.stats import norm 

avg=140
std=5
N=10000000
a=[]
height=np.random.randn(N) *std+avg       
for i in range(1,10001):
    result=np.random.choice(height,100).mean()
    a.append(result)

s_avg=np.mean(a)
s_std=np.std(a)

x=np.arange(120,160,0.001) 
y=norm.pdf(x,s_avg,s_std)

■ Q-166 위에서 만든 x 에 있는 키값들은 x 축으로 두고 확률 밀도함수
그래프를 생하는데 y축의 확률밀도함수값을 구할 때 문제 164번에서 
구한 평균값,표준편차를 이용하세요 

import numpy as np

cnt = 0

height = np.random.randn(100000)*5+140
for i in range(1,1001):
    result = np.random.choice(height)
    if result >= 145 and result < 150:
        cnt = cnt + 1
print(cnt/1000)
