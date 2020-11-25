# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 23:50:46 2020

@author: goboy
"""

Q-23 for loop 문을 이용해서 구구단 2단을 출력하시오
2 x 1 =2
2 x 2 = 4 

for i in range (1,10):
    print( '2 x' , i, '=',  2*i )

설명 : for loop 문은 특정 문장을 반복해서 수행하고 싶을때
       사용하는 파이썬 문법
      위의 문법은 1부터 9까지 9번 반복하겠다. 

Q-24 구구단 전체를 파이썬으로 출력하시오

2 x 1 =2
2 x 2 =4
   ……
9 X 8 = 72 

for i in range (1,10):
    print( '2 x', i,'=',2*i)
for i in range (1,10):
    print( '3 x', i,'=',3*i)
     ………
for i in range (1,10):
    print( '9 x', i,'=',9*i)

■ 중첩 for loop 문 

loop 문을 중첩시켜서 수행한다. loop문 자체를 반복시킨다

예제)

for i in range(1,10):
    print('2x', i , '=' , 2 * i) 

애를 실행문으로 놔두고 싶다면 

         ↓

for j in range(1,10):           
    for i in range(1,10):                  →  실행문이된다
    print('2x', i , '=' , 2 * i) 

설명: 2단을 출력하는 for loop 문이 9번 실행되면서 2단이 9번 나왔습니다.
   2단을 9번 나오는게 아니라 2단부터 9단까지 출력해야하므로
   다음과 같이 작성해야 합니다.

※ (:) 다음에는 무조건 4칸 띄우세요 

for j in range(1,10):           
    for i in range(1,10):                  →  실행문이된다
    print('2x', i , '=' , 2 * i) 

for j in range(2,10):                    ← ----- j는 2부터 10미만 출력된다
    for i in range(1,10):                ← -----i 는 1부터 10미만까지 출력
        print( j, 'x' , i , ' = ' , j* i)

설명: j=2일 때 i 가 1~9까지 반복 실행
       j =3 일때 i 가 1~9까지 반복 실행
      j=4 일때 i 가 1~9 까지 반복 시행 


Q-25 주사위를 10번던졌을때 나오는 주사위의 눈을 10개 출력하시오

import random

dice=[1,2,3,4,5,6,]
for i in range(1,11):
    print(random.choice(dice))

Q-26 주사위를 10번 던졌을때 짝수가 나오는 횟수를 출력하시오

import random

dice=[1,2,3,4,5,6,]
cnt=0
for i in range(1,11):
   result=random.choice(dice)
   if result % 2 == 0:
       cnt=cnt+1
print(cnt)


Q-27 위의 주사위를 10번 던져서 짝수가 나오는 획수를 확인하는 작업을 
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
                  
Q-28 동전을 100번 던져서 앞면이 나올 확률을 출력하시오

import random

coin=['앞면','뒷면']
cnt=0
for i in range(1,101):
    result =random.choice(coin)
    if result == '앞면':
        cnt=cnt+1
print(cnt/100)   

Q-29.위의 동전을 100번 던져서 앞면이 나올 확률을 구하는 작업을 50번 
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

■ 리스트 append 함수의 기본 문법 
*해보기
a = []                                  # 비어있는 리스트 a를 생성합니다

a.append(7)                          # 비어있는 리스트 a를 생성합니다.
print(a)                                # a 리스트에 숫자 7을 넣는다.
a.append(8)                          # 리스트에 숫자 8을 넣는다. 
print(a)                             

Q-30 파이선 리스트의 append 함수를 이용해서 위의 확률 50개를 
리스트에 담으시오

import random

coin=['앞면','뒷면']
a = []
for j in range(1,51):
    cnt=0
    for i in range(1,101):
        result =random.choice(coin)
        if result == '앞면':
            cnt=cnt+1
    print(cnt/100)    
   a.append( cnt/100)
print(a) 

print (a) # a 리스트에 담겨있는 값들을 출력한다. 


Q-31 두개의 동전을 300번 던져서 동시에 둘다 앞면이 나오는
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

Q-32 x 라는 리스트를 만드는 x 라는 리스트의 위에 문제에서 앞면이
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


Q-33 확률변수 x 의 값들의 평균과 분산과 표준편차를 출력하시오


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

Q-34 한개의 주사위를 360번 던져서 3의 배수의 눈이 나오는 횟수를  구하는 것을 1000번 하고 그 1000개를 X 변수에 넣고
이 X 의 평균,분산,표준편차를 출력하시오 


import random
import numpy as np

dice=[1,2,3,4,5,6]                                  ----주사위 생성
a=[]                                                  ----cnt 에 0을 할당합니다.

for j in range(1,1001):      ----(360번 반복수행하는것을) 1000번 반복수행하는 loop
    cnt=0
    for i in range(1,361):                    ---360번 반복수행하는 for loop 
        result=random.choice(dice)   ----주사위의 눈을 하나 출력해서 result에담는다.
        if result %3 == 0:               ---결과값에서       
            cnt=cnt+1                    
     a.append(cnt)

print(np.mean(a))
print(np.var(a))        
print(np.std(a))


■  12.for 문 개념 배우기 2 (for~continue~break)

for 반복문 내에서 continue 를 만나면 그 다음 반복 실행으로 넘어가며
break  만나면 for 반복문을 완전히 벗어나게 됩니다.

예제) for 변수 in 범위:
       ….실행코드
       continue # 이부분을 그냥 지나치고 다음 반복문을 수행해라
       ….실행코드
       break      #for 반복문을 탈출


Q-35.숫자 1번부터 10번까지 출력하시오

 for i in range(1,11):
    print(i)

Q-36 위의 결과에서 숫자 5만 출력하지 않고 나머지 숫자만 출력하시오

for i in range(1,11):
    if i== 5:
        continue # 이부분을 그냥 지나치고 다음 루프 실행문을 계속 실행해라
    print(i)

Q-37 (알고리즘 문제 1번) 1부터 10까지의 숫자를 출력하는데
짝수만 출력하시오

for i in range(0,11):
    if i % 2 == 1:
        continue         # 이부분을 지나가는 것이니까 제외 되고 나온다. 
    print(i)

Q-38 알고리즘 문제 2번 1부터 10까지의 합을 파이썬으로 구현하시오

 cnt=0
    for i in range(1,11):
        cnt=cnt+i
print(cnt)

■  for 문에서 사용하는 break 문

 " 루프문을 중단시키는 역활을 하는 키워드 "

예제)

for  i  in  range(1, 11): # 1 부터 10까지 루프를 돌리는데 
    print (i)  # i 를 출력을 하다가 
    if  i  == 3:  # i 가 3 이면 
        break    # 루프문을 종료시켜라 ~

Q-39 1부터 100번까지 출력하는 for loop문을 작성하는데 다음과 같이 숫자를
물어보게 해서 입력된 숫자까지만 출력되게하시오 

a = int( input( '숫자를 입력하세요'))
for i in range(1,101):
    print(i)
    if i == a:
        break

Q-40 (알고리즘 문제 19번) 두숫자를 각가 물어보게 하고 입력받아 
두 숫자의 최대공약수를 출력하시오 ! 

힌트 : 16%i == 0 and 24%i == 0: 
힌트: Print(max(16,24))  
num1=int( input('첫번째 숫자를 입력하세요~'))
num2=int( input('두번째 숫자를 입력하세요~'))

for i in range(max(num1,num2),1,-1):
    if num1%i == 0 and num2%i == 0:
        break
print (num1,'와',num2,'의 최대공약수는' ,i, '입니다.')

■  013.for 문 개념 배우기 3 (for else)

for 반복문을 완전히 수행했을 때만 실행하는 부분을 정의하려면
for ~ else 문을 사용해야 합니다.
for ~ else 에서 else 뒤에 실행되는 코드는 for 반복문을 
성공적으로 수행해야지만 실행 됩니다.

예제)
for  i  in  range(1, 11):
    print (i) 
else:
    print ('Perfect')   #  break 에 의해서 루프문이 중단되면  else 다음에
                                   # 실행문이 실행되지 않습니다. 

Q-41 위의 예제 코드를 수정해서 break를 넣어서 숫자를 물어보게 하고 숫자를
입력하면 해당 숫자만큼 1번부터 숫자가 출력되게 하시오

a = int ( input ('숫자를 입력하세요'))
for i in range(1,a+1):
    print(i)

Q-42.위의 입력한 숫자까지 다 출력하면 아래에 perfect 이란 단어가 출력되게 
하시오! 
a= int ( input( '숫자를 입력하게 하시오'))
for i in range(1,a+1):
    print(i)
else:
    print('perfect')   

Q-42 위의 코드를 수정해라 중단할 숫자를 또 물어보게 해서
아래와 같이 실행되게 하시오! 
for  i  in  range( 1,  a+1 ):
    print (i)
else:
    print('perfect')


■ 014 while 문 개념 배우기 (while~continue~break)

for 루프문처럼 while 루프문도 같은 반복문 입니다.
for 루프문은 특정 범위에서 반복 실행하게 하는 반면에
while 루프문은 특정 조건에서 코드를 반복 실행하게 합니다.
        							
Q-44.아래와 같이 숫자를 물어보게 하고 숫자를 입력하면 해당 숫자만큼 *이 출력되게 하세요!          

a = int(input( '숫자를 입력하세요'))
x=0
while x<a:
    x=x+1
    print(x *'★')


Q-45 아래와 같이 결과가 출력되게 하시오!
숫자를 입력하세요 

b= int(input('숫자를 입력하세요'))

while b>0:
    print('★' * b)
    b=b-1


Q-46. 주사위 2개를 동시에 던져서 두개의 주사위의 눈의 합이 10이 되는
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

print( len(a))  # 리스트안의 요소의 갯수를 확인할수 있습니다. 


Q-47 (알고리즘 10번) 위의 코드를 이용해서 두개의 주사위의 눈의 합이 10이 되는 확률을 구하시오

import random
dice=[1,2,3,4,5,6]
cnt=0
x=[]                                           ]
while (cnt<10000):
    result_A = random.choice(dice)
    result_B = random.choice(dice)
    if result_A+result_B==10:  # 두개의 주사위의 눈의 합이 10 이면 
        x.append(result_A+result_B) # x 리스트에 추가해라 ~
    cnt=cnt+1  # cnt 를 1씩 증가시킨다. 
print(len(x)/10000)  # x 리스트에 있는 요소의 갯수를 len 으로 세고 
                      
■  015 None 개념 배우기 

None 은 아무것도 없다는 의미의 상수 입니다.
아무것도 없다는 것을 나타내기 위해서 주로 활용됩니다. 

예)
x=0 
while x<10:
    print(x)
    x=x+1 

위의 while loop 문에서의 x 변수는 숫자만 담기는 변수입니다.
그런데 어떨때는 숫자가 들어갈 수 도 있고, 어떨때는 문자가 들어갈수도 있어서
처음에 변수 선언시 결정을 못하겠다면 아래와 같이 하면 됩니다.

x = None   
a=1 
if a==1:                       
    x=[1,2,3,4]              # x라는 변수에 리스트를 담았습니다. 
else:
    x= 'I love python'   # x라는 변수에 문자열을 담았습니다.

print(x)  


■ 016.정수형 자료 이해하기 

자연수(1,2,3….) 와 음수 (-1,-2,-3…)와 0으로 이루어진 수의 체계를 정수라고 합니다. 

예) a=123
    b=-178
    c= 0 

일반 프로그래밍에서 지원하는 정수형 상수의 범위는 
-2,147,473,647 ~~~ 2,147,473,647 인데 (2의 31승) 
파이썬은 메모리가 허횽하는 범위에서 지원가능한 수를 다 사용할수 있습니다.

Q-48 위의 말이 맞는지 for loop문으로 테스트 해서 확인하시오!
파이썬에서는 정수형 변수가 담을 수 있는 상수의 범위가
어떻게 되는지 테스트 하시오! 

for i in range(1000000):
    a=i
    print(i)

Q-49 3의 2승을 파이썬으로 구하세요! 

print( 3 ** 2)

Q-50 루트 4를 파이썬으로 파이썬으로 구하세요. 

import math
print ( math.sqrt(4) ) 

print(random.uniform(0,1) ) 

Q-51 알고리즘을 이용해서 원주율의 근사값을 파이썬으로 구하세요! 
몬테 카를로 알고리즘을 이용해서 원주율의 근사값을 파이썬으로 구하세요

import random
cnt = 0
 
for i in range(0,10001): 
    result1 = random.uniform(0,1) 
    result2 = random.uniform(0,1) 
   
    if (result1**2) + (result2**2) <=1 :
        cnt = cnt+1  
print(cnt/10000*4)

■  017 실수형 자료 이해하기
실수는 소수로 나타낼 수 있는 유리수와 소수로 나타낼 수 없는
무리수로 구성된 집합입니다. (무리수의 예: 원주율,오일러,자연상수 e)
파이썬은 실수를 지원하기 위해서 부동 소수형을 제공합니다. 

*부동 소수형의 특징
	1. 8바이트만 이용해서 수를 표현합니다. 즉 한정된 범위의 
      소수만 표현할수 있습니다. 
 2.  디지털 방식으로 소수를 표현해야 하므로 정밀도의 한계가 있습니다. 
    

■  복소수형 자료 이해하기 

복소수                   허수

정수 
유리수                  i 제곱하면 -1이 되는 수 
무리수

복소수는 실수부와 허수부로 되어있고, 허수부는 숫자뒤에 문자 i를 이용하는데 파이썬에서는 j를 사용합니다.

예 : c1 = 1    +      7j
         실수부        허수부 

print(c1.real) # 복소수형 자료에서  실수부만 취한다.
print(c1.img) # 복소수형 자료에서 허수부만 취한다.
c2=complex(2,3)  # 실수부가 2이고 허수부가 3인 복소수를 만든다. 
print(c2)   # 22


Q-52 아래의 수학식을 파이썬으로 구현해서 답을 출력하시오
(1-2i)^2 -2(1-2i)-12 

c1 = complex(1,-2)
result = c1**2 - 2*c1 -12
print(result)  # (-17+0j)

