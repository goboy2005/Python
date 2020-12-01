# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 23:03:39 2020

@author: goboy
"""


■ Q-86 이름이 SCOTT인 사원의 이름과 월급을 출력하시오 
   
import pandas as pd
emp=pd.read_csv("c://data//emp3.csv")
print( emp   [[   'ename','sal']]  [ emp ['ename'] == 'SCOTT'  ]   )

■ Q-87 위의 scott 을 담은 문자형 변수 a에서 알파벳 0를 출력하시오 
 
a='scott'
print(a[2])

■ Q-88 아래의 문자형 변수에서 맨 끝의 철자인 h를 출력하시오! 
         b='smith'
  
b='smith'
print(b[4])

b='smith'
print(b[-1])


■ Q-89 판다스를 이용해서 emp3.csv 에서 이름을 출력하는데 
       이름의 첫번째 철자만 출력하시오! 
       (Use pandas and print the first character of the employees' name) 

import pandas as pd
emp=pd.read_csv("c://data//emp3.csv")
for i in emp  [ 'ename']:
    print(i[0])


■ Q-90 판다스를 이용해서 emp3.csv를 가져와서 이름의 끌글자를 출력하시오
        (use pandas and print out the last character of each employees' name)

import pandas as pd
emp=pd.read_csv("c://data//emp3.csv")
for i in emp ['ename']:
    print(i[-1])


■ Q-91 위의 결과에서 앞에 이름도 같이 출력하시오! 
        (This time also print the full name of each employees' name) 

import pandas as pd
emp=pd.read_csv("c://data//emp3.csv")
for i in emp ['ename']:
    print(i,i[-1])


■ Q-92 이름의 첫번째 철자가 S 로 시작하는 사원들의 이름을 출력하시오

select ename
from emp
where ename like 'S%' ; 

import pandas as pd
emp=pd.read_csv("c://data//emp3.csv")
for i in emp['ename']:
    if i[0] =='S':
        print(i) 


■ Q-93이름의 끝글자가 T 로 끝나는 사원들의 이름을 출력하시오 using pandas 
       (Print the ename of employees who's their name ends with 'T'

import pandas as pd
emp=pd.read_csv("c://data//emp3.csv")
for i in emp['ename']:
    if i[-1] =='T':
        print(i)

■ Q-94 이름의 두번째 철자가 M인 사원의 이름을  출력하시오
import pandas as pd 
emp=pd.read_csv("c://data//emp3.csv")
for i in emp['ename']:
    if i[1] == 'M':
        print(i)

■ Q-95  아래의 SQL을 판다스로 구현하시오
select substr(ename,1,3)
  from emp ;

import pandas as pd 
emp=pd.read_csv("c://data//emp3.csv")
for i in emp['ename']:
        print(i[0:3] ) 

■ Q-96 아래의 SQL을 판다스로 구현하시오 
select subst(ename,-2,2)             K I      ( N  G ) 이것을 뽑으시오! 
from emp;                                       -2    -1 

import pandas as pd 
emp=pd.read_csv("c://data//emp3.csv")
for i in emp['ename']:
    print(i[-2 :])

■ Q-97.아래의 SQL을 판다스로 구현하시오! 

select substr(ename,2,3) 
  from emp;

a='i love'
b='python'
print(a+b) i love python

■ Q-98 아래의 두개의 리스트를 연결하여 같이 출력하시오

a=[2,3,4,5]
b=[9,2,4,8]

print( a +b ) 

■ Q-99 아래의 SQL을 판다스로 구현하시오 !
select ename || sal
        from emp;

import pandas as pd 
emp=pd.read_csv("c://data//emp3.csv")
for i, k in zip(emp['ename'],  emp['sal'] ):
    print(i+ str(k)) 
    
■ Q-100 주사위의 눈 6개를 100개 담은 리스트 dice 100을 만드시오 

dice100=[1,2,3,4,5,6] *100
print(dice)


■ Q-101 초등학생 키가 10ㅐ가 들어있는 아래의 tall 리스트의 요소 10개를
10000개로 증가시켜서 만드시오 
Tall=[129.3, 130.2, 132.5, 134.7, 136.3, 137.8, 138.1, 140.2, 142.3 , 145.2] 

tall10000=[129.3, 130.2, 132.5, 134.7, 136.3, 137.8, 138.1, 140.2, 142.3 , 145.2] *100000
print(tall10000) 

■ Q-102.위의 모집단의 평균값,분산,표준편차 출력하시오 

import numpy as np
tall10000=[129.3, 130.2, 132.5, 134.7, 136.3, 137.8, 138.1, 140.2, 142.3 , 145.2] *100000

print(np.mean(tall10000))
print(np.var(tall10000))
print(np.std(tall10000))


tall10000=tall*10000 # 초등학생 키 데이터 10000개 생성(모집단 생성)

for i in range(1,21): # 20번 반복하면서  
    print(random.choice(tall10000) ) # 모단에서 랜덤으로 키하나를 추출 


■ Q-103. 위의 모집단 tall10000 에서 표본을 20개를 랜덤으로 추출하시오 !

import  numpy  as  np 
import  random  

tall = [ 129.3,  130.2, 132.5, 134.7, 136.3, 137.8,  138.1, 140.2, 142.3, 145.2] 

tall10000 = tall*10000 # 초등학생 키 데이터 10000 개 생성(모집단 생성)

for  i  in  range(1, 21):          #  20번 반복 하면서 
    print( random.choice( tall10000) )         # 모집단에서 랜덤으로 키하나를 추출


■ Q-104 위의 랜덤으로 추출한 표본 20개를 비어있는 리스트 a 에 담으시오

import random
a=[]
tall10000=[129.3, 130.2, 132.5, 134.7, 136.3, 137.8, 138.1, 140.2, 142.3 , 145.2] *100000
for i in range(1,21):
    result=random.choice(tall10000)
    a.append(result)
print(a)

모집단에서 랜덤으로 키하나를 추출해서 a 리스트에 담는다. 

■ Q-105 위의 표본의 평균값을 출력하시오 !

import numpy as np
import random
a=[]
tall10000=[129.3, 130.2, 132.5, 134.7, 136.3, 137.8, 138.1, 140.2, 142.3 , 145.2] *100000
for i in range(1,21):
    result=random.choice(tall10000)
    a.append(result)

print(np.mean(a))

예제: a='scott'
       print( len(a) ) 


■ Q-107모평균이 30이고 모표준편차가 7인 모집단을 구성하시오! 

import numpy as np
avg= 30
std=7
N=1,000,000 

mogipdan=np.random.randn(N) * std +avg 
print(mogipdan) 


■ Q-108 위의 모집단의 모평균을 출력하시오! 

import  numpy  as  np 

avg = 30
std = 7
N = 1000000

mogipdan = np.random.randn(N) * std + avg 
print ( np.mean( mogipdan ) )


■ Q-109 아래의 SQL을 판다스로 구현하시오! 
select ename,sal
 from emp
  where job in ('SALESMAN','ANALYST') ;

import pandas as pd 
emp=pd.read_csv("c://data//emp3.csv")
print(emp[['ename','job']] [emp['job'].isin(['SALESMAN','ANALYST' ]) ]) 


■ Q-110 아래의 SQL을 판다스로 구현하시오 

Select ename,job
 from emp
  where job not in ('SALESMAN','ANALYST') 

import pandas as pd 
emp=pd.read_csv("c://data//emp3.csv")
print(emp[['ename','job']] [~emp['job'].isin(['SALESMAN','ANALYST' ]) ]) 


■ Q-111 아래와 같은 글씨가 출력되게 하시오! 
"모집단의"  모평균은
"모집단읜" 모분산은
"모집단"의 표준편차는 

a=""""모집단의" 모평균은""" 
b=""""모집단의" 모분산은"""
c=""""모집단의" 표준편차는 """
print(a)
print(b)
print(c)


■ Q-112모평균이 30이고 모표준편차가 7인 모집단 1,000,000개의 모평균과
모분산과 모표준편차를 아래와 같이 출력하시오 

avg=30
std=7
N=1000000

mogipdan=np.random.randn(N)*std+avg

print(a,  np.mean(mogipdan))
print(b,  np.var(mogipdan))
print(c,  np.std(mogipdan))

■ -113모평균이 30이고 모 표준편차가 7인 모집단 (1000000개)에서 표본을 49개를 뽑으시오! 

import numpy as np

avg=30
std=7
N=1000000

mogipdan=np.random.randn(N)*std+avg
print(np.random.choice(mogipdan,49))

■ Q-114 위에서 뽑은 49개의 평균값을 출력하시오 !


import numpy as np

avg=30
std=7
N=1000000

mogipdan=np.random.randn(N)*std+avg

print(np.random.choice( mogipdan,49).mean())

■ Q-115 위에서 출력한 표본의 평균값 하나가  아니라 100개가 출력되게 하시오! 

import numpy as np

avg=30
std=7
N=1000000
mogipdan=np.random.randn(N)*std+avg
for i in range(1,101):
    print(np.random.choice( mogipdan,49).mean())

■ Q-116 그리고 그것을 a 리스트에 담으세요 

avg=30
std=7
N=1000000
a=[]
mogipdan=np.random.randn(N)*std+avg
for i in range(1,101):
    d=(np.random.choice( mogipdan,49).mean())
    a.append(d)
print(a)   

■ Q-117 위에서 구한 표본평균의 평균값과 표준편차를 아래와 같이 출력하시오!

"표본평균" 의 평균값은?
"표본평균" 의 표준편차는?

avg=30
std=7
N=1000000
a=[]
mogipdan=np.random.randn(N)*std+avg
for i in range(1,101):
    d=(np.random.choice( mogipdan,49).mean())
    a.append(d)

print( """ "표본평균" 의 평균값은 """  , np.mean(a)  ,'입니다')
print( """ "표본평균" 의 표준편차는 """  ,np.std(a)  ,'입니다'  )


txt1='자바'
txt2='파이썬'
print( '나는 %s 보다 %s 가 더 익숙합니다' %(txt1,txt2) )


■ Q- 118.아래의 변수를 이용해서 아래와 같이 출력되게 하시오! 
5는 10보다 작습니다. 

num1 = 5 
num2 = 10
print( '숫자 %d 는  %d 보다 작습니다.'   %(num1,num2)  )


■ Q-119 문제 117번의 결과가 아래와 같이 출력되게 하시오! 
(문자열 포맷을 이용하세요) 
표본평균의 평균값은 29.967904..이고 분산값은 29.96790
표준편차는 1.0058238308 입니다. 

avg=30
std=7
N=1000000
a=[]
mogipdan=np.random.randn(N)*std+avg
for i in range(1,101):
    d=(np.random.choice( mogipdan,49).mean())
    a.append(d)

print( '표준평균의 평균값은 %f 이고 분산값은 %f 이고 표준편차값은 %f 입니다.'
 %(np.mean(a),  np.var(a),np.std(a) ) )

■ Q-120 위의 결과가 아래와 같이 소수점 두번째 자리까지만 나오게 하시오! 

avg=30
std=7
N=1000000
a=[]
mogipdan=np.random.randn(N)*std+avg
for i in range(1,101):
    d=(np.random.choice( mogipdan,49).mean())
    a.append(d)

print( '표준평균의 평균값은 %.2f 이고 분산값은 %.2f 이고 표준편차값은 %.2f 입니다.'
 %(np.mean(a),  np.var(a),np.std(a) ) )

 %.2f : Use this 


■ Q-121 어느 비행기 탑승객의 짐의 무게는 평균이 18kg 이고 표준편차가 3kg 인 정규분포를 따른다고 한다
        이 비행기 탑승객 중에서 36명을 임의추출할때,짐의 무게가 17kg이상일확률을 구하여라
        (단,z 가 표준정규분포를 따르는 확률변수일때, p(0<= Z<=2) =0.4772  

import numpy as np
import random

avg=18
std=3
N=10000000
cnt=0
population=np.random.randn(N)* std+avg 
for i in range (1,1001):
    result=np.random.choice(population,36).mean()
    if result > 17:
        cnt+=1
print(cnt/1000)
