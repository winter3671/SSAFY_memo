### Many to many relationships
- Many to many relationships(M:N or N:M)
  - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우

#### 중개 모델
- 중개 모델
  - 다대다 관계에서 두 모델을 연결하는, 특별한 기능을 가진 모델

#### ManyToManyField
- ManyToManyField()
  - M:N 관계 설정 모델 필드
  - 이 필드를 설정하면 Django는 자동으로 중간 테이블(중개 모델)을 생성하여 각 모델 간의 관계를 관리
  - 모델 클래스 내부에 필드로 정의하며, `어느 모델에 정의해도 관계는 동일하게 유지`됨
  - 필드명은 다대다 관계를 나타내기 위해 복수형으로 작성 권장
- ManyToManyField 조작
  - .add() 메서드
    - 중개 테이블에 새로운 데이터를 추가할 때 사용
    - 인자로 연결할 대상 모델의 인스턴스를 넣어서 사용
  - .remove() 메서드
    - 중개 테이블에 있는 데이터를 삭제할 때 사용
    - 인자로 전달한 인스턴스를 중개 테이블에서 제거하며, 대상 객체 자체는 삭제되지 않음
- ManyToManyField 특징
  - M:N 관계 설정 시 사용하는 모델 필드
  - 어느 모델에서든 관련 객체에 접근할 수 있는 양방향관계
  - 동일한 관계는 한 번만 저장되며, 중복되지 않음
- ManyToManyField의 대표 인자
  - related_name
    - 역참조 이름을 변경할 때 설정하는 인자
  - symmetrical
    - 관계 설정 시 대칭에 대한 설정을 하는 인자
  - through
    - 직접 생성한 중개 테이블을 등록하는 인자

#### 'through' argument
- through 속성
  - 중개 테이블에 '추가 데이터'를 사용해 M:N 관계를 형성하려는 경우에 사용
  - ManyToManyField() 안에 through="추가 클래스" 형식으로 사용

#### ManyToManyField 인자
- 'related_name' argument
  - 역참조시 사용하는 manager name을 변경
    - 기본값인 '역참조모델명_set'을 다른 이름으로 변경할 때 사용
    - 이름을 변경하면 더 이상 기본 값을 사용할 수 없음
- 'symmetrical' argument
  - 관계 설정 시 대칭 유무 설정
  - ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용
  - 기본 값: True
    - symmetrical 값이 True이면, 자동으로 서로 참조하도록 함
- 'through' argument
  - 사용하고자 하는 중개모델을 지정
  - 일반적으로 `추가 데이터를 M:N 관계와 연결하려는 경우`에 활용