# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:50:04 2020

@author: goboy
"""



■ Q-253.  아래의 txt 변수에서 w 를 출력하시오 !

txt = 'A tale that was not right' 
     
print (txt[12])

■ Q-254.  위의 txt 변수에서 맨끝의 철자인 t 를 출력하시오 

txt = 'A tale that was not right'
print (txt[-1])

■ Q-255.  emp2.csv 에서 이름만 출력하시오 ! 
 판다스를 이용하지 말고 emp2.csv 파일에 직접 읽어들여서 출력하시오 !

import   csv 
file = open("c:\\data\\emp2.csv")
emp_csv = csv.reader(file)
for  emp_list  in  emp_csv:
    print (emp_list[1] )


■ Q-256. 위의 출력된 이름의 데이터 유형이 무엇인지 확인하시오 !

import   csv 
file = open("c:\\data\\emp2.csv")
emp_csv = csv.reader(file)
for  emp_list  in  emp_csv:
    print (type(emp_list[1] ))

■ Q-257.  문제255번을 다시 수행해서 emp2.csv 에서 이름을 출력하는데
이름의 첫번째 철자만 출력하시오 !

import   csv 
file = open("c:\\data\\emp2.csv")
emp_csv = csv.reader(file)
for  emp_list  in  emp_csv:
    print (emp_list[1][0])  # a[0]

■ Q-258.  위의 결과를 다시 출력하는 첫번째 철자가 소문자로 출력되게하시오
             ( 힌트:   'SCOTT'.lower()   )  
                         문자열.lower() 

import   csv 
file = open("c:\\data\\emp2.csv")
emp_csv = csv.reader(file)
for  emp_list  in  emp_csv:
    print (emp_list[1][0].lower())  # a[0].lower()


■ Q-259.  아래의 SQL을 파이썬으로 구현하시오 !
( 판다스 이용하지말고 그냥 emp2.csv 를 읽어서 구현)

select  ename, substr( ename, 1, 3)
          from  emp;


import   csv 
file = open("c:\\data\\emp2.csv")
emp_csv = csv.reader(file)
for  emp_list  in  emp_csv:
    print ( emp_list[1],  emp_list[1][0:3] )

예제
txt = 'aAbBcCdDeEfFgGhHiIjJkK'
result = txt[0:]  # 0번째 부터 문자끝까지 출력
print (result )
result2 = txt[0 : : 2 ] # 문자열에서 2칸씩 건너뛰면서 출력
print(result2)

■ Q-260. 위의 txt 문자열에서 짝수번째 철자들만 출력하시오 !

txt = 'aAbBcCdDeEfFgGhHiIjJkK'
result3 = txt[1: : 2]
print(result3)


■ Q-261.  이름을 출력하는데 이름의 철자를 거꾸로 출력하시오 !
 ( emp2.csv 를 읽어서 하세요 ~ 파이썬으로만 하세요)

import   csv 
file = open("c:\\data\\emp2.csv")
emp_csv = csv.reader(file)
for  emp_list  in  emp_csv:
    print ( emp_list[1][ : : -1] )

■ Q-262.  아래의 SQL 을 파이썬으로 구현하시오 ! (emp2.csv 를 이용하세요)

SQL> select  ename || job
           from  emp;

파이썬>
import   csv 
file = open("c:\\data\\emp2.csv")
emp_csv = csv.reader(file)
for  emp_list  in  emp_csv:
    print ( emp_list[1] + emp_list[2] )

■ Q-263. 아래와 같이 결과가 출력되게하시오 !

SQL> select   ename || '의 직업은 ' || job || '입니다.'
          from  emp;

KING 의 직업은 PRESIDENT 입니다.
BLAKE 의 직업은 MANAGER 입니다. 
  : 
  :

파이썬>
import   csv 
file = open("c:\\data\\emp2.csv")
emp_csv = csv.reader(file)
for  emp_list  in  emp_csv:
    print ( emp_list[1] +' 의 직업은 ' + emp_list[2] + ' 입니다' )


■ Q-264. for loop문을 이용해서 숫자 1부터 5까지 출력하시오 !

for  i  in  range(1, 6):
    print (i)

■ Q-265.  숫자를 물어보게하고 숫자를 입력하면 해당 숫자까지 숫자가
출력되게하시오 !

a = int( input('숫자를 입력하세요 ~ ') )

for  i  in  range(1, a+1):
    print (i)

■ Q-266. 위의 코드를 수정해서 숫자를 물어보게하고 아래와 같이
★ 이 출력되게하시오 !

숫자를 입력하시오 ~  5

★
★★
★★★
★★★★
★★★★★

a = int( input('숫자를 입력하세요 ~ ') )

for  i  in  range(1, a+1):
    print (i * '★')

■ Q-267. (알고리즘 22번 문제)   아래와 같이 사각형이 출력되게하시오 !
                         
가로의 숫자를 입력하세요 ~  3
세로의 숫자를 입력하세요 ~  5

★★★
★★★
★★★
★★★
★★★

a= int(input('가로의 숫자를 입력하세요~'))
b= int(input('세로의 숫자를 입력하세요~'))

for i in range(1, b+1):
    print(a * '★')


■ Q-268.  emp2.csv 에서 이름을 출력하는데 이름에 S 를 포함하고 있는
사원들의 이름을 출력하시오 !

select  ename
           from  emp
           where  ename  like '%S%';


import   csv 
file = open("c:\\data\\emp2.csv")
emp_csv = csv.reader(file)
for  emp_list  in  emp_csv:
    if  'S'  in  emp_list[1]:   # if  'b'  in  txt:
        print( emp_list[1] ) 


■ Q-269.  문제268번 코드를 수정해서 출력하는데 이름에 S 자가 포함된
사원의 이름이 몇명인지 출력하시오 !

 결과: 5               
import   csv 
file = open("c:\\data\\emp2.csv")
emp_csv = csv.reader(file)
cnt = 0
for  emp_list  in  emp_csv:
    if  'S'  in  emp_list[1]:   #  이름에 S 자가 포함되어져 있으면 
        cnt = cnt + 1

print (cnt)


■ Q-270. (점심시간 문제) 겨울왕국 스크립트에서 elsa 라는 문자열(단어)이
몇번 나오는가?   세원이 코드를 실행하세요 ~

winter = open("c:\\data\\winter.txt")  # winter.txt 를 winter 로 불려온다.
winter2 = winter.read().split("\n") # 엔터로 먼저 줄 단위로 분리를 해야함

cnt = 0
for i in winter2:
    for j in i.split(' '):
        if 'elsa' in j.lower():
            cnt +=1
            print(j,cnt)

Elsa 329

오전에 배웠던 내용으로만 elsa 가 몇건 들어있는지 카운트

winter = open("c:\\data\\winter.txt")  # winter.txt 를 winter 로 불려온다.
winter2 = winter.read().split(" ")
cnt = 0
for  i  in  winter2:
    if 'elsa'  in  i.lower():
        cnt = cnt + 1
        print(i.lower(), cnt)

elsa 304
confidence. anna elsa? elsa love. elsa  305

설명:  위의 결과를 보면 304 다음에 elsa 가 3개가 있으므로 305가 되면 안되는
        데 305가 된 이후는 confidence. anna elsa? elsa love. elsa 를
        하나의 문장으로 보았기 때문입니다.  어절별로 분리한걸로 코드를
        구현했지만 실제로는 어절별로 분리가 되지 않았습니다.
        그래서 위와같은 실수를 하지 않으려면 해결하는 방법은 ?

       먼저 스크립트를 행단위로 먼저 분리를 하고나서 어절별로 분리를
       해야 합니다.

winter = open("c:\\data\\winter.txt")
winter2 = winter.read().split("\n")  # 행단위로 분리하는 코드

cnt = 0
for i in winter2: 
    for k  in  i.split(' '):
        print(k)

위에 방법은 세원이가 한 방법이고 아래는 건준이가 한 방법 

winter=open('c:\\data\\winter.txt')
winter2=winter.read().split()  # 아무것도 안쓰면 어절별로 나뉜다. 
cnt=0                             # 아무것도 안쓰면 기본값이 어절별입니다. 
for i in winter2:  # 어절별로 분리한 것들을 하나씩 가져오면서 
    if 'elsa' in i.lower():
        cnt+=1
print(cnt)



■ Q-272. 스티븐 잡스 연설문인 jobs.txt 를 한행 한행씩 출력하시오 !
                                                                            
stev  = open("c:\\data\\jobs.txt", encoding='UTF8')
stev2 = stev.read().split('\n') #  한행씩 분리하는 작업
for  i  in  stev2:   # 한행씩 분리된 스크립트를 읽어서 
    print(i)           # 한행씩 출력한다. 

설명:  위의 코드를 실행했는지 cp949 에러가 나면 encoding 에 UTF8 도
        써보고 ANSI 도 써보고 CP949 도 써보세요 ~

■ Q-273.  위에서 한행씩 출력하고 있는 스크립트를 철자 하나씩 출력하시오
                                           
stev  = open("c:\\data\\jobs.txt", encoding='UTF8')
stev2 = stev.read().split('\n') 
for  i  in  stev2:   
    for  k  in  i:  # 스크립트 한행을 읽어서 철자를 하나씩 불러오는 코드
        print(k)    # 그 철자를 출력한다. 

■ Q-274.  위에서 출력된 철자가 알파벳이면 cnt 를 증가시켜서
스티븐 잡스 연설문에 알파벳이 몇개가 있는지 출력하시오 !

stev  = open("c:\\data\\jobs.txt", encoding='UTF8')
stev2 = stev.read().split('\n') 
cnt = 0
for  i  in  stev2:   
    for  k  in  i:  # 스크립트 한행을 읽어서 철자를 하나씩 불러오는 코드
        if  k.isalpha() == True:
            cnt = cnt + 1

print(cnt)                     # 9255 


■ Q-275. 스티븐 잡스 연설문에는 숫자가 몇개가 있는지 출력하시오 !

stev  = open("c:\\data\\jobs.txt", encoding='UTF8')
stev2 = stev.read().split('\n') 
cnt = 0
for  i  in  stev2:   
    for  k  in  i:  # 스크립트 한행을 읽어서 철자를 하나씩 불러오는 코드
        if  k.isdigit() == True:
            cnt = cnt + 1
            print ( k,  cnt )

print(cnt) 


■ Q-276.  스티븐 잡스 연설문에는 긍정단어가 몇개가 있는지 확인하세요 ~
코드를 답글로 올리세요 

positive = open('c:\\data\\positive-words.txt', encoding='CP949')
pos = positive.read().split('\n') # positive 에서 행별로 분리해서 pos 에 담는데
                                        # pos 는 리스트 입니다. 
                                        # pos 리스트에 긍정단어들이 들어있습니다
stev = open('c:\\data\\jobs.txt', encoding='UTF8')
stev2 = stev.read().split() # 스티븐 잡스 연설문을 어절별로 분리하여 
                                # stev2 에 입력했는데 stev2 도 리스트이고
                                # stev2 리스트에는 스티븐 잡스 연설문이 어절별로
                                # 분리되어서 저장되어 있습니다.
cnt = 0
for i in stev2:  # stev2 에서 단어들을 하나씩 빼옵니다. 
    if i.lower() in pos:  # i의 단어가 pos 긍정단어 리스트에 존재하면 
        cnt += 1     # cnt 를 1씩 증가 시킵니다. 
print(cnt)
68개 


■ Q-277.   emp2.csv 에서 이름과 월급을 출력하시오 !

import  csv

file = open("c:\\data\\emp2.csv")
emp_csv=csv.reader(file)

for  emp_list  in  emp_csv:
    print( emp_list[1], emp_list[5] )

■ Q-278.  이름을 물어보게하고 이름을 입력하면 해당 사원의 이름과 월급이
출력되게하는데 소문자로 입력하던 대문자로 입력하던  잘 출력되게하시오 !

이름을 입력하세요 ~  scott

SCOTT  3000

import  csv

name = input('이름을 입력하세요 ~') 

file = open("c:\\data\\emp2.csv")
emp_csv=csv.reader(file)

for  emp_list  in  emp_csv:
    if  emp_list[1].lower() == name.lower(): # 양쪽 다 소문자로 변경
        print( emp_list[1], emp_list[5] )


■ Q-279. 스티븐 잡스 연설문에서는 정관사 the 가 몇번 나오는가 ?

stev = open('c:\\data\\jobs.txt', encoding='UTF8')
stev2 = stev.read().split() # 스티븐 잡스 연설문을 어절별로 분리하여 
                                # stev2 에 입력했는데 stev2 도 리스트이고
                                # stev2 리스트에는 스티븐 잡스 연설문이 어절별로
                                # 분리되어서 저장되어 있습니다.
cnt = 0
for i in stev2:  
    if  i.lower().strip() =='the':  # 양쪽에 공백이 있을지 모르므로 확인사살 코드
        cnt = cnt + 1
        print(i.lower(), cnt)
print( cnt )


■ Q-280.  안철수 연설문에서는 국민 이라는 단어가 몇번 나오는지 
카운트 하시오 !  (ahn.txt) 

ahn = open('c:\\data\\ahn.txt', encoding='UTF8')
ahn2 = ahn.read()  # split 안했으니까 그냥 안철수 연설문을 읽어서 
                        #  통채로 ahn2 에 입력한다. 
print( ahn2) # 안철수 연설문 전체가 출력됨
print( ahn2.count('국민') ) # 안철수 연설문에서 국민이라는 단어가 몇개
                                 # 있는지 출력합니다. 


■ Q-281.  동전을 10번 던져서 앞면이 2개가 나오는 지난번 마지막 문제의
 확률 10개를 가지고 막대그래프를 그리시오 !

import  matplotlib.pyplot  as  plt

y_value = [0.00191, 0.01, 0.07, 0.16 ]
x_index = [ 0, 1, 2, 3 ]
plt.bar( x_index, y_value, color='red' )
plt.show()

■ Q-282.  위의 그래프의 결과에 제목, x축 라벨과 y축 라벨을 같이 출력하시오

import  matplotlib.pyplot  as  plt

y_value = [0.00191, 0.01, 0.07, 0.16 ]
x_index = [ 0, 1, 2, 3 ]
plt.bar( x_index, y_value, color='red' )
plt.title('coin Probability')  # 그래프 제목
plt.xlabel('cnt')               # 그래프 x축 라벨
plt.ylabel('probability')     # 그래프 y축 라벨 
plt.show()

■ Q-283. 지난번 마지막 문제인 동전을 10번 던져서 앞면이 2개 나오는
아래의 확률 결과를 가지고 막대그래프로 시각화 하시오!
 지난번 마지막 문제 코드가져다가 시각화 하세요 ~~
 코드와 그래프를 같이 올리세요 ~~


import random
def coin_prob(num):
    coin = ['앞면','뒷면']
    cnt = 0
    for k in range(1,10001):
        a = [ ]
        for i in range(1,11):
            result = random.choice(coin)
            a.append(result)
        if a.count('앞면') == num:
            cnt = cnt + 1
    return cnt/10000

b=[]
for i in range(0,11):
    result2 = coin_prob(i)
    b.append(result2)

import matplotlib.pyplot as plt

y_value = b
x_index = [0,1,2,3,4,5,6,7,8,9,10]

plt.bar ( x_index, y_value)
plt.title('Coin Probability')
plt.xlabel('cnt')
plt.ylabel('probability')
plt.show()
