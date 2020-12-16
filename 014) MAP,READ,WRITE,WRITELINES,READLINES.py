# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 22:12:03 2020

@author: goboy
"""


■ Q-391.   숫자를 입력해서 해당 숫자가 3000 보다 크면  숫자 1을
              리턴하게 하고 입력하는 숫자가 3000 보다 작다면 0을 리턴하는
              함수를 생성하시오 !

def  high_income(num):
    if  num >= 3000:
        return  1 
    else:
        return  0

print ( high_income(3500) ) 

■ Q-392.  위에서 만든 함수를 map 함수에 적용해서 아래의 리스트의 요소를
             high_income 함수의 입력 매개변수로 입력해서 아래의 결과가
             출력되게하시오 !
a = [ 4000, 5000, 2000, 3500, 1000 ]

def  high_income(num):
    if  num >= 3000:
        return  1 
    else:
        return  0

a = [ 4000, 5000, 2000, 3500, 1000 ]

result = map( high_income, a )
print ( list(result) ) 

■ Q-393.  동전을 지정된 숫자만큼  던져서 앞면이 나오는지 뒷면이 나오는지 
             출력하는 함수를 생성하시오 !

import  random

def  coin_cnt(num):
    coin = ['앞면', '뒷면']
    for  i  in  range(1, num+1):
        result = random.choice(coin)
        print(  result  )

coin_cnt(5) 

■ Q-394.  위의 함수를 수정해서 숫자를 입력하면 해당 숫자만큼 동전을 
             던져서 동전이 앞면이 나오는 확률을 출력하시오 !

print ( coin_cnt(100) )

import  random

def  coin_cnt(num):
    coin = ['앞면', '뒷면']
    cnt = 0
    for  i  in  range(1, num+1):
        result = random.choice(coin)
        if  result =='앞면':
            cnt = cnt + 1 
    return  cnt / num

print ( coin_cnt(100) )  

■ Q-395.  위에서 만든 coin_cnt 함수에 아래의 a 리스트의 요소들을 적용해서
             결과로 확률이 출력되게하시오 

a = [ 10, 100, 1000, 10000, 100000 ]

import  random

def  coin_cnt(num):
    coin = ['앞면', '뒷면']
    cnt = 0
    for  i  in  range(1, num+1):
        result = random.choice(coin)
        if  result =='앞면':
            cnt = cnt + 1 
    return  cnt / num

a = [ 10, 100, 1000, 10000, 100000 ]
result = map( coin_cnt, a )
print ( list( result)  ) # [0.4, 0.46, 0.486, 0.4965, 0.49929]

설명:  동전을 던지는 횟수가 많아 질 수록 0.5 에 근사한 값이 출력되고 있다.

■ Q-396. 주사위를 던져서 주사위의 눈이 5가 나올 확률을 출력하는 
           함수를 만들고 아래의 a 리스트의 주사위를 던지는 횟수를
            map 함수로 적용해서 확률이 점점 1/6 로 근사해지는지 
            실험하시오 !

a = [ 10, 100, 1000, 10000, 100000 ]

result = map( dice_cnt,  a )
print ( list(result) ) 

import  random
def  dice_cnt(num):
    dice = list( range(1, 7)  )
    cnt = 0
    for  i  in  range(1, num+1):
        result = random.choice(dice)
        if  result == 5 :
            cnt = cnt + 1 
    return  cnt / num

a = [ 10, 100, 1000, 10000, 100000 ]

result = map( dice_cnt,  a )
print ( list(result) )   # [0.1, 0.09, 0.181, 0.163, 0.16772]

■ Q-397.   아래의 불량품이 들어있는 박스에서 제품을 3개를 뽑았을때
              3개중에 2개가 불량품일 확률을 출력하는 함수를 만드시오 ~
              함수를 실행할 때 3개를 뽑은 횟수를 입력매개변수로 사용하세요
              복원 추출로 하세요 !

box = ['정상', '정상', '불량품', '정상', '불량품', '정상', '정상', '불량품'] 

print ( box_cnt(100) )        #   

import  numpy  as  np
                               
def  box_cnt(num):
    box = ['정상', '정상', '불량품', '정상', '불량품', '정상', '정상', '불량품']
    cnt = 0
    for  i  in  range(1, num+1):
        result = list( np.random.choice( box, 3, replace=True) )
        if  result.count('불량품') == 2:
            cnt = cnt + 1
    return  cnt / num       

print ( box_cnt(100) ) 

■ Q-398. 위에서 만든 box_cnt 함수에 아래의 a 리스트의 횟수를 map 함수로
            적용해서 확률이 출력되게하시오 !

import  numpy  as  np
                               
def  box_cnt(num):
    box = ['정상', '정상', '불량품', '정상', '불량품', '정상', '정상', '불량품']
    cnt = 0
    for  i  in  range(1, num+1):
        result = list( np.random.choice( box, 3, replace=True) )
        if  result.count('불량품') == 2:
            cnt = cnt + 1
    return  cnt / num              

a = [ 10, 100, 1000, 10000, 100000 ]
result = map( box_cnt, a)
print ( list(result ))   # [0.3, 0.35, 0.274, 0.2684, 0.26458]


■ Q-399.  중앙일보에서 인공지능으로 검색한 기사인 mydata3.txt 를
             파이썬으로 불러서 출력하시오 !

f = open('c:\\data\mydata3.txt', encoding='UTF8')
data = f.read() # 파일을 한번에 전부 읽어오는 함수 입니다. 
print ( data )
f.close()  # 파일을 닫는다.  닫는 코드를 안쓰면 스파이더를 실행하고 있으면
            # 계속 파일이 열려있게 됩니다. 파일을 계속 열면 메모리를 계속
           # 차지하고 사용하고 있게 됩니다. 
           # 텍스트 파일의 크기가 크면 메모리를 많이 사용하고 있게 됩니다.
           # 그래서 사용이 끝났으면 반드시 close() 로 닫습니다. 

■ Q-400. 위의 중앙일보 기사에서 빅데이터 라는 단어가 몇번 나오는지
            count 하시오 ! 

f = open('c:\\data\mydata3.txt', encoding='UTF8')
data = f.read() # 파일을 한번에 전부 읽어오는 함수 입니다. 
print( data.count('빅데이터') )  # 11번 
f.close() 


■ Q-401.  위의 스티븐 잡스 연설문 데이터를 모두 읽어 오시오 !
             ( readline() 함수를 이용하세요 ~ )

f = open("c:\\data\\jobs.txt", encoding='UTF8' )
data = f.readline() # while 문이 실행될 수 있도록 마중물 역활을 한다.
while  data:  # data 변수안에 data 가 있으면 True 없으면 False 입니다. 
    print ( data  )
    data = f.readline() # 그 다음줄을 읽어서 data 변수에 입력합니다.
f.close() 
            

■ Q-402.  위에서 한줄씩 읽은 데이터에서 인공지능이라는 단어가 나오면 
             count 하게 하시오 !

f = open("c:\\data\\mydata3.txt", encoding='UTF8' )
data = f.readline() # while 문이 실행될 수 있도록 마중물 역활을 한다.
while  data:  # data 변수안에 data 가 있으면 True 없으면 False 입니다. 
    print ( data.count('인공지능') ) 
    data = f.readline() #           그 다음줄을 읽어서 data 변수에 입력합니다.
f.close() 

■ Q-403. 위의 count 한 건수를 다 누적시켜서 출력하시오 !

f = open("c:\\data\\mydata3.txt", encoding='UTF8' )
data = f.readline() # while 문이 실행될 수 있도록 마중물 역활을 한다.
cnt = 0 
while  data:  # data 변수안에 data 가 있으면 True 없으면 False 입니다. 
    cnt = cnt + data.count('인공지능')        
    data = f.readline() # 그 다음줄을 읽어서 data 변수에 입력합니다.
print (cnt)   # 24 
f.close() 

■ Q-404. 위의 코드를 수정해서 단어를 물어보게하고 단어를 입력하면
            해당 단어가 몇건 나오는지 출력되게하시오 !

단어를 입력하세요 ~   인공지능

결과 :  이 기사에서 인공지능 단어는 24번 나왔습니다. 

word = input('단어를 입력하세요 ~ ') 

f = open("c:\\data\\mydata3.txt", encoding='UTF8' )
data = f.readline() # while 문이 실행될 수 있도록 마중물 역활을 한다.
cnt = 0 
while  data:  # data 변수안에 data 가 있으면 True 없으면 False 입니다. 
    cnt = cnt + data.count(word)        
    data = f.readline() # 그 다음줄을 읽어서 data 변수에 입력합니다.
print ('이 기사에서 ', word, ' 단어는 ', cnt, '번 나왔습니다.' )  
f.close() 


■ Q-405.  아래의 파란색 공과 빨간색 공이 들어있는 박스에서 
             5개의 공을 뽑았을때 그중 2개가 파란색 공일 확률을 출력하는
            함수를 만들고 공을 뽑는 횟수를 10, 100, 1000, 10000, 100000
             했을때의 확률을 map 함수를 이용해서 출력하시오 !
             (점심시간 문제)

a = [ 10, 100, 1000, 10000,100000 ]  

파란색 공 : 24개  +   빨간색 공 : 26개   ---> 총 50개의 공을 박스에 넣으세요


■ Q-406. 아래의 리스트를 mydata9.txt 로 저장하시오 !

listdata2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
result = sorted( listdata2 )  
print (result)                                                                         # [ 1, 2, 2, 3, 5, 7, 8 ]
f = open("c:\\data\\mydata9.txt", "w") 
f.write( str(result) ) 
f.close()               

* writelines 예제:

data = []                        # data 라는 비어있는 리스트 생성 
while  True:                               # 무한 루프를 수행합니다. 
    text = input( '저장할 내용을 입력하세요 ')
    if  text =='':                       # text 에 아무것도 입력하지 않으면 
        break                             # break 문을 실행해서 무한루프를 종료합니다. 
    data.append( text + '\n' )  # text 가 엔터와 함께 data 리스트에 append
                                       # 됩니다.
f = open('c:\\data\\mydata99.txt', 'w') # mydata99.txt 를 생성하겠다.
f.writelines(data)  # data 리스트의 내용을 mydata99.txt 에 저장하겠다.
f.close()

설명: open 의 옵션중 w 는 그냥 쓰기 이고, a 는 추가 입니다. 


■ Q-407. 다음과 같이 내용과 링크를 수정하시오 ~ 
  (링크는 아무거나 하세요 ~) 

양건준님은 오늘 점심에 지하식당으로 내려가서 반 친구들과 같이
우육탕을 먹었습니다. 코로나에 대한 걱정도 있었지만 용기내서 
먹었습니다. 우육탕집 식당 홈페이지는 바로가기를 누르세요.  바로가기 


■ Q-408. ecologincalpyramid.html 문서에서 number 클래스에 있는 
            숫자들만 긁어와서 출력하시오 !

from   bs4  import  BeautifulSoup  

f = open("c:\\data\\ecologicalpyramid.html") 
soup = BeautifulSoup( f , "html.parser") 
result = soup.find_all(class_ ="number")  
for  i  in  result:                                 # result 리스트안의 요소를 하나씩 가져옵니다 
    print ( i.get_text()  )

■ Q-409. 위에서 긁어온 숫자들을 a 라는 비어있는 리스트에 저장한후
            a 안의 요소들을 정렬하고 a 리스트 출력하시오 !

from   bs4  import  BeautifulSoup  

f = open("c:\\data\\ecologicalpyramid.html") 
soup = BeautifulSoup( f , "html.parser") 
result = soup.find_all(class_ ="number")  
a = [ ]
for  i  in  result: # result 리스트안의 요소를 하나씩 가져옵니다 
    a.append( int(i.get_text())  )

a.sort()
print (a)

[50, 80, 100, 100, 1000, 2000, 100000, 100000]

■ Q-410.  중앙일보사 홈페이지로 가서 신문기사 하나를 보시오 

  ctl + s 로 기사의 html 문서를 aa77.html 로 c 드라이브 밑에 data 밑에
  저장합니다.

■ Q-411. aa77.html 을 beautifulsoup 모듈의 함수를 쓸 수 있도록 
            파싱하고 파싱된 결과를 출력하세요 ~

from   bs4  import  BeautifulSoup  

f = open("c:\\data\\aa77.html", encoding="UTF8") 
soup = BeautifulSoup( f , "html.parser") 
print (soup)

■ Q-412.  위의 기사의 본문을 가져오기 위해서 기사 본문의 class 이름이
무엇인지 확인하세요 ~

크롬의 개발자 모드 단축키인 F12 를 누르면 옆에 html 코드 창이 나오면서
개발자 모드 화면이 열립니다. 그러면 위쪽에 화살표를 클릭하고 
기사본문을 클릭하면 html 문서에 class 이름을 확인할 수있는 html 문서쪽으로
바로 이동합니다.

■ Q-413.  클래스 이름 article_body mg fs4 로 접근하여 text 를 긁어오시오

from   bs4  import  BeautifulSoup  

f = open("c:\\data\\aa77.html", encoding="UTF8") 
soup = BeautifulSoup( f , "html.parser") 
result = soup.find_all(class_ = 'article_body mg fs4')
for  i  in  result:
    print ( i.get_text() )            

■ Q-414. (오늘의 마지막 문제)  위에서 스크롤링한 중앙일보 기사를
c 드라이브 밑에 mytext23.txt 로 저장하시오 !
 
from bs4 import BeautifulSoup
f = open("c:\\data\\aa77.html", encoding="UTF8")
soup = BeautifulSoup(f,"html.parser")
result = soup.find_all(class_ ='article_body mg fs4')
a=[]
for i in result:
    a.append(i.get_text())
h = open("c:\\data\\mytext23.txt",'w')
h.write(str(a))
h.close()
