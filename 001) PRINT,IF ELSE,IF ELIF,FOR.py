■ Q-1.아래의 스크립트를 배치모드로 실행하시오!

for i in[1,2,3,4,5,6,7]:
    print(i)

■ Q-2.아래와 같은 결과가 나오게 spyder 에서 프로그래밍 하시오!

for i in [2,3,4]:
    print(i)

■ Q-3.파이썬의 예약어가 무엇이 있는지 확인하시오

 import keyword
    print(keyword.kwlist)


■ Q-4.위의 예약어를 변수로 사용하면 에러가 나는지 직접 테스트 하시오
 
and=1 
 
■ Q-6.숫자형 변수의 자료형을 확인하시오

a=2
print (type(a))

■ Q-7.아래의 리스트에서 문자 k를 출력하시오!
mmm = [ 'a','b','d','e','k','m','n','z']

 mmm = ['a','b','c','d','k']
    print (mmm[4])

■ Q-8.동전을 던져서 앞면이 나오는지 뒷면이 나오는지 확인하시오!

import random    # random 이라는 모듈을 이 코드에서 쓰겠다.
                                  ↓
                        특정 목적으로 만든 파이썬 코드의 집합

import random
       
coin=['앞면','뒷면']
print(random.choice(coin))

■ Q-9.위에서는 동전을 던졌는데 이번에는 주사위를 던져서
주사위의 눈이 뭐가 나오는지 확인하는 파이썬 코드를 작성하시오! 

import random

dice=[1,2,3,4,5,6]
print(random.choice(dice))


■ Q-10.점심시간에 했던 주사위의 눈이 6개 있는 변수를 만들고 
if 을 써서 주사위의 눈에 숫자 5가 있습니다. 라는 메세지가 출력되게 하시오 

dice=[1,2,3,4,5,6]
if 5 in dice:
     print ('주사위의 눈에 숫자 5 가 있습니다')

■ Q-11.위의 코드를 수정해서 숫자를 물어보게하고 숫자를 입력하면 위의 메세지가 
출력되게 하시오!

a=int(input('숫자를 입력하세요'))

dice=[1,2,3,4,5,6]
if a in dice:
     print ('주사위의 눈에 숫자  ',a,' 가 있습니다')  

■ Q-12.주사위의 을 담은 dice변수를 만들고 숫자를 물어보게 해서 해당숫자가 주사위의 눈중에
있으면 해당숫자가 있습니다 라는 메세지가 출력되게하고 없으면 해당숫자가 없습니다.
라는 메세지가 출력되게 하시오.

숫자를 입력하세요 2
  2가 주사위의 눈에 있습니다.
숫자를 입력하세요 7

7가 주사위의 눈에 없습니다.

a = int((input('숫자를 입력하세요')))
dice=[1,2,3,4,5,6]
if a in dice:
     print('주사의의 눈에 숫자 ',a,' 가 있습니다')
else:
     print('주사위의 눈에 숫자 ',a,' 이 없습니다')

■ Q-13.숫자 2개를 아래와 같이 각각 물어보게 하고 아래처럼 메세지가 출력되게 하시오!

첫번째 숫자를 입력하세요 ~3
두번째 숫자를 입력하세요 ~2

3은2보다 큽니다. 

a = int( input( '첫번째 숫자를 입력하세요' ) )
b = int( input( '두번쨰 숫자를 입력하세요' ) )
if a > b :
     print( a , '은' , b '보다 큽니다' )
else a < b:
     print( a , '은' , b '보다 큽니다' )

■ Q-15.아래와 같은결과가 출력는 파이썬 코드를 작성하시오! 

숫자를 입력하세요 ~ 5 

★
★★
★★★
★★★★
★★★★★

a = int ( input( '숫자를 입력하세요'))
for i in range(1,a+1):
    print( '★' * i)

■ Q-16.점심시간에는 주사위를 1번만 던졌는데 지금은 주사위를 10번 던져서 출력되는
눈을 확인하시오! 

import random

dice=[1,2,3,4,5,6]

for i in range(1,11):                                  
    print (random.choice(dice))

■ Q-17.동전을 10번던지세요 ~ 

import random
    
    coin=['앞면','뒷면']
    for i in range(1,11):
        print (random.choice(coin))

■ Q-18.동전을 10번 던졌을떄 앞면이 나오는 횟수가 어떻게 되는가

   import random
    
    coin=['앞면','뒷면']
    cnt = 0                                                
    for i in range(1,11):
       result = random.choice(coin)             
        if reslut == '앞면': 
            cnt=cnt+1                              
print(cnt)                                                
                                                                                              
■ Q-19.주사위를 100번 던져서 주사위의 눈이 3이 나오는 횟수를 출력하시오

import random
dice=[1,2,3,4,5,6]
cnt=0
for i in range(1,101):
    result = random.choice(dice)
if result == 3:
    cnt=cnt+1
print(cnt)

■ Q-20.주사위를 1000번 지고 주사위의 눈이 5가 나올 확률을 구하시오

import random
dice=[1,2,3,4,5,6]
cnt=0
for i in range(1,101):
    result=random.choice(dice)
    if result == 5:
        cnt=cnt+1
    print(cnt)

■ Q-21.동전을 10000번 던져서 앞면이 나올확률을 출력하시오

import random
coin=['앞면','뒷면']
cnt=0
for i in range(1,10001):
    result = random.choice(coin)
    if result =='앞면':
        cnt=cnt+1
print(cnt/10000)

■ Q-22.오늘의 마지막 문제 
주사위 하나와 동전하나를 동시에 던져서 주사위의 눈은 5가 나오고
동전은 앞면이 나올 확률은 어떻게 되는가 

import random
dice=[1,2,3,4,5,6]
coin=['앞면','뒷면']
cnt=0
for i in range(1,1000001):
    resultc=random.choice(coin) 
    resultd=random.choice(dice)
    if resultc=='앞면' and resultd==5:
        cnt=cnt+1
print(cnt/1000000)
