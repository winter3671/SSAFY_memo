### Create a table
#### CREATE TABLE
- CREATE TABLE syntax
```sql
CREATE TABLE table_name(
  column_1 data_type constraints,
  column_2 data_type constraints,
  ...,
);
```
  - 각 필드에 적용할 데이터 타입 작성
  - 테이블 및 필드에 대한 제약조건(constraints) 작성
- PRAGMA
```sql
PRAGMA table_info('examples');
```
  - 테이블 schema(구조) 확인
- SQLite 데이터 타입
  - NULL: 아무런 값도 포함하지 않음
  - TEXT: 문자열
    - VARCHAR, CHAR은 TEXT에 포함
  - INTEGER: 정수
  - BLOB: 이미지, 동영상, 문서 등 바이너리 데이터
  - REAL: 부동 소수점
- 제약 조건(Constraints)
  - 테이블의 필드에 적용되는 규칙 또는 제한사항
  - 데이터의 무결성을 유지하고 데이터베이스의 일관성을 보장
- 대표 제약 조건 3가지
  - PRIMARY KEY
    - 해당 필드를 기본 키로 지정
    - `INTEGER 타입에만 적용`되며, INT, BIGINT 등과 같은 다른 정수 유형에는 적용 X
  - NOT NULL
    - 해당 필드에 NULL 값을 허용하지 않도록 지정
  - FOREIGN KEY
    - 다른 테이블과의 외래 키 관계를 정의
- AUTOINCREMENT 특징
  - 필드의 자동 증가를 나타내는 특수한 키워드
  - 주로 primary key 필드에 적용
  - INTEGER PRIMARY KEY AUTOINCREMENT가 작성된 필드는 항상 새로운 레코드에 대해 이전 최대 값보다 큰 값을 할당
  - 삭제된 값은 무시되며 재사용할 수 없게 됨

### Modifying table fields
#### ALTER TABLE
- ALTER TABLE 역할
![ALTER TABLE](수업자료/ALTER%20TABLE.png)
- ALTER TABLE ADD COLUMN syntax
```sql
ALTER TABLE
  table_name
ADD COLUMN
  column_definition;
```
  - ADD COLUMN 키워드 이후 추가하고자 하는 새 필드 이름과 데이터 타입 및 제약 조건 작성
  - 단, 추가하고자 하는 필드에 `NOT NULL`제약 조건이 있을 경우, NULL이 아닌 기본 값 설정 필요
  - 테이블 생성 시 정의한 필드는 기본 값이 없어도 NOT NULL 제약조건으로 생성됨
  - 내부적으로 Default value는 NULL으로 설정됨
- ALTER TABEL RENAME COLUMN syntax
```sql
ALTER TABLE
  table_name
RENAME COLUMN
  current_name TO new_name;
```
  - RENAME COLUMN 키워드 뒤에 이름을 바꾸려는 이름을 지정하고 TO 키워드 뒤에 새 이름을 지정
- ALTER TABLE DROP COLUMN syntax
```sql
ALTER TABLE
  table_name
DROP COLUMN
  column_name;
```
  - DROP COLUMN 키워드 뒤에 삭제 할 필드 이름 지정
- ALTER TABLE RENAME TO syntax
```sql
ALTER TABLE
  table_name
RENAME TO
  new_table_name;
```
  - RENAME TO 키워드 뒤에 새로운 테이블 이름 지정

### Delete a table
#### DROP TABLE
- DROP TABLE syntax
```sql
DROP TABLE table_name;
```

### Modifying data
#### Insert data
- INSERT syntax
```sql
INSERT INTO table_name (c1, c2, ...)
VALUES (v1, v2, ...);
```
  - INSERT INTO 절 다음에 테이블 이름과 괄호 안에 필드 목록 작성
  - VALUES 키워드 다음 괄호 안에 해당 필드에 삽입할 값 목록 작성

#### Update data
- UPDATE syntax
```sql
UPDATE table_name
SET column_name = expression,
[WHERE
  condition];
```
  - SET 절 다음에 수정할 필드와 새 값을 지정
  - WHERE 절에서 수정할 레코드를 지정하는 조건 작성
  - WHERE 절을 작성하지 않으면 모든 레코드를 수정
    - sql에서 대괄호는 선택의 의미를 가짐

#### Delete data
- DELETE syntax
```sql
DELETE FROM table_name
[WHERE
  condition];
```
  - DELETE FROM 절 다음에 테이블 이름 작성
  - WHERE 절에서 삭제할 레코드를 지정하는 조건 작성
  - WHERE 절을 작성하지 않으면 모든 레코드를 삭제

### Joining tables
#### INNER JOIN
- INNER JOIN syntax
```sql
SELECT
  select_list
FROM
  table_a
INNER JOIN table_b
  ON table_b.fk = table_a.pk
```
  - FROM 적 이후 메인 테이블 지정
  - INNER JOIN 절 이후 메인 테이블과 조인할 테이블을 지정
  - ON 키워드 이후 조인 조건을 작성
  - 조인 조건은 table_a와 table_b 간의 레코드를 일치시키는 규칙을 지정

#### LEFT JOIN
- LEFT JOIN syntax
```sql
SELECT
  select_list
FROM
  table_a
LEFT JOIN table_b
  ON table_b.fk - table_a.pk;
```
  - FROM 절 이후 왼쪽 테이블 지정
  - LEFT JOIN 절 이후 오른쪽 테이블 지정
  - ON 키워드 이후 조인 조건을 작성
    - 왼쪽 테이블의 각 레코드를 오른쪽 테이블의 모든 레코드와 일치시킴