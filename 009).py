# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:26:14 2020

@author: goboy
"""

Python Day 9 Problems 

■ Q-221.  부서번호, 부서번호별 평균월급을 출력하시오 !

select  deptno, avg(sal)
  from emp
  group  by deptno;

pandas>
import  pandas  as  pd
emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp.groupby('deptno')['sal'].mean().reset_index()
print( result )

■ Q-222. 위의 결과에서 평균월급을 출력할 때 정수부분만 출력하고 싶다면?
(소수점 이전만 출력)

import  pandas  as  pd
emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp.groupby('deptno')['sal'].mean().reset_index().astype(int)
print( result )

■ Q-223. 직업과 직업별 토탈월급을 출력하시오 !

select  job, sum(sal)
   from emp
        group  by  job; 

import  pandas  as  pd
emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp.groupby('job')['sal'].sum().reset_index()
print( result )

■ Q-224. 부서위치, 부서위치별 토탈월급을 출력하시오 !
select  d.loc,  sum(e.sal)
    from  emp  e,  dept   d
       where  e.deptno = d.deptno
           group  by  d.loc; 

import  pandas  as  pd
emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")
result = pd.merge( emp, dept, on ='deptno')
result2 = result.groupby('loc')['sal'].sum().reset_index()
print (  result2 )

■ Q-225.  아래의 SQL을 판다스로 구현하시오 ! 

SQL>  select  d.loc,  nvl(sum(e.sal),0)
           from  emp  e,  dept   d
           where  e.deptno (+) = d.deptno
           group  by  d.loc; 


import  pandas  as  pd
emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")
result = pd.merge( emp, dept, how='right', on ='deptno')
result2 = result.groupby('loc')['sal'].sum().reset_index()
print (  result2 )

■ Q-226.  아래의 SQL을 판다스로 구현하시오 !

SQL> select   deptno,  count(*)
         from  emp
         group  by  deptno;

import  pandas  as  pd
emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp.groupby('deptno')['empno'].count().reset_index()
print(result)

■ Q-227. emp122.csv 를 내려받아 판다스 데이터 프레임으로 만들고
출력하시오 !

import  pandas  as  pd

emp122 = pd.read_csv("c:\\data\\emp122.csv")
print (emp122) 

■ Q-228.  통신사, 통신사별 인원수를 출력하시오 !

import  pandas  as  pd

emp122 = pd.read_csv("c:\\data\\emp122.csv")
result = emp122.groupby('TELECOM')['INDEX'].count().reset_index()
print(result)
0      kt     15
1      lg      4
2      sk     11

■ Q-229.  우리반 테이블에서  통신사가 kt 이고 나이가 30살 이상인 
학생들의 이름과 나이와 통신사를 출력하시오 !

import pandas as pd
emp122=pd.read_csv('c:\\data\\emp122.csv')
result=emp122[['ENAME','AGE','TELECOM']][(emp122['TELECOM']=='kt')&(emp122['AGE']>=30)]
print(result)

설명:  and  는  판다스에서 & 이고 or 는 판다스에서  |  입니다.
        그리고 &, | 를 사용할 때는 양쪽 조건에 소괄호를 둘러줘야 합니다. 

■ Q-230.  판다스를 이용하지 말고 이름과 월급*12.3  를 출력하시오 

['7839', 'KING', 'PRESIDENT', '0', '1981-11-17', '5000', '0', '10']
['7698', 'BLAKE', 'MANAGER', '7839', '1981-05-01', '2850', '0', '30']
['7782', 'CLARK', 'MANAGER', '7839', '1981-05-09', '2450', '0', '10']
['7566', 'JONES', 'MANAGER', '7839', '1981-04-01', '2975', '0', '20']
['7654', 'MARTIN', 'SALESMAN', '7698', '1981-09-10', '1250', '1400', '30']
['7499', 'ALLEN', 'SALESMAN', '7698', '1981-02-11', '1600', '300', '30']
['7844', 'TURNER', 'SALESMAN', '7698', '1981-08-21', '1500', '0', '30']
['7900', 'JAMES', 'CLERK', '7698', '1981-12-11', '950', '0', '30']
['7521', 'WARD', 'SALESMAN', '7698', '1981-02-23', '1250', '500', '

import   csv 
file = open("c:\\data\\emp2.csv")   # os 에 있는 emp2.csv 를 읽어서
                                                 # file 이라는 변수에 넣는다.
emp_csv = csv.reader(file)  #  file 변수에 있는 csv 파일을 읽어서 emp_csv
                                 #  변수에 넣는다. 
print (emp_csv)  # 이 상태에서 그냥 프린트 하면 메모리가 주소만 나옵니다.
                   
for  emp_list  in  emp_csv:  # csv 파일의 내용을 한행씩 리스트에 담아서 
    print( emp_list[1], int(emp_list[5])*12.3 )            # 출력합니다.


설명: csv 파일의 내용을 읽어서 출력할 때 기본적으로 월급도 문자형으로
        출력되므로 산술연산을 하려면 int() 함수를 이용해서 숫자형으로 
        변환해주어야 합니다. 

KING 61500.0
BLAKE 35055.0
CLARK 30135.0
JONES 36592.5
MARTIN 15375.0
ALLEN 19680.0
TURNER 18450.0
JAMES 11685.0
WARD 15375.0
FORD 36900.0
SMITH 9840.0
SCOTT 36900.0
ADAMS 13530.0
MILLER 15990.000000000002

■ Q-231.  위의 결과를 다시 출력하는데 소수점 첫번째 자리에서 반올림되게
하시오 !

import   csv 
file = open("c:\\data\\emp2.csv")   # os 에 있는 emp2.csv 를 읽어서
                                                 # file 이라는 변수에 넣는다.
emp_csv = csv.reader(file)  #  file 변수에 있는 csv 파일을 읽어서 emp_csv
                                 #  변수에 넣는다. 
print (emp_csv)  # 이 상태에서 그냥 프린트 하면 메모리가 주소만 나옵니다.
                   
for  emp_list  in  emp_csv:  # csv 파일의 내용을 한행씩 리스트에 담아서 
    print( emp_list[1], round(int(emp_list[5])*12.3) )            # 출력합니다.

■ Q-232.  직업이 SALESMAN 인 사원들의 이름과 직업을 출력하는데
판다스 이용하지말고 emp2.csv 을 읽어서 출력하시오 !

import   csv 
file = open("c:\\data\\emp2.csv")   
emp_csv = csv.reader(file) 
                               
for  emp_list  in  emp_csv:
    if  emp_list[2] =='SALESMAN':  
        print( emp_list[1], emp_list[2] )          

■ Q-233.(점심시간 문제)  부서번호가 20번인 사원들의 이름과 월급과 
부서번호를 출력하시오 ~   

판다스를 이용한 방법:


판다스를 이용하지 않은 방법:
import csv

file=open("c:\\data\\emp2.csv") #os에 있는 emp2.csv를 읽어서 file 변수에 넣는다
emp_csv=csv.reader(file) # file 변수에 있는 csv 파일을 읽어서 emp_csv 변수에 넣는다

for emp_list in emp_csv:
    if int(emp_list[7])==20:
        print(emp_list[1],int(emp_list[6]), emp_list[7])

['7839', 'KING', 'PRESIDENT', '0', '1981-11-17', '5000', '0', '10']
['7698', 'BLAKE', 'MANAGER', '7839', '1981-05-01', '2850', '0', '30']
['7782', 'CLARK', 'MANAGER', '7839', '1981-05-09', '2450', '0', '10']
['7566', 'JONES', 'MANAGER', '7839', '1981-04-01', '2975', '0', '20']
['7654', 'MARTIN', 'SALESMAN', '7698', '1981-09-10', '1250', '1400', '30']
['7499', 'ALLEN', 'SALESMAN', '7698', '1981-02-11', '1600', '300', '30']
['7844', 'TURNER', 'SALESMAN', '7698', '1981-08-21', '1500', '0', '30']
['7900', 'JAMES', 'CLERK', '7698', '1981-12-11', '950', '0', '30']
['7521', 'WARD', 'SALESMAN', '7698', '1981-02-23', '1250', '500', '30']
['7902', 'FORD', 'ANALYST', '7566', '1981-12-11', '3000', '0', '20']
['7369', 'SMITH', 'CLERK', '7902', '1980-12-09', '800', '0', '20']
['7788', 'SCOTT', 'ANALYST', '7566', '1982-12-22', '3000', '0', '20']
['7876', 'ADAMS', 'CLERK', '7788', '1983-01-15', '1100', '0', '20']
['7934', 'MILLER', 'CLERK', '7782', '1982-01-11', '1300', '0', '10']


■ Q-234.  판다스를 이용해서 emp3.csv 를 읽어다가 이름과 월급을 출력
하는데 월급을 출력할때 소수점 이하는 버리고 정수부분만
출력되게하시오 !

import  pandas   as  pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print ( emp[['ename', 'sal']] ) 

설명:  int() 함수를 따로 안써도 정수형으로 출력되고 있습니다. 
        판다스를 이용하지 않았을때와는 다르게 숫자는 바로 숫자형으로
        출력해주고 있습니다.


■ Q-235.   판다스를 이용해서 이름과 월급을 출력하는데 월급을 출력할때
실수형으로 출력하시오 !

import  pandas   as  pd
emp = pd.read_csv("c:\\data\\emp3.csv")

emp['sal'] = emp['sal'].apply(float) 
                       # emp 데이터프레임의 sal 컬럼의 
                        # 데이터를 float(실수형)로 변환해서  emp 데이터 프레임
                        # 에 sal 컬럼의 데이터로 변경해라 ~
print ( emp[['ename', 'sal']] ) 


■ Q-236.  아래의 리스트에서  숫자가 300 이상이면 출력하고 
300 미만이면 출력되지 않게 하시오 !

b = [ 100, 352, 254, 456, 123, 234, 567, 903 ] 

def get_over(num):
    if  num >= 300:
        return  num
    else:
        return 

result = filter( get_over,  b )
print (list(result))  # [352, 456, 567, 903]

■ Q-237. 우리반 데이터에서 나이가 30살 이상인 나이만 따로 결과로
리스트로 출력하시오 
                        
[ 31, 30, .....  ] 

import   pandas   as  pd

emp122= pd.read_csv("c:\\data\\emp122.csv")
a = []
for   i  in   emp122['AGE']:
     if  i >= 30:
          a.append(i)

print (max(a))

■ Q-238.  사원 테이블에서 최대월급을 출력하시오 !( emp3.csv) 

1. 판다스를 이용했을때
import  pandas  as  pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print( emp['sal'].max() )
                   .min()
                   .mean()
                   .sum()

2. 판다스를 이용하지 않았을때 

import   csv
file = open("c:\\data\\emp2.csv")
emp = csv.reader(file)
a = []
for   i  in  emp:
    a.append( int(i[5]) )

print( max(a) )

■ Q-239.  우리반 데이터(emp122.csv) 에서 최소나이를 출력하시오 !

1. 판다스 이용했을때

import  pandas  as  pd
emp122 = pd.read_csv("c:\\data\\emp122.csv")
print ( emp122['AGE'].min() )

2. 판다스 이용하지 않았을때 

 emp122.csv 를 복사해서 emp1222.csv 로 붙여넣는다.

import   csv
file = open("c:\\data\\emp1222.csv")
emp = csv.reader(file)
a = [ ]
for  i  in  emp:
    a.append( int(i[2]) )
print(min(a)) 


UnicodeDecodeError: 'cp949' codec can't decode byte 0xec in position 3: illegal multibyte sequence 

emp1222.csv 를 메모장으로 열어서 다른 이름으로 저장하기를 누르고
인코딩을 확인하면 UTF-8 로 되어있을텐데 이것을 ANSI 로 변경하고
저장하시오 !

import   csv
file = open("c:\\data\\emp1222.csv")
emp = csv.reader(file)
a = [ ]
for  i  in  emp:
    a.append( int(i[2]) )
print(min(a))


■ Q-240.  커미션이 결측치(NaN) 인 사원들의 이름과 커미션을 출력하시오

import  pandas  as  pd

emp = pd.read_csv("c:\\data\\emp3.csv")
print ( emp[['ename', 'comm']] [ emp['comm'].isnull() ]  )  

■ Q-241. 커미션이 결측치(NaN) 이 아닌 사원들의 이름과 커미션을 
 출력하시오 !

import  pandas  as  pd

emp = pd.read_csv("c:\\data\\emp3.csv")
print ( emp[['ename', 'comm']] [ ~ emp['comm'].isnull() ]  )  

* 데이터 받았으면  데이터 분석을 하기 전에 데이터 전처리를 해야하는데
  전처리중에서 결측치 확인하는 단계가 있습니다. 

■ Q-242. emp3.csv 에 결측치가 있는지 확인하는 방법 ?

import  pandas  as  pd

emp = pd.read_csv("c:\\data\\emp3.csv")
print( emp.isnull() )

문제243. emp3.csv 에 결측치가 몇개인지 확인하는 방법 ?

import  pandas  as  pd

emp = pd.read_csv("c:\\data\\emp3.csv")
print( emp.isnull().sum() )

index          0
empno        0
ename        0
job             0
mgr           1
hiredate      0
sal             0
comm        10
deptno       0

설명: 결측치가 있으면 데이터 분석하기가 어렵고 머신러닝을 이용한 
       데이터 분석인 경우 좋은(정확도가 높은) 머신러닝 모델이 나오기 
       어렵습니다. 결측치를 처리를 해줘야 합니다.

■ Q-244.  타이타닉 데이터에 결측치가 어느 컬럼에 많은지 확인하시오 !

import  pandas  as  pd

tat = pd.read_csv("c:\\data\\train.csv")
print( tat.isnull().sum() )

PassengerId      0
Survived         0
Pclass             0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64

■ Q-245.   판다스를 이용해서  이름과 부서위치를 출력하시오!
(emp3.csv 와 dept3.csv 를 이용해서 조인하세요 )

import  pandas   as  pd

emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")

result = pd.merge( emp, dept, how='inner', on='deptno')
print ( result[['ename', 'loc'] ]) 

■ Q-246.  emp 데이터 프레임에 loc 컬럼을 추가하고 해당 사원의 부서위치로
값을 갱신하시오 !

import  pandas   as  pd

emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")

result = pd.merge( emp, dept, how='inner', on='deptno')
emp['loc'] = result['loc']  # emp 데이터프레임에 loc 컬럼 추가하면서
print (emp)                  # result 의 loc 로 값을 갱신합니다. 

설명: 파생변수를 왜 추가를 하냐면?   

     emp 테이블에서 퇴사할것 같은 사원이 누군인지 예측하시오 !
 
      머신러닝을 이용해서 예측을 하면 됩니다. 

      머신러닝이 예측을 잘하려면 좋은 데이터를 주고 학습시켜야 합니다. 

      자기의 월급이 자기가 속한 직업의 평균월급보다 더 작은 월급을
      받는 사원이면 퇴사할 가능성 높다.
      직업별 평균월급이 emp 데이터 프레임에 추가 되어 있으면
      머신러닝이 예측하기 좋은 데이터가 추가가 된것 입니다.

■ Q-247.  직업, 직업별 평균월급을 판다스로 출력하시오 !

import  pandas  as  pd

emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp.groupby('job')['sal'].mean().reset_index()

result['sal'] = result['sal'].astype(int)  # result 데이터프레임에 sal 을 정수형으로
print(result)                                # 변환해서 result 데이터프레임에 sal 에
                                               # 반영하겠다. 

         job        sal
0    ANALYST   3000
1      CLERK      1037
2    MANAGER  2758
3  PRESIDENT   5000
4   SALESMAN  1400

■ Q-248.  emp 와 result 를 서로 조인해서  조인된 전체 데이터 프레임을
출력하시오 !

result2 = pd.merge( emp,  result, how='inner', on='job') 
print ( result2 )

설명:  emp 에도 sal 이 있고 result 에도 sal 이 있어서 emp 의 sal 은
        컬럼명이 sal_x 로 변경되었고  result 의 sal 은 sal_y 로 변경되었습니다.
        sal_y 는 해당 직업의 평균월급입니다.

■ Q-249.  emp  데이터 프레임에  컬럼을 하나 추가하는데  job_avgsal 로
추가하고 문제248번에서 구한 직업별 평균월급인 result2['sal_y'] 의
값으로 값을 갱신하시오 !

emp['job_avgsal'] =  result2['sal_y']
print (emp)

설명:  현업에서 머신러닝 데이터 분석가들이 하는 일중 상당수가 
        바로 이런 파생변수를 추가하는 작업입니다. 좋은 파생변수를 추가해야
        머신러닝이 예측을 잘 할 수 있습니다.
        게임회사에서 어떻게 응용하냐면 그 게임을 이탈될것 같은 유져를
        머신러닝으로 찾아서 형평성에 어긋나지 않도록 하면서 그 유져가
        인식하지 못하도록 조용히 혜택을 줍니다. 

■ Q-250.  emp 데이터 프레임에 해당 사원이 근무하는 부서번호의 
평균월급을 sal_avg 라는 이름으로 파생변수를 생성하시오 !


■ Q-251.  emp 데이터 프레임을 출력하는데 월급이 높은 사원부터
출력하시오 !

import   pandas   as  pd

emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp.sort_values('sal', ascending=False)
print ( result )

설명:  판다스를 사용할 때 데이터를 정렬하려면 위와 같이 sort_values 함수를
        이용하면 됩니다. 
  
        ascending=True  :  낮은값에 높은값 순으로 정렬하겠다.
        ascending=False :  높은값에 낮은값 순으로 정렬하겠다. 

■ Q-252. (오늘의 마지막 문제) 아래의 SQL을 판다스로 구현하시오 !

select  job, sum(sal)
     from  emp
         group  by  job
             aving  sum(sal) >= 6000
                 order by  sum(sal)  desc; 
