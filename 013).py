# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 02:25:35 2020

@author: goboy
"""



■ Q-351. 아래의 리스트의 짝수 번째 요소의 합을 출력하시오

listdata = [ 2, 2, 1, 3, 8, 4, 3, 9, 2, 20 ]

result = listdata[1: : 2]
print(sum(result))

■ Q-352. (알고리즘 문제) 아래의 리스트에 1부터 10까지의 숫자중에
없는 숫자가 하나있다 그 없는 숫자는 무엇인가 ?

a = [ 2, 1, 5, 4, 6, 7, 9, 10, 3 ] 

result = sum(range(1, 11) ) - sum(a)
print (result)

■ Q-353.  While loop 문을 이용해서 무한루프문을 수행하시오 !

while  True:
    print('aaaaaaaaaaaaaaaaa') 

■ Q-354.  이번에는 위의 True 대신에 숫자 1 을 넣고 무한 루프문을
   수행하시오 !

while  1:
    print( 'aaaaaaaaaaaaaaaa')

■ Q-355. 아래의 2개의 리스트를 가지고 sol 딕셔너리를 생성하시오 !
(for 루프문과 zip 을 이용하세요 ~ ) 
sol_eng = ['sun', 'mercury', 'venus', 'earth', 'mars' ]
sol_kor  =['태양', '수성', '금성', '지구', '화성']

결과 :  
print(sol)
{'태양': 'sun', '수성': 'mercury', '금성': 'venus', '지구':' 'earth', '화성':'mars'}

sol_eng = ['sun', 'mercury', 'venus', 'earth', 'mars' ]
sol_kor  =['태양', '수성', '금성', '지구', '화성']
sol = {}                                                
for  i,  k   in  zip( sol_kor, sol_eng ):
    sol[i] = k
print (sol)

■ Q-356. 아래의  딕셔너리의 값중에 Fire 를 피땀눈물로 변경하시오 !

dict = { '방탄소년단':'Fire', '소녀시대':'Gee' }
print(dict)
dict['방탄소년단']='피땀눈물'
print(dict)

■ Q-357. 아래의 딕셔너리의 값중에서 Fire 를 피땀눈물로 변경하시오 

dict = {'소녀시대' : ['다시만난세계','Gee'], '방탄소년단' : ['DNA', 'Fire'] }

print(dict['방탄소년단'])  # ['DNA', 'Fire']

dict['방탄소년단'][1] ='피땀눈물'
print(dict)

■ Q-358. 아래의 딕셔너리에서 다시만난세계의 값만 지우시오 !

dict = {'소녀시대' : ['다시만난세계','Gee'], '방탄소년단' : ['DNA', 'Fire'] }

del  dict['소녀시대'][0]
print(dict) 


■ Q-359. 위와 같이 딕셔너리의 요소를 지우는게 아니라 딕셔너리 자체를
메모리에서 지우려면 어떻게 해야하는가 ?

dict = {'소녀시대' : ['다시만난세계','Gee'], '방탄소년단' : ['DNA', 'Fire'] }
del  dict
print (dict) # <class 'dict'>  

■ Q-360.  위의 sol 사전에 있는 키를 추출해서 아래와 같이 결과를 출력하시오

sol = {'태양': 'sun', '수성': 'mercury', '금성': 'venus', '지구': 'earth', '화성':'mars'}

결과:  태양, 수성, 금성, 지구, 화성    

sol = {'태양': 'sun', '수성': 'mercury', '금성': 'venus', '지구': 'earth', '화성':'mars'}
for  i  in  sol.keys():
    print ( i, end=',')

■ Q-361.  위의 결과에서 맨끝에 있는 콤마(,) 는 출력되지 않게 하시오 

결과:  태양,수성,금성,지구,화성

sol = {'태양': 'sun', '수성': 'mercury', '금성': 'venus', '지구': 'earth', '화성':'mars'}
for  i  in  sol.keys():
    print ( i, end=',')

■ Q-362. 아래의 sol 딕셔너리에서 값들만 아래와 같이 출력하시오 

sol = {'태양': 'sun', '수성': 'mercury', '금성': 'venus', '지구': 'earth', '화성':'mars'}

결과:  sun,mercury,venus,earth,mars,

sol = {'태양': 'sun', '수성': 'mercury', '금성': 'venus', '지구': 'earth', '화성':'mars'}

for  i  in  sol.values():
    print( i, end=',') 

■ Q-363. 아래의 gini 딕셔너리에서 값만 추출하시오 !

gini = {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'], '마이클 잭슨': ['beat it', 'smooth criminal']}

결과:
 ['yesterday', 'imagine']
 ['너랑나', '마슈멜로우']
 ['beat it', 'smooth criminal']

gini = {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'], '마이클 잭슨': ['beat it', 'smooth criminal']}
for  i  in  gini.values():
    print(i)

■ Q-364.  위의 결과를 다시 출력하는데 결과 리스트 3개중에 0번째 요소만 출력하시오!

 ['yesterday', 'imagine']
 ['너랑나', '마슈멜로우']                      
 ['beat it', 'smooth criminal']

결과:  
yesterday
너랑나
beat it'

gini = {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'], '마이클 잭슨': ['beat it', 'smooth criminal']}
for  i  in  gini.values():
    print(i[0])

■ Q-365.  지난주 목요일 마지막 문제의 자신의 답을 가져와서 gini 딕셔러니에서
악만 출력하는데 아티스트별로 노래가 겹치지 않게 출력하시오 !

gini = {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'],
          '마이클 잭슨': ['beat it', 'smooth criminal']}

결과: 
yesterday, 너랑나, beat it, imagine, 마슈멜로우, smooth criminal

import random
gini = {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'], '마이클 잭슨': ['beat it', 'smooth criminal']}

a=[]
for j in gini.values():
    a.append(j[0])

for j in gini.values():
    a.append(j[1])  
print(a) # [ 'yesterday', '너랑나', 'beat it', 'imagine', '마슈멜로우', 'smooth criminal']
bond = ','
result = bond.join(a)
print(result)

■ Q-366.  아래의 gini 딕셔너리의 값들의 리스트를 아래의 결과처럼 리스트에 담으시오 ! 

gini = {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'],
           '마이클 잭슨': ['beat it', 'smooth criminal']}

결과:
[ ['yesterday', 'imagine'],  ['너랑나', '마슈멜로우'],  ['beat it', 'smooth criminal'] ]

답:
gini = {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'],'마이클 잭슨': ['beat it', 'smooth criminal']}
gini2 = list( gini.values() )  # 리스트형으로 변환한다. 
print (gini2)  

[['yesterday', 'imagine'], ['너랑나', '마슈멜로우'], ['beat it', 'smooth criminal']]

■ Q-367. 위에서 출력된 gini2 리스트의 요소들을 shuffle 로 섞어 보시오  !

from  random import  shuffle
gini = {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'],'마이클 잭슨': ['beat it', 'smooth criminal']}
gini2 = list( gini.values() )  # 리스트형으로 변환한다. 
shuffle(gini2)
print (gini2)  

[['yesterday', 'imagine'], ['beat it', 'smooth criminal'], ['너랑나', '마슈멜로우']]
[['너랑나', '마슈멜로우'], ['yesterday', 'imagine'], ['beat it', 'smooth criminal']]

■ Q-368.(점심시간 문제) 
지난시간 만들었던 마지막 문제의 자신의 답과 리스트의 요소를 무작위로 섞는
shuffle 함수를 이용해서 코드를 수행할 때마다 곡이 무작위로 섞여서 출력되게
하시오 !  ( 단 조건은 아티스트별로 노래가 겹치면 안된다. 바로 음악 바로 옆에
다른 아티스트의 노래가 나와야 합니다.)

너랑나, yesterday, beat it, 마슈멜로우,imagine,smooth criminal,
yesterday,beat it, 너랑나, imagine, smooth criminal, 마슈멜로우


■ Q-369.  위의 gini 딕셔너리의 요소들의 items 를 뽑아서 리스트에 담으시오 

gini = {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'],'마이클 잭슨': ['beat it', 'smooth criminal']}

result = list( gini.items() )
print (result)

■ Q-370. 위의 result 에서 음악 첫번째 곡들만 아래와 같이 출력하시오 !

yesterday
너랑나
beat it

gini = {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'],'마이클 잭슨': ['beat it', 'smooth criminal']}

result = list( gini.items() )
for   i   in   result:
    print (i[1][0])

['yesterday', 'imagine']
['너랑나', '마슈멜로우']
['beat it', 'smooth criminal']


■ Q-371.  위의 결과를 reverse 되게 해서 출력하시오 !

 결과:  ['오마이걸', '소녀시대', '방탄 소년단'] 

dict2 = { '소녀시대' : '소원을 말해봐', '방탄 소년단' : 'DNA',  '오마이걸' : '살짝 설랬어'  } 
result = dict2.keys()
print ( sorted( result, reverse=True ) ) 

■ Q-372.  우리반 데이터(emp1222.csv) 에서 이름과 통신사를 출력하시오 !
import  csv
file = open("c:\\data\\emp1222.csv", encoding="CP949")
emp_csv = csv.reader(file)

for  emp_list  in  emp_csv:
    print ( emp_list[1], emp_list[5] )    

* defaultdictionary 를 이용해서 딕셔너리의 값을 리스트로 구성하는 코드

from  collections  import  defaultdict 
gini = defaultdict(list)
gini['kt'].append('허혁')
gini['kt'].append('정다희')
gini['sk'].append('박혜진')
gini['sk'].append('김승순')
print( gini )

defaultdict(<class 'list'>, {'kt': ['허혁', '정다희'], 'sk': ['박혜진', '김승순']})

■ Q-373.  우리반 데이터에서 통신사를 key 로 하고 학생이름을 값으로 해서 
defaultdictionary 를 생성하시오 ! ( default dictionary 이름은 telecom 으로 하세요)

from  collections  import  defaultdict 
telecom = defaultdict(list)

import  csv
file = open("c:\\data\\emp1222.csv", encoding="CP949")
emp_csv = csv.reader(file)

for  emp_list  in  emp_csv:
    telecom[emp_list[5]].append(emp_list[1])

print( telecom )


■ Q-374. 위에서 구성한 telecom  딕셔너리에서 통신사가 kt 인 학생들을 출력하는데
이름을 ㄱ ㄴ ㄷ ㄹ 순으로 정렬해서 출력하시오 !  

from collections import defaultdict
telecom=defaultdict(list)                    

import  csv
file = open("c:\\data\\emp1222.csv", encoding="CP949")
emp_csv = csv.reader(file)

for  emp_list  in  emp_csv:
    telecom[emp_list[5]].append(emp_list[1])

result = telecom['kt']
print ( sorted(result)  )


■ Q-375. 알파벳 대문자를 출력하시오 !

import   string
print ( string.ascii_uppercase )

결과:  ABCDEFGHIJKLMNOPQRSTUVWXYZ

■ Q-376.  위의 코드와 ord() 함수를 이용해서 아래의 결과를 출력하시오 

결과:   A ----------------->  65
         B ------------------> 66
                    :
                    :
         Z ------------------->  90

답:
import   string

for  i  in   string.ascii_uppercase:
    print (  i , ' -----------> ', ord(i)  )


■ Q-377. 아래와 같이 결과를 출력하시오 !

결과:

65 -----------> A
66 -----------> B
        :
        :
90 -----------> Z

답:
for  i   in  range(65, 91):
    print (i, '------------->', chr(i)  )


■ Q-378.  아래의 결과를 출력하시오 !

 34 + 256 - 71 * 34  =  -2124

답:
a = ' 34 + 256 - 71 * 34'
print ( a, ' = ', eval(a)  )

■ Q-379. 아래의 리스트의 숫자를 뽑아내서 아래의 문자열을 생성하시오

  a = [ 34, 22, 45, 27, 31, 33, 55 ]

결과:  34 + 22 + 45 + 27 + 31 + 33 + 55

a = [ 34, 22, 45, 27, 31, 33, 55 ]
bond='+'
result = bond.join(a)
print(result) 

TypeError: sequence item 0: expected str instance, int f

a = [34,22,45,27,31,33,55]
b = []
for i in a:
    b.append(str(i))  # 문자로 변경해서 b 리스트에 추가한다. 
print(b)  # ['34', '22', '45', '27', '31', '33', '55']
bond='+'
result = bond.join(b)
print (result)  # 34+22+45+27+31+33+55

■ Q-380. 아래의 리스트를 가지고 아래의 결과를 출력하시오 

a = [34,22,45,27,31,33,55]

결과:  34+22+45+27+31+33+55 = 247  

a = [34,22,45,27,31,33,55]
b = []
for i in a:
    b.append(str(i))  # 문자로 변경해서 b 리스트에 추가한다. 
print(b)  # ['34', '22', '45', '27', '31', '33', '55']
bond='+'
result = bond.join(b)
print (result, '=', eval(result))

■ Q-381.  우리반 데이터(emp1222.csv) 에서 나이를 읽어들여  아래와 같이 
결과가 출력되게하시오 

결과 :  24 + 27 + 26 + 27 + ......................... 34 = ?  

import  csv
file = open("c:\\data\\emp1222.csv", encoding="CP949")
emp_csv = csv.reader(file)
b = [ ]
for  emp_list  in  emp_csv:
    b.append( emp_list[2] )                        

print(b)                                                                       # ['34', '22', '45', '27', '31', '33', '55']
bond='+'
result = bond.join(b)
print (result, '=', eval(result))

■ Q-382.  아래의 함수를 그냥 이름없는 한줄짜리 함수로 만들어 보시오 !

def  gob_func(a,b):
    return  a*b 

k = lambda  a,b : a*b
print ( k(2, 3) ) 

■ Q-383.  아래의 함수를 그냥 이름 없는 한줄짜리 함수로 생성하시오 !

def   odd_func(a):
    if  a % 2 ==0:
        return  '짝수 입니다'
    else:
        return '홀수 입니다'

print ( odd_func(2) )  # 짝수 입니다.
print ( odd_func(3) )  # 홀수 입니다.

k = lambda a  : '짝수 입니다' if a % 2 == 0 else '홀수 입니다'
print( k(2) )
print( k(3) )

■ Q-384.  아래의 함수를 lambda 로 구현하시오 !

def  high_income(a):
    if  a >= 3000:
        return '고소득자 입니다'
    else:
        return '일반 소득자 입니다.'

k = lambda  a :  '고소득자 입니다.' if  a >= 3000  else  '저소득자입니다'
print ( k(4000) )

■ Q-385. 아래의 함수를 lambda 로 구현하시오 !
(평균값 140, 표준편차 5 ) 

def  child_tall(num):
    if  140 - 1.96 * 5 <= num <= 140 + 1.96 * 5:
        return '신뢰구간 95% 안에 있습니다'
    else:
        return '신뢰구간 95% 안에 없습니다'

print( child_tall(147)  )
print ( child_tall(157) )

신뢰구간 68% ---> 평균 ± 1 * 표준편차
신뢰구간 95% ---> 평균 ± 1.96 * 표준편차
신뢰구간 99% ---> 평균 ± 2.58 * 표준편차 

답: 한줄 짜리 함수로는 너무 길어서 안할께요 ~

■ Q-386. 초등학생 키 데이터를  120 ~ 160  사이로 해서 0.001 간격으로
생성하시오 !

import  numpy  as  np 
x = np.arange(120, 160, 0.001) 
print(len(x))  # 40000

■ Q-387. 위에서 만든 40000건의 데이터에 대한 확률밀도함수값을 출력하시오
( 평균값 140, 표준편차 5 ) 
        
from  scipy.stats  import  norm
import  numpy  as  np 
x = np.arange(120, 160, 0.001) 
y = norm.pdf( x, 140, 5)  # 확률밀도함수 
print(y)

■ Q-388.  위의 데이터중 x 값과 y 을 가지고 시각화 하시오 !

from  scipy.stats  import  norm
import  numpy  as  np 
import  matplotlib.pyplot  as  plt 

x = np.arange(120, 160, 0.001) 
y = norm.pdf( x, 140, 5)  # 확률밀도함수 
plt.plot( x, y, color='red') 
plt.show()

■ Q-389. 위의 그래프에서 신뢰구간 95% 에 해당하는 부분만 색깔로 칠하시오

신뢰구간 68% ---> 평균 ± 1 * 표준편차
신뢰구간 95% ---> 평균 ± 1.96 * 표준편차
신뢰구간 99% ---> 평균 ± 2.58 * 표준편차 

from  scipy.stats  import  norm
import  numpy  as  np 
import  matplotlib.pyplot  as  plt 

x = np.arange(120, 160, 0.001)                      
y = norm.pdf( x, 140, 5)  # 확률밀도함수 
plt.plot( x, y, color='red') 
plt.fill_between( x, y, where = ( x >= 140 - 1.96*5 ) & (x<= 140+1.96*5), color='red',   alpha=0.5) 
plt.show()


■ Q-390. (오늘의 마지막 문제) 위의 코드를 이용해서 confidence_interval 함수를 생성
하고 아래와 같이 신뢰구간을 넣으면 해당 신뢰구간에 해당하는 그래프가
출력되게하시오 !

신뢰구간 68% ---> 평균 ± 1 * 표준편차
신뢰구간 95% ---> 평균 ± 1.96 * 표준편차
신뢰구간 99% ---> 평균 ± 2.58 * 표준편차 

from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
def confidence_interval(level):
    if level == 68:
        x = np.arange(120,160,0.001)
        y = norm.pdf(x,140,5)
        plt.plot(x,y,color = 'blueviolet')
        plt.fill_between(x,y,where = (x >= 140 -1*5 ) & (x <= 140 + 1*5), color = 'blueviolet', alpha = 0.5)
        plt.show()
    elif level == 95:
        x = np.arange(120,160,0.001)
        y = norm.pdf(x,140,5)
        plt.plot(x,y,color = 'blueviolet')
        plt.fill_between(x,y,where = (x >= 140 -1.96*5 ) & (x <= 140 + 1.96*5), color = 'blue', alpha = 0.5)
        plt.show()
    elif level == 99:
        x = np.arange(120,160,0.001)
        y = norm.pdf(x,140,5)
        plt.plot(x,y,color = 'blueviolet')
        plt.fill_between(x,y,where = (x >= 140 -2.58*5 ) & (x <= 140 + 2.58*5), color = 'green', alpha = 0.5)
        plt.show()
confidence_interval(68)
confidence_interval(95)
confidence_interval(99)
