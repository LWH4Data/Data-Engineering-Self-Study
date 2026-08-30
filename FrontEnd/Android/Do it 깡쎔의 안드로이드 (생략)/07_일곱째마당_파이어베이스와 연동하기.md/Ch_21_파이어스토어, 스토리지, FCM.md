<h1>1. 파이어스토어 데이터베이스</h1>
<ul>
  <li>
    파이어베이스는 <strong>파이어스토어 데이터베이스(Firestore Database)</strong>와 <strong>실시간 데이터베이스(Realtime Database)</strong> 두 가지 클라우드를 기반으로 한 데이터베이스를 제공한다.
  </li>
    <ul>
      <li>
        파이어스토어 데이터베이스는 실시간 데이터베이스보다 <strong>더 많고 빠른 쿼리</strong>를 제공한다.
      </li>
      <li>
        실시간 데이터베이스는 여러 클라이언트에서 상태를 <strong>실시간으로 동기화</strong>해야 하는 모바일 앱을 만드는 솔루션이다.
      </li>
    </ul>
</ul>

<br>

<h2>1-1. 파이어스토어 사용 설정</h2>
<ul>
  <li>
    파이어스토어를 사용하기 위해서는 파이어베이스에서 새로운 데이터베이스를 만들어야한다.
  </li>
  <li>
    새로운 DB 생성 후에는 아래와 같이 모듈 수준의 빌드 그래들 파일에 <strong>파이어스토어 라이브러리</strong>를 등록한다.
  </li>
    <ul>
      <li>
        implementation("com.google.firebase:firebase-firestore")
      </li>
    </ul>
</ul>

<br>

<h2>1-2. 파이어스토어 데이터 모델</h2>
<ul>
  <li>
    파이어스토어는 NoSQL DB로 테이블이나 행이 없고 대신 <strong>컬렉션</strong>으로 정리되는 문서에 데이터를 저장한다.
  </li>
    <ul>
      <li>
        각 문성는 <strong>key-value 쌍의 데이터</strong>가 저장되며 모든 문서는 <strong>컬렉션</strong>으로 정리된다.
      </li>
      <li>
        문서의 하위에는 다시 <strong>하위 컬렉션(sub collection)</strong>도 포함할 수 있다.
      </li>
    </ul>
</ul>

<br>

<h2>1-3. 파이어스토어 보안 규칙</h2>
<ul>
  <li>
    파이어스토어에 <strong>보안 규칙</strong>을 설정하여 데이터를 이용할 때 여러 조건을 설정할 수 있다.
  </li>
  <li>
    보안 규칙은 콘솔의 [규칙] 탭에서 <strong>match</strong>와 <strong>allow</strong> 구문을 조합하여 설정한다.
  </li>
    <ul>
      <li>
        match: 데이터베이스 <strong>문서를 식별</strong>한다.
      </li>
      <li>
        allow: <strong>접근 권한</strong>을 작성한다.
      </li>
    </ul>
  <li>
    allow 구문에서 쓰기 권한을 나타내는 write는 문서의 <strong>생성, 수정, 삭제를 포함</strong>한다.
  </li>
    <ul>
      <li>
        쓰기 권한만 따로 지정하고 싶다면 <strong>create, update, delete</strong>를 사용한다.
      </li>
    </ul>
  <li>
    match 구문에 <strong>allow 구문을 나열</strong>하여 여러 조건을 설정할 수도 있다.
  </li>
  <li>
    조건을 설정할 때 문서에 저장된 데이터를 이용할 경우 <strong>resouce.data</strong>를 이용한다.
  </li>
  <li>
    사용자에게 전달받은 데이터를 데이터베이스에 저장된 데이터와 비교할 경우 request.resource.data로 사용자에게 전달받은 데이터를 활용한다.
  </li>
</ul>

```text
>> 1. 모든 문서의 읽기/쓰기 거부 예.
rules_version = '2';
service cloud.firestore {
    match /databases/{database}/documents {
        >> 모든 문서 대상.
        match /{document=**} {
            >> 읽기/쓰기 거부
            allow read, write: if false;
        }
    }
}
```

```text
>> 2. 모든 문서의 읽기/쓰기 허용 예.
rules_version = '2';
service cloud.firestore {
    match /databases/{database}/documents {
        >> 모든 문서 대상
        match /{document=**} {
            >> 읽기/쓰기 허용
            allow read, write: if true;
        }
    }
}
```

```text
>> 3. 인증된 사용자에게만 모든 문서의 읽기/쓰기 허용.
rules_version = '2';
service cloud.firestore {
    match /databases/{database}/documents {
        >> 모든 문서 대상.
        match /{document=**} {
            >> 인증된 사용자에게만 읽기/쓰기 허용.
            allow read, wrtie: if request.auth.uid != null;
        }
    }
}
```

```text
>> 4. 자신의 데이터만 읽기/쓰기 허용.
rules_version ='2';
service cloud.firestore {
    match /databases/{database}/documents {
        match /users/{userId} {
            >> 자신의 데이터만 읽기, 수정, 삭제 허용.
            allow read, update, delete: if request.auth.uid == userId;
            >> 인증된 사용자에게만 문서 생성 허용.
            allow create: if request.auth.uid != null;
        }
    }
}
```

```text
>> 5. 문서에 저장된 데이터 활용.
rules_version = '2';
service cloud.firestore {
    match /databases/{database}/documents {
        match /cities/{city} {
            >> 문서의 visibility 값이 public 일 때만 읽기 허용.
            allow read: if resource.data.visibility == 'public';
        }
    }
}
```

```text
>> 6. 전달받은 데이터 활용 (request.resource.data)
rules_version = '2';
service cloud.firestore {
    match /databases/{database}/documents {{
        >> 전달받은 데이터가 0 이상일 때만 population 데이터 수정 허용.
        >> 단, name 데이터는 수정할 수 없음.
        allow update: if request.resource.data.population > 0
            && request.resource.data.name == resource.data.name;
    }}
}
```

<br>

<h2>1-3. 데이터 저장하기</h2>
<ul>
  <li>
    안드로이드 앱에서 파이어스토어를 이용할 수 있게 되었다면 다음으로 해야하는 단계는 <strong>파이어스토어의 객체</strong>를 얻는 것이다.
  </li>
</ul>

```kotlin
// 1. 파이어스토어 객체 얻기.
var db: FirebaseFirestore = FirebaseFirestore.getInstance()
```

<h3>1-3-1. add() 함수로 데이터 저장하기</h3>
<ul>
  <li>
    파이어스토어에는 데이턱 <strong>문서 단위</strong>로 저장되고 문서는 <strong>컬렉션</strong>에 저장된다.
  </li>
</ul>