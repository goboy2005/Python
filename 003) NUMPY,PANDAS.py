# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 20:36:54 2020

@author: goboy
"""

Day 3 Problems 

■ Q-53.주사위 1개를 10번 던지시오 ! 

import random
dice=[1,2,3,4,5,6]
for i in range(1,11):
    print(random.choice(dice))  

■ Q-54 주사위를 10번던져서 주사위의 눈이 3이 나오는 횟수를 출력하시오!

import random
dice=[1,2,3,4,5,6]
cnt=0
for i in range(1,11):
    result=random.choice(dice)
    if result == 3:
        cnt=cnt+1
print(cnt)

■ Q-55 주사위를 10번던져서 주사위의 눈이 짝수가 나오는 횟수를 
출력하시오!

import random
dice=[1,2,3,4,5,6]
cnt=0
for i in range(1,11):
    result=random.choice(dice)
    if result %2==0:
        cnt += 1
print(cnt)


■ Q-56 주사위를 2개를 동시에 던져 두개의 눈의 합이 10이 되는 횟수를 출력하시오!
(주사위 2개를 20번 던지세요!) 

import random

dice=[1,2,3,4,5,6]
cnt=0
for i in range(1,21):
    result1=random.choice(dice)
    result2=random.choice(dice)
    if result1+result2==10:
        cnt += 1
print(cnt)

■ Q-57 주사위 2개를 던져서 두눈의 합이 10이 되는 확률을 출력하시오! 

import random

dice=[1,2,3,4,5,6]
cnt=0
for i in range(1,101):
    result=random.choice(dice)
    result2=random.choice(dice)
        if result+result2 == 10:
            cnt=cnt+1
print(cnt/100)  

■ Q-58.  아래의 수학식을 파이썬으로 구현하시오 !

import  math 

print( 2 * math.log2(10) + (1/3) * math.log2(10)  )


■ Q-59.  주사위를 10 번 던져서 주사위의 눈이 3이 나오는 횟수를 
출력하시오 ! ( 축약 연산자를 이용해서 출력하시오 ! )

import  random

dice = [ 1, 2, 3, 4, 5, 6 ]
cnt = 0
for  i  in   range(1, 11):
    result = random.choice(dice)
    if  result == 3:
        cnt += 1  # 축약을 사용할 수 도 있습니다. 
print (cnt)


■ Q-60.  주사위를 20번 던져서 주사위의 눈이 4이상 나오는 횟수를 출력
 하시오 !

import  random

dice1 = [ 1, 2, 3, 4, 5, 6 ]
cnt = 0
for  i  in  range(1, 21):
    result = random.choice(dice1)
    if  result >= 4:
        cnt = cnt + 1 
print (cnt)

■ Q-61. (통계 정규분포 문제) 주사위 한개를 288회 던져서 주사위의 눈이 
 5이상 나오는 횟수를 출력하시오 !

import  random

dice1 = [ 1, 2, 3, 4, 5, 6 ]
cnt = 0
for  i  in  range(1, 289):
    result = random.choice(dice1)
    if  result >= 5:
        cnt = cnt + 1 
print (cnt)

■ Q-62. (통계 정규분포 문제) 주사위 한개를 288회 던져서 주사위의 눈이 
 5이상 나오는 확률을 출력하시오 !

import  random

dice1 = [ 1, 2, 3, 4, 5, 6 ]
cnt = 0
for  i  in  range(1, 289):
    result = random.choice(dice1)
    if  result >= 5:
        cnt = cnt + 1 

print (cnt/288)

■ Q-63. 주사위 한개를 288회 던질때 5이상의 눈이 나올 횟수를 출력하는데
이 작업을 100 번해서 횟수 100개 출력되게하시오 !
 
import  random

dice1 = [ 1, 2, 3, 4, 5, 6 ]
for  j  in  range(1, 101):
    cnt = 0
    for  i  in  range(1, 289):
        result = random.choice(dice1)
        if  result >= 5:
            cnt = cnt + 1 
    print (cnt)

■ Q-64. ( 점심시간 문제) 위에서 출력된 횟수 100개를 비어있는 리스트
           a 리스트에 담고 a 리스트의 갯수를 출력하시오 ! 

for j in range(1,101) 
    cnt = 0   
    for i in range(1,289):     
        result = random.choice(d)
        if result >= 5:
            cnt = cnt + 1
     a.append(cnt)      

print(a)

■ Q-65.동전을 100번 던져서 앞면이 나오는 횟수를 출력하시오

coin=['앞면','뒷면']
cnt=0
for i in range(1,101):
    result=random.choice(coin)
    if result=='앞면':
        cnt += 1
print(cnt)

■ Q-66 동전 한개와 주사위 한개를 동시에 100번 던져서 동전이 앞면이 나오고 주사위의 눈이 5가 나오는 횟수를 출력하시오

import random
coin=['앞면','뒷면']
dice=[1,2,3,4,5,6]
cnt=0
for i in range(1,101):
    result1 = random.choice(coin)
    result2 = random.choice(dice)
    if result1 == '앞면' and result2 == 5:
        cnt += 1 
print(cnt)

■ Q-67 동전한개와 주사위 한개를 동시에 100번 던져서
동전이 앞면이 나오고 주사위의 눈이 5가 나오는 횟수를 출력하는
행위를 50번 해서 횟수가 50개가 출력되게 하시오

import random
coin=['앞면','뒷면']
dice=[1,2,3,4,5,6]
for j in range(1,51):
    cnt=0
    for i in range(1,101):
        result1=random.choice(coin)
        result2=random.choice(dice)
        if result1 == '앞면' and result2== 5:
            cnt = cnt+ 1 
    print(cnt)

■ Q- 68. 위의 횟수 50개를 비어 있는 리스트 a 리스트에 담으시오 !

import  random
coin = ['앞면', '뒷면']
dice = [ 1, 2, 3, 4, 5, 6 ]
a = []
for  j  in  range(1, 51):
    cnt = 0
    for  i  in  range(1, 101):
        result1 = random.choice(coin)
        result2 = random.choice(dice)
        if  result1 == '앞면'  and result2==5 :
            cnt = cnt + 1
    
    a.append(cnt)

print(a)

■ Q-69 담겨진 a리스트의 요소들의 갯수를 확인하시오!

import random
coin=['앞면','뒷면']
dice=[1,2,3,4,5,6]
a=[]
for j in range(1,51):
    cnt=0
    if i in range(1,101):
        result1=random.choice(dice)
        result2=random.choice(coin)
        if result1==5 and result2 =='앞면':
            cnt=cnt+1
   
        a.append(cnt)
print(len(a))

■ Q-70.1 위의 a 리스트의 요소들의 평균값을 출력하시오 
(numpy를 이용해서 구현하시오 b=[7,4,2,3,4]

import numpy as np
b=[1,2,3,3,3]
print(np.mean(b))

■ Q-70.2 아래의 리스트의 요소들의 평균집합을 출력하시오! (numpy 사용 x)
b=[1,2,4,3,4,3,2,3,4,5,4,3]

b=[1,3,3,4,4,5,2,2,2,2,3,2,1000]
cnt=0
for i in b:
    cnt=cnt+i
print(cnt/len(b))

■ Q-70.3 69 번 문제를 numpy 를 사용해서 평균을 구하시오! 

import numpy as np

import random
coin=['앞면','뒷면']
dice=[1,2,3,4,5,6]
a=[]
for j in range(1,51):
    cnt=0
    if i in range(1,101):
        result1=random.choice(dice)
        result2=random.choice(coin)
        if result1==5 and result2 =='앞면':
            cnt=cnt+1
   
        a.append(cnt)
print(len(a))

print(np.mean(a))

■ Q-71 64 번 코드를 가져와서 a 리스트의 요소들과 평균과 분산과 표준편차를   
 출력하시오 ( 주사위를 288번 던져서 주사위의 눈이 5이상 나오는 횟수를 
 구하는 작업을 100번이상해서 a 리스트에 담은것이 64 )

import random
import numpy as np

dice=[1,2,3,4,5,6]
a=[]
for j in range(1,101):
    cnt=0
    for i in range(1,289):
        result=random.choice(dice)
        if result>=5:
            cnt=cnt+1
        a.append(cnt)
print(np.mean(a))

■ Q-72 위의 a 리스트의  요소들을 하나씩 빼내서 나열 출력하시오 

import random
import numpy as np

dice=[1,2,3,4,5,6]
a=[]
for j in range(1,101):
    cnt=0
    for i in range(1,289):
        result=random.choice(dice)
        if result>=5:
            cnt=cnt+1
        a.append(cnt)

for k in a:
    print(k)

■ Q-74 그러면 a 리스트의 요소들의 숫자가 90 이상이고 106 이하일 갯수를 
출력하시오 ! 

import random
dice = [1,2,3,4,5,6]
a=[]
for j in range(1,101):
    cnt = 0
    for i in range(1,289):
            result = random.choice(dice)
            if result >= 5:
                cnt += 1
    a.append(cnt)


cnt1=0
for k in a :
    if k >=90 and k<=106:
        cnt1=cnt1+1
print(cnt1) 

■ Q-75 그러면 a 리스트의 요소들의 숫자가 90이상이고 106이하인 요소들의 확률을 출력
하시오! 

import random
dice = [1,2,3,4,5,6]
a=[]
for j in range(1,101):
    cnt = 0
    for i in range(1,289):
        result = random.choice(dice)
        if result >= 5:
            cnt += 1
    a.append(cnt)
cnt1 = 0
for k in a:
    if k >= 90 and k <= 106:
        cnt1 = cnt1 +1
print(cnt1/100)

■ Q-76 (SQL ----→ 판다스 문법) 사원테이블 에서 이름과 월급을 출력하시오

SQL
select ename,sal
from emp;

pandas 
import pandas as pd
emp = pd.read_csv("c://data//emp3.csv")
print(emp [ ['ename','sal'] ] ) 


■ Q-77 (아래의 SQL을 판다스로 구현하시오)
select ename,sal,job,hiredate
from emp;

import pandas as pd
emp = pd.read_csv("c://data//emp3.csv")
print( emp [ ['ename','sal','job','hiredate']])



■ Q-78.아래의 SQL 을 판다스로 구현하시오
select ename,sal
from emp
where job='SALESMAN';

import pandas as pd
emp = pd.read_csv("c://data//emp3.csv")
print( emp [ ['ename','sal']]          [emp['job']=='SALESMAN'] )
                                          
 
■ Q-79월급이 3000 이상인 사원들의 이름과 월급을 출력하시오

import pandas as pd
emp=pd.read_csv("c://data//emp3.csv")
print ( emp [ ['ename','sal',]]  [emp['sal'] >= 3000 ]  )


■ Q-80 아래의 SQL을 판다스로 구현하시오
select ename,sal
from emp
where sal between 1000 and 3000;

import pandas as pd
emp=pd.read_csv("c://data//emp3.csv")
print(emp [['ename','sal']] [emp ['sal'].between(1000,3000) ] ) 


■ Q-81.월급이 1000에서 3000사이가 아닌 사원들의 이름과 월급을 출력하시오! 
(not 이 판다스에서는 ~입니다.) 

import pandas as pd
emp=pd.read_csv("c://data//emp3.csv")
print(emp [['ename','sal']] [ ~ emp ['sal']. between(1000,3000) ] ) 

■ Q-82 직업이 CLERK,SALESMAN인 사원들의 이름과 직업을 출력하시오! 

SQL  
select ename,job
from emp
where job in ('CLERK','SALESMAN')

Pandas
import pandas as pd 
emp=pd.read_csv("c://data//emp3.csv" ) 
print( emp [['ename','job']]   [ emp ['job'].isin (['SALESMAN','CLERK']) ] )

■ Q-83 이번에는 직업이 CLERK, SALESMAN이 아닌 사원들의 이름과 직업을 출력해라

import pandas as pd 
emp=pd.read_csv("c://data//emp3.csv" ) 
print( emp [['ename','job']]   [~ emp ['job'].isin (['SALESMAN','CLERK']) ] )

■ Q-84 커미션이 null 인사원들의 이름과 커미션을 출력하시오
select ename,comm
from emp
where comm is null;

Pandas 
import pandas as pd
emp=pd.read_csv("c://data//emp3.csv")
print(emp [['ename','comm']] [ emp ['comm'].isnull()] )

■ Q-85 커미션이 Null 이 아닌 사원들의 이름과 커미션을 출력하시오!
import pandas as pd
emp=pd.read_csv("c://data//emp3.csv")
print(emp [['ename','comm']] [ ~emp ['comm'].isnull()] )


■ Q-86. 6개의 제품이 들어있는 상자가 있는데 그중에 2개가  불량품이라고 하자
제품검사를 위해서 3개를 추출했을때 적어도 한개가 불량품일 확률은?
 
import random

a=['정상','정상','정상','정상','불량','불량']
cnt=0
for i in range(1,1001):
    result1=random.choice(a)
    result2=random.choice(a)
    result3=random.choice(a)
    if result1=='정상' and result2=='정상' and result2=='정상' :
        cnt=cnt+1
print(1- (cnt/1000))


