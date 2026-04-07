<h1>1. API 도큐먼트 (p.494)</h1>
<ul>
  <li>
    자바 API(application Programming Interface) 도큐먼트는 클래스와 인터페이스의 집합인 <strong>라이브러리를 사용하는 방법</strong>을 기술한 것이다. 
  </li>
  <li>
    https://docs.oracle.com/en/java/javase/index.html
  </li>
  <li>
    API 도큐먼트를 활용하는 방법을 다루고 있기에 필요할 떄 참고.
  </li>
</ul>

<br><br>

<h1>2. java.base 모듈 (p.498)</h1>
<ul>
  <li>
    java.base는 <strong>모든 모듈이 의존</strong>하는 기본 모듈로, 모듈 중 유일하게 <strong>requires를 하지 않아도 사용</strong>할 수 있다.
  </li>
  <li>
    java.base에 속한 주요 패키지와 용도를 정리해 둔 표를 참고할 수 있다.
  </li>
</ul>

<br><br>

<h1>3. Object 클래스</h1>
<ul>
  <li>
    클래스를 선언할 때 <strong>extends 키워드</strong>로 다른 클래스를 상속하지 않으면 <strong>암시적으로 java.lang.Object</strong>를 상속하게 된다.
  </li>
    <ul>
      <li>
        따라서 결국 자바의 모든 클래스는 <strong>Object의 자식</strong>이거나 <strong>자손 클래스</strong>이다.
      </li>
      <li>
        따라서 <strong>Object가 가진 메소드</strong>는 <strong>모든 객체</strong>에서 사용할 수 있다.
      </li>
    </ul>
</ul>

<br>

<h2>3-1. 객체 동등 비교</h2>
<ul>
  <li>
    Object의 <strong>equals() 메소드</strong>는 객체의 <strong>번지를 비교</strong>하고 <strong>boolean 값</strong>을 리턴한다.
  </li>
  <li>
    equals() 메소드의 메개변수 타입은 <strong>Object</strong>이다.
    → Object는 <strong>모든 클래스의 조상</strong>이다.
    → 따라서 <strong>자동 타입 변환</strong>에 의해 모든 객체가 매개값으로 대입될 수 있다.
  </li>
  <li>
    equals() 메소드는 비교 연산자 ==과 <strong>동일한 결과(boolean)</strong>를 리턴한다.
  </li>
    <ul>
      <li>
        <strong>equals()</strong>는 <strong>값을 비교</strong>하고, <strong>==</strong>는 <strong>주소</strong>를 비교한다는 차이가 있다.
      </li>
      <li>
        다시 이야기하면 equals() 메소드는 재정의해서 <strong>동등 비교용</strong>으로 사용된다.
      </li>
    </ul>
</ul>

<br>

<h2>3-2. 객체 해시코드</h2>
<ul>
  <li>
    객체 해시코드란 객체를 식별하는 <strong>정수</strong>를 의미한다.
  </li>
  <li>
    Object의 <strong>hashCode() 메소드</strong>는 객체의 <strong>메모리 번지</strong>를 이용해 해시코드를 생성하기에 <strong>객체마다 다른 정수값</strong>을 리턴한다.
  </li>
  <li>
    hashCode() 매소드의 용도는 equals()와 유사하게 <strong>두 객체가 동등</strong>한지 비교할 때 주로 사용된다.
  </li>
  <li>
    hashCode()도 equals()와 마찬가지로 객체의 데이터를 기준으로 <strong>재정의</strong>해서 <strong>새로운 정수값을 리턴</strong>하도록 하는 것이 일반적이다.
  </li>
    <ul>
      <li>
        <strong>객체</strong>가 다르더라도 <strong>내부 데이터</strong>가 동일하다면 같은 정수값을 리턴하기 위해 사용한다.
      </li>
    </ul>
  <li>
    자바는 두 객체가 동등함을 비교할 때 hashCode()와 equals() 메소드를 같이 사용하는 경우가 많다.
  </li>
    <ul>
      <li>
        <strong>hashCode()</strong>: 리턴하는 정수값이 같은지 먼저 확인한다.
      </li>
      <li>
        <strong>equals()</strong>: hashCode가 같더라도 <strong>실제 객체의 내용</strong>이 다른 경우가 있기에 한 번 더 확인한다.
      </li>
    </ul>
  <li>
    나중에 배우는 HashSet은 동등 객체를 <strong>중복 저장하지 않는다</strong>는 특징이 있다.
  </li>
    <ul>
      <li>
        HashSet()은 hashCode()와 equals() 메소드를 활용하여 동등 객체인지 판단한다.
      </li>
    </ul>
</ul>

```java
// 1. 해시 정의
public int hashCode();
```

<br>

