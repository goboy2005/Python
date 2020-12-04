# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:30:51 2020

@author: goboy
"""


■ Q-191 숫자를 물어보게하고 숫자를 입력하면 해당 숫자만큼 
1번부터 출력되게하는 코드를 작성하시오 !

a = int( input('숫자를 입력하세요 ') )
for  i  in  range(1, a+1):
    print (i)

설명: 위의 코드의 경우에는 숫자를 입력할 때 아파벳 a를 넣으면 
예외처리가 되어서 잘못된 값을 입력하셨습니다. 라는 말만 나오고 
에러에 대한 정확한 원인파악은 하기가 어렵습니다. 

잘못된 값을 입력하셨습니다. 말고도 정확한 에러에 대한 원인을 파악을 하고싶다면 ? 
아래와 같이 작성하면 됩니다. 어떻게 작성하냐면

■ Q-192. 위의 코드에 예외처리를 해서 숫자를 물어볼때 문자를 입력하면
잘못된 값을 입력하셨습니다.라고 메세지가 출력되게하시오

try:
    a = int( input('숫자를 입력하세요 ') )
    for  i  in  range(1, a+1):
        print (i)
except:
    print ('잘못된 값을 입력하셨습니다.')

설명: 위의 코드의 경우에는 숫자를 입력할 때  알파벳 a 를 넣으면
        예외처리가 되어서 잘못된 값을 입력하셨습니다. 라는 말만 나오고
        에러대한 정확한 원인파악은 하기가 어렵습니다.

잘못된 값을 입력하셨습니다 말고도 정확한 에러에 대한 원인을 파악을 
하고 싶다면 아래와 같이 작성하면 됩니다.

try:
    a = int( input('숫자를 입력하세요 ') )
    for  i  in  range(1, a+1):
        print (i)
except  Exception  as  e:
    print ('잘못된 값을 입력하셨습니다.')
    print (e)  # 에러가 난 이유를 출력해줍니다. 

숫자를 입력하세요 ~  a

잘못된 값을 입력하셨습니다.
invalid literal for int() with base 10: 'a'


■ Q-193.판다스를 이용해서 emp3.csv의 데이터를 로드하는데 
이름을 물어보게 하고 이름을 물어보게 하고 이름을 입력하면 해당 사원의
이름과 월급이 출력되게 하시오! 


import pandas as pd
name=input('이름을 입력하세요')
emp=pd.read_csv("c:\\data\\emp3.csv")

print(emp[['ename','sal' ] ] [ emp['ename'] ==name.upper() ])


■ Q-194.위의 코드에 사용자 정의 예외처리를 해서 월급이 고소득자는 
해당 사원의 월급을 볼수 없습니다. 라는 메세지가 출되게게 하시오
( 월급이 3000이상인 사원들을 고소득자로 보고 작성하시오) 

import pandas as pd
name=input('이름을 입력하세요')
emp=pd.read_csv("c:\\data\\emp3.csv")
result=emp['sal' ] [ emp['ename'] == name.upper()] 
print(type(result))
(result 의 type 이 현재         

import pandas as pd
name=input('이름을 입력하세요')
emp=pd.read_csv("c:\\data\\emp3.csv")
result=emp['sal' ] [ emp['ename'] == name.upper()].values[0]  
print(result)


설명 emp데이터 프레임에서 어떤 특정값을 딱 하나만 출력하려면
위와 같이 작성해줘야 합니다. 

import pandas as pd
name=input('이름을 입력하세요')
emp=pd.read_csv("c:\\data\\emp3.csv")
result=emp['sal' ] [ emp['ename'] == name.upper()].values[0]
if result>3000:
    raise Exception('해당 사원의 월급은 볼 수 없습니다')
print(result)
    #print(emp[['ename']] , [emp['ename']] == name.upper() )

■ Q-195. 위의 코드에 사용자 정의 예외처리를 해서 월급이 고소득자는
해당 사원의 월급을 볼 수 없습니다. 라는 메세지가 출력되게하시오
 (월급이 3000 이상인 사원들을 고소득자로 보고 작성하시오)

import  pandas  as  pd

name = input('이름을 입력하세요 ~ ') 
emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp[ 'sal' ] [ emp['ename'] == name.upper() ].values[0]  
if  result >= 3000:
    raise  Exception('해당 사원의 월급은 볼 수 없습니다')
print ( emp[['ename','sal']] [ emp['ename'] ==name.upper() ])

이름을 입력하세요 ~ smith
이름을 입력하세요 ~ scott 

이름을 입력하세요 ~ scott
Traceback (most recent call last):

  File "C:\Users\stu\.spyder-py3\temp.py", line 7, in <module>
    raise  Exception('해당 사원의 월급은 볼 수 없습니다')

Exception: 해당 사원의 월급은 볼 수 없습니다

■ Q-196위의 코드를 수정해서 이름을 물어보게하고 이름과 직업을 
 출력하는 코드로 작성하는데 직이 SALESMAN 이면
 해당 사원의 정보는 볼수 없습니다. 라는 메세직 출력되면서
 프로그램이 종료되게 하시오! 

import pandas as pd
name=input('이름을 입력하세요')
emp=pd.read_csv("c:\\data\\emp3.csv")
result=emp['job']  [ emp['ename'] == name.upper()].values[0]
if result =='SALESMAN':
    raise Exception('해당사원의 정보는 볼수 없습니다')
else:
    print(emp['job']  [ emp['ename'] == name.upper()].values[0])


■ Q-197.아래처럼 사원 이름 물어보게하고 사원이름을 입력하면
해당 사원의 이름과 월급이 출력되게 하시오! 


import pandas as pd
name=input('사원 이름을 입력하세요~') 
emp=pd.read_csv('c:\\data\\emp3.csv")
print(emp [[ 'ename',sal']]  [emp['ename']==name.upper() ] )

■ Q-198 없는 사원이름을 입력하면 해당 사원은 없습니다. 

import pandas as pd
try:
    
    name=input('사원 이름을 입력하세요~') 
    emp=pd.read_csv("c:\\data\\emp3.csv")
    print(emp [[ 'ename','sal']]  [emp['ename']==name.upper()].values[0] )
except LookupError:
    print('해당 사원은 없습니다')

&

import pandas as pd
try:
    
    name=input('사원 이름을 입력하세요~') 
    result=emp['ename'] [emp['ename']==name.upper()].values[0]
    emp=pd.read_csv("c:\\data\\emp3.csv")
    print(emp [[ 'ename','sal']]  [emp['ename']==result] )
except LookupError:
    print('해당 사원은 없습니다')
    
설명: result=emp['ename'][emp['ename']] ==name.upper()].values[0]
    이 코드에서 Values[0] 을 사용하면 Series(컬럼)가 아니라
    값으로 출력이 되어서 result 에 담기게 됩니다. 없는 사원이름을
    입력하면 result 에 값이 입력되지 않게 되므로 LookupError 예외 처리가
    되어서 해당 사원은 없습니다. 라는 메세지가 출력되는 겁니다. 


■ Q-199(점심시간 문제) 직업을 물어보게하고 직업을 입력하면
해당 사원의 이름과 직업과 월급이 출력되게 하는 코드를
성하는데 없는 직업을 입력하면 해당직업은 사원테이블에 없습니다
라는 메세지가 력되게하시오!

import pandas as pd
try:
    zob=input('직업을 입력하세요')
    result=emp['job'] [emp['job']==zob.upper()].values[0]
    emp=pd.read_csv("c:\\data\\emp3.csv")
    print(emp[['ename','job','sal']] [emp['job']==result])
except LookupError:
        print('해당 직업을 가진 사없습니다')




■ Q-200.딕셔너리 자료형을 만들고 위와같이 type을 확인하시오 

b={'사과':'apple','배':'perar'}
print(type(b))

■ Q-201.아래와 이 두개의 숫자를 각각 물어보게 하고 아래의 메세지가
출력되게 하시오! 

첫째 숫자를 입력하세요 1113
두번째 숫자를 입력하세요 ~ 23 

a=int(input('숫자를 입력하세요'))
b=int(input('두번째 숫자를 입력하세요'))
c=a%b
print('%d를 %d로 나누면 %d 가 남습니다' %(a,b,c)) 


■ Q-202.  아래와 같이 실행되게 코드를 수행하시오 !

첫번째 숫자를 입력하시오 ~   1113
두번째 숫자를 입력하시오 ~   23

1113을 23으로 나눈 몫은 48 이고 나머지는 9 입니다. 

첫번째 숫자를 입력하시오 ~   1113
두번째 숫자를 입력하시오 ~  0 

0 으로는 나눌 수 없습니다. 

try:
    a =  int(  input('첫번째 숫자를 입력하시오 ~ ')  )
    b =  int(  input('두번째 숫자를 입력하시오 ~ ')  )
    result1, result2 = divmod(a,b) 
    print ( '%d를 %d 으로 나눈 몫은 %d 이고 나머지는 %d 입니다.' %(a,b,result1, result2)  )
except  ZeroDivisionError:
    print ('0 으로 나눌 수 없습니다.')

▶ 64 Pandas 를 이용한 데이터 검색 

SQL,Pandas 를 자유롭게 사용할 수 있어야 합니다.
SQL --- Pandas, Pandas ---SQL

예제: emp[ ['ename','sal']] [emp['ename']=='SCOTT']


■ Q-203 dept3.csv를 판다스로 로드해서 dept데이터 프레임
전체를 출력하시오! 

import pandas as pd
dept=pd.read_csv("c:\\data\\dept3.csv")
print(dept)



■ Q-204.부서치가 Dallas 의 부서번호와 부서명(dname)을 
출력하시오! 

import pandas as pd
dept=pd.read_csv("c:\\data\\dept3.csv")
print(dept[['deptno','dname' ]]   [dept[ 'loc' ] =='DALLAS' ] )

■ Q-205. DALLAS 에서 근무하는 사원들의 이름과 부서위치를 출력하시오

Pandas

import   pandas   as  pd
emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")
result = pd.merge(  emp, dept,  on='deptno')

print ( result[ ['ename', 'loc'] ] [ result['loc']=='DALLAS' ] )


;



■ Q-206.월급이 3000 이상인 사들의 이름과 월급과 부서위치를 출력하시오! 

select e.ename,e.sal,d.loc
  from emp e, dept d
    where e.deptno=d.deptno and
             e.sal>3000;

import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
dept=pd.read_csv("c:\\data\\dept3.csv")
result=pd.merge( emp,dept, on = 'deptno') 
print(result[['ename','sal','loc'] ]  [result['sal'] >=3000])


■ Q-207.부서번호가 10번,20번인 사원들의 이름과 부서위치와 부서번호를 출력하시오!

select  e.ename, d.loc, e.deptno
            from  emp  e,  dept  d
            where  e.deptno = d.dpetno   and  e.deptno in (10, 20) :

import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
dept=pd.read_csv("c:\\data\\dept3.csv")
result=pd.merge( emp,dept, on = 'deptno') 
print(result[[ 'ename','loc','deptno']] [result['deptno'].isin([10,20])])


■ Q-208 월급이 1000에서 3000인 사이인 사원들의 이름과 월급과 부서위치를 출력하시오

select e.ename,e.sal,d.loc
  from emp e, dept d
    where e.deptno=d.deptno
            and sal between 1000 and 3000;

import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
dept=pd.read_csv("c:\\data\\dept3.csv")
result=pd.merge( emp,dept, on = 'deptno') 
print(result[[ 'ename','sal','loc']] [result['sal'].between(1000,3000)])

■ Q-209 아래의 SQL을 판다스로 구현하시오 ! 

select e.ename,d.loc
  from emp e, dept d
    where e.deptno(+)=d.deptno ;

모자란 쪽에 (+)를 붙혀줘야 합니다! 
왜냐하면 

import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
dept=pd.read_csv("c:\\data\\dept3.csv")
result=pd.merge( emp,dept, on = 'deptno',how='right')
print(result[[ 'ename','loc']]) 



■ Q-210. 아래의 SQL을 Pandas 로 구현하시오 

select  e.ename,  d.loc
           from  emp  e  full  outer  join  dept   d
           on  ( e.deptno = d.deptno );

Pandas> 
emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")

result = pd.merge( emp, dept, on = 'deptno' , how='outer')
print( result[['ename',  'loc']] ) 

■ Q-211 아래의 서브쿼리를 Pandas 로 구현하시오! 

select ename,sal
   from emp
     where job=(select job
                        from  
                           emp
                             where ename='SCOTT');

import pandas as pd 
emp=pd.read_csv("c:\\data\\emp3.csv")
jjob=emp['job'] [emp ['ename']=='SCOTT'].values[0]
print(emp[['ename','sal' ]] [emp['job']==jjob]  )


■ Q-212 아래의 서브쿼리의 결과를  Pandas 로 수행하시오! 

select ename,sal
   from emp
     where job=(select job
                        from  
                           emp
                             where ename='SCOTT')
     and ename!='SCOTT'; 

import pandas as pd 
emp=pd.read_csv("c:\\data\\emp3.csv")
jjob=emp['job'] [emp ['ename']=='SCOTT'].values[0]
print(emp[['ename','sal' ]] [(emp['job']==jjob) & (emp['ename']!='SCOTT')]  )


■ Q-213 아래의 SQL을 판다스로 구현하시오! 

select max(sal)
   from emp
     where deptno=20;

import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
print(emp['sal'] [emp['deptno'] ==20].max() )

■ Q-214 아래의 SQL을 판다스로 구현하시오!  

select min(sal)
   from emp 
     where job='SALESMAN';

import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
print(emp['sal'] [emp['job'] =='SALESMAN' ].min() )

■ Q-215. emp12.csv 를 판다스 데이터 프레임으로 만들어서 출력하시오 !

import   pandas  as  pd

emp12 = pd.read_csv("c:\\data\\emp12.csv")
print(emp12)

■ Q-216. 우리반에서 최소 나이를 출력하시오 !

import   pandas  as  pd

emp12 = pd.read_csv("c:\\data\\emp122.csv")
print(emp12['AGE'].min() )

■ Q-217 아래의 SQL을 판다스로 구현하시오! 

select job,max(sal)
    from emp
       group by job

import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
result=emp.groupby('job')['sal'].max()
print(result)

■ Q-218 아래의 SQL을 판다스로 구현하시오! 

select deptno,sum(sal)
  from emp
    group by depnto:

import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
result=emp.groupby('deptno')['sal'].sum().reset_index()
print(result)


■ Q-219아래의 SQL을 판다스로 구현하시오! 

select deptno,sum(sal)
    from emp
       where deptno!=20
           group by deptno;
 
import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
result=emp.groupby('deptno')['sal'].sum().reset_index() 
print(result[[ 'deptno','sal']] [result['deptno'] !=20])


■ Q-220




def coin_prob(num):
    for i in range(num+1):
