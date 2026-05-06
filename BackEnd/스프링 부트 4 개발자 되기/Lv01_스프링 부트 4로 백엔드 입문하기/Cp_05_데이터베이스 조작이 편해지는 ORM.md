<h1>1. 데이터베이스란?</h1>
<h2>1-1. 데이터베이스 관리자, DBMS</h2>
<ul>
  <li>
    데이터베이스를 관리하기 위한 소프트웨어를 DBMS(Database Management System)이라 한다.
  </li>
    <ul>
      <li>
        DBMS는 여러 요구사항을 충족하면서도 효율적으로 DB를 관리하도록 운영한다.
      </li>
    </ul>
  <li>
    DBMS에는 관계형, 객체-관계형, 도큐먼트형, 비관계형 등이 있고 관계형이 가장 널리 사용된다.
  </li>
</ul>

<h3>1-1-1. 관계형 DBMS</h3>
<ul>
  <li>
    관계형 DBMS는 relational을 붙여 RDBMS라 한다.
  </li>
  <li>
    관계형이라는 말을 사용하는 이유는 DBMS가 <strong>관계형 모델</strong>을 기반으로 하기 때문이다.
  </li>
  <li>
    RDBMS는 <strong>테이블 형태</strong>로 저장되며 <strong>행</strong>과 <strong>열</strong>이 존재한다.
  </li>
</ul>

<h3>1-1-2. H2, MySQL</h3>
<ul>
  <li>
    도서에서 사용할 RDBMS는 H2와 MySQL 이다. 이중 H2는 <strong>자바</strong>로 작성되어 있다.
  </li>
  <li>
    H2는 스프링 부트가 지원하는 <strong>인메모리 관계형 데이터베이스</strong>로 애플리케이션 자체 내부에 데이터를 저장한다.
  </li>
    <ul>
      <li>
        이러한 특징으로 애풀리케이션을 다시 실행하면 데이터가 초기화되는 문제가 있지만 사용하기 간편하다는 장점이 있어 테스트 시에 자주 활용한다.
      </li>
    </ul>
</ul>

<h3>1-1-3. 꼭 알아야할 데이터베이스 용어</h3>
<ul>
  <li>
    <strong>테이블</strong>
  </li>
    <ul>
      <li>
        데이터베이스에서 데이터를 구성하기 위한 <strong>가장 기본적인 단위</strong>이다.
      </li>
      <li>
        <strong>행</strong>과 <strong>열</strong>로 구성되며 행은 <strong>여러 속성</strong>으로 구성된다.
      </li>
    </ul>
  <li>
    <strong>행</strong>
  </li>
    <ul>
      <li>
        행(row)은 테이블의 <strong>가로로 배열된 데이터의 집합</strong>을 의미한다.
      </li>
      <li>
        행은 반드시 고유한 식별자인 <strong>기본키</strong>를 가진다.
      </li>
      <li>
        행을 <strong>record</strong>라 부르기도 한다.
      </li>
    </ul>
  <li>
    <strong>열</strong>
  </li>
    <ul>
      <li>
        열(column)은 <strong>행에 저장되는 유형</strong>의 데이터이다.
      </li>
      <li>
        특정 행에는 다른 행의 데이터가 들어갈 수 없기에 데이터에 대한 <strong>무결성을 보장</strong>한다.
      </li>
    </ul>
  <li>
    <strong>기본키</strong>
  </li>
    <ul>
      <li>
        기본키(primary key)는 <strong>행을 구분할 수 있는 식별자</strong>이다.
      </li>
      <li>
        테이블에서 <strong>유일한 값</strong>이어야하며 중복 값을 가질 수 없다.
      </li>
      <li>
        보통 다른 데이터를 <strong>수정, 삭제, 조회</strong>할 때 사용하며 다른 테이블과 <strong>관계</strong>를 맺어 데이터를 가져올 수도 있다.
      </li>
      <li>
        기본키의 값은 <strong>수정</strong>되어서는 안되며 <strong>유효</strong>해야 한다. (NULL 불가).
      </li>
    </ul>
  <li>
    <strong>쿼리</strong>
  </li>
    <ul>
      <li>
        쿼리는(query) DB에서 데이터를 조회, 삭제, 수정, 생성 등의 처리를 하기위해 사용하는 <strong>명령어</strong>이며 SQL언어를 사용한다.
      </li>
    </ul>
</ul>

<br>

