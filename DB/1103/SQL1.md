### Database
#### Database란?
- 데이터베이스
  - 체계적으로 정리된 데이터의 모음
- 데이터
  - 저장이나 처리를 위해 변환된 정보
- 데이터베이스의 역할
  - CRUD(Create, Read, Update, Delete)

### Relational Database
#### Relational Database란?
- 관계형 데이터베이스
  - 데이터 간에 관계가 있는 데이터 항목들의 모음
  - 테이블, 행, 열의 정보를 구조화하는 방식
  - 서로 관련된 데이터 포인터를 저장하고, 이에 대한 액세스를 제공
- 데이터베이스 역할
  - 관계
    - 여러 테이블 간의 논리적 연결
    - 데이터를 각각의 테이블에 나눠 저장하되, 공통된 키 값을 통해 서로 연결하여 필요할 때 함께 조회하거나 조작할 수 있도록 함
    - 관계로 인해 두 테이블을 사용하여 데이터를 다양한 형식으로 조회할 수 있음
- 관계형 데이터베이스 관련 키워드
  - Table(Relation, 관계)
    - 데이터를 기록하는 곳
  - Field(Column, Attribute)
    - 각 필드에는 고유한 데이터 형식(타입)이 저장됨
  - Record(Row, Tuple)
    - 각 레코드에는 구체적인 데이터 값이 저장됨
  - Database(Schema)
    - 테이블의 집합
  - Primary Key(PK, 기본 키)
    - 각 레코드의 고유한 값
    - 관계형 데이터베이스에서 레코드의 식별자로 활용
  - Foreign Key(FK, 외래 키)
    - 테이블의 필드 중, 다른 테이블의 레코드를 식별할 수 있는 키
    - 다른 테이블의 기본 키를 참조
    - 각 레코드에서 서로 다른 테이블 간의 관계를 만드는 데 사용

### RDBMS
#### DBMS란?
- DBMS(Database Management System)
  - 데이터베이스를 관리하는 소프트웨어 프로그램
  - 데이터 저장 및 관리를 용이하게 하는 시스템
  - 데이터베이스와 사용자 간의 인터페이스 역할
  - 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움
- RDBMS(Relational Database Management System)
  - 관계형 데이터베이스 관리 소프트웨어 프로그램
  - 공통된 키를 통해 서로 `관계`를 맺고 함께 사용할 수 있게 해주는 시스템
- RDBMS 서비스 종류
  - SQLite
  - MySQL
  - PostgreSQL
  - Oracle Database
  - ...
- SQLite
  - 경향의 오픈 소스 데이터베이스 관리 시스템
  - 설치 없이 가볍게 실행 가능해 모바일 앱이나 소규모 프로그램에 적합
  
#### 데이터베이스 정리
- 데이터베이스 정리
  - Table은 데이터가 기록되는 곳
  - Table에는 행에서 고유하게 식별 가능한 기본 키라는 속성이 있으며,
  - 외래 키를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만들 수 있음
  - 데이터는 기본 키 또는 외래 키를 통해 결합(join)될 수 있는 여러 테이블에 걸쳐 구조화 됨

### SQL
#### SQL이란?
- SQL(Structure Query Language)
  - 테이블의 형태로 구조화 된 관계형 데이터베이스에게 요청을 질의(요청)
  - 데이터베이스에서 데이터베이스 관리 시스템(DBMS)에게 데이터를 찾아달라고 요청하는 `표준화된 요청서 양식`과 같음
  - 사람이 사용하는 모호한 말이 아닌 `명확하게 약속된 형식`에 따라 정확한 요청을 전달하는 언어
- SQL Syntax
```sql
SELECT column_name FROM table_name;
```
  - SQL 키워드는 대소문자를 구분하지 않음
    - 하지만 대문자로 작성하는 것을 권장(명시적 구분)
  - 각 SQL Statements의 끝에는 세미콜론(';')이 필요
    - 세미콜론은 각 SQL Statements을 구분하는 방법(명령어의 마침표)

#### SQL Statements
- SQL Statements
  - SQL을 구성하는 가장 기본적인 코드 블록
- SQL Statements의 유형
  - DDL: 데이터 정의
  - DQL: 데이터 검색
  - DML: 데이터 조작
  - DCL: 데이터 제어
![4가지 유형](수업자료/SQL%20Statements%204가지%20유형.png)

### Querying data
#### DQL
- DQL
  - 데이터 검색(Read)
  - SQL 키워드: SELECT

#### SELECT
- SELECT syntax
```sql
SELECT
  select_list
FROM
  table_name;
```
  - SELECT 키워드 이후 데이터를 선택하려는 필드를 하나 이상 지정
  - FROM 키워드 이후 데이터를 선택하려는 테이블의 이름을 지정
- SELECT 정리
  - 테이블의 데이터를 조회 및 반환
  - '*'를 사용하여 모든 필드 선택

#### ORDER BY
- ORDER BY syntax
```sql
SELECT
  select_list
FROM
  table_name
ORDER BY
column1 [ASC|DESC]
column2 [ASC|DESC]
...;
```
  - FROM clause 뒤에 위치
  - 하나 이상의 컬럼을 기준으로 결과를 오름차순(ASC, 기본 값), 내림차순(DESC)으로 정렬
- 정렬에서의 NULL
  - NULL값이 존재할 경우 오름차순 정렬 시 결과에 NULL이 먼저 출력

#### Filtering Data
- Filtering Data 관련 Keywords
  - Clause
    - DISTINCT
    - WHERE
    - LIMIT
  - Operator
    - BETWEEN
    - IN
    - LIKE
    - Comparison
    - Logical

#### DISTINCT
- DISTINCT syntax
```sql
SELECT DISTINCT
  select_list
FROM
  table_name;
```
  - SELECT 키워드 바로 뒤에 작성해야 함
  - SELECT DISTINCT 키워드 다음에 고유한 값을 선택하려는 하나 이상의 필드를 지정

#### WHERE
- WHERE syntax
```sql
SELECT
  select_list
FROM 
  table_name
WHERE
  search_condition;
```
  - FROM clause 뒤에 위치
  - search_condition은 비교연산자 및 논리연산자(AND, OR, NOT 등)를 사용하는 구문이 사용됨
  - python에서 if문의 역할
- NULL 비교
  - NULL은 '값이 존재하지 않음'이므로, '='연산자를 사용하면 결과가 UNKNOWN이 되어 기대한 결과를 얻지 못함
  - IS와 IS NOT을 사용해야 명시적 비교가 가능
- WildCard
  - '%'
    - 0개 이상의 문자열과 일치하는지 확인
  - '_':
    - 단일 문자와 일치하는지 확인

#### LIMIT
- LIMIT syntax
```sql
SELECT
  select_list
FROM
  table_name
LIMIT [offset,] row_count;
```
  - 하나 또는 두 개의 인자를 사용(0 또는 양의 정수)
  - row_count는 조회하는 최대 레코드 수를 지정

#### GROUP BY
- GROUP BY syntax
```sql
SELECT
  c1, c2, ..., cn, aggregate_function(ci)
FROM
  table_name
GROUP BY
  c1, c2, ..., cn;
```
  - FROM 및 WHERE 절 뒤에 배치
  - GROUP BY 절 뒤에 그룹화 할 필드 목록을 작성
- Aggregation Function
  - 집계 함수
  - 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수
  - SUM, AVG, MAX, MIN, COUNT
- HAVING
  - GROUP BY에서 WHERE을 대체하여 사용
  - GROUP BY 뒤에 HAVING을 붙여서 사용 가능