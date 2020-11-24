파이썬을 통해서 우리가 얻어야할 지식

1.빅데이터 수집을 위한 웹스크롤링을 할 수 있는 능력 키우기
2.SQL 처럼 파이썬으로 데이터를 검색하고 데이터를 분석할 수 있는
  능력 키우기
3.딥러닝 개발자(연구원) 가 되기위한 기본 코딩능력 갖추기 

파이썬 설치

아나콘다 최신 버전으로 설치 하세요~

파이썬 기본 프로그램 + 여러가지 유용한 패키지들

spyder 툴로 파이썬 코드를 연습하겠습니다. 


■  001 대화식 모드로 프로그래밍 하기 

*파이썬을 실행하는 방법 2가지

1.대화식 모드 : 한라인 한라인식 실행하는 모드
예제)
a=1
b=2
a+b
3

2.배치 모드 : 여러개의 스크립트로 작성해서 한번에 실행하는 모드
스파이더에서 아래와 이 스크립트를 적어주고 전체 선택한 후에 ctl +enter 로
실행한것이 배치 모드이다. 
예제)
a=1
b=2
print(a+b)

Q-1.아래의 스크립트를 배치모드로 실행하시오!

for i in[1,2,3,4,5,6,7]:
    print(i)

■  002.텍스트 에디트로 프로그래밍 

spyder 와 같은 텍스트 창에서 프로그램 코드를 작성하는 것을 말한다.
spyder 프로그램에서 ctl + enter 키로 코드를 실행하거나 F5를 누르면 실행된다.

Q-2.아래와 같은 결과가 나오게 spyder 에서 프로그래밍 하시오!

for i in [2,3,4]:
    print(i)

■  003.변수명 만들기

"어떤값을 임시로 저장하는 변수의 이름을 만드는 방법과 규칙을 배웁니다"

예)
a=1
b=2
print(a+b)

설명: a 라는 변수에 숫자 1을 할당한다.
*변수 이름에는 다음 문자만 사용할 수 있습니다

※ 변수이름을 생성시 주의할 사항
1.변수이름에는 다음 문자만 사용할 수 있습니다.
-소문자(a~z)
-대문자(A~Z)
-숫자(0~9) 
-언더스코어(_) 

2.변수 이름은 숫자로 시작할 수 없습니다. (문자로 시작해야합니다)

3.예약어를 사용 할 수 없습니다. (파이썬에는 이미 사용학 있는 단어를 예약어라고 합니다.)

Q-3.파이썬의 예약어가 무엇이 있는지 확인하시오

 import keyword
    print(keyword.kwlist)


Q-4.위의 예약어를 변수로 사용하면 에러가 나는지 직접 테스트 하시오
 
and=1 
 

■  004.변수에 값 대입하기

-다양한 값을 변수에 대입하는 방법을 배웁니다.
-파이썬은 변수에 값을 대입할 때 = (assingment) 기호를 사용합니다.

예제)
a=1
b='scott'
print(b) 

다른 프로그램 언어에서는 아래와 같이 좀더 복잡한 코드로 작성해야한다.
b varchar2(10):='scott'; 

파이썬의 코드는 심플함을 철학으로 삼고 있습니다.
파이썬의 기본 철학을 확인하는 코드

import this 


파이썬은 c/c java 와는 달리 변수를 선언할때 숫자형 자료인지 문자형 자료인지
자료형을 명시하지 않아도 됩니다.

PL/SQL                    VS                파이썬

a number(10):=2;                            a=b

Q-5.변수의 자료형을 확인하시오!
             ↓
       문자형 숫자형

b='scott'
print(type(b))


Q-6.숫자형 변수의 자료형을 확인하시오

a=2
print (type(a))


