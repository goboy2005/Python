# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:56:03 2020

@author: goboy
"""

Python Day 7 Problmes 

■ Q-167.  총 클래스를 생성하는데 총 클래스로 아래와 같이 총(제품)을 생성하면
'총이 만들어졌습니다. 총알은 0발 장전되었습니다.' 라는 메세지가 출력되게 
총 클래스를 만드시오 

class Gun():
    def __init__(self):
        self.bullet=0
        print('총이 만들어졌습니다 총알은' ,self.bullet, '장전되어있씁니다' )

yfs_gun1=Gun()

■ Q-168자열 포멧을 이용해서 위의 메세지를 더 자연스럽게 출력되게 하시오 !
 
class Gun():
    def __init__(self):
        self.bullet=0
        print('총이 만들어졌습니다 총알은 %d 발 장전되어있습니다' %self.bullet)

yfs_gun1=Gun()


■ Q-169. 충전한 금액보다 더 많은 금액을 소비하면 어떻게 되는지 테스트하시오 !

class  Card(): # 부모 클래스
    def  __init__(self):
       self.cash = 0
       print  ('카드가 발급되었습니다.')
    
    def  charge(self, num):
        self.cash += num
        print ( num, '원이 충전되었습니다.')

    def  consume(self, num):
        if  self.cash >= num:  # 잔액이 소비하는 돈보다 커야지만 쓸 수있게
            self.cash -= num
            print ( num, '원이 사용되었습니다.')
        else:
            print ('잔액이 부족합니다')
            
yys_card1 = Card()
yys_card1.charge(10000)
yys_card1.consume(80000) 

카드가 발급되었습니다.
10000 원이 충전되었습니다.
잔액이 부족합니다

■ Q-170. 팀장님이 만든 Card()  클래스를 상속받아 영화할인 카드를
생성하시오 !  ( 영화할인 카드 클래스: Movie_Card() )  

class  Movie_Card( Card ): #  부모클래스인 Card 클래스를 상속받아
    pass                         #  Movie_Card 클래스를 만든다. 

m_card1 = Movie_Card()
m_card1.charge(100000)
m_card1.consume(8000) 

카드가 발급되었습니다.
100000 원이 충전되었습니다.
8000 원이 사용되었습니다.

■ Q-171.  이번에는 제대로 영화관에서 사용하면 할인이 될 수 
있도록  영화 클래스를 생성하시오 !

class  Movie_Card( Card ):   # 부모에게 __init__,  charge , consume 를 상속받았다.
    def  consume(self, num, place):  # 부모에게 받은 consume 는 내가 만든 consume로
        if  place=='영화관':             # 덮어쓰기(overriding ) 가 됩니다. 
            num = 0.8 * num
            if  self.cash >= num:  # 잔액이 num 보다 크다면 카드를 사용하고 
                self.cash -= num
                print( place, '에서 ', num, '원이 사용되었습니다.')
            else:                      # 아니면 잔액이 부족하다고 출력해라 ~
                print('잔액이 부족합니다')
       else:   # 영화관에서 사용한게 아니라면 아래의 코드가 수행되게 해라 ~
           if  self.cash >= num:
               self.cash -= num
               print ( place, '에서', num, '원이 사용되었습니다.')
           else:
               print('잔액이 부족합니다')

m_card1 = Movie_card()
m_card1.charge(20000)
m_card1.consume(12000,'영화관')
m_card1.consume(2000,'편의점') 

카드가 발급되었습니다.
20000 원이 충전되었습니다.
영화관 에서  9600.0 원이 사용되었습니다.
편의점 에서 2000 원이 사용되었습니다. 
    

■ Q-172.  위의 영화할인 카드에 할인 장소를 추가해서 
 주유소에서도 20% 할인 될 수 있도록 코드를 수정하시오 !

m_card1 = Movie_card()
m_card1.charge(100000)
m_card1.consume(12000,'영화관')
m_card1.consume(30000,'주유소')
m_card1.consume(2000,'편의점') 

답:

class  Movie_Card( Card ):   # 부모에게 __init__,  charge , consume 를 상속받았다.
    def  consume(self, num, place):  # 부모에게 받은 consume 는 내가 만든 consume로
        if  place  in  ('영화관', '주유소'):           
            num = 0.8 * num
            if  self.cash >= num:  # 잔액이 num 보다 크다면 카드를 사용하고 
                self.cash -= num
                print( place, '에서 ', num, '원이 사용되었습니다.')
            else:                      # 아니면 잔액이 부족하다고 출력해라 ~
                print('잔액이 부족합니다')
       else:   # 영화관에서 사용한게 아니라면 아래의 코드가 수행되게 해라 ~
           if  self.cash >= num:
               self.cash -= num
               print ( place, '에서', num, '원이 사용되었습니다.')
           else:
               print('잔액이 부족합니다')

m_card1 = Movie_card()
m_card1.charge(20000)
m_card1.consume(12000,'영화관')
m_card1.consume(2000,'편의점') 


■ Q-173. (점심시간 문제)  영화관과 주유소에서는 20% 할인되게하고 
스타벅스에서는 10% 할인되게 코드를 수정하시오

m_card1 = Movie_card()
m_card1.charge(100000)
m_card1.consume(12000,'영화관')
m_card1.consume(30000,'주유소')
m_card1.consume(6000,'스타벅스')
m_card1.consume(2000,'편의점')

# 부모 클래스
class Card:
    def __init__(self):
        self.cash=0
        print('카드가 발급되었습니다')
    def charge(self,num):
        self.cash+=num
        print(num,'원이 충전되었습니다')
    def consume(self,num):
        if self.cash>=num:
            self.cash-=num
            print(num,'원이 사용되었습니다')
        else:
            print('잔액이 부족합니다')
# 자식 클래스
class Movie_Card(Card):
    def consume(self,num,place): # 오버라이딩(덮어쓰기)
        if place in ('영화관','주유소'):
            num=0.8*num
            if self.cash>=num:
                self.cash-=num
                print(place,'에서',num,'원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다')
        elif place=='스타벅스':
            num*=0.9
            if self.cash>=num:
                self.cash-=num
                print(place,'에서',num,'원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다')
        else:
            if self.cash>=num:
                self.cash-=num
                print(num,'원이 사용되었습니다')
            else:
                print('잔액이 부족합니다')
m_card1=Movie_Card()
m_card1.charge(100000)
m_card1.consume(200000,'집')
m_card1.consume(10000,'편의점')
m_card1.consume(10000,'영화관')
m_card1.consume(10000,'주유소')
m_card1.consume(10000,'스타벅스')


■ Q-174.  위에서 생성한 객체 emp_chulsu 의 email 변수에 있는 내용을 출력해보시오 !

print( emp_chulsu.email )  # chulsu.kim@gmail.com

■ Q-175.  철수의 월급을 회사규정에 따라 인상시키시오 !

emp_chulsu.apply_raise()  #  emp_chulsu 객체의 apply_raise() 메소드를 실행한다. 
print(emp_chulsu.pay)  # 5500000

■ Q-176. 이번에는 새로운 사원 철수2 로 emp_chulsu2 객체를 생성하시오 !

emp_chulsu2 = Employees('chulsu2', 'kim', 5000000)

■ Q-177.  철수2 사원이 월급을 인상시키기 위한 인스턴스 변수를 알아냈습니다.
자기는 월급을 10% 인상이 아니라 20% 인상 시키고 싶어서 아래와 같이
 emp_chulsu2 객체의 멤버인 raise_amount 라는 변수에 1.2 를 할당하고 
월급을 인상시키는 apply_raise() 메소드를 실행을 했다. 

emp_chulsu2.raise_amount = 1.2

print( emp_chulsu2.pay ) # 5000000
emp_chulsu2.apply_raise()
print(emp_chulsu2.pay ) # 6000000

■ Q-178. 그래서 위와 같이 악용이 될수 없도록 막는 방법이 무엇입니까 ?

class  Employees:
    raise_amount = 1.1  # 클래스 변수
    def __init__(self, first, last, pay): # 객체가 만들어질때
        self.first = first               # 바로 작동되는 함수
        self.last  = last
        self.pay   = pay
        self.email = first.lower() + '.' + last.lower() + '@gmail.com'
        self.raise_amount = 1.1  # 인스턴스 변수

    def  full_name(self): #사원의 전체이름을 출력하는 함수
        return  '{} {}'.format(self.first, self.last)

    def  apply_raise(self): # 월급을 인상하는 함수
        self.pay = int( self.pay * Employees.raise_amount)  # 클래스 변수를 사용 
#                                             ↑
#                아까는 여기가 self 였는데 지금은 클래스 이름인 Employees 가 있다.
#                이자리에 인스턴스 변수가 아니라 클래스 변수를 썼습니다. 

emp_chulsu2 = Employees('chulsu2', 'kim', 5000000)

emp_chulsu2.raise_amount = 1.2   # 인스턴스 변수만 변경할 수 있고 클래스 변수는
                                             # 변경할 수 없다. 

print(emp_chulsu2.pay)   # 5000000
emp_chulsu2.apply_raise()
print(emp_chulsu2.pay)  # 5500000

설명:  위와 같이 민감한 변수(멤버)들은 인스턴스 변수가 아니라
         클래스 변수(멤버) 를 사용해서 계산되게 코딩해야합니다.

클래스내의 변수는 2개가 있는데 

  1. 클래스 변수 :  메소드 바깥의 변수
                         객체 생성이후에 안의 값을 변경할 수 없다.

  2. 인스턴스 변수 : 메소드 안의 변수 
                          객체 생성이후에 안의 값을 변경할 수 있다. 

■ Q-179. 판다스를 이용해서 emp3.csv 에서 이름과 월급을 출력하시오 !

import  pandas  as  pd

emp = pd.read_csv("c:\\data\\emp3.csv")
print ( emp[ ['ename', 'sal'] ] ) 

■ Q-180.  이름이 SCOTT 인 사원의 이름과 월급을 출력하시오 !

import  pandas  as  pd

emp = pd.read_csv("c:\\data\\emp3.csv")
print ( emp[ ['ename', 'sal'] ] [ emp['ename']=='SCOTT' ] ) 

■ Q-181.  input 함수를 이용해서 이름을 물어보게 하고 이름을 입력하면
해당 사원의 이름과 월급일 출력되게 하시오 !

이름을 입력하세요 ~   SCOTT

SCOTT   3000

import  pandas  as  pd
name = input('이름을 입력하세요 ~')

emp = pd.read_csv("c:\\data\\emp3.csv")
print ( emp[ ['ename', 'sal'] ] [ emp['ename']== name  ] ) 

■ Q-182.  이번에는 소문자로 이름을 입력해도 출력되게하시오 !

힌트:   print ( 'scott'.upper() )

이름을 입력하세요 ~   scott

 SCOTT   3000

답:
import  pandas  as  pd
name = input('이름을 입력하세요 ~')

emp = pd.read_csv("c:\\data\\emp3.csv")
print ( emp[ ['ename', 'sal'] ] [ emp['ename']== name.upper()  ] ) 

■ ■ Q-183.  그런데 이번에는 위의 코드를 실행하는데 없는 사원이름을
입력하시오 !

이름을 입력하세요 ~   jack  

Empty DataFrame
Columns: [ename, sal]
Index: []

■ Q-184.  위의 코드에 예외처리를 해서  없는 사원이름을 입력하면
입력하신 이름의 사원은 존재하지 않습니다. 라는 메세지가 
출력되게하시오 !

답:  이것은 에러가 아니라서 예외처리가 되지 않습니다. 

■ Q-185.  숫자를 입력하면 해당 숫자의 제곱값이 출력되는 코드를 구현하시오

숫자를 입력하세요 ~   2

   4 

답:  
num = int( input( '숫자를 입력하세요 ~ ') )
print ( num**2 )

■ Q-186.  try ~ except 예외처리를 이용해서 아래와 같이
문자를 입력하면 '잘못된 값을 입력하셨습니다' 라는 메세지가
출력되게 하시오 !

숫자를 입력하세요 ~   a

잘못된 값을 입력하셨습니다. 
                                                  
try:
    num = int( input('숫자를 입력하세요' ) )
    print ( num**2 )
except:
    print('잘못된 값을 입력하셨습니다')

설명: try 와 except 사이의 있는 코드에서 에러가 나야지만 
       except 이후의 문장을 실행합니다. 


■ Q-187.  아까 했던 나누기 프로그램을 수정해서 나누기가 성공하면
성공적으로 나누기를 하였습니다. 라는 메세지가 출력되게하시오

분자를 입력하세요 ~  10
분모를 입력하세요 ~   2

 5
성공적으로 나누기를 하였습니다. 

답:

try:
    x = input('분자의 숫자를 입력하세요 ~')
    y = input('분모의 숫자를 입력하세요 ~')
    print  (int(x) / int(y) )
except:
    print( '당황하셨겠지만 잘못된 값을 입력하셔서 나누기를 할 수 없습니다.')
else:
    print ( '성공적으로 나누기를 하였습니다' )


■ Q-188.  나누기하는 프로그램을 실행할 때 오류가 나던 오류가 나지 않던
무조건 아래의 메세지가 출력되게하시오 !

분자를 입력하세요 ~  10                           10
분모를 입력하세요 ~   2                             0

5                                             나누기를 할 수 없습니다. 
이준혁이 만든 프로그램입니다.        이준혁이 만든 프로그램입니다.
답:
try:
    x = int( input('분자의 숫자를 입력하세요') )
    y = int( input('분모의 숫자를 입력하세요') )
    print( x / y )
except:
    print ('나누기를 할 수 없습니다.')
finally:
    print ('이준혁이 만든 프로그램입니다')

■ Q-189. 동전을 10번던져서 앞면이 2번 나올 확률을 출력하세요 !
   ( 동전을 10번 던지는 작업을 10000 번 수행되게 하시오)

import random

coin =['앞면', '뒷면']
cnt=0
a = []
for   i   in  range(1, 11):
    result = random.choice(coin)
    a.append(result)

print (a)    
  
['앞면', '뒷면', '뒷면', '뒷면', '뒷면', '앞면', '뒷면', '뒷면', '앞면', '앞면'] 

import random

coin =['앞면', '뒷면']
cnt=0
a = []
for   i   in  range(1, 11):
    result = random.choice(coin)
    a.append(result)
print (a.count('앞면'))    


import random

coin =['앞면', '뒷면']                       
cnt = 0

for  k in  range(1, 10001):
    a = []
    for   i   in  range(1, 11):
        result = random.choice(coin)
        a.append(result) 

    #['앞면', '뒷면', '뒷면', '뒷면', '뒷면', '앞면', '뒷면', '뒷면', '앞면', '앞면']
          
    if a.count('앞면')== 2:
        cnt = cnt + 1
        
print(cnt/10000)              # 확률 

■ Q-190. (오늘의 마지막 문제) 위의 코드를 함수로 생성하여 확률이 
출력되게하시오 !

coin_prob(2) # 0.04314 
coin_prob(4) #  0.2065 
             ↑

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
    print(cnt/10000)

coin_prob(2)
coin_prob(4)