<h2>3-3. 객체 문자 정보</h2>
<ul>
  <li>
    Object의 <strong>toString() 메소드</strong>는 객체의 <strong>문자 정보</strong>를 리턴한다.
  </li>
    <ul>
      <li>
        객체의 문자 정보란 객체를 <strong>문자열로 표현한 값</strong>을 의미한다.
      </li>
      <li>
        Object의 toString() 메소드는 기본적으로 <strong>'클래스명@16진수해시코드'</strong>로 구성된 문자열을 리턴한다.
      </li>
    </ul>
  <li>
    객체의 문자 정보가 중요한 경우 Object의 toString() 메소드를 재정의하여 <strong>간결하고 유익한 정보</strong>를 리턴하도록 해야 한다.
  </li>
    <ul>
      <li>
        <strong>Date 클래스</strong>는 toString()을 재정의하여 <strong>날짜와 시간</strong>을, <strong>String 클래스</strong>는 toString()을 재정의하여 <strong>저장된 문자열</strong>을 반환하도록 하고 있다. 
      </li>
    </ul>
  <li>
    System.out.println() 메소드는 <strong>기본타입이거나 문자열</strong>일 경우 <strong>해당 값</strong>을 그대로 출력한다.
  </li>
    <ul>
      <li>
        <strong>매개값</strong>이 객체일 경우에는 <strong>toString()을 호출</strong>하여 리턴값을 출력한다.
      </li>
    </ul>
</ul>

```java
// 1. toString()를 활용한 
Object obj = new Object();  // Object 타입의 객체 하나 생성

// obj의 정보를 문자열로 바꿔서 출력
// 기본 toString()은 "클래스이름@해시값(16진수)" 형태로 만들어줌
System.out.println(obj.toString());

// 결과
// - java.lang.Object → 객체의 클래스 이름
// - @ → 구분자
// - de6ced → obj의 hashCode 값을 16진수로 바꾼 것 (객체 식별용 값)
java.lang.Object@de6ced
```

<br><br>

<h1>3-4. 레코드 선언</h1>
<ul>
  <li>
    데이터 전달을 위한 DTO(Data Transfer Object)를 작성할 때 <strong>반복적으로 사용되는 코드를 줄이기 위해</strong> Java 14부터 record가 도입되었다.
  </li>
</ul>

```java
// 1. Person DTO 사례
// Person DTO
public class Person {
  // 데이터 읽기만 가능하도록 private final 선언.
  private final String name;
  private final int age;

  // 생성자.
  public Person(String name, int age) {
    this.name = name;
    this.age = age;
  }
  
  // Getter 메소드.
  public String name() { return this.name; }
  public int age() {return this.age; }

  // 각 메소드 재정의.
  // 동등 비교를 위한 hashCode 오버라이드.
  @Override
  public int hashCode() { ... }

  // 동등 비교를 위한 equals() 오버라이드.
  @Override
  public boolean equals(Object obj) { ... }

  // 의미 있는 문자열 출력을 위한 toString() 오버라이드.
  @Override
  public String toString() { ... }
}

// 2. record 활용.
public record Person(String name, int age) {
/*
< 컨파일 시 변경점들 > 
- 변수의 타입과 이름을 사용해 private final 필ㄷ 자동 생성.
- 생성자 및 Getter 메소드 자동 추가.
- hashCode(), equals(), toString() 메소드를 재정의한 코드로 자동 추가.
*/
}
```

<br><br>

<h2>3-5. 롬복 사용하기</h2>
<ul>
  <li>
    롬복(Lombok)은 JDK에 포함된 표준 라이브러리는 아니지만 즐겨 사용하는 <strong>자동 코드 생성 라이브러리</strong>이다.
  </li>
  <li>
    record와 마찬가지로 DTO 클래스를 작성할 때 Getter, Setter, hasCode(), equals(), toString() 메소드를 자동 생성한다.
  </li>
    <ul>
      <li>
        필드는 record와 달리 <strong>final이 아니다</strong>.
      </li>
      <li>
        값을 읽는 Getter는 <strong>getXxx(또는 isXxx)</strong>로, 값을 변경하는 Setter는 <strong>setXxx</strong>로 생성된다.
      </li>
        <ul>
          <li>
            getXxx와 setXxx는 JavaBeans의 정식 Getter와 Setter이다.
          </li>
        </ul>
    </ul>
  <li>
    나머지는 이클립스 세팅이기에 skip.
  </li>
  <li>
    다양한 어노테이션을 활용해 다양한 방법으로 활용할 수 있다.
  </li>
</ul>

<br><br>

<h1>4. System 클래스</h1>
<ul>
  <li>
    <strong>java.lang 패키지</strong>에 속하는 <strong>System 클래스</strong>를 이용하면 <strong>운영체제의 일부 기능</strong>을 이용할 수 있다.
  </li>
    <ul>
      <li>
        기본적으로 자바는 JVM 위에서 실행되기에 운영체제의 모든 기능에 접근이 어렵다.
      </li>
    </ul>
  <li>
    System 클래스의 정적(static) 필드와 메소드를 이용하면 프로그램 종료, 기보드 입력, 콘솔(모니터) 출력, 현재 시간 읽기, 시스템 프로퍼티 읽기 등이 가능하다.
  </li>
  <li>
    정적 멤버와 용도는 p514 참고.
  </li>
</ul>

<br>

<h2>4-1. 콘솔 출력</h2>
<ul>
  <li>
    <strong>out 필드</strong>를 이용하면 <strong>콘솔에 원하는 문자열을 출력</strong>할 수 있다.
  </li>
  <li>
    <strong>err 필드</strong>도 out 필드와 동일하지만, 콘솔 종류에 따라 에러 내용이 <strong>빨간색</strong>으로 출력된다는 차이가 있다.
  </li>
</ul>

<br>

