# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 23:12:09 2020

@author: goboy
"""

■ 150. 이미지를 숫자로 변환하는 방법 ( 폐사진 )


예제1.  c 드라이브 밑에 images 폴더에 있는 사진들의 이름을 불러오는 
함수를 생성합니다.

import  os 
test_image ='c:\\images'

def  image_load(path):
    file_list = os.listdir(path)         # 해당 디렉토리의 파일명을 추출한다. 
    return   file_list

print ( image_load( test_image) ) 

['1.png', '10.png', '11.png', '12.png', '13.png',
 '14.png', '15.png', '16.png', '17.png', '18.png', '19.png',
 '2.png', '20.png', '3.png', '4.png', '5.png', '6.png', '7.png', 
'8.png', '9.png']

예제2. 위의 결과에서 숫자만 나오게 함수의 코드를 수정하시오 !

import  os 
import  re                       # 데이터 정제를 전문으로 하는 모듈 
test_image ='c:\\images'

def  image_load(path):
    file_list = os.listdir(path)     # 해당 디렉토리의 파일명을 추출한다. 
    file_name = [] 
    for  i  in  file_list:
        a = re.sub('[^0-9]', '', i)  
#  i 의 값중에서 숫자가 아닌것들은 싱글 두개를 붙인것('')  인 null 로 변경해라 
        file_name.append(a)        
    return  file_name

print ( image_load( test_image) ) 

['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '3', '4', '5', '6', '7', '8', '9']

■ Q-476.  위에서 출력되고 리스트 안의 요소들은 문자입니다. 그런데 문자가 아니라
리스트의 요소들이 숫자가 되게 하세요 

import  os 
import  re  # 데이터 정제를 전문으로 하는 모듈 
test_image ='c:\\images'

def  image_load(path):
    file_list = os.listdir(path)                # 해당 디렉토리의 파일명을 추출한다. 
    file_name = [] 
    for  i  in  file_list:
        a = re.sub('[^0-9]', '', i)                 #  i 의 값중에서 숫자가 아닌것들은 싱글 두개를 붙인것('')
        file_name.append(int(a))            # 인 null 로 변경해라 
    return  file_name

print ( image_load( test_image) ) 

[1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 3, 4, 5, 6, 7, 8, 9]

■ Q-477. 위의 리스트의 요소가 ascending 하게 정렬되게 하시오 

import  os 
import  re  # 데이터 정제를 전문으로 하는 모듈 
test_image ='c:\\images'

def  image_load(path):
    file_list = os.listdir(path)            # 해당 디렉토리의 파일명을 추출한다. 
    file_name = [] 
    for  i  in  file_list:
        a = re.sub('[^0-9]', '', i)        #  i 의 값중에서 숫자가 아닌것들은 싱글 두개를 붙인것('')
        file_name.append(int(a))      # 인 null 로 변경해라 
        file_name.sort()
    return  file_name

print ( image_load( test_image) ) 

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

■ Q-478.  위의 함수의 코드를 추가해서 아래와 같이 출력되게 하시오 !

 [ '1.png', '2.png', '3.png', '4.png', ......................................................  '20.png' ]

import  os 
import  re  # 데이터 정제를 전문으로 하는 모듈 
test_image ='c:\\images'

def  image_load(path):
    file_list = os.listdir(path)         # 해당 디렉토리의 파일명을 추출한다. 
    file_name = [] 
    for  i  in  file_list:
        a = re.sub('[^0-9]', '', i)            #  i 의 값중에서 숫자가 아닌것들은 싱글 두개를 붙인것('')
        file_name.append(int(a))       # 인 null 로 변경해라 
        file_name.sort()

    file_res = []
    for  k  in  file_name:
        file_res.append( str(k) + '.png')
    return  file_res

print ( image_load( test_image) ) 

['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', 
'8.png', '9.png', '10.png', '11.png', '12.png', '13.png', '14.png', 
'15.png', '16.png', '17.png', '18.png', '19.png', '20.png']

■ Q-479.  위의 함수의 코드를 수정해서 아래와 같이 이름 앞에 절대경로가 붙게 하시오 !

['c:\\images\\1.png', 'c:\\images\\2.png', 'c:\\images\\3.png',
 ............................., 'c:\\images\\20.png']

import  os 
import  re                                                     # 데이터 정제를 전문으로 하는 모듈 
test_image ='c:\\images'

def  image_load(path):
    file_list = os.listdir(path)                # 해당 디렉토리의 파일명을 추출한다. 
    file_name = [] 
    for  i  in  file_list:
        a = re.sub('[^0-9]', '', i)               #  i 의 값중에서 숫자가 아닌것들은 싱글 두개를 붙인것('')
        file_name.append(int(a))             # 인 null 로 변경해라 
        file_name.sort()

    file_res = []
    for  k  in  file_name:
        file_res.append( 'c:\\images\\' + str(k) + '.png')
    return  file_res

print ( image_load( test_image) ) 

['c:\\images\\1.png', 'c:\\images\\2.png', 'c:\\images\\3.png', 
'c:\\images\\4.png', 'c:\\images\\5.png', 'c:\\images\\6.png', 
'c:\\images\\7.png', 'c:\\images\\8.png', 'c:\\images\\9.png',
'c:\\images\\10.png', 'c:\\images\\11.png', 'c:\\images\\12.png', 
'c:\\images\\13.png', 'c:\\images\\14.png', 'c:\\images\\15.... ]

예제3.  폐사진 이미지를 숫자로 변환하기 위하여 필요한 파이썬 모듈을  install 하시오 

  아나콘다 프롬프트 창을 엽니다. 

  conda   install   opencv                       

  위의 명령어로 했을 때 에러가 나면 아래와 같이 하세요 !

  pip  install   opencv-python 

설명:  opencv 모듈은 이미지를 파이썬에서 숫자로 변환하고 다양한 이미지 처리를
        할 수 있게 해주는 기술을 제공해주는 함수 
                    
예: 구글지도나 카카오 지도, 네이버 지도에 보면 street view 가 있는데 거기에 
     사람얼굴이나 자동차 번호판을 모자이크 처리를 해줘야 합니다. 

예제4.  위에서 설치한 opencv 모듈을 이용해서 폐사진을 숫자로 변환한다.

import  cv2   #  opencv 모듈을 임폴트 하겠다. 
import  os 
import  re  # 데이터 정제를 전문으로 하는 모듈 
test_image ='c:\\images'

def  image_load(path):
    file_list = os.listdir(path)             # 해당 디렉토리의 파일명을 추출한다. 
    file_name = [] 
    for  i  in  file_list:
        a = re.sub('[^0-9]', '', i)            #  i 의 값중에서 숫자가 아닌것들은 싱글 두개를 붙인것('')
        file_name.append(int(a))              # 인 null 로 변경해라 
        file_name.sort()

    file_res = []
    for  k  in  file_name:
        file_res.append( 'c:\\images\\' + str(k) + '.png')

    image = []
    for   h  in  file_res:
        img = cv2.imread(h)                    #  이미지를 숫자로 변환하는 코드 
        image.append( img )

    return   image   

print ( image_load( test_image) ) 

예제5. 위의 숫자로 변환한 리스트를 인공 신경망에 넣기 위해서는 
         numpy 모듈의 array 형태로 제공을 해줘야 합니다.  위의 리스트를
         numpy  array 로 변환합니다. 

import   numpy   as  np                    # 행렬 연산을 쉽고 빠르게 할 수 있게해주는 모듈
import  cv2                                        #  opencv 모듈을 임폴트 하겠다. 
import  os 
import  re                                         # 데이터 정제를 전문으로 하는 모듈 
test_image ='c:\\images'

def  image_load(path):
    file_list = os.listdir(path)               # 해당 디렉토리의 파일명을 추출한다. 
    file_name = [] 
    for  i  in  file_list:
        a = re.sub('[^0-9]', '', i)              #  i 의 값중에서 숫자가 아닌것들은 싱글 두개를 붙인것('')
        file_name.append(int(a))        # 인 null 로 변경해라 
        file_name.sort()

    file_res = []
    for  k  in  file_name:
        file_res.append( 'c:\\images\\' + str(k) + '.png')

    image = []
    for   h  in  file_res:
        img = cv2.imread(h)                      #  이미지를 숫자로 변환하는 코드 
        image.append( img )

    return   np.array( image )

print ( image_load( test_image) ) 

■  151. 이미지를 숫자로 변환하는 방법 (개와 고양이)

  개와 고양이 사진을 분류하는 인공신경망을 만들려면 
  개와 고양이 사진을 각각 2000장씩 내려 받아서 숫자로 변환하는 작업을
  해줘야 합니다. 
  
예제1. 머신러닝 데이터 분석의 세계대회인 케글에서 개와 고양이 사진을
        내려 받습니다.  구글에서 kaggle 로 검색 하세요 ~~

kaggle  검색에서   cat and dog

예제2. 개사진 30장만 c 드라이브 밑에 images2 라는 폴더에 넣으세요


예제3.   c 드라이브 밑에 images2 라는 폴더에 있는 이미지 이름을 
           가져오는 함수를  image_load2 라는 함수로 생성하시오 !

import  os
path ="c:\\images2"

def  image_load2(path):               
    file_list = os.listdir(path)
    return   file_list

print ( image_load2(path) )

예제4.  위의 개사진 이름에서 숫자만 출력하시오 !

import  os
import  re
path ="c:\\images2"

def  image_load2(path):               
    file_list = os.listdir(path)
    file_name =[]
    for   i   in  file_list:
        a = re.sub('[^0-9]', '', i)
        file_name.append( int(a) )
    return  file_name

print ( image_load2(path) )

예제5.  file_name 리스트 안의 숫자를 정렬해서 출력되게하시오 !

import  os
import  re
path ="c:\\images2"

def  image_load2(path):               
    file_list = os.listdir(path)
    file_name =[]
    for   i   in  file_list:
        a = re.sub('[^0-9]', '', i)
        file_name.append( int(a) )
        file_name.sort()
    return  file_name

print ( image_load2(path) )

예제6.  아래와 같이 절대경로와 확장자가 붙어서 출력되게하시오 !

[ 'c:\\images2\\dog1.jpg'  , 'c:\\images2\\dog2.jpg' , ..............  ]   

import  os
import  re
path ="c:\\images2"

def  image_load2(path):               
    file_list = os.listdir(path)
    file_name =[]
    for   i   in  file_list:
        a = re.sub('[^0-9]', '', i)
        file_name.append( int(a) )
        file_name.sort()
    
    file_res=[]
    for  k  in  file_name:
        file_res.append('c:\\images2\\dog' + str(k) +'.jpg')
        
    return file_res
        
print ( image_load2(path) )

예제7.  위의 개사진 이미지들을 opencv 와 numpy 를 이용해서 숫자로 변환하고 
          numpy  array 로 반환되게 하시오 !

import  os
import  re
import  cv2
import  numpy  as np
path ="c:\\images2"

def  image_load2(path):               
    file_list = os.listdir(path)
    file_name =[]
    for   i   in  file_list:
        a = re.sub('[^0-9]', '', i)
        file_name.append( int(a) )
        file_name.sort()
    
    file_res=[]
    for  k  in  file_name:
        file_res.append('c:\\images2\\dog.' + str(k) +'.jpg')
    
    image =[]    
    for  h  in  file_res:
        img = cv2.imread(h)
        image.append(img)

    return  np.array(image)        

print ( image_load2(path) )

■ Q-480. (점심시간 문제) 지난번에 여러분들이 직접 스크롤링한 사진 20장을 
 c 드라이브 밑에  images3 에 넣고  숫자로 변환하는 함수를 
image_load3 로 생성하시오 !

import  cv2   
import  os 
import  re  

path = "c:\\images3"  

def image_load3(path):
    file_list = os.listdir(path) 
    file_name=[] 
    for i in file_list:  
        a=re.sub('[^0-9]','',i)  
        file_name.append( int(a)) 
        file_name.sort()
    return file_name

print( image_load3(path)) 

■ 152. 필수 알고리즘1 (합성곱 연산)

알고리즘 문제을 풀어야하는 이유 ?

  1. 지금까지 배운 파이썬 문법을 완성하는 단계 - 알고리즘 문제 해결 

  2. 구글, 네이버, 카카오와 같이 대기업으로 지원하고자 한다면
     알고리즘 문제를 많이 풀어봐야 합니다.
 
                        ↓
   프로그래머스 사이트에 여러 알고리즘 문제들이 올라와 있음

   하루에 하나씩 꾸준히 풀면서 실력을 천천히 쌓아 올리면 됩니다. 
  
* 합성곱 연산 알고리즘 ? 

  딥러닝의 필수 알고리즘 (퍼셉트론, 합성곱 연산 알고리즘) 
  이미지의 형상을 무시하지 않고 이미지를 그대로 인공 신경망이
  학습 할 수 있게 해준 수학 행렬 연산입니다.
  합성곱에서 원본 이미지는 학습해야할 데이터(사진) 이고
  필터(filter) 는 원본이미지에서 특징을 잡아내는데 사용되는 행렬입니다.
  특징을 잡아서 feature map 을 생성하여 원본이미지의 형태를 
  이해하는 것을 합성곱 연산이라고 합니다. 
 
■ Q-481.  아래의 두 행렬을 만들고 덧셈 연산을 하시오 !

a = [ [ 1, 2, 3 ] , [ 0, 1, 2 ], [ 3, 0, 1] ]
b = [ [ 2, 0, 1 ],  [ 0, 1, 2 ], [1, 0, 2 ] ]

import  numpy  as  np
a2 = np.array(a)
b2 = np.array(b)
print ( a2 + b2) 

[[3 2 4]
 [0 2 4]
 [4 0 3]]

■ Q-482.  아래의 두 행렬을 만들고 두행렬의 원소들의 곱을 구하시오 

a = [ [ 1, 2, 3 ] , [ 0, 1, 2 ], [ 3, 0, 1] ]
b = [ [ 2, 0, 1 ],  [ 0, 1, 2 ], [1, 0, 2 ] ]

import  numpy  as  np
a2 = np.array(a)
b2 = np.array(b)
print ( a2 * b2) 

[ [2 0 3]
  [0 1 4]
  [3 0 2] ]

■ Q-483.  위에서 원소들의 곱으로  출력된 결과인 3x3 행렬의 요소들을 
모두 다 더하시오 !

결과 : 15 

위의 코드들 ...
a2 = np.array(a)
b2 = np.array(b)
result = a2 * b2
print ( np.sum(result) )  # 행렬안의 원소들의 합을 출력합니다. 

설명:  numpy 란 ?    python 언어에서 기본적으로 지원하지 않는 배열(array)
                           혹은 행렬(matrix) 의 계산을 쉽게해주는 라이브러리 
                           입니다.  머신러닝에서 많이 사용하는 선형대수학에
                           관련된 수식들을 python 에서 쉽게 프로그래밍 할 수 
                           있게 해줍니다. 

■ Q-484.  아래의 4x4 행렬을 만드시오 !

import  numpy  as  np
a = [ [ 1, 2, 3, 0 ], [ 0, 1, 2, 3 ], [ 3, 0, 1, 2 ], [ 2, 3, 0, 1] ]
a2 = np.array(a) 
print (a2)

■ Q-485. 아래의 4x4 행렬에서 빨간색으로 지정한 영역의 숫자들만 출력하시오

위의 코드들 ...
print  ( a2[ 0:3, 0:3 ] )        # 행을 0 이상에서 3미만까지 
                                              # 열을 0 이상에서 3미만까지 
[[1 2 3]
 [0 1 2]
 [3 0 1]]

■ Q-486. 아래의 4x4 행렬에서 빨간색으로 지정한 영역의 숫자들만 출력하시오

위의 코드들 ...
print( a2[ 0:3,  1:4 ] ) 
             행    열 

■ Q-487. 아래의 4x4 행렬에서 빨간색으로 지정한 영역의 숫자들만 출력하시오!

위의 코드들 ...
print ( a2[ 1:4, 0:3 ] )

■ Q-488. 아래의 4x4 행렬에서 빨간색으로 지정한 영역의 숫자들만 출력하시오!

위의 코드들 ...
print ( a2[ 1:4, 1:4 ] )

■ Q-489. 아래의 4x4 행렬에서 위에서 빨간색으로 지정된 4개의 영역의
숫자들을 for loop 문을 이용해서 모두 출력하시오 !

a2[ 0:3, 0:3 ]
a2[ 0:3, 1:4 ]          
a2[ 1:4, 0:3 ] 
a2[ 1:4, 1:4 ]                                   

import numpy as np

a = [[1,2,3,0], [0,1,2,3], [3,0,1,2], [2,3,0,1]]
a2 = np.array(a)

for i, k in zip(range(0,2), range(3,5)):                           # i 가 0, 1  , k가  3, 4 
    for j, h in zip(range(0,2), range(3,5)):                       # j 가 0, 1 , h 가 3, 4 
        print(i,k, j,h)
 
         0, 3,  0, 3  --> i 가 0 , k가 3일때 j 가 0이고 h가 3 
         0, 3,  1, 4  --> i 가 0,  k 가 3일때 j가 1이고 h가 4
         1, 4,  0, 3  --> i가  1, k 가 4일때 j가 0이고 h가 3
         1, 4,  1, 4  --> i가  1, k 가 4일때 j가 1이고 h가 4 
       

import numpy as np

a = [[1,2,3,0], [0,1,2,3], [3,0,1,2], [2,3,0,1]]
a2 = np.array(a)

for i, k in zip(range(0,2), range(3,5)): # i 가 0, 1  , k가  3, 4 
    for j, h in zip(range(0,2), range(3,5)): # j 가 0, 1 , h 가 3, 4 
        print(a2[i:k, j:h])

주원이 코드:

a = [ [1,2,3,0] , [0,1,2,3] , [3,0,1,2] , [2,3,0,1]] 
for i in range(0,2):   # 0, 1
    for j in range(0,2):  # 0, 1
        print(a2[i:i+3,j:j+3])  #  i 가 0일때 j 가 0, 1  
                                       0:3, 0:3  --> i 가 0일때 j 가 0 일때 
                                       0:3, 1:4  --> i 가 0일때 j 가 1 일때 

                                                                                                                #  i 가 1일때 j 가 0, 1
                                      1:4, 0:3   --> i가 1일때 j 가 0일때
                                      1:4, 1:4  --> i가 1일때 j 가 1일때 

■ Q-490.  위에서 선택한 4개의 행렬(3x3) 과 아래의 filter 행렬(3x3) 과의
원소의 곱을 출력하시오 !

import  numpy  as  np
f  = [ [ 2, 3, 4 ], [ 1, 2, 3] ,[2, 0, 1] ]
filter = np.array(f)
a = [ [1,2,3,0] , [0,1,2,3] , [3,0,1,2] , [2,3,0,1]] 
a2 = np.array(a) 

for i in range(0,2):   # 0, 1
    for j in range(0,2):  # 0, 1
        print(a2[i:i+3,j:j+3] * filter )  

[[ 2  6 12]
 [ 0  2  6]
 [ 6  0  1]]
[[4 9 0]
 [1 4 9]
 [0 0 2]]
[[0 3 8]
 [3 0 3]
 [4 0 0]]
[[ 2  6 12]
 [ 0  2  6]
 [ 6  0  1]]

■ Q-491.   위에서 출력된 3x3 행렬 4개에 대한 원소들의 합이 각각 출력되게
하시오

[[ 2  6 12]
 [ 0  2  6]        ---------> 35 
 [ 6  0  1]]
[[4 9 0]
 [1 4 9]           ---------> 29 
 [0 0 2]]
[[0 3 8]
 [3 0 3]          --------->  21
 [4 0 0]]
[[ 2  6 12]
 [ 0  2  6]         -------> 35 
 [ 6  0  1]]


import  numpy  as  np
f  = [ [ 2, 3, 4 ], [ 1, 2, 3] ,[2, 0, 1] ]
filter = np.array(f)
a = [ [1,2,3,0] , [0,1,2,3] , [3,0,1,2] , [2,3,0,1]] 
a2 = np.array(a) 

for i in range(0,2):                                                # 0, 1
    for j in range(0,2):                                            # 0, 1
        print( np.sum( a2[i:i+3,j:j+3] * filter) )  
35
29
21
35

■ Q-492.  위에서 출력된 4개의 숫자로 아래의 행렬(2x2)을 만드시오 !

   35  29
   21  35 

import  numpy  as  np
f  = [ [ 2, 3, 4 ], [ 1, 2, 3] ,[2, 0, 1] ]
filter = np.array(f)
a = [ [1,2,3,0] , [0,1,2,3] , [3,0,1,2] , [2,3,0,1]] 
a2 = np.array(a) 

result = []                    
for i in range(0,2):                                                              # 0, 1
    for j in range(0,2):                                                          # 0, 1
        result.append( np.sum( a2[i:i+3,j:j+3] * filter) )  

result2 = np.array(result).reshape(2,2)  # 넘파이 어레이의 2x2 행렬로 변경 
print(result2)

설명:  a2 라는 원본이미지(개사진)에 filter(랜덤으로 생성한 이미지)를
        가지고 원본이미지를 스트라이드(양옆위아래로 스캔) 하면서
        특징을 잡아내에 특징 이미지를 추출(result2) 하는것을 합성곱이라고
        합니다.

■ Q-493. (필수 알고리즘1) 아래의 원본 이미지 행렬(5x5) 행렬에서 
필터행렬(4x4)로 스트라이딩 해서 합성곱해서 특징(2x2)을 추출하시오 

 4x4  ---> 3x3  ---> 2x2              
 5x5  ---> 4x4  ---> 2x2              

import numpy as np
f=[[3,1,4,1],[2,3,3,4],[5,1,2,1],[6,1,3,4]]
filter = np.array(f)
a=[[2,3,1,4,7],[3,1,6,4,3],[2,1,5,3,1],[6,2,4,1,2],[7,3,1,2,3]]
a2=np.array(a)
result = []
for i in range(2):
    for j in range(2):
        result.append(np.sum(a2[i:i+4,j:j+4]*filter))

result2 = np.array(result).reshape(2,2)
print(result2)

■  153. 필수 알고리즘2 (이진 탐색)

■ Q-494.  아래의 리스트에서 숫자 3이 있는지 순차 탐색으로 구현하시오 !
있으면 숫자 3이 있습니다. 라는 메세지가 출력되게하시오 !

a = [ 15, 11, 1, 3, 8 ]  

설명: 순차탐색이란 ? 주어진 데이터를 처음부터 차례데로 비교하면서
                           찾는 방법 

a=[15,11,1,3,8]
for i in a:
    if i==3:
        print('숫자 3이 있습니다')
        break
else:
    print('숫자 3이 없습니다')

■ Q-495. 위의 코드를 수정해서 숫자를 물어보게 하고 숫자를 입력하면
해당 숫자가 존재하는지 존재하지 않는지가 출력되게하시오 !

검색할 숫자를 입력하세요 ~   3

숫자 3은 있습니다. 

b = int(input('검색할 숫자를 입력하세요 ~'))

a=[15,11,1,4,8]
for i in a:
    if i==b:
        print('숫자', b,'이 있습니다')
        break
else:
    print('숫자', b,'이 없습니다')

* 이진탐색 ? 정렬된 데이터를 좌우 둘로 나눠서 원하는 값의 
탐색범위를 좁혀가며 찾는 방법 

■ Q-496. 아래의 a 리스트에서 중앙값을 찾으시오

a = [ 1, 7, 11, 12, 14, 23, 33, 47, 51, 64, 67, 77, 139, 672, 871 ]

import  numpy  as  np
a_n = np.array(a)
print ( np.median(a_n) )

■ Q-497. a 리스트에서 첫번째 숫자 부터 중앙값에 해당하는 숫자
까지만 검색하시오 

힌트:  a.index(요소명)

a = [ 1, 7, 11, 12, 14, 23, 33, 47, 51, 64, 67, 77, 139, 672, 871 ]

결과: [ 1, 7, 11, 12, 14, 23, 33, 47 ]

답: 
a = [ 1, 7, 11, 12, 14, 23, 33, 47, 51, 64, 67, 77, 139, 672, 871 ]

import  numpy  as  np
a_n = np.array(a)                               
a_m =  np.median(a_n) 
print ( a[   :  a.index(a_m) + 1 ] )

■ Q-498. 위의 a 리스트에서 문제497번에서 선택된 숫자들을 중앙값까지
포함해서 다 지우고 아래의 결과만 출력되게하시오 !

결과:  [ 51, 64, 67, 77, 139, 672, 871 ]

a = [ 1, 7, 11, 12, 14, 23, 33, 47, 51, 64, 67, 77, 139, 672, 871 ]

import  numpy  as  np
a_n = np.array(a)                               
a_m =  np.median(a_n) 
del ( a[   :  a.index(a_m) + 1 ] )
print (a)

■ Q-499.   위의 결과로 출력된 아래의 리스트에서 중앙값을 출력하시오 !

[51, 64, 67, 77, 139, 672, 871]

a = [ 1, 7, 11, 12, 14, 23, 33, 47, 51, 64, 67, 77, 139, 672, 871 ]

import  numpy  as  np
a_n = np.array(a)                               
a_m =  np.median(a_n) 
del ( a[   :  a.index(a_m) + 1 ] )
a_m2 = np.median(a)
print(a_m2)                                                               # 77.0 

■ Q-500.  지금 위에서 출력한 중앙값 77이 내가 검색하고자 하는 67보다
크다면 아래의 결과 리스트만 출력되게 하시오 

[51, 64, 67, 77, 139, 672, 871]

결과:   [ 51, 64, 67 ] 

위의 코드들...
a_m2 = np.median(a)
if  a_m2 > 67:
    del ( a[ a.index(a_m2) : ] )
else:
    del( a[ : a.index(a_m2) ] )
print(a)

■ Q-501. (오늘의 마지막 문제)  EBS 에 나온 영상데로 이진탐색을 구현하시오
필수 알고리즘 2번 문제



a=[1,7,11,12,14,23,33,47,51,64,67,77,139,672,871]
num=int(input('검색할 숫자를 입력하세요 : '))
cnt=0 # 검색 횟수 변수 선언


while(True):
    cnt+=1 # 검색 횟수 1씩 증가


    import numpy as np
    a_n=np.array(a)


    if len(a)%2==1:    # 리스트의 요소의 개수가 홀수면 np.median(a_n)하면 바로 나오지만
        a_m=int(np.median(a_n))
    else:                  # 짝수면 가운데 값 두 개를 더해서 반으로 나눈 값을 반환해서 줘서 리스트의 없는 중위값이 나와버림
        a_m=a[len(a)//2]  # 그래서 중위값을 그 두 개의 가운데 값 중 오른쪽 값을 중위값이라 따로 정의


    if len(a)==1: # 계속 쪼개다가 남은 리스트의 개수가 1개가 되면 while문을 어떻게든 끝내야하기 때문에 따로 조건문
        if num==a_m:
            print(num,'은 이진탐색 ', cnt, '번 만에 검색되었습니다')
            break
        else:
            print(num, '은 리스트에 없습니다')
            break
    if num==a_m:
        print(num,'은 이진탐색 ', cnt, '번 만에 검색되었습니다')
        break # 검색되면 바로 while문을 끝내야 함
    elif num>a_m:
        del a[:a.index(a_m)]
    else:
        del a[a.index(a_m):]
