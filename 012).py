# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 23:19:22 2020

@author: goboy
"""


===========================================
===========================================



■ Q-319. 아래의 a 리스트의 요소 화성 다음에 소행성을 요소로 입력하시오!

a = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성' ]

a.insert( a.index('화성') + 1, '소행성')

print(a)

■ Q-320.  아래의 a 리스트에서 목성을 지우시오 !

a = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성' ]

del(a[ a.index('목성') ] )
print(a)

■ Q-321.  아래의 빨간공 2개와 파란공 3개가 들어있는 주머니에서
공을 하나 랜덤으로 빼면 그 공이 주머니에서 지워지게 하시오  !

box = [ 'red', 'blue', 'red', 'blue', 'blue' ]  

import  random

result = random.choice(box)
if  result =='red':
    box.remove('red')
else:
    box.remove('blue')
print(box)

box = ['red', 'blue', 'red', 'blue', 'blue']

import random
a = random.choice(box)
box.remove(a)
print(box)

■ Q-322.  아래의  주머니에서 임의로 하나의 공을 뽑았을 때  
그 공이 파란색일 확률은 어떻게 되는가 ?  ( 복원 추출)
공을 뽑은 작업을 10000 번 수행하시오 !

box = ['red', 'blue', 'red', 'blue', 'blue']

import   randomcnt = 0
for  i  in  range(1, 10001):
    result = random.choice(box) # 실행문1
    if  result == 'blue':      # 실행문2
        cnt = cnt + 1

print ( cnt /10000)  # 0.5936

■ Q-323.   파란공 70개와 빨간공 30개가 들어있는 주머니를 만드시오 

a = ['blue'] * 70
b = ['red']  * 30
box = a + b
print (box)

■ Q-324. 위의 box 에 들어있는 요소가 몇개인지 확인하시오 !

a = ['blue'] * 70
b = ['red']  * 30
box = a + b
print (box)
print( len(box) )  # 100

■ Q-325.  위의 box 에 있는 요소들을 무작위로 섞으시오 !

from  random  import  shuffle  # from 패키지 import 모듈 

a = ['blue'] * 70
b = ['red']  * 30
box = a + b
print (box)
shuffle(box)  # box 안의 요소들을 무작위로 섞는다. 
print(box)

■ Q-326.  위의 box 에서  공 3개를 추출했을때  그 공 3개가 다 파란색일
확률은 어떻게 되는가 ?  ( 공을 뽑은 작업을 10000 번 수행하세요)
복원 추출하세요 ~

from  random  import  shuffle  # from 패키지 import 모듈 
import  random 

a = ['blue'] * 70
b = ['red']  * 30
box = a + b
shuffle(box)                       # box 안의 요소들을 무작위로 섞는다. 
cnt = 0
for  i   in  range(1, 10001):
    result = random.sample( box, 3 )   # box 에서 공을 3개씩 추출한다. 
    if  result.count('blue') == 3:              # result 리스트의 요소가 blue 인 갯수 3개이면
        cnt = cnt + 1                              # cnt 의 값을 누적시켜라 ~
print( cnt /10000 )                         # 0.327
    
■ Q-327. 이번에는 위의 box 에서 공을 3개를 뽑았을때 그중 2개가 
blue 일 확률을 출력하시오 !( 비복원 추출, 공을 뽑는 작업을 10000번
수행하세요 ~)

from  random  import  shuffle  # from 패키지 import 모듈 
import  random 

a = ['blue'] * 70
b = ['red']  * 30
box = a + b
shuffle(box)  # box 안의 요소들을 무작위로 섞는다. 
cnt = 0
for  i   in  range(1, 10001):
    result = random.sample( box, 3 ) # box 에서 공을 3개씩 추출한다. 
    if  result.count('blue') == 2:  # result 리스트의 요소가 blue 인 갯수 2개이면
        cnt = cnt + 1  # cnt 의 값을 누적시켜라 ~
print( cnt /10000 )  # 0.4577

설명:  ranom 패키지의 sample 함수는 비복원 추출 입니다. 

■ Q-328.  위의 문제를 복원추출로 수행하시오 

# 넘파이의 랜덤 초이스는 복원 추출합니다.
import numpy as np
box = []
a = ['blue']*70
b = ['red']*30
box = a+b                  

cnt = 0
cnts = 0
for i in range(1,10001):
    result = list(np.random.choice(box,3,replace=True)) # replace =True 면 복원 
    cnts += 1
    if result.count('blue')==2:
        cnt += 1
print(cnt/cnts)

■ Q-329.  세원이가 올린 코드를 참조해서 아래의 문제를 해결하시오!
         
 6개의 제품이 들어있는 상자가 있는데 그 중에 2개가 불량품이라고
 했을때 제품 검사를 위해 3개를 추출했을때 1개가 불량품일 확률을 
 출력하시오 ! ( 복원 추출로 하세요 ~)

box = ['정상', '불량품', '정상', '정상', '불량품', '정상' ]

import numpy as np
box = ['정상', '불량품', '정상', '정상', '불량품', '정상' ]

cnt = 0
cnts = 0
for i in range(1,10001):
    result = list(np.random.choice(box,3,replace=True)) # replace =True 면 복원 
    cnts += 1
    if result.count('불량품')==1:
        cnt += 1
print(cnt/cnts)  # 0.446


■ Q-330. 위의 a 리스트의 요소를 다 지우시오 !

a=['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '혜왕성']
del( a[:] )
print(a)   # [] 

■ Q-331. (점심 시간 문제)  초등학생 10만명의 체중 데이터를 가지고 
 히스토그램 그래프를 그리시오 ~~
      
   ( 초등학생 10만명의 평균 체중은 45kg 이고 표준편차는 5 입니다.)

 30kg ~  60kg 까지  간격 2kg 으로 x 축의 간격(계급) 을 정하세요 ~
 30  ~ 32
 32  ~ 34              코드와 그래프를 같이 올리세요 ~~
     :                    (한결이가 사용했던 xtick 을 이용해서 그리세요 ~)
 58 ~  60

import numpy as np
import matplotlib.pyplot as plt
weight = np.random.randn(100000)*5+45
bins = list(range(30,61,2))
plt.xticks(bins)
plt.hist(weight,bins,rwidth = 0.8, alpha = 0.7, color = 'blueviolet')

■ Q-332. 점심시간에 만들었던 초등학생 10만명의 체중 데이터를 모수로 
보고 10만명의 체중 데이터에서 100명을 샘플링하여 평균을 
 구하시오 !

import numpy as np
N = 1000000
std = 5
avg = 45
population_weight = np.random.randn(N) * std + avg
result  = np.random.choice(population_weight, 100, replace=True).mean()
print (result)

■ Q-333. 위의 모집단에서 표본 100명을 추출하여 표본평균을 구하는 
작업을 1000번 수행해서 1000개의 표본평균을 a 라는 비어있는
리스트에 넣으시오 !

import numpy as np
N = 1000000
std = 5
avg = 45
population_weight = np.random.randn(N) * std + avg
a = []
for  i  in  range(1, 1001):
    result  = np.random.choice(population_weight, 100, replace=True).mean()
    a.append(result)
print(a)

■ Q-334.  위의 a 리스트의 요소의 갯수를 출력하시오 

import numpy as np
N = 1000000
std = 5
avg = 45
population_weight = np.random.randn(N) * std + avg
a = []
for  i  in  range(1, 1001):
    result  = np.random.choice(population_weight, 100, replace=True).mean()
    a.append(result)
print(len(a))

■ Q-335. 위의 표본평균 1000개를 가지고 히스토그램 그래프를 그리시오

 x 축 계급의 범위 : 30 ~ 60 (간격 2)  
import matplotlib.pyplot as plt
import numpy as np
N = 1000000
std = 5
avg = 45
population_weight = np.random.randn(N) * std + avg
a = []
for  i  in  range(1, 1001):
    result  = np.random.choice(population_weight, 100, replace=True).mean()
    a.append(result)
bins = list(range(40,51,1))
plt.xticks(bins) #x축 tick
plt.grid()
plt.hist( a, bins, rwidth = 0.9, color = 'black')
plt.xlabel('kg') #x축 label
plt.ylabel('cnt') #y축 label


■ Q-336. 우리반 데이터의 나이를 비어있는 리스트 a 에 입력하고 나서
우리반 나이 데이터중에서 27 살이 몇명있는지 출력하시오 !
 ( 판다스 사용하지 말고  emp1222.csv 를  로드해서 하세요)

import  csv
file = open("c:\\data\\emp1222.csv", encoding="CP949")
emp_csv = csv.reader(file)
a = [ ]
for  emp_list  in  emp_csv:
    a.append( int(emp_list[2] ) )

print (a.count(27) )  # 5

■ Q-337. 파이썬에서 정의된 모든 변수들을 확인하시오 !

a = [ 1, 2, 3, 4, 5 ]
b = 'scott'
c = 30

print( dir() )

■ Q-338.  emp2.csv 에서 월급을 비어있는 리스트인 a 에 담고 
월급을 역순으로 정렬해서 리스트의 요소로 구성하시오 !

import   csv
file = open("c:\\data\\emp2.csv")
emp_csv=csv.reader(file)                       45분까지 쉬세요 ~~
a = [ ] 
for  emp_list  in  emp_csv:
    a.append( int(emp_list[5] ) )
a.sort(reverse=True)
print(a)


■ Q-339.  아래의 artist 라는 리스트에 가수이름들을 추가하고 
music 리스트에 음악 리스트를 추가하시오 !

artist = ['비틀즈', '비틀즈', '아이유', '아이유' ,'마이클 잭슨', '마이클 잭슨']
music =['yesterday', 'imagine', '너랑나', '마슈멜로우', 'beat it', 'smooth criminal']

■ Q-340.  아래에 artist 를 키 로 하고  music 을 값으로 해서 아래와 같은 딕셔너리를 구성하시오!

 artist = ['비틀즈',, '아이유',  ,'마이클 잭슨']
 music = [ 'yesterday',  '너랑나',  'beat it' ]

gini =  { '비틀즈' : 'yesterday' , '아이유' : '너랑나',  '마이클잭슨': 'beat it' }

답:  
gini = {}  #  비어있는 딕셔너리를 gini 라는 이름으로 생성한다. 
gini['비틀즈'] = 'yesterday'
gini['아이유'] ='너랑나'
gini['마이클 잭슨'] = 'beat it' 
print(gini) # {'비틀즈': 'yesterday', '아이유': '너랑나', '마이클 잭슨': 'beat it'}

■ Q-341. 위와 같이 일일이 손으로 노가다 하지 말고 아래의 2개의 리스트를
이용해서 for 문과 zip 을 이용해서 한번에 gini 딕셔너리를 구성하시오

artist = ['비틀즈', '아이유',  ,'마이클 잭슨']
music = [ 'yesterday',  '너랑나',  'beat it' ]

print(gini)

{'비틀즈': 'yesterday', '아이유': '너랑나', '마이클 잭슨': 'beat it'}

artist = ['비틀즈', '아이유', '마이클 잭슨']
music = [ 'yesterday',  '너랑나',  'beat it' ]
gini = {}  # 비어있는 딕셔너리 gini 를 만든다.ㅏ 
for  i,  k  in  zip( artist, music):
    gini[ i ] = k
print (gini)


■ Q-342. 아래의 music 리스트에서 요소를 하나씩 빼내는데 앞에 인덱스 번호도 같이
출력되게하시오 !

artist = ['비틀즈', '비틀즈', '아이유', '아이유' ,'마이클 잭슨', '마이클 잭슨']
music =['yesterday', 'imagine', '너랑나', '마슈멜로우', 'beat it', 'smooth criminal']

for   i,  k  in  enumerate(music):
    print(i, k)

■ Q-343.  aritist 리스트를 가지고 아래와 같이 결과를 출력하시오 !
artist = ['비틀즈', '비틀즈', '아이유', '아이유' ,'마이클 잭슨', '마이클 잭슨']
music =['yesterday', 'imagine', '너랑나', '마슈멜로우', 'beat it', 'smooth criminal']

artist = ['비틀즈', '비틀즈', '아이유', '아이유' ,'마이클 잭슨', '마이클 잭슨']
for   i,  k   in   enumerate( artist ):
    print ( k,  i )

■ Q-344. 아래의 두개의 리스트를 가지고 아래와 같이 결과를 출력하시오 ! 

artist = ['비틀즈', '비틀즈', '아이유', '아이유' ,'마이클 잭슨', '마이클 잭슨']
music =['yesterday', 'imagine', '너랑나', '마슈멜로우', 'beat it', 'smooth criminal']

결과:
비틀즈            yesterday  --> music[0]
비틀즈            imagine    --> music[1]
아이유            너랑나      --> music[2]
아이유            마슈멜로우 --> music[3]
마이클 잭슨      beat it     --> music[4]
마이클 잭슨      smooth criminal --> music[5]

artist = ['비틀즈', '비틀즈', '아이유', '아이유' ,'마이클 잭슨', '마이클 잭슨']
music =['yesterday', 'imagine', '너랑나', '마슈멜로우', 'beat it', 'smooth criminal']
for   i,  k   in   enumerate( artist ):
    print ( k, music[i] )


from  collections  import  defaultdict 
gini = defaultdict(list)
gini['비틀즈'].append('yesterday')
print(gini)
gini['비틀즈'].append('imagine')
print(gini)

defaultdict(<class 'list'>, {'비틀즈': ['yesterday', 'imagine']})

■ Q-345. 그럼 위에서 만든 default 딕셔너리에 아이유를 키로 하고 너랑나, 마슈멜로우를
값으로 해서 추가하시오 ! 

 {'비틀즈': ['yesterday', 'imagine'] ,'아이유' : ['너랑나','마슈멜로우'] }

from  collections  import  defaultdict 
gini = defaultdict(list)
gini['비틀즈'].append('yesterday')
gini['비틀즈'].append('imagine')
gini['아이유'].append('너랑나')
gini['아이유'].append('마슈멜로우')
gini['마이클잭슨'].append('beat it')
gini['마이클잭슨'].append('smooth criminal') 
print(gini)

■ Q-346. 위와 같이 일일이 손으로 노가다 하지 말고 enumerate 를 이용해서 
gini 딕셔너리를 구성하시오 !

artist = ['비틀즈', '비틀즈', '아이유', '아이유' ,'마이클 잭슨', '마이클 잭슨']
music =['yesterday', 'imagine', '너랑나', '마슈멜로우', 'beat it', 'smooth criminal']

from  collections  import  defaultdict gini=defaultdict(list)
for   i,  k   in   enumerate( artist ):
    gini[ k ].append( music[i] ) 

print(gini)

■ Q-347. (346연결)  위의 gini  딕셔너리에서  음악만 추출하시오 ( 딕셔너리의 값만 추출 )
 딕셔너리에서 키값을 추출할 때는 :  딕셔너리이름.keys()
 딕셔너리에서 값만 추출할 때는   :   딕셔너리이름.values() 

for  i  in   gini.values():
    print(i)

['yesterday', 'imagine']
['너랑나', '마슈멜로우']
['beat it', 'smooth criminal']

for  i  in   gini.values():
    for  k  in  i:  #                      ['yesterday', 'imagine'], ['너랑나', '마슈멜로우']
        print(k)

■ Q-348.  위의 코드 음악들을 비어있는 리스트인 a 에 담으시오 ! 

[ 'yesterday', 'imagine', '너랑나', '마슈멜로우', 'beat it', 'smooth criminal' ]

답:                                         40분까지 쉬세요 ~~~ 
a = []
for  i  in   gini.values():
    for  k  in  i:  #  ['yesterday', 'imagine'], ['너랑나', '마슈멜로우']
        a.append(k)
print(a)

■ Q-349.  아래의 코드를 수행해서 gini.values() 의 요소들을 프린트 해보시오 !
artist = ['비틀즈', '비틀즈', '아이유', '아이유' ,'마이클 잭슨', '마이클 잭슨']
music =['yesterday', 'imagine', '너랑나', '마슈멜로우', 'beat it', 'smooth criminal']

from  collections  import  defaultdict 
gini=defaultdict(list)
for   i,  k   in   enumerate( artist ):
    gini[ k ].append( music[i] ) 
for   j  in   gini.values():
    print(j[0]) 

['yesterday', 'imagine']
['너랑나', '마슈멜로우']
['beat it', 'smooth criminal']

■ Q-350. (오늘의 마지막 문제)
            아래와 같이 결과를 출력하시오 !  바로 옆에 다른 아티스트의
            노래가 나와줘야 합니다. 

yesterday, 너랑나, beat it, imagine, 마슈멜로우, smooth criminal


from collections import defaultdict
gini = defaultdict(list)
music = ['yesterday','imagine','너랑나','마시멜로우','beat it','smooth criminal']
artist = ['비틀즈','비틀즈','아이유','아이유','마이클잭슨','마이클잭슨']
b=[]
c=[]
bond=','
for i, k in enumerate(artist):
    gini[k].append(music[i])
for j in gini.values():
        b.append(j[0])
        c.append(j[1])
result = bond.join(b+c)
print(result)