<h2>4-2. 키보드 입력</h2>
<ul>
  <li>
    자바는 키보드로부터 입력된 키를 읽기 위해 System 클래스에서 in 필드를 제공한다.
  </li>
  <li>
    in 필드롤 통해 read() 메소드를 호출하면 입력된 키의 코드값을 얻을 수 있다.
  </li>
    <ul>
      <li>
        키 코드는 각 키에 부여되어 있는 번호이다.
      </li>
    </ul>
  <li>
    read() 메소드는 <strong>'Enter'</strong>를 누르기 전까지는 <strong>대기 상태</strong>이고, 'Enter'를 누른 뒤 키들을 하나씩 읽기 시작한다.
  </li>
  <li>
    read() 메소드는 <strong>IO Exception</strong>을 발생시킬 수 있기에 예외 처리가 필요하다.
  </li>
</ul>

```java
// 1. in필드의 read() 메소드 활용.
int keyCode = System.in.read();
```

<br>

<h1>4-3. 프로세스 종료</h1>
<ul>
  <li>
    운영체제는 <strong>실행 중인 프로그램</strong>을 <strong>프로세스(process)</strong>로 관린한다.
  </li>
  <li>
    자바 프로그램 시작
    <br>→ JVM 프로세스 생성
    <br>→ 생성된 프로세스가 main() 메소드 호출
  </li>
  <li>
    프로세스를 강제 종료하고 싶다면 <strong>System.exit() 메소드</strong>를 사용한다.
  </li>
    <ul>
      <li>
        exit() 메소드는 <strong>int 매개값</strong>을 필요로하며 이를 <strong>종료 상태값</strong>이라 한다.
      </li>
        <ul>
          <li>
            종료 상태값에 상관없이 <strong>0</strong>은 정상 종료, <strong>1 혹은 -1</strong>은 비정상종료를 의미한다.
          </li>
        </ul>
      <li>
        Java 17 이전에는 SecurityManager를 통해 종료 상태를 활용한 특정 행위가 가능하였으나 이후 버전에서는 불가하다.
      </li>
    </ul>
</ul>

<br>

<h2>4-4. 진행 시간 읽기</h2>
<ul>
  <li>
    System. 클래스의 <strong>currentTimeMillis() 메소드</strong>와 <strong>nanoTime() 메소드</strong>는 <strong>1970년 1월 1일 0시</strong>부터 시작해서 현재까지 진행된 시간을 리턴한다.
  </li>
    <ul>
      <li>
        <strong>long currentTImeMillis()</strong>: <strong>1/1000초</strong> 단위로 진행된 시간을 리턴.
      </li>
      <li>
        <strong>long nanoTime()</strong>: <strong>1/10^9초</strong> 단위로 진행된 시간을 리턴.
      </li>
    </ul>
  <li>
    프로그램의 <strong>시작과 끝</strong>에 읽고 차이를 구하면 <strong>프로그램 처리 시간</strong>을 구할 수 있다.
  </li>
</ul>

<br>

<h2>4-5. 시스템 프로퍼티 읽기</h2>
<ul>
  <li>
    <strong>시스템 프로퍼티(System Property)</strong>란 자바 프로그램이 <strong>시작</strong>될 때 <strong>자동 설정되는 시스템의 속성</strong>을 의미한다.
  </li>
    <ul>
      <li>
        예를 들면 운영체제 종류, 사용자 정보, 자바 버전 등이 있다.
      </li>
    </ul>
  <li>
    시스템 프로퍼티의 주요 속성 이름(key)과 값(value)에 대한 설명은 p520 참고.
  </li>
</ul>

<br><br>

<h1>5. 문자열 클래스</h1>
<ul>
  <li>
    문자열 클래스
  </li>
    <ul>
      <li>
        <strong>String</strong>: 문자열을 저장하고 조작할 때 사용.
      </li>
      <li>
        <strong>StringBuilder</strong>: <strong>효율적인</strong> 문자열 조작 기능이 필요할 때 사용.
      </li>
      <li>
        <strong>StringTokenizer</strong>: <strong>구분자</strong>로 연결된 문자열을 분리할 때 사용.
      </li>
    </ul>
</ul>

<br>

<h2>5-1. String 클래스</h2>
<ul>
  <li>
    <strong>String 클래스</strong>는 문자열을 <strong>저장</strong>하고 <strong>조작</strong>할 때 사용한다.
  </li>
  <li>
    문자열 리터럴은 <strong>자동으로 String 객체</strong>로 생성되지만, String 클래스의 <strong>다양한 생성자</strong>를 이용해서 직접 객체를 생성할 수도 있다.
  </li>
</ul>

```java
// 1. 기본 문자셋으로 바이트 배열을 문자열로 변환 (디코딩)
// - byte[]: 0~255 범위의 숫자들의 배열 (문자가 아니라 데이터 자체)
// - 디코딩: 이 숫자들을 문자로 해석하는 과정
// - 기본 문자셋: JVM/OS에 설정된 기본 인코딩 방식 사용
String str = new String(byte[] bytes);


// 2. 특정 문자셋으로 바이트 배열을 문자열로 변환 (디코딩)
// - byte[]: 문자로 변환되기 전의 원시 데이터
// - 디코딩: 지정한 규칙으로 바이트를 문자로 해석
// - charsetName: "UTF-8", "EUC-KR" 등 해석 방식 지정 (깨짐 방지)
String str = new String(byte[] bytes, String charsetName);
```