<h2>1-2. SQL 문으로 데이터베이스 조작하는 연습하기</h2>
<h3>1-2-1. 데이터 조회하기:SELECT 문</h3>
<ul>
  <li>
    SELECT [무엇을?]
    <br>FROM [어디에서?]
    <br>WHERE [무슨?]
  </li>
</ul>

```SQL
-- 연습 문제 01.
SELECT * 
FROM customers
WHERE id = 1

-- 연습 문제 02.
SELECT id, name
FROM customers
WHERE phone_number = '010-2222-2222'
```

<h3>1-2-2. 조건 넣어보기:WHERE 절</h3>
<ul>
  <li>
    내용이 별로 없기 때문에 연습 문제만 풀고 skip.
  </li>
</ul>

```SQL
-- 연습 문제 01.
WHERE age >= 20

-- 연습 문제 02.
WHERE age >= 10 and age <= 30
WHERE age BETWEEN 10 and 30

-- 연습 문제 03.
WHERE name LIKE '김%' OR '이%';
```

<h3>1-2-3. 데이터 추가하기:INSERT 문</h3>
<ul>
  <li>
    INSERT INTO [어디에?]
    <br>VALUES [어떤 값을?]
  </li>
</ul>

<h3>1-2-4. 데이터 삭제하기:DELETE 문</h3>
<ul>
  <li>
    DELETE FROM [어디에서] WHERE [어떤 조건으로?];
  </li>
</ul>

<h3>1-2-5. 데이터 수정하기:UPDATE 문</h3>
<ul>
  <li>
    UPDATE [어디에?]
    <br>SET [무슨 걸럼을? = 어떤 값으로?]
    <br>WHERE [어떤 조건으로?]
  </li>
  <li>
    주의해야 할 점은 WHERE절이 없다면 모든 데이터의 수정이 이루어지기에 <strong>WHERE절을 체크</strong>해 주어야 한다.
  </li>
</ul>

```SQL
-- 연습 문제 01
UPDATE customers
SET name = '김일'
WHERE id = 1;

-- 연습 문제 02
UPDATE customers
SET phone_number = ' '
```

<br><br>

<h1>2. ORM이란?</h1>
<ul>
  <li>
    ORM(Object-relational mapping)은 <strong>자바의 객체와 데이터베이스를 연결</strong>하는 프로그래밍 기법이다.
  </li>
  <li>
    <strong>ORM의 장점</strong>
  </li>
    <ul>
      <li>
        SQL을 직접 작성하지 않고 데이터베이스에 접근할 수 있다.
      </li>
      <li>
        객체지향적 코드로 작성할 수 있어 <strong>비즈니스 로직</strong>에만 집중할 수 있다.
      </li>
      <li>
        데이터베이스 시스템이 추상화되어 있어 DB를 변경하여도 추가 작업이 적다. (<strong>DB 종속성이 낮아진다</strong>).
      </li>
      <li>
        매핑하는 정보가 명확하여 <strong>ERD에 대한 의존도</strong>를 낮출 수 있고 <strong>유지보수가 용이</strong>하다.
      </li>
    </ul>
  <li>
    <strong>ORM의 단점</strong>
  </li>
    <ul>
      <li>
        프로젝트의 복잡성이 커질수록 사용 난이도가 올라간다.
      </li>
      <li>
        복잡하고 무거운 쿼리는 ORM으로 해결이 불가한 경우가 있다.
      </li>
    </ul>
</ul>

<br><br>

<h1>3. JPA와 하이버네이트?</h1>
<ul>
  <li>
    ORM에도 여러 종류가 있으며 자바는 <strong>JPA(Java persistence API)</strong>를 표준으로 사용한다.
  </li>
    <ul>
      <li>
        JPA는 RDBMS를 사용하는 방식을 정의한 <strong>인터페이스</strong>이다.
      </li>
        <ul>
          <li>
            JPA가 인터페이스이기에 실제 사용을 위해서는 <strong>ORM 프레임워크</strong>를 추가로 선택해야 한다.
          </li>
        </ul>
    </ul>
  <li>
    주로 사용하는 ORM은 <strong>하이버네이트(hibernate)</strong>이다.
  </li>
    <ul>
      <li>
        하이버네이트는 내부적으로 <strong>JDBC API</strong>를 사용한다.
      </li>
      <li>
        하이버네이트의 목표는 자바 객체를 통해 <strong>DB의 종류에 상관없이 DB를 사용</strong>할 수 있게하는 데 있다.
      </li>
    </ul>
</ul>

<br>

