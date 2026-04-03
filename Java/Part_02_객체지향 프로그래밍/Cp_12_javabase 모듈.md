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