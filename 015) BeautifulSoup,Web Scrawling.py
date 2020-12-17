# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 22:03:53 2020

@author: goboy
"""

■ 142. 웹스크롤링 실전 1단계 (ebs 레이디 버그 게시판)

 우리회사의 신제품이 출시 되었을때 그 제품에 대한 사람들의 반응을
 데이터 분석을 하고자 할때 웹스크롤링 + 데이터 시각화를 이용하면
  됩니다. 

■ 예1. ebs 레이디버그 시청자 게시판의 url 을 가지고 직접 html 문서를
내려 받을 수 있도록 코드를 구현 ( 어제는 우리가 ctl + s 를 누르고 웹페이지를 우리 피씨에 저장하고
구현을 했는데 오늘은 그렇게 하지 않고 웹에서 바로 html 문서를
           내려 받을 수 있도록 구현 )

from  bs4  import  BeautifulSoup
import  urllib.request   # 웹상의 url 을 파이썬이 인식할 수 있도록 해주는
                              # 모듈


list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url = urllib.request.Request(list_url) #  사람이 알아볼 수 있는 위의 url 을 파이썬이 알아
                                              # 볼 수 있도록 변환 첫번째 작업
result = urllib.request.urlopen(url).read().decode("utf-8") 
                      # 위의 url 의 html 문서들을 result 변수에 담았다. 
print (result)  #  위의 url 의 html 전체 문서가 다 출력되고 있음.

■ 예제2.  위에서 긁어온 html 코드를 Beautiful soup 의 함수를 이용해서
웹스크롤링을 할 수 있도록 Beautiful soup 을 쓸수 있게 파싱하시오

from  bs4  import  BeautifulSoup
import  urllib.request   # 웹상의 url 을 파이썬이 인식할 수 있도록 해주는
                              # 모듈

list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url = urllib.request.Request(list_url) #  사람이 알아볼 수 있는 위의 url 을 파이썬이 알아
                                              # 볼 수 있도록 변환 첫번째 작업
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")
print (soup)                  

■ 예제3.  지금 페이지의 시청자 게시판의 글 내용에 해당하는 부분의 테그와 클래스 이름을
          알아내시오 

< p class_ = "con" >  재미있다  < /p> 

■ 예제4.  p 테그중에 class 가 con 에 해당하는 부분을 스크롤링 하시오 !

앞의 코드들  ....
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")
result2 = soup.find_all( 'p',  class_ ='con') 
print (result2) 

설명:  find 함수는 맨 처음 하나만 가져오는데 find_all 은 p 테그에 class 이름 con 에 
        해당하는 부분을 모두 가져온다. 

■ 예제5. 위의  결과에서 html 문서 말고  한글 텍스트만 가져오시오 !
( 위의 result2 는 리스트 입니다.) 

앞의 코드들 ...
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")
result2 = soup.find_all( 'p',  class_ ='con') 
for  i  in  result2:
    print ( i.get_text() ) 

■ 예제6. 위에서 출력되고 있는 텍스트들이 좀더 깔끔하게 나오게 하시오 !

result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")
result2 = soup.find_all( 'p',  class_ ='con') 
for  i  in  result2:
    print ( i.get_text("  ", strip=True) ) 

■ 예제7. 위에서 출력되고 있는 텍스트들이  params 라는 비어있는 리스트에 
담기게 하시오 !

앞의 코드들 ...
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")
result2 = soup.find_all( 'p',  class_ ='con') 
params = []
for  i  in  result2:
    params.append( i.get_text("  ", strip=True) )
print(params) 

■ 예제8. 게시글을 올린 날짜를 스크롤링하기 위해서 게시글 날짜가 있는 html 문서의
테그 이름과 클래스 이름을 확인하시오 !

테그와 클래스를 확인하는 법은 F12 누르고 개발자 모드열고 화살표 누르면 알수있다. 

■ 예제9.  기존 코드에 위의 날짜를 스크롤링하는 코드를 추가하고 
위의 날짜를 모두 스크롤링해서 params2 라는 리스트에 담으시오 ~

# 1. 웹에서 html 문서를 가져와 beautifulsoup 으로 파싱 
from  bs4  import  BeautifulSoup
import  urllib.request   # 웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈
                    
list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url = urllib.request.Request(list_url) #  사람이 알아볼 수 있는 위의 url 을 파이썬이 알아
                                                              # 볼 수 있도록 변환 첫번째 작업
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")

# 2. 시청자 게시판의 날짜와 본문 내용을 가져옵니다.
result1 = soup.find_all( 'span', class_ ='date')
result2 = soup.find_all( 'p',  class_ ='con') 
 
# 3. 시청자 게시판의 날짜와 본문을 params1 와 params2 리스트에 담습니다.
params1 = []
params2 = [] 
for  i  in  result1:
    params1.append( i.get_text("  ", strip=True) )
for  i  in  result2:
    params2.append( i.get_text("  ", strip=True) )
print ( params1)
print ( params2)

■ 예제10.  위의 날짜와 본문 내용이 아래와 같이 출력되게하시오 ! ( zip 과  +  를 이용하시면 됩니다.)
2020.12.11 19:52   재미있 다           
2020.12.11 19:06   어제 흐름상 종영 같지 않았는데 갑자기 끝이네요??

앞의 코드들 .....
for  i  in  result2:
    params2.append( i.get_text("  ", strip=True) )

for   k,  h   in   zip(  params1,  params2 ):
    print ( k + '   '  + h ) 

전체코드:

# 1. 웹에서 html 문서를 가져와 beautifulsoup 으로 파싱 
from  bs4  import  BeautifulSoup
import  urllib.request   # 웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈
                    
list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url = urllib.request.Request(list_url)         # 사람이 알아볼 수 있는 위의 url 을 파이썬이 알아
                                                                 #  볼 수 있도록 변환 첫번째 작업
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")

# 2. 시청자 게시판의 날짜와 본문 내용을 가져옵니다.
result1 = soup.find_all( 'span', class_ ='date')
result2 = soup.find_all( 'p',  class_ ='con') 
 
# 3. 시청자 게시판의 날짜와 본문을 params 와 params2 리스트에 담습니다.
params1 = []
params2 = [] 
for  i  in  result1:
    params1.append( i.get_text("  ", strip=True) )
for  i  in  result2:
    params2.append( i.get_text("  ", strip=True) )
    
# 4. 날짜와 본문을 같이 출력 합니다.     
for   k,  h   in   zip(  params1,  params2 ):
    print ( k + '   '  + h ) 

■ 예제12. 아래의 결과를 출력하는데 페이지 번호가 1번 부터 22번까지 변경되어서 
출력되게하시오  

for  i  in  range(1, 23):
    print ( 'http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=' +str(i) + '&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&')

■ 예제13.  예제12번 코드를 예제10번 코드에 적용해서 레이디 버그 전체 게시판의 글들이 날짜함께 출력되게하시오 

1. 예제10번 코드를 가져옵니다. 

2. 예제10번 코드에서 url 의 페이지 번호가 1번부터 22번까지 변경되면서 날짜와 게시글을 
   가져올 수  있도록 코드를 수정하시오 !

# 1. 웹에서 html 문서를 가져와 beautifulsoup 으로 파싱 
from  bs4  import  BeautifulSoup
import  urllib.request   # 웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈
                    
for  i  in  range(1, 23):
    list_url = 'http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=' +str(i) + '&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&'
    
    url = urllib.request.Request(list_url) #  사람이 알아볼 수 있는 위의 url 을 파이썬이 알아
                                                  # 볼 수 있도록 변환 첫번째 작업
    result = urllib.request.urlopen(url).read().decode("utf-8") 
    soup = BeautifulSoup( result, "html.parser")
    
    # 2. 시청자 게시판의 날짜와 본문 내용을 가져옵니다.
    result1 = soup.find_all( 'span', class_ ='date')
    result2 = soup.find_all( 'p',  class_ ='con') 
     
    # 3. 시청자 게시판의 날짜와 본문을 params 와 params2 리스트에 담습니다.
    params1 = []
    params2 = [] 
    for  i  in  result1:
        params1.append( i.get_text("  ", strip=True) )
    for  i  in  result2:
        params2.append( i.get_text("  ", strip=True) )
        
    # 4. 날짜와 본문을 같이 출력 합니다.     
    for   k,  h   in   zip(  params1,  params2 ):
        print ( k + '   '  + h ) 

설명:  위의 params1 과 params2  리스트가 for  문 안쪽에 있기 때문에 
        페이지 번호가 돌때 마다 params 리스트 안의 내용이 새로운 날짜와 내용으로
        변경되게 됩니다. 

■ 예제14. params1 과 params2 에 레이디 버그 시청자 게시판의 모든 게시날짜와 본문
 내용이 들어가게 코드를 수정하시오 !

# 0.  웹스크롤링에 필요한 모듈을 임폴트 합니다. 
from  bs4  import  BeautifulSoup
import  urllib.request   # 웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈

# 1. 레이디 버그 게시판 게시날짜와 게시글 전체를 다 담은 리스트 2개를 만듭니다. 
params1 = []  # 게시날짜를 담을 것이고
params2 = []  # 게시본문을 담을것입니다.

for  i  in  range(1, 23):     # 페이지 번호를 1번부터 22번까지 변경하려고 for 을 사용 
    list_url = 'http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=' +str(i) + '&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&'
    
    url = urllib.request.Request(list_url) #  사람이 알아볼 수 있는 위의 url 을 파이썬이 알아
                                                  # 볼 수 있도록 변환 첫번째 작업
    result = urllib.request.urlopen(url).read().decode("utf-8") 
    soup = BeautifulSoup( result, "html.parser")
    
    # 3. 시청자 게시판의 날짜와 본문 내용을 가져옵니다.
    result1 = soup.find_all( 'span', class_ ='date')
    result2 = soup.find_all( 'p',  class_ ='con') 
     
    # 4. 시청자 게시판의 날짜와 본문을 params 와 params2 리스트에 담습니다.
     for  i  in  result1:
        params1.append( i.get_text("  ", strip=True) )
    for  i  in  result2:
        params2.append( i.get_text("  ", strip=True) )
        

# 4. 날짜와 본문을 같이 출력 합니다.     
for   k,  h   in   zip(  params1,  params2 ):
    print ( k + '   '  + h ) 

■ Q-415.(점심시간 문제)  레이디 버그 게시판의 전체 게시글은 총 몇건인가 ?

# 0. 웹스크롤링에 필요한 모듈을 임폴트 합니다. 
from  bs4  import  BeautifulSoup
import  urllib.request   # 웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈

# 1. 레이디 버그 게시판 게시날짜와 게시글 전체를 다 담은 리스트 2개를  만듭니다. 
params1 = []    # 게시날짜를 담을 것이고 
params2 = []    # 게시본문을 담을 것입니다                 

for  i  in  range(1, 23):   # 페이지 번호를 1번부터 22번가지 변경하려고 for 문을 사용 
   # 2. 웹에서 html 문서를 가져와 beautifulsoup 으로 파싱 
    list_url = 'http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=' +str(i) + '&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&'
    
    url = urllib.request.Request(list_url)                                    #  사람이 알아볼 수 있는 위의 url 을 파이썬이 알아
                                                                                                 # 볼 수 있도록 변환 첫번째 작업
    result = urllib.request.urlopen(url).read().decode("utf-8") 
    soup = BeautifulSoup( result, "html.parser")
    
    # 3. 시청자 게시판의 날짜와 본문 내용을 가져옵니다.
    result1 = soup.find_all( 'span', class_ ='date')
    result2 = soup.find_all( 'p',  class_ ='con') 
     
    # 4. 시청자 게시판의 날짜와 본문을 params 와 params2 리스트에 담습니다.

    for  i  in  result1:
        params1.append( i.get_text("  ", strip=True) )
    for  i  in  result2:
        params2.append( i.get_text("  ", strip=True) )
        
print(len(params1) )  # 429


■ Q-416.  게시글 429개 전체를 c 드라이브 밑에 mytext34.txt 라는 이름으로 저장하시오

* 텍스트 파일을 저장하는 파이썬 코드 

text = 'abcdefghigklmn'

f = open('c:\\data\\mytext32.txt', 'w', encoding='UTF8')
f.write( text )
f.close()

# 1. 웹에서 html 문서를 가져와 beautifulsoup 으로 파싱 
from  bs4  import  BeautifulSoup
import  urllib.request   # 웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈

params1 = []
params2 = []                   

f = open('c:\\data\\mytext34.txt', 'w', encoding='UTF8')

for  i  in  range(1, 23):
    list_url = 'http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=' +str(i) + '&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&'
    
    url = urllib.request.Request(list_url) #  사람이 알아볼 수 있는 위의 url 을 파이썬이 알아
                                                  # 볼 수 있도록 변환 첫번째 작업
    result = urllib.request.urlopen(url).read().decode("utf-8") 
    soup = BeautifulSoup( result, "html.parser")
    
    # 2. 시청자 게시판의 날짜와 본문 내용을 가져옵니다.
    result1 = soup.find_all( 'span', class_ ='date')
    result2 = soup.find_all( 'p',  class_ ='con') 
     
    # 3. 시청자 게시판의 날짜와 본문을 params 와 params2 리스트에 담습니다.
 
    for  i  in  result1:
        params1.append( i.get_text("  ", strip=True) )
    for  i  in  result2:
        params2.append( i.get_text("  ", strip=True) )
        
# 4. 날짜와 본문을 같이 출력 합니다.     
for   k,  h   in   zip(  params1,  params2 ):
    f.write ( k + '   '  + h + '\n' ) 

f.close()

■  143. 웹스크롤링 실전2 (중앙일보사) 

중앙일보사 홈페이지에서 인공지능으로 검색을 했을때 나오는
기사들을 전부 웹스크롤링 한다. 

■ 예제1. 중앙일보사 홈페이지에서 인공지능으로 검색했을 때 나오는
 url 을 가져오시오 !

https://news.joins.com/Search/JoongangNews?page=1&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=JoongangNews

■ 예제2.  위의 사이트에서 보이는 상세기사를 클릭하고 그 기사의  url 을 복사하시오 

https://news.joins.com/article/23947044
https://news.joins.com/article/23946979
https://news.joins.com/article/23946876

■ 예제3.  인공지능으로 검색했을 때 나오는 상세기사들의 url 을 스크롤링 하시오 !

#1. 웹스크롤링에 필요한 모듈을 임폴트 합니다. 
from  bs4  import  BeautifulSoup
import  urllib.request   

#2. 중앙일보에서 인공지능으로 검색했을 나오는 첫페이지의 html 코드를 
# beautiful soup 에서 이용할 수 있도록 파싱합니다.

list_url = 'https://news.joins.com/Search/JoongangNews?page=1&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=JoongangNews'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")

#3.  상세기사 url 을 가져올 수 있도록 테그와 클래스를 찾습니다.
# 찾아보니 테그는 h2 이고 클래스 이름은 headline mg 입니다.
    
result1 = soup.find_all( 'h2', class_ = 'headline mg')
print (result1 )

#4. 위의 result1은 리스트 이므로 for loop 문을 이용해서 리스트에 있는 요소를
# 하나씩 빼내면서  href 의 값을 얻어냅니다. 

for  i  in  result1:  # result1 리스트의 요소를 하나씩 빼내는 코드
    for  k  in   i:  # h2 테그 안쪽의 요소인 a 테그를 가져오긴 위한 코드 
        print(k.get("href") )  # a 테그의 href 의 값을 얻어내라 ~

■ 예제4. 위의 상세 기사 url 을 params 라는 비어 있는 리스트에 다 append 시키시오 

#1. 웹스크롤링에 필요한 모듈을 임폴트 합니다. 
from  bs4  import  BeautifulSoup
import  urllib.request   

#2. 중앙일보에서 인공지능으로 검색했을 나오는 첫페이지의 html 코드를 
# beautiful soup 에서 이용할 수 있도록 파싱합니다.

list_url = 'https://news.joins.com/Search/JoongangNews?page=1&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=JoongangNews'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")

#3.  상세기사 url 을 가져올 수 있도록 테그와 클래스를 찾습니다.
# 찾아보니 테그는 h2 이고 클래스 이름은 headline mg 입니다.
    
result1 = soup.find_all( 'h2', class_ = 'headline mg')
print (result1 )

#4. 위의 result1은 리스트 이므로 for loop 문을 이용해서 리스트에 있는 요소를
# 하나씩 빼내면서  href 의 값을 얻어냅니다. 

params =[ ]

for  i  in  result1:  # result1 리스트의 요소를 하나씩 빼내는 코드
    for  k  in   i:  # h2 테그 안쪽의 요소인 a 테그를 가져오긴 위한 코드 
        params.append(k.get("href") )  # a 테그의 href 의 값을 얻어내라 ~

print(params)

■ 예제5. 상세기사 url 중에 하나를 복사해 오고 그 상세기사 url 의 웹페이지로 접속해서
본문 기사의 테그 이름과 클래스 이름이 무엇인지 확인하시오 !


답:  테그이름은 div 테그 이고 클래스 이름은 "article_body mg fs4" 입니다. 

■ 예제6. 위의 상세기사의 본문 텍스트를 스크롤링해서 출력하시오 !
       
#1. 웹스크롤링에 필요한 모듈을 임폴트 합니다. 
from  bs4  import  BeautifulSoup
import  urllib.request   

#2. 상세 기사 url 로  검색했을 나오는 페이지의 html 코드를 
# beautiful soup 에서 이용할 수 있도록 파싱합니다.

list_url = 'https://news.joins.com/article/23947044'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")

#3.  상세기사의 본문을 가져올 수 있도록 테그와 클래스를 찾습니다.
# 찾아보니 테그는 div 이고 클래스 이름은 article_body mg fs4 입니다.
    
result1 = soup.find_all( 'div', class_ = 'article_body mg fs4')
print (result1 )

#4. 위의 result1은 리스트 이므로 for loop 문을 이용해서 리스트에 있는 요소를
# 하나씩 빼내면서  본문의 텍스트를 얻어냅니다. 

params2 =[ ]

for  i  in  result1:  # result1 리스트의 요소를 하나씩 빼내는 코드
    params2.append( i.get_text(" ", strip=True) )  

print(params2)

■ 예제7. 상세기사 url 을 가져와서 params 리스트에 넣고 출력하는 예제4번 코드를
함수로 생성하시오 !

print ( j_scroll() )

■ 예제8. 상세 기사 url 로 본문 기사를 스크롤링해서 리스트에 담았던 예제6번을
j_detail_scroll()  함수로 생성하시오 !

#1. 웹스크롤링에 필요한 모듈을 임폴트 합니다. 
from  bs4  import  BeautifulSoup
import  urllib.request   

def j_detail_scroll():
    #2. 상세 기사 url 로  검색했을 나오는 페이지의 html 코드를 
    # beautiful soup 에서 이용할 수 있도록 파싱합니다.
    list_url = 'https://news.joins.com/article/23947044'
    url = urllib.request.Request(list_url) 
    result = urllib.request.urlopen(url).read().decode("utf-8") 
    soup = BeautifulSoup( result, "html.parser")
    
    #3.  상세기사의 본문을 가져올 수 있도록 테그와 클래스를 찾습니다.
    # 찾아보니 테그는 div 이고 클래스 이름은 article_body mg fs4 입니다.
        
    result1 = soup.find_all( 'div', class_ = 'article_body mg fs4')
    print (result1 )
    
    #4. 위의 result1은 리스트 이므로 for loop 문을 이용해서 리스트에 있는 요소를
    # 하나씩 빼내면서  본문의 텍스트를 얻어냅니다. 
    
    params2 =[ ]
    
    for  i  in  result1:  # result1 리스트의 요소를 하나씩 빼내는 코드
        params2.append( i.get_text(" ", strip=True) )  
    
    return params2


print( j_detail_scroll() )

■ 예제9.   지금 만든 j_detail_scroll() 함수는 상세기사 딱 한개의 본문을 출력하는 함수인데
이 j_detail_scroll() 함수에  j_scroll() 함수를 실행했을때 나오는 상세 url 여러개를
제공할 수 있도록 코드를 수정하시오 !

#1. 웹스크롤링에 필요한 모듈을 임폴트 합니다. 
from  bs4  import  BeautifulSoup
import  urllib.request   

def  j_scroll():  함수 코드 ............ 예제7번 코드 

def  j_detail_scroll():  함수 코드 ...... 예제8번 코드 

■  중앙일보 전체코드
					
#1. 웹스크롤링에 필요한 모듈을 임폴트 합니다. 
from  bs4  import  BeautifulSoup
import  urllib.request   

def  j_scroll():
    list_url = 'https://news.joins.com/Search/JoongangNews?page=1&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=JoongangNews'
    url = urllib.request.Request(list_url) 
    result = urllib.request.urlopen(url).read().decode("utf-8") 
    soup = BeautifulSoup( result, "html.parser")
    
    
    result1 = soup.find_all( 'h2', class_ = 'headline mg')
    
    
    params=[]
    for  i  in  result1:  
        for  k  in   i: 
            params.append(k.get("href") ) 
    return params        

def j_detail_scroll():
    #2. 상세 기사 url 로  검색했을 나오는 페이지의 html 코드를 
    # beautiful soup 에서 이용할 수 있도록 파싱합니다.
    list_url = j_scroll()
    params2 =[ ]
    for i  in  list_url:
        url = urllib.request.Request(i) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        soup = BeautifulSoup( result, "html.parser")
        
        #3.  상세기사의 본문을 가져올 수 있도록 테그와 클래스를 찾습니다.
        # 찾아보니 테그는 div 이고 클래스 이름은 article_body mg fs4 입니다.
            
        result1 = soup.find_all( 'div', class_ = 'article_body mg fs4')
        
        #4. 위의 result1은 리스트 이므로 for loop 문을 이용해서 리스트에 있는 요소를
        # 하나씩 빼내면서  본문의 텍스트를 얻어냅니다. 
        
        for  i  in  result1:  # result1 리스트의 요소를 하나씩 빼내는 코드
            params2.append( i.get_text(" ", strip=True) )  
    
    return params2

print( j_detail_scroll())               


■ Q-417.  동아일보에서 검색 키워드(예: 인공지능) 를 가지고 검색을 한후 
그 url 을 얻어낸다.

https://www.donga.com/news/search?p=1&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1
https://www.donga.com/news/search?p=16&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1
https://www.donga.com/news/search?p=31&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1

■ Q-418.   상세기사 url 을 리스트에 담는 d_scroll() 함수를 생성 하세요 
def  d_scroll():
    list_url = 'https://www.donga.com/news/search?p=1&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1'
    url = urllib.request.Request(list_url) 
    result = urllib.request.urlopen(url).read().decode("utf-8") 
    soup = BeautifulSoup( result, "html.parser")      
    result1 = soup.find_all( 'p', class_ = 'txt') 
    params=[]
    for  i  in  result1:  
        for  k  in   i: 
            params.append(k.get("href") ) 
    return params        

print ( d_scroll()  )

■ Q-419. 상세기사 url 로 기사본문을 스크롤링하는 d_detail_scroll() 함수를 생성한다. 

def d_detail_scroll():
    #2. 상세 기사 url 로  검색했을 나오는 페이지의 html 코드를 
    # beautiful soup 에서 이용할 수 있도록 파싱합니다.
    list_url = d_scroll()
    params2 =[ ]
    for i  in  list_url: 
        url = urllib.request.Request(i) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        soup = BeautifulSoup( result, "html.parser")
        
        #3.  상세기사의 본문을 가져올 수 있도록 테그와 클래스를 찾습니다.
        # 찾아보니 테그는 div 이고 클래스 이름은 article_body mg fs4 입니다.
            
        result1 = soup.find_all( 'div', class_ = 'article_txt')
        
        #4. 위의 result1은 리스트 이므로 for loop 문을 이용해서 리스트에 있는 요소를
        # 하나씩 빼내면서  본문의 텍스트를 얻어냅니다. 
        
        for  i  in  result1:  # result1 리스트의 요소를 하나씩 빼내는 코드
            params2.append( i.get_text(" ", strip=True) )  
    
    return params2

■  동아일보 전체 스크롤링 코드

from  bs4  import  BeautifulSoup
import  urllib.request 

def  d_scroll():
    list_url = 'https://www.donga.com/news/search?p=1&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1'
    url = urllib.request.Request(list_url) 
    result = urllib.request.urlopen(url).read().decode("utf-8") 
    soup = BeautifulSoup( result, "html.parser")      
    result1 = soup.find_all( 'p', class_ = 'txt') 
    params=[]
    for  i  in  result1:  
        for  k  in   i: 
            params.append(k.get("href") ) 
    return params        

def d_detail_scroll():
    #2. 상세 기사 url 로  검색했을 나오는 페이지의 html 코드를 
    # beautiful soup 에서 이용할 수 있도록 파싱합니다.
    list_url = d_scroll()
    params2 =[ ]
    for i  in  list_url: 
        url = urllib.request.Request(i) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        soup = BeautifulSoup( result, "html.parser")
        
        #3.  상세기사의 본문을 가져올 수 있도록 테그와 클래스를 찾습니다.
        # 찾아보니 테그는 div 이고 클래스 이름은 article_body mg fs4 입니다.
            
        result1 = soup.find_all( 'div', class_ = 'article_txt')
        
        #4. 위의 result1은 리스트 이므로 for loop 문을 이용해서 리스트에 있는 요소를
        # 하나씩 빼내면서  본문의 텍스트를 얻어냅니다. 
        
        for  i  in  result1:  # result1 리스트의 요소를 하나씩 빼내는 코드
            params2.append( i.get_text(" ", strip=True) )  
    
    return params2


print( d_detail_scroll())


■ Q-420 한겨례 신문사에서  인공지능으로 검색했을때 나오는 기사 본문을
스크롤링하는 함수 두개를 생성하시오 !  

  1. h_scroll()  : 상세기사 url 을 가져오는 함수 
  2. h_detail_scroll()  : 상세기사 url 로 기사본문을 가져오는 함수 


■ Q-421. (오늘의 마지막 문제) 신문사 하고 싶은곳 에서 여러분들이
스크롤링하고 싶은 키워드를 넣고 검색했을때 나오는 본문기사들을
수집하는 함수 2개를 생성하시오 ~
( 밑에 페이지 번호 1,2,3 만 스크롤링하세요)

1.  jj_scroll()  :  상세기사 url 가져오는 함수 
2.  jj_detail_scroll()  : 상세기사 url 로 본문 기사를 가져오는 함수 