<h2>3-1. 엔티티 매니저란?</h2>
<ul>
  <li>
    요청 → 엔티티 매니저 팩토리 → 엔티티 매니저 → 커넥션 → DB
  </li>
  <li>
    스프링 부트는 내부에서 엔티티 매니터 팩토리 <strong>하나</strong>만 생성하여 관리한다.
  </li>
    <ul>
      <li>
        엔티티 매니저의 사용은 <strong>@PersistenceContext</strong> 혹은 <strong>@Autowired</strong> 애너테이션을 활용한다.
      </li>
    </ul>
  <li>
    스프링 부트는 기본적으로 <strong>빈을 하나</strong>만 생성하여 공유하기 때문에 <strong>동시성 문제</strong>가 발생할 수 있다.
  </li>
    <ul>
      <li>
        실제로는 엔티티 매니저가 아닌 <strong>프록시(가짜) 엔티티 매니저</strong>를 사용한다.
      </li>
      <li>
        필요할 때 DB 트랜잭션과 관련된 실제 엔티티 매니저를 호출한다.
      </li>
    </ul>
  <li>
    A 요청과 B 요청이 동시에 들어온다
    <br>→ 둘 다 같은 Service 빈을 사용한다
    <br>→ 둘 다 같은 프록시 EntityManager 필드를 호출한다
    <br>→ 프록시는 현재 스레드/트랜잭션을 확인한다
    <br>→ A 요청은 A 트랜잭션용 실제 EntityManager로 연결된다
    <br>→ B 요청은 B 트랜잭션용 실제 EntityManager로 연결된다
    <br>→ A와 B는 각각 별도의 영속성 컨텍스트에서 엔티티를 관리한다
    <br>→ 그래서 EntityManager 자체의 상태는 섞이지 않는다
  </li>
    <ul>
      <li>
        요청별 EntityManager 분리
        <br>→ 영속성 컨텍스트가 섞이는 문제를 막는다
      </li>
      <li>
        같은 DB row 동시 수정
        <br>→ 여전히 갱신 손실 같은 동시성 문제가 생길 수 있다
        <br>→ 이 문제는 락, 트랜잭션 격리 수준, @Version 같은 방식으로 따로 해결한다
      </li>
    </ul>
</ul>

<h3>3-1-1. 엔티티</h3>
<ul>
  <li>
    엔티티(entity)는 데이터베이스의 <strong>테이블과 매핑되는 객체</strong>를 의미한다.
  </li>
    <ul>
      <li>
        객체인 점은 동일하나 데이터베이스의 테이블과 직접 연결된다는 특징이 있고 <strong>쿼리를 실행</strong>하는 객체이다.
      </li>
    </ul>
</ul>

<h3>3-1-2. 엔티티 매니저</h3>
<ul>
  <li>
    엔티티 매니저(entity manager)는 엔티티를 관리하여 DB와 애플리케이션 사이에서 <strong>객체를 생성, 수정, 삭제하는 등의 역할</strong>을 한다.
  </li>
  <li>
    엔티티 매니저를 만드는 곳을 <strong>엔티티 매니저 팩토리(entity manager factory)</strong>라 한다.
  </li> 
</ul>

```java
// 1. 엔티티 매니저 사용 방법 예.
@PersistenceContext
// 프록시 엔티티 매니저이며 필요할 때 진짜 엔티티 매니저를 호출한다.
EntityManager em;
```

<br>

<h2>3-2. 영속성 컨텍스트란?</h2>
<ul>
  <li>
    영속성 컨텍스트는 JAP의 중요한 특징 중 하나로 <strong>엔티티를 관리하는 가상</strong>의 공간이다.
  </li>
  <li>
    스프링 부트는 JPA가 알아서 자바 코드를 쿼리로 변경해주는 것은 편리하지만 영속성 컨텍스트의 기본 개념을 알아 두는 것이 도움이 된다.
  </li>
</ul>

<h3>3-2-1. 1차 캐시</h3>
<ul>
  <li>
    영속성 컨텍스트는 <strong>내부에 1차 캐시</strong>를 가지고 있다.
  </li>
    <ul>
      <li>
        캐시의 <strong>키</strong>는 엔티티의 <strong>@Id 애너테이션</strong>이 달린 <strong>기본키</strong> 역할을 하는 식별자이며 <strong>값은 엔티티</strong>이다.
      </li>
    </ul>
  <li>
    엔티티를 조회하면 1차 캐시에서 먼저 데이터를 조회한다.
    <br>→ 값이 있다면 반환한다.
    <br>→ 값이 없다면 DB에서 조회하여 1차 캐시에 저장하고 반환한다.
  </li>
  <li>
    캐시된 데이터를 조회할 때에는 DB를 거치지 않기에 성능적으로 장점이 있다.
  </li>
