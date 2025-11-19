### 객체
#### 객체
- Object
  - 키로 구분된 데이터 집합을 저장하는 자료형

#### 구조 및 속성
- 객체 구조
  - 중괄호('{}')를 이용해 작성
  - 중괄호 안에는 key: value 쌍으로 구성된 속성(property)를 여러 개 작성 가능
  - key는 문자형만 허용
  - value는 모든 자료형 허용
  - 점('.') 표기법 또는 대괄호('[]') 표기법으로 객체 속성에 접근
    - 평소에는 점 표기법을 사용하는것을 추천
  - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능
- in 연산자
  - 속성이 객체에 존재하는지 여부를 확인
  - 객체의 키나 배열의 인덱스 존재 여부를 확인하는 연산자
  - 객체에서 값의 포함 여부를 확인하려면 'in'대신 'hasOwnProperty()' 메서드를 사용하는 것이 올바른 방법임
```js
console.log('greeting' in user) // true
console.log('country' in user) // false
```

#### 메서드
- Method
  - 객체 속성에 정의된 함수
  - object.method() 방식으로 호출
  - 메서드는 객체가 행동할 수 있게 함
- Method 기본 문법
  - 메서드도 값이 함수인 속성
```js
const myObj2 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach(function (number) {
      console.log(this) // window
    })
  }
}

console.log(myObj2.myFunc())
```
  - 메서드는 일반 함수와 달리 자신이 속한 객체의 다른 속성들에 접근할 수 있음

#### This
- 'this' keyword
  - Method는 'this' 키워드를 사용해 객체 자신의 속성이나 메서드에 접근하여 특정 작업을 수행할 수 있음
```js
const person = {
  name: 'Alice',
  greeting: function () {
    return `Hello my name is ${this.name}`
  },
}

console.log(person.greeting()) // Hello my name is Alice
```
  - JavaScript에서 this는 함수를 `호출하는 방법`에 따라 가리키는 대상이 달라짐
    - 일반 함수에서의 단순 호출이라면, 대상은 전역 객체
    - 객체에서의 메서드 호출이라면, 대상은 메서드를 호출한 객체
```js
const myFunc = function () {
  return this
}

console.log(myFunc()) // window
```
```js
const myObj = {
  data: 1,
  myFunc: function () {
    return this
  }
}

console.log(myObj.myFunc()) // myObj
```
- 중첩된 함수에서의 this의 문제점
  - forEach의 인자로 전달된 콜백 함수는 일반 함수로 호출되므로, this는 전역 객체를 가리킴
  - 해결책
    - `화살표 함수는 자신만의 this를 가지지 않음`
    - 따라서 외부함수(myFunc)에서의 this 값을 가져옴
- 'this' 정리
  - JavaScript의 함수는 호출될 때 this를 암묵적으로 전달 받음
  - JavaScript에서 this는 함수가 `호출되는 방식`에 따라 결정되는 현재 객체를 나타냄
  - Python의 self와 Java의 this가 선언 시점에 이미 값이 정해지는 것과 달리, JavaScript의 this는 `함수가 호출될 때 동적으로 결정`
  - 장점
    - 함수(메서드)를 하나만 만들어 여러 객체가 공유하여 각자 자신의 데이터로 동작하게 할 수 있음
  - 단점
    - 유연함이 실수로 이어질 수 있음

#### 추가 객체 문법
- `단축 속성`
  - 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우, 단축 구문을 사용할 수 있음
```js
const name = 'Alice'
const age = 30
const user = {
  name,  // name: name,
  age,   // age: age,
}
```
- 단축 메서드
  - 메서드 선언 시 function 키워드 생략 가능
```js
const myObj1 = {
  myFunc() {     // myFunc: function () {
    return 'Hello'
  }
}
```
- 계산된 속성
  - 키가 대괄호([])로 둘러싸여 있는 속성
  - 고정된 값이 아닌 변수 값을 사용할 수 있음
  - 대괄호 안의 표현식이 너무 복잡해지면, 어떤 키가 생성될 지 파악하기 어려워 가독성이 떨어질 수 있음
  - 동적으로 키를 만들다 보면 의도치 않게 같은 이름의 키가 생성되어, 기존 값이 덮어써질 위험이 있음
```js
const product = prompt('물건 이름을 입력해주세요')
const prefix = 'my'
const suffix = 'property'
const bag = {
  [product]: 5,
  [prefix + suffix]: 'value',
}
console.log(bag)  // {연필: 5, myproperty: 'value'}
```
- 구조 분해 할당
  - 배열 또는 객체를 분해하여 객체 속성을 변수에 쉽게 할당할 수 있는 문법
```js
const userInfo = {
  firstName: 'Alice',
  userId: 'alice123',
  email: 'alice123@gmail.com'
}
const { firstName } = userInfo  // const firstName = userInfo.firstname
const { firstName, userId} = userInfo  // const userId = userInfo.userId
const { firstName, userId, email } = userInfo  // const email = userInfo.email
```
- 객체와 전개 구문
  - 객체 복사
    - 객체 내부에서 객체 전개
  - 얕은 복사에 활용 가능