<br>

<h2>5-2. StringBuilder 클래스</h2>
<ul>
  <li>
    String은 문자열을 수정할 수 없기에 <strong>수정</strong>이 필요하다면 <strong>StringBuilder</strong>를 사용해야 한다.
  </li>
    <ul>
      <li>
        StringBuilder는 <strong>내부 버퍼(데이터를 저장하는 메모리)</strong>에 문자열을 저장해두고 그 안에서 <strong>추가, 수정, 삭제 작업</strong>을 하도록 설계되어 있따.
      </li>
    </ul>
  <li>
    String은 내부 문자열을 <strong>수정할 수 없으며</strong>, 내부 문자열을 변경할 수 있는 것 처럼 보여도 실제로는 <strong>새로운 String 객체를 생성</strong>한다.
  </li>
</ul>

```java
// ABC + DEF로 수정되는 것 처럼 보이지만,
// 실제로는 ABCDEF라는 새로운 String 객체를 생성한다.
String data = "ABC";
data += "DEF";
```

<br>

<h2>5-3. StringTokenizer 클래스</h2>
<ul>
  <li>
    문자열이 구분자(delimeter)로 연결되어 있는 경우 구분자를 기준으로 문자열을 분리할 때 String의 <strong>split() 메소드</strong>나 java.util 패키지의 <strong>StringTokenizer 클래스</strong>를 이용할 수 있다.
  </li>
    <ul>
      <li>
        <strong>split() 메소드</strong>: <strong>정규표현식</strong>으로 구분한다.
      </li>
      <li>
        <strong>StringTokenizer 클래스</strong>: <strong>문자</strong>로 구분한다.
      </li>
    </ul>
  <li>
    주로 split()은 <strong>여러 구분자</strong>를 다룰 때에, StringTokenizer는 <strong>하나의 구분자</strong>를 다룰 때에 사용한다.
  </li>
  <li>
    StringTokenizer 객체는 다음의 메소드를 이용할 수 있다.
  </li>
    <ul>
      <li>
        <strong>countTokens()</strong>: 분리할 수 있는 문자열의 <strong>총 수</strong>
      </li>
      <li>
        <strong>hasMoreTokens()</strong>: 남아 있는 문자열이 있는지 여부
      </li>
      <li>
        <strong>nextToken()</strong>: 문자열을 하나씩 가져옴.
      </li>
        <ul>
          <li>
            더 이상 가져올 문자열이 없다면 예외를 발생시키기에 미리 hasMoreTokens()로 확인하는 것이 좋다.
          </li>
        </ul>
    </ul>
</ul>

```java
// 1. 여러 종류의 구분자 구분 - split()
String data = "홍길동&이수홍,박연수,김자바-최명호";
String[] names = data.split("&|,|-");

// 2. 하나의 구분자를 구분하는 StringTokenizer
String data = "홍길동/이수홍/박연수";
StringTokenizer st = new StringTokenizer(data, "/");
```

<br><br>

<h1>6. 포장 클래스</h1>
<ul>
  <li>
    자바는 <strong>기본 타입(byte, char, short, int, long, float, double, boolean)의 값을 갖는 객체</strong>를 생성할 수 있으며 이런 객체를 <strong>포장(wrapper) 객체</strong>라 한다.
  </li>
  <li>
    포장 객체 생성을 위한 클래스는 <strong>java.lang 패키지</strong>에 포함되어 있다.
  </li>
    <ul>
      <li>
        char와 int 타입이 각각 Charactor와 Integer것을 제외하고 나머지 타입은 모두 첫 문자가 대문자 인것 외에 차이가 없다.
      </li>
    </ul>
  <li>
    포장 객체는 기본 타입의 값을 변경할 수 없고 <strong>단지 객체로 생성</strong>하는 데 목적이 있다.
  </li>
    <ul>
      <li>
        이런 객체가 필요한 이유는 15장에서 다룰 <strong>컬렉션 객체</strong> 때문이다.
      </li>
    </ul>
</ul>

<br>

<h2>6-1. 박싱과 언박싱</h2>
<ul>
  <li>
    기본 타입의 값을 <strong>포장 객체</strong>로 만드는 과정을 <strong>박싱(boxing)</strong>, 반대로 포장 객체에서 <strong>기본 타입을 얻는 과정</strong>을 <strong>언박싱(unboxing)</strong>이라 한다.
  </li>
  <li>
    박싱은 포장 클래스 변수에 <strong>기본 타입 값이 대입</strong>될 때 발생한다. 반면 언박싱은 기본 타입 변수에 <strong>포장 객체가 대입</strong>될 때 발생한다.
  </li>
    <ul>
      <li>
        언박싱은 <strong>연산 과정</strong>에서도 발생한다.
      </li>
    </ul>
</ul>

```java
// 1. 박싱과 언박싱
Integer obj = 100;    // 박싱
int value = obj;      // 언박싱
int value = obj + 50; // 언박싱 후 연산이 진행된다.
```

<br>