■  005.주석 처리하기(#)

프로그램에서 주석부은 인터프리터에 의해  무시되는 텍스트의
한 부분니다. 코드를 설명하거나 나중에 어떤 문제를 고치기 위해
표시하는등 다양한 목적으로 주석을 사용할 수 있습니다.
코드를 작성할 때 주석을 잘 작성해두면 차후에 코드를 다시 보거나
타인이 코드를 검토할 때 매우 중요한 정보로 활용이 될 수 있습니다.
그래서 주석을 항상 달아주는 습을 가지는것이 좋습니다. 

예제)
1.한줄 주석

a=1 #변수 a에 숫자 1을 할당합니다
print(a) #a의 결과를 출력합니다.

2.여러줄 주석
"""아래의 프로그램은 a 변수에 1을 할당해서 프린트하는
프로그램입니다. """ 
a=1
print(a)

Q-7.아래의 리스트에서 문자 k를 출력하시오!
mmm = [ 'a','b','d','e','k','m','n','z']

 mmm = ['a','b','c','d','k']
    print (mmm[4])

(파이썬은 list 순서가 0,1,2,3,4 순이다) 0 부터 시작한다는 것을 기억하자.

Q-8.동전을 던져서 앞면이 나오는지 뒷면이 나오는지 확인하시오!

import random    # random 이라는 모듈을 이 코드에서 쓰겠다.
                                  ↓
                        특정 목적으로 만든 파이썬 코드의 집합

import random
       
coin=['앞면','뒷면']
print(random.choice(coin))


Q-9.위에서는 동전을 던졌는데 이번에는 주사위를 던져서
주사위의 눈이 뭐가 나오는지 확인하는 파이썬 코드를 작성하시오! 

import random

dice=[1,2,3,4,5,6]
print(random.choice(dice))

■  006. 자료형 개념 배우기

  " 자료형이란 프로그래밍을 할 때 쓰이는 숫자, 문자열등의
    자료 형태로 사용되는 모든것을 뜻합니다."

* 파이썬에서 자주 다루게 되는 자료형이 5가지가 있습니다.

1. 숫자형 자료형 : 숫자를 표현하는 자료형 
    예:  a = 1 

2. 문자형 자료형 : 문자를 표현하는 자료형
    예:  b = 'scott' 

3. 리스트 자료형 : [  ] 대괄호 안에 임의 객체를 순서있게 나열한 자료형
    예:  d = [ 1, 2, 3 ]  # 파이썬은 시작을 0 부터 시작합니다. 
                 0 1  2
         print (d) 
         print (d[0]) # d 리스트에서 첫번째 요소를 프린트해라 !

4. 튜플 자료형:  리스트와 비숫하지만 요소값을 변경할 수 없다는 것이
                          리스트와 다른점 입니다.
    예:  c = ( 1, 2, 3 )
         print (c) 
         print(c[0])

5. 사전 자료형:  사전 자료형은 {  } 중괄호 안의 키:값으로 된 쌍이 요소로
                    구성된 순서가 없는 자료형입니다.

예: m = { 'i' : '나는', 'am':'입니다', 'boy':'소년' }
    print (m) 

Q-7 아래의 리스트에서 문자 k 를 출력하시오 !

mmm =  [ 'a', 'b', 'd', 'e', 'k', 'm', 'n', 'z' ]

print ( mmm[4] )



■  007. 자료형 출력 개념 배우기(print)

  print 함수를 이용하면 다양한 자료형을 화면에 출력할 수 있습니다.

예:  
a = 200
b = 'i love python'
c = [ 'a', 'b', 'c' ]
print (a)
print (b)
print (c)

■  008.들여쓰기 개념 배우기 

파이썬에는 실행코드 부분을 묶어주는 ( ) 괄호가 없습니다. 
파이썬은 다른 프로그래밍 언어와달리 if,for,while 등과 같은 
제어문 ,루프문의 실행코드 부분을 구분해주는 괄호가 없습니다. 
대신 들여쓰기로 괄호를 대신합니다. 
파이썬에서 제어문이나 함수이름,클래스 이름 뒤에 콜론(:)으로
제어문,함수이름,클래스이름의 끝을 표시하며 콜론(:) 다음에
실행코드를 작성하는데 이때 들여쓰기를 해야합니다.

