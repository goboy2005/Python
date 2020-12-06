# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:30:51 2020

@author: goboy
"""

Python Day 8 Problems 

■ Q-191 숫자를 물어보게하고 숫자를 입력하면 해당 숫자만큼 
1번부터 출력되게하는 코드를 작성하시오 !

a = int( input('숫자를 입력하세요 ') )
for  i  in  range(1, a+1):
    print (i)

■ Q-192. 위의 코드에 예외처리를 해서 숫자를 물어볼때 문자를 입력하면
잘못된 값을 입력하셨습니다.라고 메세지가 출력되게하시오

try:
    a = int( input('숫자를 입력하세요 ') )
    for  i  in  range(1, a+1):
        print (i)
except  Exception  as  e:
    print ('잘못된 값을 입력하셨습니다.')
    print (e)  # 에러가 난 이유를 출력해줍니다. 


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
result=emp['sal'] [ emp['ename'] == name.upper()].values[0]
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
    print(emp[['ename','sal']] [emp['ename']==name.upper()].values[0])
except LookupError:
    print('해당 사원은 없습니다')

■ Q-199(점심시간 문제) 직업을 물어보게하고 직업을 입력하면
해당 사원의 이름과 직업과 월급이 출력되게 하는 코드를
성하는데 없는 직업을 입력하면 해당직업은 사원테이블에 없습니다
라는 메세지가 력되게하시오!

import pandas as pd
try:
    zob=input('직업을 입력하세요')
    emp=pd.read_csv("c:\\data\\emp3.csv")
    result=emp['job'] [emp['job']==zob.upper()].values[0]    
    print(emp[['ename','job','sal']] [emp['job']==result])
except LookupError:
        print('해당 직업을 가진 사람은없습니다')
            
■ Q-200.딕셔너리 자료형을 만들고 위와같이 type을 확인하시오 

b={'사과':'apple','배':'perar'}
print(type(b))

■ Q-201.아래와 이 두개의 숫자를 각각 물어보게 하고 아래의 메세지가
출력되게 하시오! 
(첫째 숫자를 입력하세요 1113
두번째 숫자를 입력하세요 ~ 23 )

a=int(input('숫자를 입력하세요'))
b=int(input('두번째 숫자를 입력하세요'))
c=a%b
print('%d를 %d로 나누면 %d 가 남습니다' %(a,b,c)) 

■ Q-202.  아래와 같이 실행되게 코드를 수행하시오 !

try:
    a =  int(  input('첫번째 숫자를 입력하시오 ~ ')  )
    b =  int(  input('두번째 숫자를 입력하시오 ~ ')  )
    result1, result2 = divmod(a,b) 
    print ( '%d를 %d 으로 나눈 몫은 %d 이고 나머지는 %d 입니다.' %(a,b,result1, result2)  )
except  ZeroDivisionError:
    print ('0 으로 나눌 수 없습니다.')

■ Q-203 dept3.csv를 판다스로 로드해서 dept데이터 프레임
전체를 출력하시오! 

import pandas as pd
dept=pd.read_csv("c:\\data\\dept3.csv")
print(dept)

■ Q-204.부서치가 Dallas 의 부서번호와 부서명(dname)을 
출력하시오! 

import pandas as pd
dept=pd.read_csv("c:\\data\\dept3.csv")
print(dept[['deptno','dname' ]]  [dept[ 'loc' ] =='DALLAS' ] )

■ Q-205. DALLAS 에서 근무하는 사원들의 이름과 부서위치를 출력하시오

import   pandas   as  pd
emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")
result = pd.merge(  emp, dept,  on='deptno')
print ( result[ ['ename', 'loc'] ] [ result['loc']=='DALLAS' ] )

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

import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
dept=pd.read_csv("c:\\data\\dept3.csv")
result=pd.merge( emp,dept, on = 'deptno',how='right')
print(result[[ 'ename','loc']]) 

■ Q-210. 아래의 SQL을 Pandas 로 구현하시오 

select  e.ename,  d.loc
           from  emp  e  full  outer  join  dept   d
           on  ( e.deptno = d.deptno );

emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")
result = pd.merge( emp, dept, on = 'deptno' , how='outer')
print( result[['ename', 'loc']] ) 

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


■ Q-220 동전 10개 던져서 0부터 10까지 나올확률을 모두 나열해서 뽑으시오

def p_coin(num):    
    import random
    coin = ['앞면','뒷면']
    cnt=0
    
    for j in range(1,10001):  
        a=[]
        
        for i in range(1,11): 
            result = random.choice(coin)
            a.append(result)
            
        if a.count('앞면') == num: 
               cnt += 1       
    return(cnt/10000)
   
for k in range(0,11):
   print('동전을 10번 던져서', k ,'개 앞면이 나올 확률', p_coin(k))