<h2>6-2. 문자열을 기본 타입 값으로 변환</h2>
<ul>
  <li>
    포장 클래스는 문자열을 <strong>기본 타입 값으로 변환</strong>할 때에도 사용된다.
  </li>
  <li>
    대부분의 포장 클래스에는 <strong>parse + 기본타입</strong> 명으로 된 <strong>정적(static) 메소드</strong>가 있다. 
  </li>
    <ul>
      <li>
        메소드는 문자열을 해당 <strong>기본 타입 값으로 변환</strong>한다.
      </li>
    </ul>
</ul>

<br>

<h2>6-3. 포장 값 비교</h2>
<ul>
  <li>
    포장 객체를 비교할 때에는 <strong>==</strong>와 <strong>!= 연산자</strong>를 사용할 수 없다. 연산 내부의 값을 비교하는 것이 아니라 <strong>포장 객체의 번지</strong>를 비교하기 때문이다.
  </li>
    <ul>
      <li>
        일부 <strong>값의 범위</strong>를 갖는 타입(boolean, char, byte, short, int)는 <strong>객체의 주소를 공유</strong>하기에 가능하다.
      </li>
      <li>
        그럼에도 포장 객체에 정확히 어떤 값이 저장될지 모르는 상황이라면 사용을 지양해야 한다.
      </li>
    </ul>
  <li>
    대신 <strong>equals() 메소드</strong>를 사용하여 <strong>내부 값을 비교</strong>할 수 있다.
  </li>
</ul>

```java
// 1. 포장 객체 번지 비교로 인해 false 반환.
Integer obj1 = 300;
Integer obj2 = 300;
System.out.println(obj1 == obj20);
```

<br><br>

<h1>7. 수학 클래스</h1>
<ul>
  <li>
    Math 클래스는 <strong>수학 계산</strong>에 사용할 수 있는 메소드를 제공하며 <strong>모두 정적(static)</strong>이며 Math 클래스로 <strong>바로 사용</strong>이 가능하다.
  </li>
  <li>
    각 메소드에 대해서는 p531 참고.
  </li>
  <li>
    random() 메소드는 <strong>0.0과 1.0 사이의 double 타입 난수</strong>를 리턴한다.
  </li>
  <li>
    난수를 얻는 또 다른 방법으로는 <strong>java.util.Random</strong> 클래스가 있다.
  </li>
    <ul>
      <li>
        Random() 객체를 생성할 때에 <strong>종자값 seed</strong>를 사용할 수 있다. 
      </li>
        <ul>
          <li>
            seed는 <strong>난수를 만드는 알고리즘</strong>에 사용되는 값으로, 종자값이 같으면 같은 난수를 얻는다.
          </li>
        </ul>
    </ul>
</ul>

```java
// 1. random을 통해 start와 start + n 사이의 n개의 수 중 하나 추출.
int num = (int) (Math.random() * n) + start;
```

<br><br>

<h1>8. 날짜와 시간 클래스</h1>
<ul>
  <li>
    자바는 <strong>java.util 패키지</strong>의 <strong>Date와 Calender</strong>를 통해 컴퓨터의 날짜 및 시각을 <strong>읽을</strong> 수 있다.
  </li>
  <li>
    자바는 <strong>java.time 패키지</strong>의 <strong>LocalDateTime</strong> 등의 클래스를 통해 날짜와 시간을 <strong>조작할</strong> 수 있다.
  </li>
</ul>

<br>

<h2>8-1. Date 클래스</h2>
<ul>
  <li>
    Date는 날짜를 표현하는 클래스로 <strong>객체 간 날짜 정보를 주고받을 때</strong> 사용하나 대부분 Deprecated 되어 <strong>Date() 생성자</strong>만 주로 사용된다.
  </li>
  <li>
    Date() 생성자는 컴퓨터의 <strong>현재 날짜</strong>를 읽어 <strong>Date 객체</strong>로 만든다.
  </li>
  <li>
    현재 날짜를 <strong>문자열</strong>로 얻고 싶다면 <strong>toString() 메소드</strong>를 사용할 수 있으나 <strong>영문</strong>으로 출력된다.
  </li>
    <ul>
      <li>
        원하는 문자열로 얻고 싶다면 <strong>SimpleDateFormat 클래스</strong>와 함께 사용해야 한다.
      </li>
    </ul>
</ul>

```java
// 1. Date 객체 생성.
Date now = new Date();
```

<br>

<h2>8-2. Calendar 클래스</h2>
<ul>
  <li>
    Calendar 클래스는 <strong>달력</strong>을 표현하는 <strong>추상 클래스</strong>이다.
  </li>
    <ul>
      <li>
        날짜와 시간을 계산하는 방법이 <strong>지역과 문화</strong>에 따라 다르기에 특정 역법에 따르는 달력은 <strong>자식 클래스</strong>로 구현하도록 되어 있다.
      </li>
      <li>
        특별한 역법을 사용하는 경우가 아니라면 직접 하위 클래스를 만들 필요없이 Calendar 클래스의 <strong>정적 메소드 getInstance() 메소드</strong>를 이용하면 <strong>컴퓨터에 설정된 시간대(TimeZone)</strong>를 기준으로 <strong>Calendar의 하위 객체</strong>를 얻을 수 있다.
      </li>
    </ul>
  <li>
    Calendar가 제공하는 날짜와 시간에 대한 정보를 얻기 위해서는 <strong>get() 메소드</strong>를 이용한다.
  </li>
    <ul>
      <li>
        get() 메소드의 매개값으로 <strong>Calendar에 정의된 상수</strong>를 줌녀 상수가 의미하는 값을 리턴한다.
      </li>
    </ul>
  <li>
    Calendar 클래스의 오버로딩된 다른 getInstance() 메소드를 이용하여 미국/로스앤젤레스 등 <strong>다른 시간대의 Calendar</strong>를 얻을 수 있다.
  </li>
    <ul>
      <li>
        알고 싶은 시간대의 TimeZone 객체를 얻어 getInstance() 메소드의 <strong>매개값</strong>으로 넘겨준다.
      </li>
    </ul>
  <li>
    America/Los_Angeles와 같은 시간대 ID는 <strong>TimeZone.getAvailableIDs() 메소드</strong>의 리턴 값 중하나를 활용할 수 있다.
  </li>