예제1) 실행코드를 다음라인에 작성했을 경우

listdata = ['a', 'b', 'c']  # listdata 라는 변수로 리스트를 생성 
if  'a'   in   listdata:  #  listadata 리스트 변수에  'a' 요소가 있다면  아래의 
    print ( 'a 가 listdata 에 있습니다.' )  # 실행문을 실행해라 ~~

예제2) 실행코드를 한 라인에 작성한 경우 

listdata = ['a', 'b', 'c']
if  'a'   in   listdata:  print (' a 가 listadata 에 있습니다.')

※설명: 콜론(:)으로 if 문의 끝을 알린다.

Q-10.점심시간에 했던 주사위의 눈이 6개 있는 변수를 만들고 
if 을 써서 주사위의 눈에 숫자 5가 있습니다. 라는 메세지가 출력되게 하시오 

dice=[1,2,3,4,5,6]
if 5 in dice:
     print ('주사위의 눈에 숫자 5 가 있습니다')

Q-11.위의 코드를 수정해서 숫자를 물어보게하고 숫자를 입력하면 위의 메세지가 
출력되게 하시오!

a=int(input('숫자를 입력하세요'))

dice=[1,2,3,4,5,6]
if a in dice:
     print ('주사위의 눈에 숫자  ',a,' 가 있습니다')  

■  009.If 문 개념 배우기 1 (if~else)

어떤 조건을 참과 거짓을 판단할때 if 문을 사용합니다.
참과 거짓을 구분하여 코드를 실행하면 if~else를 사용합니다.
코드를 작성하다 보면 조건에 따라 수행하는 일을 달리 해야하는
경우가 습니다. 조건이 참인지 거짓인지 검사를 하고,참인 경우에는
이 일을 하고 거짓인 경우에는 저 일을 해라 라는 식으로 처리를 할 수
있습니다. 

예제)
 if 조건:
       실행코드1
   else:
      실행코드2

예제)
a=int( ( input('숫자를 입력하세요') ) 
      if a%2 ==0:                              # %는 나머지값을 출력하는 연산자 
    print('짝수 입니다')                      # == 은 equal 연산자 입니다.
  else:                                          # = 은 할당 연산자 입니다. 
   print('홀수 입니다') 

Q-12.주사위의 을 담은 dice변수를 만들고 숫자를 물어보게 해서 해당숫자가 주사위의 눈중에
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

(',a,' 역할은 SQL 로 치면 || 이거이다. 문자형과 숫자형을 이어주는 샘이다) 

Q-13.숫자 2개를 아래와 같이 각각 물어보게 하고 아래처럼 메세지가 출력되게 하시오!

첫번째 숫자를 입력하세요 ~3
두번째 숫자를 입력하세요 ~2

3은2보다 큽니다. 

a = int( input( '첫번째 숫자를 입력하세요' ) )
b = int( input( '두번쨰 숫자를 입력하세요' ) )
if a > b :
     print( a , '은' , b '보다 큽니다' )
else a < b:
     print( a , '은' , b '보다 큽니다' )

■  010. if문 개념 배우기 ② (if~elif)

여러개의 조건을 순차적으로 체크하고 해당 조건이 참이면
특정 로직을 수행하고자 할 때 if ~ elif 문을 사용합니다. 
예제:   
         if  조건1:
             실행코드1
         elif  조건2:
             실행코드2
         elif 조건3:
             실행코드3
         else:                           #  위의 조건1과 조건2가 조건3이 아니라면
             실행코드3

예제)문제13번을 다시 수행하는데 같은 숫자가 2개가 들어오면
       서로 같습니다. 라는 메세지가 출력되게하시오.

a = int(  input(' 첫번째 숫자를 입력하세요 ~')  ) 
b = int(  input(' 두번째 숫자를 입력하세요 ~')  )

if  a < b :
    print ( a , '은',  b, '보다 작습니다')
elif  a > b:
    print ( a, '은', b, '보다 큽니다 ')  
else:
    print ( a, '은', b, '와 같습니다.')

