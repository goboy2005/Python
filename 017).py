# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 20:12:43 2020

@author: goboy
"""


■ Q-423.  어제 조선일보에서  봉사로 검색했을 때 다운 받았던 기사에서
가장 많이 나오는 단어(어절)가 무엇인가 ?

stev = open("c:\\data\\bongsa.txt", encoding="UTF8")
stev2 = stev.read().split()      # 어절별로 분리해서 리스트에 담는다.
stev2.sort()                    # 리스트안의 요소들을 정렬

from  collections  import  Counter 
count_list = Counter(stev2)      #stev2 리스트안의 어절별로 각각 몇건씩 있는지  정리를 합니다. 
print (count_list)               
result = count_list.most_common(30)  # top 30개만 추출 
print (result)


■ Q-424.  위의 결과를 for loop 문을 이용해서 아래와 같이 출력하시오 !

for i in result:
    print(i[0],i[1])

■ Q-425.  어제 마지막 문제로 스크롤링 했던 영화 평가 게시글들에서
위와 같이 가장 많이 나오는 어절이 무엇인지 출력하시오 !
 ( 다희의 타이타닉)


■ Q-426.  웹스크롤링을 한 데이터로 감정분석(긍정적, 부정적)을 하기 위해
신성이 형의 라라랜드 영화 평가를 다운로드 해서 c 밑에 data 
밑에 두고 가장 많이 나오는 단어가 무엇인지 확인합니다.



■ Q-427.  영화 라라랜드에서 긍정적인 단어가 몇건이 나오는지 출력하시오!


positive = open('c:\\data\\positive-words2.txt', encoding='CP949')
pos = positive.read().split('\n')   # positive 에서 행별로 분리해서 pos 에 담는데 pos 는 리스트 입니다.                                                                               
stev = open('c:\\data\\sample6_laland_review.txt', encoding='UTF8')
stev2 = stev.read().split()  
# stev2 에 입력했는데 stev2 도 리스트이고,stev2 리스트에는 스티븐 잡스 연설문이 어절별로 분리되어 저장되어있다.                                                          
cnt = 0
for i in stev2:               # stev2 에서 단어들을 하나씩 빼옵니다. 
    if i.lower() in pos:       # i의 단어가 pos 긍정단어 리스트에 존재하면 
        cnt += 1                # cnt 를 1씩 증가 시킵니다. 
print(cnt)

■ Q-428. 라라랜드 영화 평가에 부정단어는 몇개가 있고 단어들은 무엇인지
출력하시오 !

negative = open('c:\\data\\negative-words2.txt', encoding='CP949')
neg = negative.read().split('\n')   # positive 에서 행별로 분리해서 pos 에 담는데 pos 는 리스트 입니다.                                                                               
stev = open('c:\\data\\sample6_laland_review.txt', encoding='UTF8')
stev2 = stev.read().split()  
# stev2 에 입력했는데 stev2 도 리스트이고,stev2 리스트에는 스티븐 잡스 연설문이 어절별로 분리되어 저장되어있다.                                                          
cnt = 0
for i in stev2:               # stev2 에서 단어들을 하나씩 빼옵니다. 
    if i.lower() in neg:       # i의 단어가 neg 부정단어 리스트에 존재하면 
        cnt += 1                 # cnt 를 1씩 증가 시킵니다. 
print(cnt)


■ 예제.  영화 라라랜드의 평가글들을 파이썬에서 워드 클라우드 그리기 

1. 아나콘다 프롬프트 창을 열고  wordcloud 패키지 설치

conda  install  wordcloud
 
또는 

pip  install   wordcloud

성공적으로 설치되면 아래의 메세지가 뜹니다. 

Successfully installed wordcloud-1.8.1

2. c 드라이브 밑에 project 폴더를 생성 


3. project 폴더 밑에  4가지 파일을 둡니다.

   -  usa_im.png
   -  s_korea.png
   -  word.txt
   -  중앙일보 스크롤링했던 기사 파일 my_text21.txt 

# 텍스트마이닝 데이터 정제

from wordcloud import WordCloud, STOPWORDS # 구두점 데이터 정제
import matplotlib.pyplot as plt  # 그래프 그리는 모듈
from os import path     #  os 에 있는 파일을 파이썬에서 인식하기 위해서
import re   #  데이터 정제를 위해서 필요한 모듈 
import numpy as np  
from PIL import Image  # 이미지 시각화를 위한 모듈 

# 워드 클라우드의 배경이 되는 이미지 모양을 결정
usa_mask = np.array(Image.open("c:\\project\\usa_im.png"))

# 워드 클라우드를 그릴 스크립트 이름을 물어봅니다. 
script = 'sample6_laland_review.txt'

# 워드 클라우드 그림이 저장될 작업 디렉토리를 설정 
d = path.dirname("c:\\project\\")

# 기사 스크립트와 os 의 위치를 연결하여 utf8로 인코딩해서 한글 텍스트를
# text 변수로 리턴한다.
text = open(path.join(d, "%s"%script), mode="r", encoding="utf-8").read()
print(text)

# 파이썬이 인식할 수 있는 한글 단어의 갯수를 늘리기 위한 작업 
file = open('c:/project/word.txt', 'r', encoding = 'utf-8')
word = file.read().split(' ')   # 어절별로 분리해서 word 에 담아 리스트로 구성한다. 
for i in word:
    text = re.sub(i,'',text)  #  re.sub('있다', '', '있다')  # <-- 라라랜드 게시글의 있다를 '' 으로
                                                                  # 으로 대체하겠다. 
# 설명: 일반적인 문장에서 자주 나오는 단어들을 전부  '' 로 아래와 같이 대체하려고 하는데
# 아래 처럼 일일히 다 써주면 너무 코딩이 많으니까 for 문을 이용해서 쉽게 한다. 
#re.sub('있다', '', '있다')
#re.sub('하지만', '', '하지만')  
 
# 워드 클라우드를 그린다. 
wordcloud = WordCloud(font_path='C://Windows//Fonts//gulim', # 글씨체
                      stopwords=STOPWORDS,   # 마침표, 느낌표,싱글 쿼테이션 등을 정제
                      max_words=1000, # 워드 클라우드에 그릴 최대 단어갯수
                      background_color='white', # 배경색깔
                      max_font_size = 100, # 최대 글씨 크기 
                      min_font_size = 1, # 최소 글씨 
                      mask = usa_mask, # 배경 모양 
                      colormap='jet').generate(text).to_file('c:\\project\\lala_cloud.png')
                  # c 드라이브 밑에 project 폴더 밑에 생성되는 워드 클라우드 이미지 이름
  
plt.figure(figsize=(15,15))  # 가로 15, 세로 15 사이즈 
plt.imshow(wordcloud, interpolation='bilinear')  # 글씨가 퍼지는 스타일 
plt.axis("off")  # 축표시 없음


■ Q-430. (점심시간 문제)  어제 마지막 문제로 받았던 영화 평가들 또는
어제 스크롤링했던 기사들을 하나 선택해서 워드 클라우드로 
그리고 그림을 올리고 검사받으세요 

 데이터 분석가 하는일 ?  웹스크롤링 ----->  시각화 (워드 클라우드)
                                                                                    감정분석 

  비정형 데이터를 활용  기업 : 기업의 의사결정의 도움을 주기위해서
                                             정부 :  현 사회현상 파악 

■ Q-431. 신성이가 받은 라라랜드 평가 게시글에서  평가 점수만 출력하시오

sample6_laland_review.txt

stev = open("c:\\data\\sample6_laland_review.txt", encoding="UTF8")
stev2 = stev.readlines()

for  i  in  stev2:
    print( int(i[6:8]) ) 

■ Q-432. 라라랜드 평가글중에 평점이 6점이상인 글들만 출력하시오 !

stev = open("c:\\data\\sample6_laland_review.txt", encoding="UTF8")
stev2 = stev.readlines()

for  i  in  stev2:
    if int(i[6:8]) >= 6:
        print ( i , end="" )

■ Q-433.  라라랜드 평가글중에 평점이 6점 이상이면 pos 라는 비어있는
리스트에 해당 평가글을 append 되게하고 6점 미만이면
nag 라는 비어있는 리스트에 평가글이 append 되게하시오 !

stev = open("c:\\data\\sample6_laland_review.txt", encoding="UTF8")
stev2 = stev.readlines()
pos =[]
nag =[] 
for  i  in  stev2:
    if int(i[6:8]) >= 6:
        pos.append( i[8:] )
    else:
        nag.append( i[8:] )
print (pos)

■ Q-434. 위의 pos 에 들어있는 긍정글들을 c 드라이브 밑에 project 밑에
pos_lala.txt 로 저장하시오 !

stev = open("c:\\data\\sample6_laland_review.txt", encoding="UTF8")
stev2 = stev.readlines()
pos =[]
nag =[] 
for  i  in  stev2:
    if int(i[6:8]) >= 6:
        pos.append( i[8:] )
    else:
        nag.append( i[8:] )

f = open("c:\\project\\pos_lala.txt", "w")
f.writelines(pos)
f.close()

■ Q-435.  6점 미만인 글들은 nag_lala.txt 로 c 드라이브 밑에 project 밑에
저장되게하시오 !

stev = open("c:\\data\\sample6_laland_review.txt", encoding="UTF8")
stev2 = stev.readlines()
pos =[]
nag =[] 
for  i  in  stev2:
    if int(i[6:8]) >= 6:
        pos.append( i[8:] )
    else:
        nag.append( i[8:] )

f = open("c:\\project\\pos_lala.txt", "w")
f.writelines(pos)
f.close()
f2 = open(c:\\project\\nag_lala.txt", "w")
f2.writelines(nag)
f2.close()

■ 145.  네이버 영화 평점을 긍정과 부정으로 분류해서 게시글 시각화 하기

  지금 우리회사 게시판에 올라온 신제품(화장품)에 대한 반응을
  긍정적인 반응과 부정적인 반응을 조사해서 보고해라  같은 일을 시킬경우 활용

■ Q-431. 신성이가 받은 라라랜드 평가 게시글에서  평가 점수만 출력하시오

sample6_laland_review.txt

stev = open("c:\\data\\sample6_laland_review.txt", encoding="UTF8")
stev2 = stev.readlines()

for  i  in  stev2:
    print( int(i[6:8]) ) 

■ Q-432. 라라랜드 평가글중에 평점이 6점이상인 글들만 출력하시오 !

stev = open("c:\\data\\sample6_laland_review.txt", encoding="UTF8")
stev2 = stev.readlines()

for  i  in  stev2:
    if int(i[6:8]) >= 6:
        print ( i , end="" ) 

■ Q-433.  라라랜드 평가글중에 평점이 6점 이상이면 pos 라는 비어있는
리스트에 해당 평가글을 append 되게하고 6점 미만이면
nag 라는 비어있는 리스트에 평가글이 append 되게하시오 !

stev = open("c:\\data\\sample6_laland_review.txt", encoding="UTF8")
stev2 = stev.readlines()
pos =[]
neg =[] 
for  i  in  stev2:
    if int(i[6:8]) >= 6:
        pos.append( i[8:] )
    else:
        neg.append( i[8:] )
print (pos)

■ Q-434. 위의 pos 에 들어있는 긍정글들을 c 드라이브 밑에 project 밑에
pos_lala.txt 로 저장하시오 !

stev = open("c:\\data\\sample6_laland_review.txt", encoding="UTF8")
stev2 = stev.readlines()
pos =[]
nag =[] 
for  i  in  stev2:
    if int(i[6:8]) >= 6:
        pos.append( i[8:] )
    else:
        nag.append( i[8:] )

f = open("c:\\project\\pos_lala.txt", "w")
f.writelines(pos)
f.close()

■ Q-435.  6점 미만인 글들은 nag_lala.txt 로 c 드라이브 밑에 project 밑에
저장되게하시오 !

stev = open("c:\\data\\sample6_laland_review.txt", encoding="UTF8")
stev2 = stev.readlines()
pos =[]
neg =[] 
for  i  in  stev2:
    if int(i[6:8]) >= 6:
        pos.append( i[8:] )
    else:
        nag.append( i[8:] )

f = open("c:\\project\\pos_lala.txt", "w")
f.writelines(pos)
f.close()
f2 = open(c:\\project\\neg_lala.txt", "w")
f2.writelines(neg)
f2.close()

■ Q-436.  그러면 위의 pos_lala_txt 의 글과 nag_lala.txt 의 글을 
워드 클라우드로 각각 시각화 하시오 !

from wordcloud import WordCloud, STOPWORDS # 구두점 데이터 정제
import matplotlib.pyplot as plt                                   # 그래프 그리는 모듈
from os import path                   #  os 에 있는 파일을 파이썬에서 인식하기 위해서
import re                                      #  데이터 정제를 위해서 필요한 모듈 
import numpy as np  
from PIL import Image               # 이미지 시각화를 위한 모듈 


usa_mask = np.array(Image.open("c:\\project\\usa_im.png"))
# 워드 클라우드의 배경이 되는 이미지 모양을 결정

script = 'pos_lala.txt'    # 워드 클라우드를 그릴 스크립트 이름을 물어봅니다. 
d = path.dirname("c:\\project\\")  # 워드 클라우드 그림이 저장될 작업 디렉토리를 설정 

text = open(path.join(d, "%s"%script), mode="r",encoding="CP949", errors='ignore' ).read()
file = open('c:/project/word.txt', 'r', encoding = 'utf-8')
# 기사 스크립트와 os 의 위치를 연결하여 utf8로 인코딩해서 한글 텍스트를 text 변수로 리턴한다.

word = file.read().split(' ')    # 어절별로 분리해서 word 에 담아 리스트로 구성한다. 
for i in word:
    text = re.sub(i,'',text)      # re.sub('있다', '', '있다')
    
        
# 워드 클라우드를 그린다. 
wordcloud = WordCloud(font_path='C://Windows//Fonts//gulim', # 글씨체
                      stopwords=STOPWORDS,      # 마침표, 느낌표,싱글 쿼테이션 등을 정제
                      max_words=1000,                   # 워드 클라우드에 그릴 최대 단어갯수
                      background_color='white',    # 배경색깔
                      max_font_size = 100,           # 최대 글씨 크기 
                      min_font_size = 1,              # 최소 글씨 
                      mask = usa_mask,              # 배경 모양 
                      colormap='jet').generate(text).to_file('c:\\project\\lala_cloud.png')
                    # c 드라이브 밑에 project 폴더 밑에 생성되는 워드 클라우드 이미지 이름
  
plt.figure(figsize=(15,15))                                           # 가로 15, 세로 15 사이즈 
plt.imshow(wordcloud, interpolation='bilinear')   # 글씨가 퍼지는 스타일 
plt.axis("off")                                          # 축표시 없음
    
■ Q-437. 평점 좋은 영화 제목만 뽑아 보는거 어떠세요?

  주원이 cinema1.txt


 * 빅데이터 기사 문제:  데이터의 구조적 관점에서 3가지로 나뉜다.(P1-4)
       
      1. 정형 데이터 : 정형화된 스키마 구조. DBMS 에 저장될 수 있는 구조
                             예: Oracle 의 emp 테이블, MySQL, MSSQL 의 테이블 

       2. 반정형 데이터: 데이터 내부의 데이터 구조에 대한 메타정보가 포함된 구조의 데이터
                                   예: html 문서, xml 문서                       

       3. 비정형 데이터 : 웹스크롤링 기술로 수집해서 모은 데이터 
                                    예:  텍스트 문서, 이미지, 동영상

■  146. 웹에 있는 사진을 스크롤링 하는 방법 (구글 이미지)

 딥러닝 기술 ?  1. cnn : 인공지능의 눈
                             예: 관련된 학습 빅데이터 ?  이미지 

                          2. rnn :  인공지능의 입과 귀
                             예: 관련된 학습 빅데이터 ?  자연어 처리를 위한 문장들

 셀레니움 써서 마치 손으로 클릭해서 이미지를 저장하듯이 저장을 하는데
 컴퓨터를 시켜서 자동화 시키는 방법으로 스크롤링을 합니다.

			 < 구글에서 이미지 스크롤링 하기  >

Step 1.  크롬 웹브라우져가 설치 되어져 있어야 합니다.

Step 2.  c 드라이브 밑에 chromedriver 폴더를 생성하고 거기에 
                                              chromedriver.exe 를 넣어야 합니다. 

Step 3.  c 드라이브 밑에 gimages 폴더를 생성합니다.

Step 4.  다운받을 이미지 키워드를 결정합니다.  '햄버거' 

Step 5.  아나콘다 프롬프트 창을 열고 selenium 을 설치합니다.

  conda  install  selenium 

  conda  list  selenium  

  또는 

  pip  install  selenium 

Step 6. 구글에서 햄버거로 검색했을때 웹스크롤링 코드 

import urllib.request    # 웹 url을 파이썬이 인식 할 수 있게하는 패키지
from  bs4 import BeautulSoup  # html에서 데이터 검색을 용이하게 하는 패키지

from selenium import webdrivifer  
# selenium : 웹 애플리케이션의 테스트를 자동화하기 위한 프레임 워크 

from selenium.webdriver.common.keys import Keys
#손으로 클릭하는것을  컴퓨터가 대신하면서 스크롤링하게 하는 패키지

import time       # 중간중간 sleep 을 걸어야 해서 time 모듈 import

                                                             url 받아오기 

binary = 'C:\chromedriver/chromedriver.exe'
# 웹브라우져로 크롬을 사용할거라서 크롬 드라이버를 다운받아 아래 파일경로의 위치에 둔다
# 팬텀 js로 하면 백그라운드로 실행할 수 있음

browser = webdriver.Chrome(binary)
# 브라우져를 인스턴스화

browser.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ei=l1AdWbegOcra8QXvtr-4Cw&ved=0EKouCBUoAQ")
# 구글의 이미지 검색 url 받아옴(아무것도 안 쳤을때의 url) 

# 구글의 이미지 검색에 해당하는 input 창의 id 가 '  ?  ' 임(검색창에 해당하는 html코드를 찾아서 elem 사용하도록 설정)
# input창 찾는 방법은 원노트에 있음

# elem = browser.find_elements_by_class_name('gLFyf gsfi')  # Tip : f12누른후 커서를 검색창에 올려두고 id를 찾으면 best

elem = browser.find_element_by_xpath("//*[@class='gLFyf gsfi']")  # 위의 코드대로 하거나 이렇게 하거나 둘 중 하나 select


                                                                검색어 입력 

elem.send_keys("햄버거")  # 여기에 스크롤링하고싶은 검색어를 입력, # elem 이 input 창과 연결되어 스스로 햄버거를 검색

elem.submit()                # 웹에서의 submit 은 엔터의 역할을 함


                                        반복할 횟수


* 스크롤을 내리려면 브라우져 이미지 검색결과 부분(바디부분)에 마우스 클릭 한번 하고 End키를 눌러야함

for i in range(1, 6):      # 5번 스크롤 내려가게 구현된 상태 range(1,5)
    browser.find_element_by_xpath("//body").send_keys(Keys.END)  #키보드 end키를 총 5번 누르는데 end1번누르고 10초 쉼
    time.sleep(10)          # END 키 누르고 내려가는데 시간이 걸려서 sleep 해줌 
                        
time.sleep(10)                           # 네트워크 느릴까봐 안정성 위해 sleep 해줌(이거 안하면 하얀색 이미지가 다운받아질 수 있음.)
html = browser.page_source     # 크롬브라우져에서 현재 불러온 소스 가져옴
soup = BeautifulSoup(html, "lxml") # html 코드를 검색할 수 있도록 설정

browser.find_element_by_xpath("//*[@class='mye4qd']").click()     # 여기가 결과 더보기 코드입니다


for i in range(1, 5):                   # 4번 스크롤 내려가게 구현된 상태 range(1,5)
    browser.find_element_by_xpath("//body").send_keys(Keys.END)    # body 에다가 두고 ,키보드 end키를 총 5번 누른다
    time.sleep(10)       

time.sleep(10)                                 # 네트워크 느릴까봐 안정성 위해 sleep 해줌(안하면 하얀색 이미지가 다운받아질 수 있음.)
html = browser.page_source                 # 크롬브라우져에서 현재 불러온 소스 가져옴
soup = BeautifulSoup(html, "lxml")    # html 코드를 검색할 수 있도록 설정


                                              그림파일 저장 

*검색한 구글 이미지의 url을 따오는 코드 

def fetch_list_url():
    params = []
    imgList = soup.find_all("img", class_="rg_i Q4LuWd")  # 구글 이미지 url 이 있는 img 태그/ _img 클래스에 가서 (f12로 확인가능.)
    for im in imgList:
        try :
            params.append(im["src"])                       # params 리스트에 image url 을 담음.
        except KeyError:
            params.append(im["data-src"])         # 이미지의 상세 url 의 값이 있는 src 가 없을 경우,  data-src 로 가져오시오
 

*검색한 구글 이미지를 Detail 함수로 만들어 저장하는 코드

def fetch_detail_url():
    params = fetch_list_url()

    for idx,p in enumerate(params,1):   
        urllib.request.urlretrieve(p, "C:/gimages/" + str(idx) + "_google.jpg")
# 다운받을 폴더경로 입력
# enumerate 는 리스트의 모든 요소를 인덱스와 쌍으로 추출 하는 함수 , 숫자 1은 인덱스를 1부터 시작해라 

fetch_detail_url()        #Detail 함수불러오기
browser.quit()            # 끝나면 브라우져 닫기


■ Q-438.  c 드라이브 밑에 gimages2 라는 폴더를 만들고 거기에  
다른 이미지를 다운로드 받으세요 ~

딥러닝으로 인공지능을 학습시키려면  한 클래스당 2000장 정도가 있으면
적당합니다. 

 개와 고양이를 알아보는 인공지능을 만들고 싶으면 ?

 개 2000 장
 고양이 2000장 

■ 147. 이미지 스크롤링 하기 ( 네이버 이미지 검색, 앞전엔 Google) 

import  urllib.request                                      # 웹 url 을 파이썬이 인식할 수 있게 하는 패키지 
from  bs4  import  BeautifulSoup                  # html 코드에서 원하는 지점을 빨리 찾을 수 있게 만든 모듈
from selenium import webdriver                  # 손으로 클릭하는것을 컴퓨터가 하겠금 하는 모듈
from selenium.webdriver.common.keys import Keys 

import time                                                                    # 중간중간 sleep 을 주려고 불러오는 모듈 

binary = 'C:\\chromedriver\\chromedriver.exe'       # 크롬 드라이버 위치 지정 

browser = webdriver.Chrome(binary)                            # browser 객체 생성 

browser.get("https://search.naver.com/search.naver?where=image&amp;sm=stb_nmr&amp;")

elem = browser.find_element_by_id("nx_query")           # 검색창 지점을 알아내서 elem 에 담는다
     #=find_elements_by_class_name("")  ( 클래스 이름으로 찾을때 필요한 코드)

                                                         검색어 입력

elem.send_keys("아이언맨")       # 컴퓨터가 아이언맨 글씨를 직접 적는다.
elem.submit()                                    # 그리고 엔터를 친다.

                                                            
                                     반복할 횟수

for i in range(1,5):             
    browser.find_element_by_xpath("//body").send_keys(Keys.END) #  end 키를 누루면서 아래로 내리는데 
    time.sleep(5)                                                              # 슬립을 5초 주면서 5번 수행한다. 

time.sleep(5)                   # 5초 멈췄다가 

html = browser.page_source                 # 현 페이지의 html 코드를 불러와서 
soup = BeautifulSoup(html,"lxml")           # BeautifulSoup을 이용할 수 있도록 파싱 한다. 


*  이미지의 상세 url 가져오는 함수 

def fetch_list_url():   
    params = []
    imgList = soup.find_all("img", class_="_img")  # img 테그의 클래스 이름 _img 로 접근
    for im in imgList:
        params.append(im["src"])                    # src 의 값을 가져와서 params 에 append 합니다. 
    return params


 *  상세 이미지 url 가져와서 이미지 다운로드하는 함수

def  fetch_detail_url():                    
    params = fetch_list_url()
    #print(params)
    a = 1 
    for p in params:
        urllib.request.urlretrieve(p, "c:/naver/"+ str(a) + ".jpg" )  # 다운받을 폴더경로 입력 
        a = a + 1                                                        # 숫자가 증가하면서 저장이 된다

fetch_detail_url()

browser.quit()

■ Q-439. (오늘의 마지막 문제)  마이크로 소프트 회사에서 만든 
검색 페이지인 bing 에서 이미지 검색을 할 수 있도록 하는
웹스크롤링 코드를 작성하시오 ! 

import urllib.request 
from bs4 import BeautifulSoup      # html 코드에서 원하는 지점을 빠르게 찾을 수 있도록 만든 모듈
from selenium import webdriver   # 손으로 클릭하는 것을 컴퓨터가 하게 만드는 모듈
from selenium.webdriver.common.keys import Keys
import time                                        # 완벽한 이미지 수집위해 중간 중간 sleep으로 로딩시간 확보

binary = 'E:\chromedriver/chromedriver.exe'      # chromedriver 위치 명시

browser = webdriver.Chrome(binary)                    # browser 객체 생성

browser.get("https://www.bing.com/?scope=images&nr=1&FORM=NOFORM")
# bing 의 이미지 검색창에 아무것도 입력하지 않은 상태의 url

elem = browser.find_element_by_id("sb_form_q") 
# 위의 url에서 검색어를 입력하는 창의 위치를 elem에 할당 F12사용

elem.send_keys("harry potter") # 컴퓨터가 위에서 지정한 elem의 위치에 'harry potter' 이라는 글씨를 직접 타이핑

elem.submit() # 검색창에 입력후 엔터키 입력

# bing은 왜인지 모르겠으나 이미지 창에서 검색후 엔터를 치면 종합검색 창으로 넘어감
# 파이썬 코드사용없이 똑같은 url에서 손으로 직접 키워드 입력후 엔터치면 이미지 검색으로 넘어감
#원인을 모르겠음.

# ⬇⬇⬇ 그래서 종합검색페이지로 넘어간 후에 이미지텝을 마우스가 클릭하도록 하는 함수 작성 ⬇⬇⬇

browser.find_element_by_id("b-scopeListItem-images").click() 
# 키워드에 대한 전체검색결과 출력된 페이지에서 '이미지' 부분을 클릭하는 함수


* 반복할 횟수 end 키를 1번씩 누르면서 내리는 작업반복

for i in range(1,16): # 사진 개수 최대한 늘려보려고 넓게 잡음
browser.find_element_by_xpath("//body").send_keys(Keys.END)
time.sleep(5)

time.sleep(5) # 1번 end 눌러서 내려온뒤에 5초 sleep

html = browser.page_source           # 현페이지의 html 코드를 불러와서
soup = BeautifulSoup(html,"lxml") # BeautifulSoup 을 이용할 수 있도록 파싱!

#print(soup)            # 중간 절차 확인차 출력해본 것
#print(len(soup))

def fetch_list_url(): # 이미지의 상세 url 가져오는 함수 생성
params = []
imgList = soup.find_all("img", class_="mimg") # img 테그의 class 이름 _img 로 접근해서
for im in imgList:
params.append(im["src"]) #src 의 값(=각 이미지의 url) 을 가져와서 params 에 append
return params

def fetch_detail_url():   # 상세 이미지 url 가져와서 그 이지미를 다운로드하는 함수
params = fetch_list_url()
#print(params)
a = 1
for p in params:
# 다운받을 폴더경로 입력
urllib.request.urlretrieve(p, "C:/bingImages/"+ str(a) + ".jpg" ) # E 드라이브 밑에 bingImages 라는 폴더를 만들어서 저장

a = a + 1

fetch_detail_url() 

browser.quit()