</ul>

<h3>3-2-2. 쓰기 지연</h3>
<ul>
  <li>
    쓰기 지연(transactional write-behind)은 트랜잭션을 커밋하기 전에는 쿼리를 모아두고 <strong>커밋 시점에 모든 쿼리를 한 번에 실행</strong>하는 것을 의미한다.
  </li>
  <li>
    쿼리를 적당한 묶음으로하여 요청을 보내기 때문에 데이터베이스 시스템의 부하를 줄일 수 있다.
  </li>
</ul>

<h3>3-2-3. 변경 감지</h3>
<ul>
  <li>
    트랜잭션을 커밋하면 1차 캐시에 저장되어 있는 엔티티의 값과 현재 엔티티의 값을 비교해 <strong>변경 사항이 있다면 값을 DB에 자동 반영</strong>한다.
  </li>
  <li>
    적당한 묶음으로 쿼리를 요청할 수 있고 DB의 시스템 부담을 줄일 수 있다.
  </li>
</ul>

<h3>3-2-4. 지연 로딩</h3>
<ul>
  <li>
    지연 로딩(lazy loading)은 쿼리로 요청한 데이터를 바로 애플리케이션에 로딩하는 것이 아니라 <strong>필요할 때 쿼리를 날려 데이터를 조회하는 것</strong>을 의미한다.
  </li>
</ul>

<br>

<h2>3-2-4. 엔티티의 상태</h2>
<ul>
  <li>
    엔티티는 4가지 상태를 가진다.
  </li>
    <ul>
      <li>
        <strong>분리(detached) 상태</strong>: 영속성 컨텍스트가 관리하고 있는 않은 상태
      </li>
      <li>
        <strong>관리(managed) 상태</strong>: 영속성 컨텍스트가 관리하고 있는 상태
      </li>
      <li>
        <strong>비영속(transient) 상태</strong>: 영속성 컨텍스트와 전혀 관계가 없는 상태
      </li>
      <li>
        <strong>삭제된(removed) 상태</strong>
      </li>
    </ul>
</ul>

```java
// 1. 엔티티 상태의 예.
public class EntityManagerTest {
  
  @Autowired
  EntityManager em;

  public void example() {
    // 엔티티 매니저가 엔티티를 관리하지 않는 상태.
    Member member = new Member(1L, "홍길동");

    // 엔티티가 괸라되는 상태.
    em.persist(member);

    // 엔티티 객체가 분리된 상태.
    em.detach(member);

    // 엔티티 객체가 삭제된 상태.
    em.remove(member);
  }
}
```

<br><br>

<h1>4. 스프링 데이터와 스프링 데이터 JPA</h1>
<ul>
  <li>
    스프링 데이터(spring data)는 엔티티 관리를 더욱 쉽게하여 개발자가 비즈니스 로직에만 집중할 수 있도록 <strong>DB 사용 기능을 클래스 레벨에서 추상화</strong> 한다.
  </li>
  <li>
    스프링 데이터 인터페이스에는 <strong>CRUD를 포함한 여러 메소드</strong>가 포함되어 있고 <strong>알아서 쿼리</strong>를 만들어준다.
  </li>
  <li>
    페이징 처리, 메소드 이름으로 자동 쿼리 빌딩 등 다양한 기능을 제공한다.
  </li>
  <li>
    도서에서는 스프링 데이터 몽고디비(spring data MongoDB)를 사용한다.
  </li>
</ul>

<br>

<h2>4-1. 스프링 데이터 JPA란?</h2>
<ul>
  <li>
    스프링 데이터 JPA는 스프링 데이터의 공통 기능에 <strong>JPA의 기술을 추가</strong>한 기술이다.
  </li>
    <ul>
      <li>
        스프링 데이터 JPA는 스프링 데이터의 인터페이스인 PagingAndSortingRepository를 상속받아 <strong>JpaRepository 인터페이스</strong>를 생성하였다.
      </li>
    </ul>
</ul>