■   011. for문 개념 배우기 ① (for)

  특정 코드를 반복적으로 수행하기 위해서는 반복문을 사용해야 하는데
  파이썬에서는 for 문 반복문을 수행하기 위해 가장 많이 사용되는 
  문법입니다. 

예제)  for  변수  in  범위:
            반복적으로 실행할 코드 

1. 리스트 범위인 경우
for  i  in  [ 1, 2, 3 ]:
    print (i)

2. 튜플 범위인 경우
for  i  in (1, 2, 3):
    print (i) 

3. range() 범위인 경우
for  i  in range(10):
    print (i)

                                           키    값 
4. 사전형 범위인 경우                ↓    ↓
m = { 'i' : '나는',  'am' : '입니다', 'boy':'소년'}
for  i  in  m:
    print (i)   # 키값만 출력되고 있습니다. 

5. 문자형 범위인 경우 
for  i  in  'i  am  a  boy':
    print(i)

■   for 루프(loop) 문의 range 사용법 정리

for  i  in  range(6):
    print (i)    # 0 부터 5까지 출력한다.

for  i   in  range(1, 6):
    print (i)  #  1 부터 5까지 출력된다. 

for  i  in  range(1, 6, 2):
    print (i)    #  1, 3, 5 를 출력한다. 

for  i  in  range(6, 1, -1):
    print (i)  # 6부터 1씩 차감해서 2까지 출력한다. 

Q-14. ★ 을 5개 출력하시오 !

★★★★★

print ('★' * 5 ) 

Q-15.아래와 같은결과가 출력는 파이썬 코드를 작성하시오! 

숫자를 입력하세요 ~ 5 

★
★★
★★★
★★★★
★★★★★

a = int ( input( '숫자를 입력하세요'))
for i in range(1,a+1):
    print( '★' * i)

Q-16.점심시간에는 주사위를 1번만 던졌는데 지금은 주사위를 10번 던져서 출력되는
눈을 확인하시오! 

import random

dice=[1,2,3,4,5,6]

for i in range(1,11):                                 # 1이상 11 미만으로 이해하면 됩니다. 
    print (random.choice(dice))



Q-17.동전을 10번던지세요 ~ 

import random
    
    coin=['앞면','뒷면']
    for i in range(1,11):
        print (random.choice(coin))

Q-18.동전을 10번 던졌을떄 앞면이 나오는 횟수가 어떻게 되는가

   import random
    
    coin=['앞면','뒷면']
    cnt = 0                                                  #cnt 라는 변수에 0을 할당한다 
    for i in range(1,11):
       result = random.choice(coin)             # 동전 던진결과를 result 변수에 해당한다.
        if reslut == '앞면': 
            cnt=cnt+1                               #할당연산자 오른쪽 부터 실행하고 실행한
print(cnt)                                                       #결과를 왼쪽 변수에 할당해 준다.
                                                       #for문의 실행문이 아닌 for 문과 위치를
                                                         #맞춰서 같은 라인에 #print(cnt) 를 쓰면은 
                                                         #for문이 다 완료 되면 print(cnt)가 수행된다



Q-19.주사위를 100번 던져서 주사위의 눈이 3이 나오는 횟수를 출력하시오

import random
dice=[1,2,3,4,5,6]
cnt=0
for i in range(1,101):
    result = random.choice(dice)
if result == 3:
    cnt=cnt+1
print(cnt)

Q-20.주사위를 1000번 지고 주사위의 눈이 5가 나올 확률을 구하시오

import random
dice=[1,2,3,4,5,6]
cnt=0
for i in range(1,101):
    result=random.choice(dice)
    if result == 5:
        cnt=cnt+1
    print(cnt)


Q-21.동전을 10000번 던져서 앞면이 나올확률을 출력하시오

import random
coin=['앞면','뒷면']
cnt=0
for i in range(1,10001):
    result = random.choice(coin)
    if result =='앞면':
        cnt=cnt+1
print(cnt/10000)

Q-22.오늘의 마지막 문제 
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
