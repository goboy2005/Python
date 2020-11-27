# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 23:50:46 2020

@author: goboy
"""

Python Day 2 Problems 

■ Q-23 for loop 문을 이용해서 구구단 2단을 출력하시오
2 x 1 =2
2 x 2 = 4 

for i in range (1,10):
    print( '2 x' , i, '=',  2*i )

■ Q-24 구구단 전체를 파이썬으로 출력하시오

2 x 1 =2
2 x 2 =4
   ……
9 X 8 = 72 

for j in range(2,10):
    for i in range(1,10):
        print( j, 'x', i, '=', j*i )

(printing a double for loop and ruuning a for loop to get the result could be differnt) 
 
■ Q-25 주사위를 10번던졌을때 나오는 주사위의 눈을 10개 출력하시오

import random

dice=[1,2,3,4,5,6,]
for i in range(1,11):
    print(random.choice(dice))

■ Q-26 주사위를 10번 던졌을때 짝수가 나오는 횟수를 출력하시오

import random

dice=[1,2,3,4,5,6,]
cnt=0
for i in range(1,11):
   result=random.choice(dice)
   if result % 2 == 0:
       cnt=cnt+1
print(cnt)


■ Q-27 위의 주사위를 10번 던져서 짝수가 나오는 획수를 확인하는 작업을 
5번반복해서 짝수가 나오는 횟수가 5개가 나오게 하시오

import  random

dice = [ 1, 2, 3, 4, 5, 6 ]

for  j  in  range(1,6):
    cnt = 0
    for  i  in   range(1, 11):
        result = random.choice(dice) 
        if  result % 2 == 0:  
            cnt = cnt + 1     
    
    print (cnt)  
                  
■ Q-28 동전을 100번 던져서 앞면이 나올 확률을 출력하시오

import random

coin=['앞면','뒷면']
cnt=0
for i in range(1,101):
    result =random.choice(coin)
    if result == '앞면':
        cnt=cnt+1
print(cnt/100)   

■ Q-29.위의 동전을 100번 던져서 앞면이 나올 확률을 구하는 작업을 50번 
반복해서 확률을 50개 출력하시오
 
import random

coin=['앞면','뒷면']
for j in range(1,51):
    cnt=0
    for i in range(1,101):
        result =random.choice(coin)
        if result == '앞면':
            cnt=cnt+1
    print(cnt/100)    

■ Q-30 파이선 리스트의 append 함수를 이용해서 위의 확률 50개를 
리스트에 담으시오

import random
dice=[1,2,3,4,5,6]
a=[]
for j in range(2,52):
    cnt=0
    for i in range(1,101):
        result=random.choice(dice)
        if result %2 == 0:
            cnt += 1
  
    a.append(cnt/100)
print(a)

■ Q-31 두개의 동전을 300번 던져서 동시에 둘다 앞면이 나오는
횟수를 출력하시오

import random
coin1=['앞면','뒷면']
coin2=['앞면','뒷면']
cnt=0
for i in range(1,301):
    result1=random.choice(coin1)
    result2=random.choice(coin2)
    if result1=='앞면' and result2=='뒷면':
        cnt=cnt+1
print(cnt)     

■ Q-32 x 라는 리스트를 만드는 x 라는 리스트의 위에 문제에서 앞면이
나오는 횟수를 x 리스트에 담는데 위의 둘다 앞면이 나오는 횟수를 출력하는
for loop문을 1000번 반복해서 x 리스트에 1000개를 입력하시오

import random

coin1 =['앞면', '뒷면']
coin2 =['앞면', '뒷면']

x = []
for  j  in  range(1, 1001):
    cnt = 0
    for   i   in   range(1, 301):
        result1 = random.choice(coin1)
        result2 = random.choice(coin2)
        if  result1=='앞면'  and  result2=='앞면':
            cnt = cnt + 1
    x.append(cnt)

print(x)    


■ Q-33 확률변수 x 의 값들의 평균과 분산과 표준편차를 출력하시오


import  random
import  numpy  as  np  # 넘파이 모듈을 이 코드에서 사용

coin1 =['앞면', '뒷면']
coin2 =['앞면', '뒷면']

x = []
for  i  in  range(1, 1001):
    cnt = 0
    for   i   in   range(1, 301):
        result1 = random.choice(coin1)
        result2 = random.choice(coin2)
        if  result1=='앞면'  and  result2=='앞면':
            cnt = cnt + 1
    x.append(cnt)

print(np.mean(x)) # 74.684
print(np.var(x))  # 55.366144
print(np.std(x))  # 7.440842962998211

■ Q-34 한개의 주사위를 360번 던져서 3의 배수의 눈이 나오는 횟수를  구하는 것을 1000번 하고 그 1000개를 X 변수에 넣고
이 X 의 평균,분산,표준편차를 출력하시오 

import numpy as np

import random
dice=[1,2,3,4,5,6]
a=[]
for j in range(1,1001):
    cnt=0
    for i in range(1,361):
        result=random.choice(dice)
        if result %3 == 0:
            cnt=cnt+1
    a.append(cnt) 

print(np.mean(a))
print(np.var(a))
print(np.std(a))


■ Q-35.숫자 1번부터 10번까지 출력하시오

 for i in range(1,11):
    print(i)

■ Q-36 위의 결과에서 숫자 5만 출력하지 않고 나머지 숫자만 출력하시오

for i in range(1,11):
    if i== 5:
        continue # 이부분을 그냥 지나치고 다음 루프 실행문을 계속 실행해라
    print(i)

■ Q-37 (알고리즘 문제 1번) 1부터 10까지의 숫자를 출력하는데
짝수만 출력하시오

for i in range(0,11):
    if i % 2 == 1:
        continue        
    print(i)

■ Q-38 알고리즘 문제 2번 1부터 10까지의 합을 파이썬으로 구현하시오

 cnt=0
    for i in range(1,11):
        cnt=cnt+i
print(cnt)


■ Q-39 1부터 100번까지 출력하는 for loop문을 작성하는데 다음과 같이 숫자를
물어보게 해서 입력된 숫자까지만 출력되게하시오 

a=int(input(  '숫자를 입력하세요'))
for i in range(1,101):
    if i == a+1:
        break
    print(i)

■ Q-40 (알고리즘 문제 19번) 두숫자를 각가 물어보게 하고 입력받아 
두 숫자의 최대공약수를 출력하시오 ! 

힌트 : 16%i == 0 and 24%i == 0: 
힌트: Print(max(16,24))  
num1=int( input('첫번째 숫자를 입력하세요~'))
num2=int( input('두번째 숫자를 입력하세요~'))

for i in range(max(num1,num2),1,-1):
    if num1%i == 0 and num2%i == 0:
        break
print (num1,'와',num2,'의 최대공약수는' ,i, '입니다.')


■ Q-41 위의 예제 코드를 수정해서 break를 넣어서 숫자를 물어보게 하고 숫자를
입력하면 해당 숫자만큼 1번부터 숫자가 출력되게 하시오

a = int ( input ('숫자를 입력하세요'))
for i in range(1,a+1):
    print(i)

■ Q-42.위의 입력한 숫자까지 다 출력하면 아래에 perfect 이란 단어가 출력되게 
하시오! 

a = int( input(' 숫자를 입력하세요 ~')  )

for  i  in  range( 1,  a+1 ):
    print (i)
else:
    print('perfect')

 Q-43. 위의 코드를 수정해서 중단할 숫자를 또 물어보게 해서 
아래와 같이 실행되게하시오 !
숫자를 입력하세요 ~    10
중단한 숫자를 입력하세요 ~  5

 1                           
 2
 3
 4
 5


a = int( input(' 숫자를 입력하세요 ~')  )
b = int( input(' 중단할 숫자를 입력하세요 ~')  )

for  i  in  range( 1,  a+1 ):
    print (i)
    if i == b:
        break

■ Q-44.아래와 같이 숫자를 물어보게 하고 숫자를 입력하면 해당 숫자만큼  *이 출력되게 하세요!          

a = int(input( '숫자를 입력하세요'))
x=0
while x<a:
    x=x+1
    print(x *'★')

■ Q-45 아래와 같이 결과가 출력되게 하시오!
숫자를 입력하세요 

b= int(input('숫자를 입력하세요'))

while b>0:
    print('★' * b)
    b=b-1

■ Q-46. 주사위 2개를 동시에 던져서 두개의 주사위의 눈의 합이 10이 되는
확률을 구하시오! 
주사위 2개를 던져서 두개의 주사위의 눈의 합을 구하는 실행문을 10000번 반복해서 그 10000 번 반복해서 그 10000개를 비어있는 a 리스트에 넣으시오

import random

dice=[1,2,3,4,5,6]
dice2=[1,2,3,4,5,6]

a=[]
x=0
while x<10000:
    result1=random.choice(dice)
    result2=random.choice(dice2)
    a.append( result1+result2)
    x=x+1
print(a)

print( len(a)) 

■ Q-47 (알고리즘 10번) 위의 코드를 이용해서 두개의 주사위의 눈의 합이 10이 되는 확률을 구하시오

import random
dice=[1,2,3,4,5,6]
cnt=0
x=[]                                           ]
while (cnt<10000):
    result_A = random.choice(dice)
    result_B = random.choice(dice)
    if result_A+result_B==10:  
        x.append(result_A+result_B) 
    cnt=cnt+1  
print(len(x)/10000)   
                     
■ Q-48 위의 말이 맞는지 for loop문으로 테스트 해서 확인하시오!
파이썬에서는 정수형 변수가 담을 수 있는 상수의 범위가
어떻게 되는지 테스트 하시오! 

for i in range(1000000):
    a=i
    print(i)

■ Q-49 3의 2승을 파이썬으로 구하세요! 

print( 3 ** 2)

■ Q-50 루트 4를 파이썬으로 파이썬으로 구하세요. 

import math
print ( math.sqrt(4) ) 

print(random.uniform(0,1) ) 

■ Q-51 알고리즘을 이용해서 원주율의 근사값을 파이썬으로 구하세요! 
몬테 카를로 알고리즘을 이용해서 원주율의 근사값을 파이썬으로 구하세요

import random
cnt = 0
 
for i in range(0,10001): 
    result1 = random.uniform(0,1) 
    result2 = random.uniform(0,1) 
   
    if (result1**2) + (result2**2) <=1 :
        cnt = cnt+1  
print(cnt/10000*4)

■ Q-52 아래의 수학식을 파이썬으로 구현해서 답을 출력하시오
(1-2i)^2 -2(1-2i)-12 

c1 = complex(1,-2)
result = c1**2 - 2*c1 -12
print(result)  # (-17+0j)

