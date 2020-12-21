# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 18:56:06 2020

@author: goboy
"""


■ 148. 오라클과 파이썬 연동하기 

                                 연동
  오라클 database  ------------------------ 파이썬 ( 통계구현, 시각화,
         ↓                                                     머신러닝, 업무자동화 )
   비지니스 데이터           emp2.csv
   (정형화된 데이터)         emp1222.csv 

 * 오라클과 파이썬을 연동하는 이유 ?

   1.  오라클 데이터 베이스에서 실시간으로 변하는 데이터를
       csv 파일로 매번 내릴려면 자주 내려야 하므로 그냥 바로 연동합니다.

   2. 파이썬의 여러 장점들을 이용해서 데이터를 분석할 수 있기 때문입니다.
      ( 통계구현, 시각화, 머신러닝 구현, 업무자동화)

   3. 폐사진을 숫자로 변환해서 오라클 database 에 저장합니다. 
      이미지를 숫자로 변환해서 오라클 database 에 저장합니다.
      db 에 저장하고 관리를 합니다. os 에 파일로 남겨만 두지 않습니다.
      db 에 저장하면 장점이 백업과 복구를 할 수 가 있다.  그리고 좀더
      효율적으로 data 를 관리를 할 수 가 있습니다.  
      os 에 파일로 저장되어 있으면 바이러스에 노출될 수도 있습니다. 

* 빅데이터 기사 시험 :  데이터의 구조에 따른 종류 3가지
                               1. 정형화 데이터  :  rdbms 에 저장된 데이터
                                                          ↓
                              relational  database  management  system 
                             ( 관계형 데이터 베이스 관리  시스템) 

                               2. 반정형화 데이터 :   html, 웹로그 데이터 
                               3. 비정형화 데이터 :   텍스트, 동영상, 이미지 데이터 
                                                            (SNS) 
* 오라클과 파이썬 연동 

 1. 도스창을 열고 리스너의 상태를 확인합니다. 
    리스너 상태 확인하는 명령어 :  lsnrctl  status 
      ↓
   외부에서 오라클에 접속하려면 리스너를 통해야지만 접속이 됩니다. 
   리스너가 접속을 허용해주어야 접속이 되는 것입니다.
   리스너가 가지고 있는 정보중 3가지를 확인해야합니다.
      1.  ip 주소  (건물주소) :  localhost
      2. 포트번호 (건물안의 복도) : 1522
      3. 서비스 이름 ( 회사이름) :  xe

  2.  위의 정보들을 이용해서 오라클 databse 에 접속을 해봅니다. 

  sqlplus scott/tiger@localhost:1521/orcl

 3.  아나콘다 프롬프트창을 열고 cx_Oracle 모듈을 설치합니다. 
    
    conda  install   cx_Oracle 

 4. 파이썬에서 오라클과 연동하는 코드를 작성한다.
    (spyder 에서 작성하세요 ~)

import  cx_Oracle
import  pandas  as   pd

dsn = cx_Oracle.makedsn("localhost", 1522, 'xe' )  #오라클 주소를 기입한다.
db = cx_Oracle.connect('system', 'oracle', dsn ) # 오라클 접속 유져 정보
cursor = db.cursor() # 결과 데이터를 담을 메모리 이름을 cursor 로 선언함
cursor.execute(""" select * from  emp """) # 작성한 쿼리문의 결과가 
                                                     # cursor 메모리에 담긴다. 
row = cursor.fetchall()   # cursor 메모리에 담긴 결과를 한번에 row 변수에
                               # 담는다.
emp = pd.DataFrame(row)
print (emp)

■ Q-440. 위의 emp 테이블 전체를 select 했는데 전체를 다 select 하지 
말고 아래의 쿼리의 결과만 select 하시오 !

 select  empno, ename, sal, deptno
   from emp;


import  cx_Oracle
import  pandas  as   pd

dsn = cx_Oracle.makedsn("localhost", 1522, 'xe' )                    #오라클 주소를 기입한다.
db = cx_Oracle.connect('system', 'oracle', dsn )                 # 오라클 접속 유져 정보
cursor = db.cursor()                                                 # 결과 데이터를 담을 메모리 이름을 cursor 로 선언함
cursor.execute(""" select empno, ename, sal, deptno from  emp """) # 작성한 쿼리문의 결과가 cursor 메모리에 담긴다. 
row = cursor.fetchall()                                                # cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다.
emp = pd.DataFrame(row)
print (emp)

■ Q-441.   dept 테이블의 모든 데이터를 조회하시오 !

import  cx_Oracle
import  pandas  as   pd

dsn = cx_Oracle.makedsn("localhost", 1522, 'xe' )          #오라클 주소를 기입한다.
db = cx_Oracle.connect('system', 'oracle', dsn )          # 오라클 접속 유져 정보
cursor = db.cursor()                                      # 결과 데이터를 담을 메모리 이름을 cursor 로 선언함
cursor.execute(""" select * from  dept""")                  # 작성한 쿼리문의 결과가 cursor 메모리에 담긴다. 
row = cursor.fetchall()                                               # cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다.
dept= pd.DataFrame(row)
print (dept)

■ Q-442.  우리반 테이블(emp12) 를 조회하시오 !

import  pandas  as   pd

dsn = cx_Oracle.makedsn("localhost", 1522, 'xe' )   #오라클 주소를 기입한다.
db = cx_Oracle.connect('system', 'oracle', dsn )     # 오라클 접속 유져 정보
cursor = db.cursor()                                   # 결과 데이터를 담을 메모리 이름을 cursor 로 선언함
cursor.execute(""" select * from  emp12 """)      # 작성한 쿼리문의 결과가 cursor 메모리에 담긴다. 
row = cursor.fetchall()                                # cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다.

emp12 = pd.DataFrame(row)
print (emp12)

■ Q-443. 월급이 1200  이상인 사원들의 이름과 월급을 출력하시오 !







■ Q-444.  사원 테이블의 월급을 막대 그래프로 그리시오 

import cx_Oracle
import  pandas  as   pd

dsn = cx_Oracle.makedsn("localhost", 1522, 'xe' )           #오라클 주소를 기입한다.
db = cx_Oracle.connect('system', 'oracle', dsn )                   # 오라클 접속 유져 정보
cursor = db.cursor()                                           # 결과 데이터를 담을 메모리 이름을 cursor 로 선언함
cursor.execute(""" select ename,sal from  emp """)      # 작성한 쿼리문의 결과가 cursor 메모리에 담긴다. 
row = cursor.fetchall()                                                           # cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다.
emp = pd.DataFrame(row)
print(list(emp[0]))

emp.index = list(emp[0])  
emp.plot(kind='bar') 

■ Q-445. (점심시간 문제) 위의 그래프의 색깔을 변경하고 그래프를 올리세요

import cx_Oracle
import pandas as pd
dsn=cx_Oracle.makedsn('localhost',1521,'orcl')

db=cx_Oracle.connect('scott','tiger',dsn)
cursor =db.cursor() 
cursor.execute("""select ename,sal from emp where sal >=1200""") 

row=cursor.fetchall() 
emp=pd.DataFrame(row)
# print(list(emp[0])) 

emp.index=list(emp[0])
emp.plot(kind='bar',color='teal')

■ Q-446.  직업, 직업별 최대월급을 출력하시오 ! 

import cx_Oracle
import  pandas  as   pd

dsn = cx_Oracle.makedsn("localhost", 1522, 'xe' )             #오라클 주소를 기입한다.
db = cx_Oracle.connect('system', 'oracle', dsn )            # 오라클 접속 유져 정보
cursor = db.cursor()                                           # 결과 데이터를 담을 메모리 이름을 cursor 로 선언함
cursor.execute(""" select job, max(sal) from  emp group by job """)  # 작성한 쿼리문의 결과가 cursor 메모리에 담긴다. 
                                                   
row = cursor.fetchall()                                    # cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다.
emp = pd.DataFrame(row)
print(emp)

■ Q-447.  직업, 직업별 토탈월급을 출력하는데 직업별 토탈월급이 
높은것부터 출력하시오 !

import cx_Oracle
import  pandas  as   pd

dsn = cx_Oracle.makedsn("localhost", 1522, 'xe' ) .
db = cx_Oracle.connect('system', 'oracle', dsn ) 
cursor = db.cursor() 
cursor.execute(""" select job, sum(sal) 
                          from  emp 
                          group by job 
                          order by sum(sal) desc """) 
                                                   
row = cursor.fetchall()   
emp = pd.DataFrame(row)
print(emp)

■ Q-448.  이름, 월급, 순위를 출력하는데 순위가 월급이 높은 사원순으로
순위를 부여하시오 !

import cx_Oracle
import  pandas  as   pd

dsn = cx_Oracle.makedsn("localhost", 1522, 'xe' ) .
db = cx_Oracle.connect('system', 'oracle', dsn ) 
cursor = db.cursor() 
cursor.execute(""" select  ename, sal, 
                           dense_rank()  over (order by sal desc) rnk
                                  from emp  """) 
                                                   
row = cursor.fetchall()   
emp = pd.DataFrame(row)
print(emp)

■ Q-449.  부서번호, 부서번호별 토탈월급을 출력하시오 !

import cx_Oracle
import  pandas  as   pd

dsn = cx_Oracle.makedsn("localhost", 1522, 'xe' ) 
db = cx_Oracle.connect('system', 'oracle', dsn ) 
cursor = db.cursor() 
cursor.execute(""" select deptno, sum(sal)
                         from  emp
                         group  by  deptno  """) 
                                                   
row = cursor.fetchall()   
emp = pd.DataFrame(row)
print(emp)

■ Q-450. 위의 결과를  막대그래프로 시각화 하시오 !

위의 코드들 ...
row = cursor.fetchall()   
emp = pd.DataFrame(row)
emp.index=list(emp[0])
emp.plot(kind='bar',color='blue')

■ Q-451.  emp 테이블 전체를 출력하는데 컬럼명이 붙어서 출력되게하시오

import cx_Oracle
import  pandas  as   pd

dsn = cx_Oracle.makedsn("localhost", 1522, 'xe' ) 
db = cx_Oracle.connect('system', 'oracle', dsn ) 
cursor = db.cursor() 
cursor.execute(""" select *
                                      from emp """) 
                                                   
row = cursor.fetchall()   
emp = pd.DataFrame(row)

colname = cursor.description            #  컬럼명을 가져온다. 
col = [ ]
for  i   in   colname:
    col.append( i[0].lower() )
print(col)
['empno', 'ename', 'job', 'mgr', 'hiredate', 'sal', 'comm', 'deptno']

■ Q-452.  위의 col 리스트에 담긴 컬럼명을 위의 데이터에 매핑시키시오

위의 코드들 

for  i   in   colname:
    col.append( i[0].lower() )
print(col)
emp = pd.DataFrame (list(row), columns=col)
print (emp)

■ Q-453.  위의 컬럼명을 이용해서 판다스 문법으로 이름과 월급을 출력하시오 

위의 코드들 
for  i   in   colname:
    col.append( i[0].lower() )
print(col)
emp = pd.DataFrame (list(row), columns=col)
print (emp[['ename', 'sal']])

■ Q-454. 월급이 3000 이상인 사원들의 이름과 월급을 출력하시오 !

위의 코드들 
for  i   in   colname:
    col.append( i[0].lower() )
print(col)
emp = pd.DataFrame (list(row), columns=col)
print ( emp[['ename', 'sal']] [ emp['sal'] >= 3000 ] )

■ Q-455.  이름과 부서위치를 출력하시오 ! ( 그냥 SQL 로 작성해서 
파이썬에서 출력되게하시오 )

import cx_Oracle
import  pandas  as   pd

dsn = cx_Oracle.makedsn("localhost", 1522, 'xe' ) 
db = cx_Oracle.connect('system', 'oracle', dsn ) 
cursor = db.cursor() 
cursor.execute(""" select e.ename, d.loc
                         from emp e, dept  d
                        where e.deptno = d.deptno""") 
                                                   
row = cursor.fetchall()   
emp = pd.DataFrame(row)
print(emp)

■ Q-456.  부서위치, 부서위치별 토탈월급을 출력하시오 !

import cx_Oracle
import  pandas  as   pd

dsn = cx_Oracle.makedsn("localhost", 1522, 'xe' ) 
db = cx_Oracle.connect('system', 'oracle', dsn ) 
cursor = db.cursor() 
cursor.execute(""" select  d.loc, sum(e.sal)
                     from emp  e, dept  d
                     where  e.deptno = d.deptno
                     group by d.loc  """) 
                                                   
row = cursor.fetchall()   
emp = pd.DataFrame(row)
print(emp)

■ Q-457. 위의 결과를 막대그래프로 시각화 하시오 !

import cx_Oracle
import  pandas  as   pd

dsn = cx_Oracle.makedsn("localhost", 1522, 'xe' ) 
db = cx_Oracle.connect('system', 'oracle', dsn ) 
cursor = db.cursor() 
cursor.execute(""" select  d.loc, sum(e.sal)
                     from emp  e, dept  d
                     where  e.deptno = d.deptno
                     group by d.loc """) 
                                                   
row = cursor.fetchall()   
emp = pd.DataFrame(row)

emp.index = list(emp[0])
emp.plot( kind='bar', color='red')


■ Q-458. 월급이  3000 이상인 사원들의 이름과 월급을 출력하시오 !

  select ename, sal
    from emp
        where sal >= 3000;

■ Q-459.  직업이 SALESMAN 인 사원들의 이름과 월급과 직업을 출력하는데
월급이 높은 사원부터 출력하시오 !

 select ename, sal, job
   from emp
   where job='SALESMAN'
        order by sal desc; 

■ Q-460.  이름과 부서위치를 출력하시오 !

select  e.ename, d.loc
  from emp e, dept  d
       where e.deptno = d.deptno;

■ Q-461.  JONES 보다 더 많은 월급을 받는 사원들의 이름과 월급을
출력하시오 ! (서브쿼리문)

mysql> select  ename, sal
    ->  from emp
    ->  where  sal > ( select sal
    ->                   from emp
    ->                   where ename='JONES');

■ Q-462. 이름, 월급, 순위를 출력하시오 ! 
(순위는 월급이 높은 순으로 순위를 부여하세요 !)

mysql> select ename, sal, rank() over (order by sal desc) 순위
    ->  from emp; 


■ Q-463.  이름, 커미션을 출력하는데 커미션이 null 인 사람들은 0 으로 
출력하시오 !

select  ename, ifnull( comm, 0 )
  from emp; 

■ Q-464.  오늘날짜를 출력하시오 !

select sysdate(); 

설명: mySQL 은 오라클과 같은 dual 이 없음

■ Q-465.  부서번호, 부서번호별 토탈월급을 출력하시오 !

select deptno, sum(sal)
   from emp
       group by deptno;

■ Q-466. 위의 결과를 다시 출력하는데 맨 아래에 전체 토탈월급이 출력되게
하시오 !

 select deptno, sum(sal)
    from emp
      group by deptno  with rollup;

※ 이제 부터가 아주 중요하니 잘 들어주세요 ~~~

■ Q-467.  scott 의 월급을 0 로 변경하세요 

update  emp
  set  sal = 0
      where  ename='SCOTT'; 

rollback;

※  mysql 은 오라클과는 다르게 기본 자동커밋이 활성화 되어있다.
자동 커밋되어버려서 rollback 을 할 수 없습니다. 
 mySQL 사용자들이 많이 하는 실수중에 하나이니 주의하세요

■ Q-468. 자동 커밋이 활성화 되어져 있는지 확인해보세요 

select @@autocommit; 

설명: 숫자 1이면 autocommit 이 켜있는것입니다.

■ Q-469. 자동 커밋 기능을 끄세요 

set  autocommit = FALSE; 

select @@autocommit;

설명: 숫자가 0 이면 자동 커밋기능이 비활성화 된것 입니다.

■ Q-470. KING 의 월급을 0 로 변경하세요 

설명: mySQL  을 켰으면 제일 먼저 확인해야하는것이 자동 커밋이 
 활성화 되었는지 확인하는게 아주 중요합니다. !!!!!!!!!!!

■ Q-471.   오라클의 listagg 함수와 같은 기능인 group_concat 을 이용해서
부서번호, 부서번호별로 속한 사원들의 이름을 가로로 
출력하시오 !

select deptno, group_concat(ename)
 from  emp
     group by deptno;

■ Q-472.  mySQL 과 파이썬을 연동해서  mySQL 의 emp 테이블을
파이썬에서 출력하시오 !

먼저 아나콘다 프롬프트 창을 열고  pymysql 을 설치하세요 !

conda  install  pymysql 


import  pymysql             # mySQL 과 파이썬 연동할 때 필요한 모듈
import  pandas as pd

conn = pymysql.connect(host="localhost", user="root",password="oracle",
                       db="orcl",charset="utf8")

curs = conn.cursor()
sql = "select * from emp"
curs.execute(sql)
rows = curs.fetchall()
colname = curs.description
col = []
for i in colname:
    col.append(i[0].lower())
    
emp = pd.DataFrame(list(rows),columns=col)
print(emp[['ename', 'sal']] )

■ Q-473.  직업, 직업별 토탈월급을 출력하시오 !

import pymysql
import pandas as pd

conn = pymysql.connect(host="localhost", user="root",password="oracle",
                                   db="orcl",charset="utf8")

curs = conn.cursor()
sql = "select job, sum(sal) from emp group by job "
             
curs.execute(sql)
rows = curs.fetchall()

emp = pd.DataFrame(rows)
print(emp)

■ Q-474.  위의 결과를 막대그래프로 시각화 하시오 !

import pymysql
import pandas as pd

conn = pymysql.connect(host="localhost", user="root",password="oracle",
                       db="orcl",charset="utf8")

curs = conn.cursor()
sql = """ select job, sum(sal) from emp group by job """
             
curs.execute(sql)
row = curs.fetchall()  
emp = pd.DataFrame(row)
print(emp)

emp.index = list(emp[0])
emp.plot( kind='bar', color='red')

 
■ Q-475.  (오늘의 마지막 문제 )
오라클과  파이썬을 연동하여 아래의  사원들을 검색하시오 !이름과 월급과 부서번호와 자기가 속한 부서번호의 평균월급을 출력하는데 자신의 월급이 자기가 속한 부서번호의 평균월급보다 더 큰 사원들만 출력하시오 !

import cx_Oracle
import pandas as pd
   
dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 
db = cx_Oracle.connect('scott','tiger',dsn) 
cursor = db.cursor()
cursor.execute("""select e.ename, e.sal, e.deptno, v.부서평균
                    from emp e, (select deptno, avg(sal) 부서평균 from emp group by deptno)v
                        where e.deptno = v.deptno and e.sal > v.부서평균 """)
row = cursor.fetchall() 
emp = pd.DataFrame(row)
print(emp)