</ul>

```java
// 1. 컴퓨터의 시간대에 맞는 시간 객체 생성.
Calendar now = Calendar.getInstance();


// 2. Calendar에 정의된 상수로 결과 받기.
int year = now.get(Calendar.YEAR);         // 년도를 리턴
int month = now.get(Calendar.MONTH) + 1;   // 월을 리턴
int day = now.get(Calendar.DAY_OF_MONTH);  // 일을 리턴
int week = now.get(Calendar.DAY_OF_WEEK);  // 요일을 리턴
int amPm = now.get(Calendar.AM_PM);        // 오전/오후를 리턴
int hour = now.get(Calendar.HOUR);         // 시를 리턴
int minute = now.get(Calendar.MINUTE);     // 분을 리턴
int second = now.get(Calendar.SECOND);     // 초를 리턴


// 3. 다른 지역의 시간대를 매개값으로 다른 지역 시간대 얻기.
TimeZone timeZone = TimeZone.getTimeZone("America/Los_Angeles");
Calendar now = Calendar.getInstance( timeZone );
```

<br>

<h2>8-3. 날씨와 시간 조작</h2>
<ul>
  <li>
    Date와 Calendar는 날짜와 시간 정보를 얻기에 충분하지만 조작하지는 못한다.
  </li>
  <li>
    날짜 데이터를 조작하기 위해서는 <strong>java.time 패키지</strong>의 <strong>LocalDateTime 클래스가 제공하는 메소드</strong>를 활용할 수 있다. (p540 참고).
  </li>
</ul>

```java
// 1. LocalDateTime 클래스를 이용해 현재 컴퓨터 날짜와 시간 얻기.
LocalDateTime now = LocalDateTime.now();
```

<br>

<h2>8-4. 날짜와 시간 비교</h2>
<ul>
  <li>
    LocalDateTime 클래스에는 <strong>날짜와 시간을 비교</strong>할 수 있는 메소드도 제공된다.
  </li>
</ul>

```java
// 1. 비교를 위해 LocatDateTime 객체를 각각 int로 얻기.
LocalDateTime target = LocalDateTime.of(year, month, dayOfMonth, hour, minute, second);
```

<br><br>

<h1>9. 형식 클래스</h1>
<ul>
  <li>
    <strong>Format(형식) 클래스</strong>는 숫자 또는 날짜를 <strong>원하는 형태의 문자열</strong>로 변환해주는 기능을 제공한다.
  </li>
  <li>
    Format 클래스는 java.text 패키지에 포함되어 있다. (p543을 참고).
  </li>
</ul>

<br>

<h2>8-5. DecimalFormat</h2>
<ul>
  <li>
    DecimalFormat은 숫자를 <strong>형식화된 문자열</strong>로 변환하는 기능을 한다. (p544 참고).
  </li>
</ul>

```java
// 1. 패턴 정보와 함께 DecimalFormat 객체를 생성하고 
//    format() 메소드로 숫자를 제공하여 패턴에 따른 형식화된 문자열 얻기.
DecimalFormat df = new DecimalFormat("#,###.0");
String result = df.format(1234567.89) // 1,234,567.9
```

<br>

<h2>8-6. SimpleDateFormat</h2>
<ul>
  <li>
    SimpleDateFormat은 날짜를 형식화된 문자열로 변환한다. (p545 참고).
  </li>
  <li>
    패턴에는 <strong>자릿수</strong>에 맞게 기호를 반복해서 작성할 수 있다.
  </li>
</ul>

```java
// 1. 날짜 형식 지정 및 출력 예.
SimpleDateFormat sdf = new SimpleDateFormat("yyyy년 MM월 dd일");
String strDate = sdf.format(new Date()); // 현재 날짜를 지정된 형식 반환
```

<br><br>

<h1>10. 정규 표현식 클래스</h1>
<ul>
  <li>
    문자열이(예를 들어 사용자 입력) <strong>정해져 있는 형식</strong>으로 구성되어 있는지 검증해야하는 경우가 있다. 이때 <strong>정규 표현식(Regular Expression)</strong>을 사용한다.
  </li>
</ul>

<br>

<h2>10-1. 정규 표현식 작성 방법</h2>
<ul>
  <li>
    정규 표현식은 문자 또는 숫자와 관련된 표현과 반복 기호가 결합된 문자열이다. (p547 참고).
  </li>
</ul>