```java
// 1. 기존의 엔티티 상태를 바꾸는 방법. (메소드를 호출).
@PersistenceContext
EntityManager em;

public void join() {
  // 기존에는 엔티티 상태를 바꿀 때 메소드를 호출한다.
  Member member = new Member(1L, "홍길동");
  em.persist(member);
}

// 2. JpaRepository
//   - `<엔티티 이름, 엔티티 기본키의 타입>`을 입력하면 기본 CRUD 
//     메소드를 사용할 수 있다.
public interface MemberRepository extends JpaRepository<Member, Long> {}
```

<br>

<h2>4-2. 스프링 데이터 JPA에서 제공하는 메서드 사용해보기</h2>
<ul>
  <li>
    build.gradle에 "testImplementation 'org.springframework.boot:spring-boot-starter-data-jpa-test'" 추가.
  </li>
  <li>
    학습 테스트를 진행한다.
  </li>
    <ul>
      <li>
        학습 테스트란 우리가 사용하는 라이브러리, 프레임워크에서 지원하는 기능을 검증하며 어떻게 동작하는지 파악하는 테스트라 보면 된다.
      </li>
    </ul>
</ul>

<h3>4-2-1. 조회 메서드 사용해보기</h3>
<ul>
  <li>
    JPA에서 데이터를 가져올 때에는 <strong>findAll() 메소드</strong>를 사용한다.
  </li>
</ul>

<h3>4-2-2. 쿼리 메서드 사용해보기</h3>
<ul>
  <li>
    id가 아닌 컬럼을 통해 조회를 할 때에는 값이 없을 수 있다. 이런 경우를 대비하여 JPA는 <strong>메소드 이름</strong>으로 쿼리를 작성하는 기능을 제공한다.
  </li>
    <ul>
      <li>
        메소드 이름으로 쿼리를 작성한다는 것은 Repository에 findBy컬럼명 형식의 메소드를 선언하면, Spring Data JPA가 <strong>메소드 이름을 해석해 자동으로 SQL 쿼리를 만들어주는 것</strong>을 의미한다.
      </li>
    </ul>
  <li>
    이와 같은 기능을 <strong>쿼리 메소드</strong>라 한다.
  </li>
    <ul>
      <li>
        JPA가 정해준 메소드 <strong>이름 규칙</strong>을 따르면 쿼리문을 구현하지 않아도 <strong>메소드처럼 사용</strong>할 수 있다.
      </li>
    </ul>
  <li>
    JPA를 이용해 표현하기 너무 복잡하거나 성능이 너무 중요해서 SQL 문을 직접 사용해야 하는 경우 <strong>@Query 메소드</strong>를 쓰기도 한다.
  </li>
    <ul>
      <li>
        @Query는 JPA가 쿼리를 생성하지 않고 <strong>사용자가 작성한 쿼리</strong>를 붙여준다.
      </li>
      <li>
        성능적으로는 개선할 여지가 남아 있을 수 있으나 쿼리문 가독성 문제를 완화한다.
      </li>
    </ul>
  <li>
    요약
  </li>
    <ul>
      <li>
        전체 조회 → findAll() 메소드.
      </li>
      <li>
        아이디로 조회 → findById()
      </li>
      <li>
        특정 컬럼으로 조회 → 쿼리 메소드 명명 규칙에 맞게 정의 후 사용.
      </li>
    </ul>
</ul>

```java
// 1. @Query 사용 예.
@Query("select m from Member m where m.name = ?1")
Optional<Member> findByNameQuery(String name);
```

<h3>4-2-3. 추가, 삭제 메소드 사용해보기</h3>
<ul>
  <li>
    JPA는 데이터를 입력할 때 INSERT 대신 <strong>save() 메소드</strong>를 사용한다.
  </li>
  <li>
    여러 엔티티를 한 번에 저장하고 싶은 경우 <strong>saveAll() 메소드</strong>를 사용한다.
  </li>
    <ul>
      <li>
        엔티티 클래스틑 테이블과 매핑되고, 엔티티 객체는 테이블의 한 행(row)과 매핑된다.
      </li>
    </ul>
  <li>
    DELETE문은 JPA의 <strong>deleteById() 메소드</strong>를 사용하여 아이디로 레코드를 삭제할 수 있다.
  </li>
  <li>
    모든 데이터를 삭제하고 싶은 경우 <strong>deleteAll() 메소드</strong>를 사용한다.
  </li>
    <ul>
      <li>
        실제 서비스에서는 거의 사용하지 않고 <strong>테스트 간 격리를 보장</strong>하기 위해 사용한다.
      </li>
      <li>
        따라서 보통 <strong>@AfterEach</strong> 애너테이션을 붙여 cleanUp() 메소드와 같은 형태로 사용한다.
      </li>
    </ul>
  <li>
    요약
  </li>
    <ul>
      <li>
        saveAll(): 한 번에 여러 레코드 추가.
      </li>
      <li>
        deleteById(): 아이디로 레코드 삭제.
      </li>
      <li>
        deleteAll(): 모든 레코드 삭제.
      </li>
    </ul>
