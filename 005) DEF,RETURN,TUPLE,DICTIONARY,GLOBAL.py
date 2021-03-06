# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 23:55:37 2020

@author: goboy
"""

Python Day 6 Problems

■ Q-122.동전의 앞면과 뒷을 포함하는 리스트 coin을 만드시오 

coin=['앞면','뒷면'] 

■ Q-123위에서 만든 coin의 요소를 10000개로 늘려서 coin_10000변수에 담으시오
 '앞면','뒷면']

coin_10000=coin*10000
print(coin_10000)

■ Q-124 위에서 만든 Coin_10000 리스트에서 표본을 10개를 추출하시오.

import numpy as np
coin=['앞면','뒷면']

coin_10000=coin*10000
print(np.random.choice(coin_10000,10))

■ Q-125 위에서 추출한 샘플 10개에서 앞면이 몇번 나오는지 출력하시오 

coin = ['앞면', '뒷면']
coin_10000 = coin * 10000
result = np.random.choice( coin_10000, 10) 
print( type(result) )
cnt = 0
for  i  in   result:  
    if  i =='앞면': 
        cnt = cnt + 1

■ Q-126  a리스트에 세번째 요소를 17로 변경하시오! 

a=[7,2,3,4,5]
a[2]=17
print(a)

■ Q-127 아래의 숫자 데이터들을 튜플로 생성하시오! 튜플 변수의 이름은 point 라고 하세요 !
(0.01,0.02,0.03,0.04,0.05)

point=(0.01,0.02,0.03,0.04,0.05)
print(point)
print(type(point))

■ Q-128 위의 튜플 point의 요소중 0.03만 뽑아서 출력하시오 

point=(0.01,0.02,0.03,0.04,0.05)
print(point[2])

■ Q-129 위의 튜플의 모든 요소를 다 출력하시오 

point=(0.01,0.02,0.03,0.04,0.05)
for i in point:
    print(i)

&

for j in 'scott':
    print(j)


■ Q-130 아래의 두개의 리스트를 각각 만들고 아래와 같이 fruit 라는
딕셔너리를 생성하시오! (for 문의 zip 사용하면 편하게 할 수 있음) 
a=['사과','배','포도','복숭아','바나나']
b=['apple','pear','grape','peach','banana']

fruit={}
for i,k in zip(a,b):
    fruit[i]=k 
print(fruit)

■ Q-131. (점심)아래의 SQL을 파이썬으로 구현하시오 !

select  lower(ename), lower(job)
             from  emp;

import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
for i, k in zip(emp['ename'],emp['job']):
    print(i.lower(), k.lower())

■ Q-132 for loop 문을 사용하여 1부터 10까지 출력하시오 

for i in range(1,11)
    print(i)

■ Q-133 1부터 10까지 다 더한 값을 출력하시오! 

cnt=0
for i in range(1,11)
    cnt=cnt+i
print(cnt)

■ Q-134 위의 코드를 이용해서 함수를 생성하는데 아래와 같이 숫자를 입력하고 함수를
실행하면 해당 숫자가 1부터 다 더한 값이 출력되게 하시오 

def all_add(n1):
    cnt=0
    for i in range(1,n1+1):
        cnt=cnt+i
    return cnt
print(all_add(10))

■ Q-135다음의 문자열 변수를 생성하고 문자열 변수의 문자를 소문자로 출력하시오! 

a='scott'
print(a.lower())

Both works 

print('SCOTT'.lower())

■ Q-136 아래의 문자열을 대문자로 출력하시오! 

a='scott'
print(a.upper())

print('scoot'.upper())

■ Q-137 아래의 문자열에서 첫번째 철자만 출력하시오 

a='scott'
print(a[0])

■ Q-138 위에출력한 첫번째 철자를 대문자로 출력하시오 

a='scott'
print( a[0].upper())

■ Q-139. 아래의 문자열 변수에서 cott 만 출력하시오 
             ( 두번째 철자부터 끝까지 출력하시오 )

a='scott'  
print (a[1:])

■ Q-140아래의 함수를 생성하시오 ! ( 첫번째 철자 대문자 나머지 소문자로 출력되게 하는 함수)
( print(initcap('scott') ) 

def initcap(v):
    return v[0:1].upper() + v[1:].lower()
print(initcap('scott'))

■ 141.abs 함수를 사용하지 말고 if 문을 이용해서 절대값을 출력하는 
my_abs 라는 함수를 생성하시오 

def my_abs(num1):
    if num1>0:
        return num1
    else:
        return-num1 
print(my_abs(-5))
print(my_abs(5))


■ Q-142 서울시 초등학생 백만명의 키를 모집단으로 구성하는데
평균키가 148.5이고 표준편차가 30인 모집단을 만드시오! 

import numpy as np

avg=148.5
std=30
N=1000000

population=np.random.randn(N) * std+avg 

■ Q-143 위의 모단에서 100명을 표본으로 추출하여 100명의 평균키를
비어있는 리스트 a에 입력하는 작업을 10000번 수행하여
a리스트에 10000개의 표본의 평균키가 입력되게 하시오! 

import numpy as np

avg=148.5
std=30
N=1000000
a=[]
population=np.random.randn(N) * std+avg 
for i in range(1,10001):
    result=np.random.choice(population,100).mean()
    a.append(result)
print(a)

설명: 초등학생 100만명의 키 모집단에서 표본을 100개 추출해서  표본평균을 10000개
모았음 … 

■ Q-144. 통계학을 전문으로 구현하는 모듈인 scipy모듈을 임포트 하여
위의 표본의 평균키값에 대한 확률밀도값을 출력하시오! 

import numpy as np
from scipy.stats import norm 

avg=148.5
std=30
N=1000000
a=[]
population=np.random.randn(N) * std+avg 
for i in range(1,10001):
    result=np.random.choice(population,100).mean()
    a.append(result)
x=np.arange(140,160,0.001)                      # 140~160 까지 0.001 간격으로 숫자를 생성
y=norm.pdf(x,np.mean(a),np.std(a))

모듈과 패키지 차이는 여러개의 모듈이 들어있는게 패키지 이다 

■ Q-145. 데이터 시각화 전문 모듈인 matplotlib를 import 하여 
위의 표본 평균값 10000개의 데이터를 시각화 하시오! 

import numpy as np
from scipy.stats import norm 
import matplotlib.pyplot as plt 

avg=148.5
std=30
N=1000000
a=[]
population=np.random.randn(N) * std+avg 
for i in range(1,10001):
    result=np.random.choice(population,100).mean()
    a.append(result)
x=np.arange(140,160,0.001)   # 140~160 까지 0.001 간격으로 숫자를 생성
y=norm.pdf(x,np.mean(a),np.std(a))

plt.plot(x,y, color='red')
plt.show()

■ Q-146 위의 확률밀도함수 그래프의 아래쪽 영역도 색깔로 채우시오!

import numpy as np
from scipy.stats import norm 
import matplotlib.pyplot as plt 

avg=148.5
std=30
N=1000000
a=[]
population=np.random.randn(N) * std+avg 
for i in range(1,10001):
    result=np.random.choice(population,100).mean()
    a.append(result)
x=np.arange(140,160,0.001)   # 140~160 까지 0.001 간격으로 숫자를 생성
y=norm.pdf(x,np.mean(a),np.std(a))

plt.plot(x,y, color='blue')
plt.show()
plt.fill_between(x,y,interpolate=True,color='skyblue',alpha=0.3)