```java
// 02-123-1234 혹은 010-1234-5678 전화번호 정규 표현식 예.
(02|010)-\d{3,4}-\d{4}

// white@naver.com 정규 표현식 예.
\w+@\w+\. \w+(\.\w+)?
```

<br>

<h2>10-2. Pattern 클래스로 검증</h2>
<ul>
  <li>
    <strong>java.util.regex 패키지</strong>의 <strong>Pattern 클래스</strong>는 정규 표현식으로 문자열을 검증하는 <strong>matches() 메소드</strong>를 제공한다.
  </li>
    <ul>
      <li>
        첫 번째 매개값은 <strong>정규 표현식</strong>, 두 번째 매개값은 <strong>검증할 문자열</strong>이다.
      </li>
    </ul>
  <li>
    검증한 후의 결과는 <strong>boolean 타입</strong>으로 리턴된다.
  </li>
  <li>
    '\'는 이스케이프 문자열로 활용될 수 있음을 주의해야 한다.
  </li>
</ul>

<br><br>

<h1>11. 리플렉션</h1>
<ul>
  <li>
    자바는 클래스와 인터페이스의 메타 정보를 <strong>Class 객체</strong>로 관리한다.
  </li>
    <ul>
      <li>
        메타 정보란 <strong>패키지의 정보, 타입 정보, 멤버(생성자, 필드, 메소드) 정보</strong> 등을 말한다.
      </li>
    </ul>
  <li>
    메타 정보를 프로그램에서 읽고 수정하는 행위를<strong> 리플렉션(reflection)</strong>이라 한다.
  </li>
</ul>

```java
// 1. 메타 정보를 얻는 방법.
// 1-1. 클래스로 얻기.
Class clazz = String.class; // Class clazz = 클래스이름.class;
Class clazz = Class.forName("java.lang.String"); // Class clazz = Class.forName("패키지...클래스이름");
// 1-2. 객체로부터 얻기.
String str = "김자바";
Class clazz = str.getClass(); // Class clazz = 객체참조변수.getClass();
```

<br>

<h2>11-1. 패키지와 타입 정보 얻기</h2>
<ul>
  <li>
    패키지와 타입(클래스, 인터페이스) 이름 정보는 다음 메소드를 통해 얻을 수 있다.
  </li>
    <ul>
      <li>
        Package getPackage(): 패키지 정보 읽기.
      </li>
      <li>
        String getSimpleName(): 패키지를 제외한 타입 이름.
      </li>
      <li>
        String getName(): 패키지를 포함한 전체 타입 이름.
      </li>
    </ul>
</ul>

<br>

<h2>11-2. 멤버 정보 얻기</h2>
<ul>
  <li>
    타입(클래스, 인터페이스)이 가지고 있는 멤버 정보는 다음 메소드를 통해 얻을 수 있다.
  </li>
    <ul>
      <li>
        Constructor[]getDeclaredConstructors(): 생성자 정보 읽기
      </li>
      <li>
        Field[]getDeclaredFields(): 필드 정보 읽기
      </li>
      <li>
        Method[]getDeclaredMethods(): 메소드 정보 읽기
      </li>
    </ul>
  <li>
    Constructor, Field, Method 클래스는 모두 <strong>java.lang.reflect 패키지</strong>에 존재하며 각각 생성자, 필드, 메소드에 대한 선언부 정보를 제공한다.
  </li>
</ul>

<br>

<h2>11-3. 리소스 경로 얻기</h2>
<ul>
  <li>
    Class 객체는 <strong>클래스 파일(*.class)</strong>의 경로 정보를 통해 <strong>상대 경로</strong>에 있는 다른 리소스 파일의 정보를 얻을 수 있다.
  </li>
  <li>
    <strong>URL getResource(String name)</strong>은 URL 정보가 담긴 <strong>URL 객체</strong>를 리턴한다.
  </li>
  <li>
    <strong>getResourceAsStream()</strong>은 파일의 내용을 읽을 수 있도록 <strong>InputStream 객체</strong>를 리턴한다.
  </li>
</ul>

```java
// 1. getPath()를 통해 절대 경로 얻기.
// 상대 경로를 기반으로 절대 경로를 얻는다.
String photo1Path = clazz.getResource("photo1.jpg").getPath();
String photo2Path = clazz.getResource("images/photo2.jpg");
```

<br><br>

<h1>12. 어노테이션</h1>
<ul>
  <li>
    코드에서 <strong>@</strong>로 작성되는 요소를 <strong>어노테이션(Annotation)</strong>이라 한다.
  </li>
  <li>
    어노테이션은 클래스 또는 인터페이스를 <strong>컴파일하거나 실행</strong>할 때 <strong>어떻게 처리해야 할 것이지 알려주는 설정 정보</strong>이다.
  </li>
  <li>
    어노테이션의 사용 용도는 다음과 같다.
  </li>
    <ul>
      <li>
        <strong>컴파일</strong> 시 사용하는 정보 전달.
      </li>
        <ul>
          <li>
            대표적인 예로 @Override가 있다. 컴파일러가 메소드 재정의 검사를 하도록 설정한다.
          </li>
        </ul>
      <li>
        <strong>빌드 툴</strong>이 코드를 자동으로 생성할 때 사용하는 정보 전달.
      </li>
      <li>
        <strong>실행 시 특정 기능</strong>을 처리할 때 사용하는 정보 전달.
      </li>
    </ul>