</ul>

<h3>4-2-4. 수정 메서드 사용해보기</h3>
<ul>
  <li>
    JPA는 <strong>트랜잭션 내</strong>에서 데이터를 수정한다. 따라서 데이터를 수정할 때에는 <strong>@Transactional 애너테이션</strong>을 메소드에 추가한다.
  </li>
    <ul>
      <li>
        객체에 값을 바꾸는 <strong>일종의 setter 메소드</strong>가 있고, @Transaction 애너테이션이 포함된 메소드가 이를 호출하면 JPA는 <strong>변경 감지(dirty checking)</strong> 기능을 통해 엔티티의 필드값이 변경될 때<strong>데이터베이스에 자동으</strong>로 반영한다.
      </li>
    </ul>
  <li>
    Test 코드에서는 @DataJpaTest 애너테이션이 트랜잭션을 관리하기에 @Transactional이 포함되어 있다. 따라서 작성하지 않아도 된다.
  </li>
    <ul>
      <li>
        하지만 <strong>실제 서비스</strong>에서는 @Transactional을 사용해야 한다.
      </li>
    </ul>
</ul>

<br><br>

<h1>5. 예제 코드 살펴보기</h1>
<ul>
  <li>
    자동키 생성 방식
  </li>
    <ul>
      <li>
        AUTO: 선택한 DB의 dialect에 따라 방식ㅇ르 자동으로 선택(기본값).
      </li>
      <li>
        IDENTITY: 기본키 생성을 DB에 위임한다(=AUTO_INCREMENT).
      </li>
      <li>
        SEQUENCE: DB 시퀀스를 사용해 기본키를 할당한다.
      </li>
      <li>
        TABLK: 키 생성 테이블을 사용한다.
      </li>
    </ul>
  <li>
    @Column 애너테이션 속성.
  </li>
    <ul>
      <li>
        name: 필드와 매핑할 컬럼 이름. 설정하지 않을 경우 필드 이름으로 지정한다.
      </li>
      <li>
        nullable: 컬럼의 null 허용 여부. 설정하지 않으면 true
      </li>
      <li>
        unique: 컬럼의 유일한 값(unique) 여부. 설정하지 않으면 false.
      </li>
      <li>
        columnDefinition: 컬럼 정보 설정. default 값을 줄 수 있다.
      </li>
    </ul>
  <li>
    리포지터리는 엔티티에 있는 데이터들을 <strong>조회하거나 저장, 변경, 삭제</strong>할 때 사용하는 <strong>인터페이스</strong>이다.
  </li>
    <ul>
      <li>
        <strong>JpaRepository 클래스를 상속</strong>받아 간단히 구현할 수 있다.
      </li>
        <ul>
          <li>
            상속을 받을 때 엔티티와 엔티티의 기본키 타입 Long을 인수로 넣어준다.
          </li>
        </ul>
    </ul>
</ul>

```java
@Getter
// Member 객체를 JPA가 관리하는 엔티티로 지정한다. (테이블 매핑).
//   - name을 사용하면 name과 일치하는 테이블에 매핑한다.
//   - name을 사용하지 않으면 클래스 이름과 동일한 테이블에 매핑한다.
@Entity
// Protected는 기본 생성자 이다.
//   - 엔티티는 반드시 기본 생성자가 있어야 한다.
//   - 접근 제어자는 public 혹은 protected를 제공한다.
//     - public 보다는 protected가 더 안전하다.
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class Member {
  
  // @Id는 Long 타입의 id 필드를 테이블의 기본키로 지정한다.
  @Id
  // @GeneratedValue는 기본키의 생성 바식을 결정한다.
  @GeneratedValue(strategy = GenerationType.IDENTITIY)
  // @Column 애너테이션은 DB의 컬럼과 필드를 매핑한다.
  @Column(name = "id", updatable = false)
  private Long id;
 
  @Column(name = "name", nullable = false)
  private String name;

  public Member(String name) {
    this.name = name;
  }

  public void changeName(String name) {
    this.name = name;
  }
}
```