```js
const obj = {b: 2, c: 3, d: 4}
const newObj = {a: 1, ...obj, e: 5}
console.log(newObj) // {a: 1, b: 2, c: 3, d: 4, e: 5}
```
- 유용한 객체 메서드
  - Object.keys()
    - Object의 key값들을 리스트로 반환
  - Object.values()
    - Object의 value값들을 리스트로 반환
  - Object.entries()
    - Object의 key와 value값들을 한 쌍으로 묶은 리스트로 반환
- Optional chaining ('?.')
  - 속성이 없는 중첩 객체에 접근하려 할 때 에러 발생 없이 안전하게 접근하는 방법
  - 만약 참조 대상이 null 또는 undefined라면 에러가 발생하는 것 대신 평가를 멈추고 undefined를 반환
```js
console.log(user.address.street) // Uncaught TypeError
console.log(user.address?.street) // undefined
```
  - 장점
    - 참조가 누락될 가능성이 있는 경우 연결된 속성으로 접근할 때 더 짧고 간단한 표현식을 작성할 수 있음
    - 어떤 속성이 필요한지에 대한 보증이 확실하지 않는 경우, 객체의 내용을 보다 편리하게 탐색할 수 있음
    - 만약 Optional chaining을 사용하지 않는다면 '&&'연산자를 사용해야 함
  - 주의사항
    - Optional chaining은 존재하지 않아도 괜찮은 대상에만 사용해야 함(남용 X)
      - 왼쪽 평가대산이 없어도 괜찮은 경우에만 선택적으로 사용할 것
      - 중첩 객체를 에러 없이 접근하는 것이 사용 목적이기 때문
    - Optional chaining 앞의 변수는 반드시 선언되어 있어야 함

#### JSON
- JSON(JavaScript Object Notation)
  - JavaScript의 Object와 유사한 구조를 가지고 있지만, JSON은 일정한 형식을 가진 `문자열`임
  - JavaScript에서 JSON을 사용하기 위해서는 Object 자료형으로 변경해야 함
- Object -> JSON
  - JSON.stringfy()를 사용해 객체를 문자열로 변환
```js
const jsObject = {
  coffee: 'Americano',
  iceCream: 'Cookie and cream',
}

// Object -> JSON
const objToJson = JSON.stringify(isObject)
```
- JSON -> Object
  - JSON.parse()를 사용해 문자열을 객체로 변환
```js
// JSON -> Object
const jsonToObj = JSON.parse(objToJson)
```

#### 배열
- 배열(Array)
  - 순서가 있는 데이터 집합을 저장하는 자료구조
- 배열 구조
  - 대괄호('[]')를 이용해 작성
  - 요소의 자료형은 제약 없음
  - length 속성을 사용해 배열에 담긴 요소 개수 확인 가능

#### 배열 메서드
- push()
  - 배열 끝에 요소를 추가
  - 원본 배열을 직접 수정
  - 반환 값: 추가된 후의 새로운 배열의 길이
  - array.push(요소)로 사용
- pop()
  - 배열 끝 요소를 제거
  - 원본 배열을 직접 수정
  - 반환 값: 제거한 요소
  - array.pop(요소)로 사용
- unshift()
  - 배열 앞에 요소를 추가
  - 배열의 모든 요소를 뒤로 한 칸씩 밀어야 하므로, 배열이 클수록 성능이 저하(가급적 사용 x)
- shift()
  - 배열 앞 요소를 제거하고, 제거한 요소를 반환
  - 배열의 모든 요소를 당겨와야 하므로, 배열이 클수록 성능이 저하(가급적 사용 x)

### Array Helper Methods
- 배열 조작을 보다 쉽게 수행할 수 있는 특별한 메서드 모음
- 배열의 각 요소를 순회하며 각 요소에 대해 함수(콜백함수)를 호출
- 메서드 호출 시 인자로 함수(콜백함수)를 받는 것이 특징

#### 콜백함수
- 콜백함수
  - 다른 함수에 인자로 전달되는 함수
  - 외부 함수 내에서 호출되어 일종의 루틴이나 특정 작업을 진행
```js
const numbers1 - [1, 2, 3]

numbers1.forEach(
  function (num) {
    console.log(num)
  }
)
// 1
// 2
// 3
```
```js
const numbers2 - [1, 2, 3]
const callBackFunction = function (num) {
  console.log(num)
}

numbers2.forEach(callBackFunction)
```
- 주요 Array Helper Methods
  - forEach
    - 배열 내의 모든 요소 각각에 대해 함수(콜백함수)를 호출
    - 반환값 없음
  - map
    - 배열 내의 모든 요소 각각에 대해 함수(콜백함수)를 호출
    - 함수 호출 결과를 모아 새로운 배열을 반환
  