</ul>

<br>

<h2>12-1. 어노테이션 타입 정의와 적용</h2>
<ul>
  <li>
    어노테이션도 하나의 <strong>타입</strong>이며 사용하기 전에 먼저 <strong>정의</strong>부터 해야 한다.
  </li>
  <li>
    어노테이션은 <strong>@interface + 어노테이션명</strong>으로 정의할 수 있으며 <strong>@어노테이션명</strong>으로 사용한다. 
  </li>
  <li>
    어노테이션은 <strong>속성</strong>을 가질 수 있으며 <strong>타입</strong>과 <strong>이름</strong>으로 구성된다.
  </li>
    <ul>
      <li>
        이름 뒤에는 <strong>()</strong>를 붙인다.
      </li>
      <li>
        속성값은 <strong>default 키워드</strong>로 <strong>기본값</strong>을 지정할 수 있다.
      </li>
    </ul>
</ul>

```java
// 1. 어노테이션 정의
//   - 정의된 어노테이션은 @AnnotationName과 같이 사용된다.
public @interface AnnotationName {
}

// 2. 어노테이션 속성 정의.
public @interface AnnotationName {
  String prop1();
  int prop2() default 1;
}

// 3. 어노테이션 사용.
@AnnotationName(prop1= "값");
@AnnotationName(prop1= "값", prop2=3);

// 4. 기본 속성 value를 생성.
public @interface AnnotationName {
  String value();
  int prop2() default 1;
}

// 5. value 속성을 갖는 어노테이션은 값만 기술하여 value 속성에 자동 대입 가능.
@AnnotationName("값");

// 6. value 속성과 다른 속성 값을 동시에 줄 때에는 value 명시.
@AnnotationName(value= "값", prop2=3);
```

<br>

<h2>12-2. 어노테이션 적용 대상</h2>
<ul>
  <li>
    어떤 대상(클래스, 메소드 등)에 설정 정보를 적용할 것인지는 <strong>ElementType 열거 상수</strong>로 정의되어 있다. (p558 참고).
  </li>
  <li>
    적용 대상을 지정할 때에는 <strong>@Target 어노테이션</strong>을 사용한다.
  </li>
    <ul>
      <li>
        @Target의 기본 속성인 value는 <strong>ElementType 배열</strong>을 값으로 갖는다.
      </li>
        <ul>
          <li>
            적용 대상을 <strong>복수 개로 지정</strong>하기 위해서이다.
          </li>
        </ul>
    </ul>
</ul>

```java
// 1. @Target을 통해 어노테이션 지정.
@Target( { ElementType.TYPE, ElementType.FIELD, ElementType.METHOD } )
public @interface AnnotationName {
}

// TYPE(클래스)에 적용.
@AnnotationName
public class ClassName{
  // 필드에 적용
  @AnnotationName
  private String fieldName;
  
  // @Target에 CONSTRUCT가 없기에 생성자에는 적용 못함.
  // @AnnotationName
  public ClassName() { }

  // 메소드에 적용.
  @AnnotationName
  public void methodName() { }
}
```

<br>

<h2>12-3. 어노테이션 유지 정책</h2>
<ul>
  <li>
    어노테이션을 정의할 때에는 <strong>언제까지 어노테이션을 유지</strong>할 것인지 지정해야 한다.
  </li>
    <ul>
      <li>
        어노테이션 유지 정책은 <strong>RetentionPolicy 열거 상수</strong>로 정의된다.
      </li>
        <ul>
          <li>
            SOURCE: 컴파일 적용 - 컴파일 후
          </li>
          <li>
            CLASS: 메모리 로딩 - 메모리 로딩 후
          </li>
          <li>
            RUNTIME: 실행 - 계속 유지
          </li>
        </ul>
    </ul>
  <li>
    <strong>유지 정책</strong>을 지정할 때에는 <strong>@Retenstion 어노테이션</strong>을 사용한다.
  </li>
    <ul>
      <li>
        @Retension의 기본 속성인 value는 RetentionPolicy 열거 상수 값을 가진다.
      </li>
    </ul>
</ul>

```java
// 1. RUNTIME 어노테이션 지정.
@Target( { ElementType.TYPE, ElementType.FIELD, ElementType.METHOD } )
@Retention( RetentionPolicy.RUNTIME )
public @interface AnnotationName {
}
```

<br><br>

<h2>12-4. 어노테이션 설정 정보 이용</h2>
<ul>
  <li>
    어노테이션은 <strong>동작이 없는 설정 정보</strong>로 어떻게 처리할 것인지는 애플리케이션의 몫이다.
  </li>
    <ul>
      <li>
        isAnnotationPresent(AnnotationName.class) 
      </li>
        <ul>
          <li>
            지정한 어노테이션 적용 여부 → boolean
          </li>
        </ul>
      <li>
        getAnnotation(AnnotationName.class)
      </li>
        <ul>
          <li>
            지정한 어노테이션이 적용되어 있다면 어노테이션 리턴, 아니라면 null 리턴 → Annotation
          </li>
        </ul>
      <li>
        getDeclaredAnnotation()
      </li>
        <ul>
          <li>
            적용된 모든 어노테이션을 리턴 → Annotation[]
          </li>
        </ul>
    </ul>
</ul>