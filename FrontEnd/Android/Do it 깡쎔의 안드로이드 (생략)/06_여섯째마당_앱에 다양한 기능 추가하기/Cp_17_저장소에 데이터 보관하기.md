<h1>1. 데이터베이스에 보관하기</h1>
<ul>
  <li>
    안드로이드폰에서 이용하는 데이터베이스 관리 시스템은 오픈소스로 만들어진 <strong>SQLite(sqlite.org)</strong>이다.
  </li>
  <li>
    SQLite는 테이블의 데이터를 <strong>앱의 저장소</strong>에 <strong>파일</strong>로 저장하며 <strong>외부 앱</strong>에서는 접근할 수 없다.
  </li>
    <ul>
      <li>
        코드에서는 SQL 질의문만 작성하면 되고 실제 데이터는 SQLite가 관리한다.
      </li>
    </ul>
  <li>
    앱은 데이터를 대부분 서버에 보관하지만 동시에 <strong>내부 저장소</strong>에 보관하기도한다.
  </li>
    <ul>
      <li>
        문자 앱 등 데이터를 <strong>내부 저장소</strong>에만 보관하는 경우도 존재하며 <strong>네트워크</strong>가 불안정할 때를 고려하는 등 <strong>안정된 서비스</strong>를 제공하기 위해서이다.
      </li>
    </ul>
</ul>

<br>

<h2>1-1. 질의문 작성하기</h2>
<ul>
  <li>
    SQLite를 사용하기 위해서는 <strong>SQLiteDatabase</strong>라는 API를 이용하며 SQLiteDatabase 객체는 <strong>openOrCreateDatabase() 함수</strong>를 호출해서 얻는다.
  </li>
  <li>
    SQLiteDatabase 객체를 얻었다면 객체에 정의된 다음 함수를 이용해 질의문을 실행할 수 있다.
  </li>
    <ul>
      <li>
        public void execSQL(String sql, Object[] bindArgs)
      </li>
        <ul>
          <li>
            첫 번째 매개변수는 전달할 질의문이다.
          </li>
          <li>
            두 번째 매개변수는 첫 번째 매개변수의 ?가 매칭될 값들의 배열을 전달한다.
          </li>
        </ul>
      <li>
        public Cursor rawQuery(String sql, String[] selectionArgs)
      </li>
    </ul>
  <li>
    테이블에 저장된 데이터를 조회할 때에는 <strong>rawQuery()</strong> 함수로 <strong>select 문</strong>을 실행한다.
  </li>
    <ul>
      <li>
        rawQuery() 함수의 반환값은 <strong>Cursor 객체</strong>로 테이블에서 조회한 <strong>행(row)의 집합</strong>으로 생각하면된다.
      </li>
    </ul>
  <li>
    조회한 행의 열(column) 데이터를 가져오려면 먼저 Cursor 객체로 <strong>행을 선택</strong>하고, <strong>해당 행의 열 데이터</strong>를 가져온다.
  </li>
    <ul>
      <li>
        Cursor 객체로 행을 선택할 때에는 <strong>moveTo~로 시작</strong>하는 다음 함수들을 이용하며 선택한 행이 존재하면 true, 존재하지 않으면 false를 반환한다.
      </li>
        <ul>
          <li>
            public abstract boolean moveToFirst(): 첫 번째 행을 선택한다.
          </li>
          <li>
            public abstract boolean moveToLast(): 마지막 행을 선택한다.
          </li>
          <li>
            public abstract boolean moveToNext(): 다음 행을 선택한다.
          </li>
          <li>
            public abstract boolean moveToPosition(int position): 매개변수로 지정한 위치의 행을 선택한다.
          </li>
          <li>
            public abstract boolean moveToPreviou(): 이전 행을 선택한다.
          </li>
        </ul>
      <li>
        Cursor 객체로 선택한 행의 열 데이터를 가져올 때에는 <strong>타입</strong>에 따라 getString(), getInt() 등의 함수를 이용한다. 함수의 매개변수에는 가져올 데이터가 저장된 열의 인덱스를 전달한다.
      </li>
        <ul>
          <li>
            public abstract String getString(int columnIndex)
          </li>
          <li>
            public abstract int getInt(int columnIndex)
          </li>
          <li>
            public abstract double get Double(int columnIndex)
          </li>
        </ul>
    </ul>
  <li>
    SQLiteDatabase 클래스의 함수를 사용하지 않고 <strong>insert(), update(), delete(), query()</strong> 함수를 사용해서 데이터를 다룰 수도 있다.
  </li>
    <ul>
      <li>
        질의문을 <strong>각 항목을 매개변수로 대입</strong>하면 질의문을 만들어 실행해 주기 때문에 질의문 코드를 직접 작성할 필요가 없다.
      </li>
        <ul>
          <li>
            public long insert(String table, String nullColumnHack, ContentValues values)
          </li>
            <ul>
              <li>
                ContentValues 객체는 <strong>열 데이터 집합</strong>이다. Map 객체처럼 <strong>key-value 형태</strong>로 데이터 집합을 저장하며 <strong>key는 테이블의 열 이름</strong>을 지정한다.
              </li>
            </ul>
          <li>
            public int update(String table, ContentValues values, String whereClause, String[] whereArgs)
          </li>
          <li>
            public int delete(String table, String whereClause, String[] whereArgs)
          </li>
          <li>
            public Cursor query(String table, String[] columns, String selection, String[] selectionArgs, String groupBy, String having, String orderBy)
          </li>
        </ul>
    </ul>
</ul>

```kotlin
// 1. 데이터베이스 객체 생성.
val db = openOrCreateDatabase(
    
    // 해당 DB 파일을 열고 SQLiteDatabase 객체를 반환한다. 
    // 파일이 없는 경우에는 새로 파일을 생성한다.
    "testdb", 
    Context.MODE_PRIVATE, 
    null)

// 2. 테이블 생성(create 문)
db.execSQL("create table USER_TB (" +
           "_id integer primary key autoincrement," +
           "name not null," +
           "phone)")

// 3. 2번에 생성한 테이블에 데이터 삽입.
db.execSQL("insert into USER_TB (name, phone) values (?,?)",
    arrayOf<String>("kkang", "0101111"))

// 4. 3에서 삽입한 데이터를 조회.
val cursor = db.rawQuery("select * from USER_TB", null)

// 5. 선택한 행의 값 가져오기.
while(cursor.moveToNext()) {
    
    // 가져온 행의 0번째 열.
    val name = cursor.getString(0)

    // 가져온 행의 1번째 열.
    val phone = cursor.getString(1)
}
```

```kotlin
// 6. insert() 함수로 데이터 삽입하기.
val values = ContentValues()
// name-kkang (key-value)
values.put("name", "kkang")
// phone-0101112 (key-value)
values.put("phone", "0101112")
db.insert("USER_TB", null, values)

// 7. query() 함수를 통해 질의문 생성.
val cursor = db.query(
    
    // 조회할 테이블명.
    "USER_TB",

    // 가져올 값이 담긴 열 이름 배열.
    arrayOf<String>("name", "phone"),
    
    // select문의 where 절 뒤에 들어갈 문자열.
    "phone=?",

    // 질의문에서 ?에 들어갈 데이터 배열.
    arrayOf<String>("0101112"),

    // select 문의 group by 절 뒤에 들어갈 문자열.
    null,

    // select 문의 having 조건.
    null,

    // select 문의 order by 조건
    null
)
```

<br>

<h2>1-2. 데이터베이스 관리하기</h2>
<ul>
  <li>
    SQLite 데이터베이스를 이용할 때 질의문을 실행해야하기 때문에 반드시 SQLiteDatabase 객체를 이용한다.
  </li>
  <li>
    <strong>SQLiteOpenHelper 클래스</strong>를 이용하면 데이터베이스 프로그램을 좀 더 구조적으로 작성할 수 있다.
  </li>
    <ul>
      <li>
        SQLiteOpenHelper 클래스느 데이터베이스를 관리하는 코드(create, alter, drop 등)를 <strong>추상화</strong>한다.
      </li>
    </ul>
  <li>
    관리 코드는 SQLiteOpenHelper 클래스로 작성하고 실제 데이터를 조작하는 코드는 필요한 곳에 작성해 성격이 다른 <strong>두 코드를 분리</strong>할 수 있다.
  </li>
  <li>
    SQLiteOpenHelper는 추상 클래스이기 때문에 이를 <strong>상속</strong>받아 <strong>하위 클래스</strong>를 작성해야한다.
  </li>
    <ul>
      <li>
        SQLiteOpenHelper를 상속받을 때 <strong>상위 클래스의 생성자</strong>를 호출하면서 적절한 정보를 넘겨주어야 한다.
      </li>
      <li>
        <strong>onCreate()</strong>와 <strong>onUpgrade()</strong> 함수는 SQLiteOpenHelper의 추상 함수이므로 하위 클래스에서 반드시 재정의한다. 두 함수는 자동으로 호출되며 이 시점을 알고 적절히 활용해야 한다.
      </li>
        <ul>
          <li>
            onCreate(): 앱이 설치된 후 <strong>SQLiteOpenHelper 클래스가 이용되는 순간</strong> 한 번 호출한다. 주로 <strong>테이블을 생성</strong>할 때 사용한다.
          </li>
          <li>
            onUpgrade(): 생성자에 지정한 <strong>DB 버전 정보</strong>가 변경될 때마다 호출한다. 주로 <strong>테이블의 스키마를 변경</strong>하는 코드를 작성한다.
          </li>
        </ul>
    </ul>
  <li>
    SQLiteOpenHelper 클래스를 이용하면 질의문을 실행하는 SQLiteDatabase 객체도 SQLiteOpenHelper 클래스를 이용해 생성한다.
  </li>
    <ul>
      <li>
        SQLiteOpenHelper 클래스의 <strong>readableDatabase</strong>나 <strong>writableDatabase</strong> 속성으로 데이터베이스 객체를 생성한다.
      </li>
    </ul>
</ul>

```kotlin
// 1. SQLiteOpenHelper의 하위 클래스 작성.
class DBHelper(context: Context): SQLiteOpenHelper(
    context,
    // DB 파일명.
    "testdb", 
    null,
    // 개발자가 숫자로 정하는 DB 버전 정보. 
    1) {
    
    // onCreate 재정의.
    override fun onCreate(db: SQLiteDatabase?) {
    }

    // inUpgrade 재정의.
    override fun onUpgrade(db: SQLiteDatabase?, oldVersion: Int, newVersion: Int){
    }
}
```

```kotlin
// 2. 데이터베이스 객체 생성.
val db: SQLiteDatabase = DBHelper(this).writableDatabase
```

<br><br>

<h1>2. 파일에 보관하기</h1>
<ul>
  <li>
    데이터베이스와 프리퍼런스는 모두 내부적으로는 파일로 저장되지만 코드에서 직접 파일을 읽거나 쓰지 않고 특정 <strong>API를 이용</strong>하는 방법이다. 하지만 안드로이드에서는 <strong>직접 파일을 읽고 쓰는 방법</strong> 또한 존재한다.
  </li>
  <li>
    안드로이드 앱에서 파일을 다룰 때에는 대부분 <strong>java.io 패키지</strong>에서 제공하는 클래스를 이용하기 때문에 일반 자바 프로그램과 큰 차이가 없다.
  </li>
    <ul>
      <li>
        File: 파일 및 디렉터리를 지칭하는 클래스
      </li>
      <li>
        FileInputStream / FileOutputStream: 파일에서 바이트 스트림으로 데이터를 읽거나 쓰는 클래스
      </li>
      <li>
        FileReader / FileWriter: 파일에서 문자열 스트림으로 데이터를 읽거나 쓰는 클래스
      </li>
    </ul>
  <li>
    안드로이드 파일 저장소는 <strong>내장 메모리(앱별 저장소)</strong>와 <strong>외장 메모리</strong>로 구분된다.
  </li>
    <ul>
      <li>
        외부 메모리는 다시 <strong>앱별 저장소</strong>와 <strong>공용 저장소</strong>로 분리되며 앱별 저장소에는 해당 앱만, 공용 저장소에서는 다른 앱들도 접근이 가능하다.
      </li>
    </ul>
</ul>

<br>

<h2>2-1. 내장 메모리의 파일 이용하기</h2>
<ul>
  <li>
    내장 메모리는 앱이 설티되면 <strong>시스템에서 자동으로 할당</strong>되는 공간이다.
  </li>
    <ul>
      <li>
        안드로이드 시스템은 앱의 패키지명으로 디렉터리(내장 메모리 공간)를 생성한다.
      </li>
      <li>
        내장 메모리이기에 다른 앱에서의 접근이 불가하다.
      </li>
    </ul>
  <li>
    앱은 <strong>민감한 데이터</strong>는 대부분 내장 메모리에 저장하나 내장 메모리는 용량이 작기 때문에 <strong>크기가 큰 데이터</strong>는 외장 메모리를 이용한다.
  </li>
  <li>
    파일을 내장 메모리에 저장할 때에는 <strong>java.io</strong>의 <strong>File 클래스</strong>를 이용한다.
  </li>
    <ul>
      <li>
        File() 생성자의 첫 번째 매개변수는 Context 객체의 <strong>filesDir 속성</strong>을 지정하고 두 번째 매개변수에는 <strong>파일명</strong>을 전달한다.
      </li>
    </ul>
</ul>

```kotlin
// 1. 파일 객체 생성 후 데이터 쓰기.
// filesDir 속성 지정 + 파일명 전달.
val file = File(filesDir, "test.txt")
val writeStream: OutputStreamWriter = file.writer()
writeStream.write("hello world")
writeStream.flush()

// 2. 파일의 데이터 읽기.
val readStream: BufferedReader = file.reader().buffered()
readStream.forEachLine {
    Log.d("kkang", "$it")
}
```

```kotlin
// 3. Context 객체의 함수를 사용해 데이터를 쓰고 읽기.
openFileOutput("test.txt", Context.MODE_PRIVATE).use {
    it.write("hello world!!".toByteArray())
}
openFileInput("test.txt").bufferedReader().forEachLine {
    Log.d("kkang", "$it")
}
```

<br>

<h2>2-2. 외장 앱별 메모리의 파일 이용하기</h2>
<ul>
  <li>
    외장 메모리는 SD 카드와 같은 외부 저장 장치도 의미하지만 내부 저장소의 파티션을 나누어 외장 메모리로도 사용이 가능하다. 따라서 모든 기기가 외장 메모리를 제공한다고 보장할 수 없기 때문에 <strong>Environment.getExternalStorageState() 함수</strong>로 <strong>외장 메모리 사용 가능 여부</strong>를 확인해야 한다.
  </li>
</ul>

```kotlin
// 1. 외장 메모리 사용 가능 여부 판단.
if (Environment.getExternalStorageState() == Environment.MEDIA_MOUNTED) {
    
    // MEDIA_MOUNTED면 가능.
    Log.d("kkang", "ExternalStorageState MOUNTED")

} else {
    
    // 아닌 경우 사용 불가능.
    Log.d("kkang", "ExternalStorageState UNMOUNTED")
}
```

<h3>2-2-1. 앱별 저장소 이용</h3>
<ul>
  <li>
    외장 메모리는 앱별 저장소와 공용 저장소로 구분된다. 만약 앱별 저장소의 파일을 외부 앱에서 접근하게 하려면 이전 장에서 배운 <strong>파일 프로바이더</strong>를 이용해야 한다.
  </li>
  <li>
    외장 메모리의 앱별 저장소 위치는 <strong>getExternalFilesDir()</strong> 함수로 구한다.
  </li>
    <ul>
      <li>
        getExternalFilesDir(null) 함수가 반환하는 위치는 "/storage/emulated/0/Android/data/패키지명/files"와 같다.
      </li>
      <li>
        매개변수는 파일의 종류를 나타내는데 null이 아닌 다음과 같은 Environment의 상수를 전달할 수도 있다.
      </li>
      <ul>
        <li>
          Environment.DIRECTORY_PICTURES
        </li>
          <ul>
            <li>
              상수가 전달된 결과는 /storage/emulated/0/Android/data/패키지명/files/Pictures와 같다.
            </li>
          </ul>
        <li>
          Environment.DIRECTORY_DOCUMENTS
        </li>
        <li>
          Environment.DIRECTORY_MUSIC
        </li>
        <li>
          Environment.DIRECTORY_MOVIES
        </li>
      </ul>
    </ul>
</ul>

```kotlin
// 1. 앱별 저장소에 접근.
// e.g. /storage/emulated/0/Android/data/패키지명/files
val file: File? = getExternalFilesDir(null)
Log.d("kkang", "${file?.absolutePath}")
```

```kotlin
// 2. 앱별 저장소에 파일 쓰기와 읽기.
// 파일 쓰기.
val file: File = File(getExternalFilesDir(null), "test.txt")
val writeStream: OutputStreamWriter = file.writer()
writeStream.write("hello world")
writeStream.flush()

// 파일 읽기.
val readStream: BufferedReader = file.reader().buffered()
readStream.forEachLine {
    Log.d("kkang", "$it")
}
```

<h3>2-2-2. 공용 저장소 이용</h3>
<ul>
  <li>
    공용 저장소의 예는 카메라 앱에서 촬영한 사진 파일은 모든 앱에서 이용할 수 있는 경우가 있다.
  </li>
  <li>
    앱별 저장소는 앱이 삭제되면 <strong>파일도 모두 삭제</strong> 되지만, 공용 저장소는 모든 앱을 위한 저장소이므로 앱을 삭제해도 <strong>파일은 삭제되지 않는다</strong>.
  </li>
  <li>
    공용 저장소는 안드로이드 시스템에서 <strong>파일 종류</strong>에 따라 <strong>지정한 폴더</strong>이다.
  </li>
    <ul>
      <li>
        파일 경로로 직접 접근하지 않고 <strong>시스템이 제공하는 API</strong>를 이용해야 한다.
      </li>
      <li>
        <strong>파일 타입(문서, 미디어 등)</strong>에 따라 이용 방법이 다르다.
      </li>
    </ul>
  <li>
    공용 공간의 미디어 타입 파일에 접근하기 위해서는 매니페스트에 <strong>퍼미션</strong>이 선언되어 있어야 하며 <strong>버전별로 다르게 지정</strong>해 주어야 한다.
  </li>
    <ul>
      <li>
        안드로이드 12(API Level 32)까지느 공용 공간 이용을 위해 하나의 퍼미션만 추가하면 되었다.
      </li>
      <li>
        안드로이드 13(API Level 33)부터는 공용 공간의 파일 타입을 구분하여 이용하기 시작해 타입에 따라 퍼미션을 지정해야 한다.
      </li>
      <li>
        안드로이드 14부터는 사용자에게 앱에서 미디어 파일에 대한 접근을 다시 선태할 수 있는 퍼미션이 추가 되었다.
      </li>
    </ul>
  <li>
    안드로이드 버전별로 퍼미션이 상이하기 때문에 <strong>퍼미션 체크 및 요청</strong>도 <strong>버전을 명시</strong>해 구분해서 체크해 주어야 한다.
  </li>
</ul>

```xml
<!-- 1. 매니페스트 퍼미션 설정. -->
<!-- API Level 32까지 -->
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>

<!-- API Level 33부터 -->
<uses-permission android:name="android.permission.READ_MEDIA_IMAGES" />
<uses-permission android:name="android.permission.READ_MEDIA_VIDEO" />

<!-- API Level 34 -->
<uses-permission android:name="android.permission.READ_MEDIA_VISUAL_USER_SELECTED" />
```

```kotlin
// 2. 버전별 퍼미션 요청.
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.UPSIDE_DOWN_CAKE) {
    requestPermissions.launch(arrayOf(READ_MEDIA_IMAGES, READ_MEDIA_VIDEO, READ_MEDIA_VISUAL_USER_SELECTED))
} else if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
    requestPermissions.launch(arrayOf(READ_MEDIA_IMAGES, READ_MEDIA_VIDEO))
} else {
    requestPermissions.launch(arrayOf(READ_EXTERNAL_STORAGE))
}
```

```kotlin
// 3. 파일 정보 획득.
val projection = arrayOf(
    // 파일의 식별자 데이터 (_ID).
    MediaStore.Images.Media._ID,
    MediaStore.Images.Media.IDSPLAY_NAME,
    MediaStore.Images.Media.SIZE,
    MediaStore.Images.Media.MIME_TYPE,
)

val collectionUri = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
    MediaStore.Images.Media.getContentUri(MediaStore.VOLUME_EXTERNAL)
} else {
    MediaStore.Images.Media.EXTERNAL_CONTENT_URI
}

contentResolver.query(
    collectionUri,
    projection,
    null,
    null,
    null,
)?.use { cursor ->
    while (cursor.moveToNext()) {
        val uri = cursor.getLong(0)
        val name = cursor.getString(1)
        val size = cursor.getLong(2)
        val mimeType = cursor.getString(3)

        Log.d("kkang", "uri: $uri, name: $name, size: $size, mimeType: $mimeType")
    }
}
```

```kotlin
// 4. 파일 읽어서 화면 출력.
sval contentUri: Uri = ContentUris.withAppendedId(
  // 
    MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
    uri
)

val resolver = applicationContext.contentResolver
resolver.openInputStream(contentUri).use { stream ->
    // stream 객체에서 작업 수행.
    val option = BitmapFactory.Options()
    option.inSampleSize = 10
    val bitmap = BitmapFactory.decodeStream(stream, null, option)
    binding.imageView.setImageBitmap(bitmap)
}
```

<br><br>

<h1>3. 공유된 프리퍼런스에 보관하기</h1>
<ul>
  <li>
    공유된 프리퍼런스는 <strong>플랫폼 API</strong>에서 제공하는 클래스로, 데이터를 <strong>key-value 형태</strong>로 저장할 때 사용한다.
  </li>
  <li>
    공유된 프리퍼런스는 <strong>앱의 간단한 데이터</strong>를 저장할 때 유용하며 내부적으로 <strong>내장 메모리의 앱 폴더에 XML 파일</strong>로 저장된다.
  </li>
  <li>
    SharedPreferences 객체를 얻는 방법은 다음 두 가지를 제공한다.
  </li>
    <ul>
      <li>
        Activity.getPreferences(int mode)
      </li>
        <ul>
          <li>
            <strong>액티비티 단위</strong>로 데이터를 저장할 때 사용한다.
          </li>
          <li>
            매개변수에 파일명이 들어가지 않으며 함수를 호출한 액티비티 클래스명으로 XML 파일이 자동으로 생성된다.
          </li>
        </ul>
      <li>
        Context.getSharedPreferences(String name, int mode)
      </li>
        <ul>
          <li>
            앱 전체의 데이터를 key-value 형태로 저장하려할 때에 사용한다.
          </li>
          <li>
            첫 번째 매개변수에 지정한 이름의 파일로 데이터가 저장된다.
          </li>
        </ul>
    </ul>
  <li>
    공유된 프리퍼런스를 이용해 데이터를 저장할 때에는 다음과 같은 <strong>SharedPreferences.Editor 클래스 함수</strong>를 이용해야 한다.
  </li>
    <ul>
      <li>
        putBoolean(String key, boolean value)
      </li>
      <li>
        putInt(String key, int value)
      </li>
      <li>
        putFloat(String key, float value)
      </li>
      <li>
        putLong(String key, long value)
      </li>
      <li>
        putString(String key, String value)
      </li>
    </ul>
  <li>
    SharedPreferences.Editor 객체는 SharedPreferences의 <strong>edit() 함수</strong>로 얻는다.
  </li>
    <ul>
      <li>
        이렇게 얻은 Editor 객체의 put~으로 시작하는 함수를 이용해 데이터를 담으면 <strong>commit() 함수</strong>를 호출하는 순간 저장된다.
      </li>
    </ul>
  <li>
    프리퍼런스에 저장된 데이터를 가져올 때에는 SharedPreferences의 <strong>게터 함수<.strong>를 이용한다.
  </li>
    <ul>
      <li>
        getBoolean(String key, boolean defValue)
      </li>
      <li>
        getFloat(String key, float defValue)
      </li>
      <li>
        getInt(String key, int defValue)
      </li>
      <li>
        getLong(String key, long defValue)
      </li>
      <li>
        getString(String key, String defValue)
      </li>
    </ul>
</ul>

```kotlin
// 1. 액티비티 데이터 저장.
val sharedPref = getPreferences(Context.MODE_PRIVATE)
```

```kotlin
// 2. 앱 전체의 데이터 저장.
val sharedPref = getSharedPreferences("my_prefs", Context.MODE_PRIVATE)
```

```kotlin
// 3. 프리퍼런스에 데이터 저장.
sharedPref.edit().run {
    putString("data1", "hello")
    putInt("data2", 10)
    commit()
}
```

```kotlin
// 4. 프리퍼런스에서 데이터 가져오기.
val data1 = sharedPref.getString("data1", "world")
val data2 = sharedPref.getInt("data2", 10)
```

<br>

<h2>3-1. 앱 설정 화면 만들기</h2>
<ul>
  <li>
    이전에는 설정 화면을 자동으로 만들어주는 API를 많이 사용했지만 안드로이드 10 버전(API 레벨 29)부터 모두 deprecated 되었고 이후 <strong>AndroidX의 Preference</strong>를 이용할 것ㅇ르 권장하고 있다.
  </li>
    <ul>
      <li>
        AndroidX의 Preference는 앱에서 설정 기능을 제공할 때 이용하는 제트팩의 API이다.
      </li>
    </ul>
  <li>
    AndroidX의 Preference를 이용하기 위해서는 빌드 그래들 파일에 다음의 라이브러리를 dependencies로 선언해야 한다.
  </li>
    <ul>
      <li>
        implementation("androidx.preference:preference-ktx:1.2.1")
      </li>
    </ul>
</ul>

<h3>3-1-1. 프리퍼런스 이용 방법</h3>
<ul>
  <li>
    프리퍼런스를 이용해 앱에 설정 기능을 제공하려면 가장 먼저 <strong>res/xml 디렉터리</strong>에 설저과 관련된 <strong>XML 파일</strong>을 생성해야 한다.
  </li>
    <ul>
      <li>
        루트 태그가 <strong>PreferenceScreen</strong>이어야 하며 하위 태그에 SwitchPreferenceCompat, Preference 등의 태그를 이용해 설정 항목을 준비한다.
      </li>
      <li>
        사용자가 설정 화면에서 설정한 값은 내부적으로 공유된 프리퍼런스를 이용해 <strong>key-value 형태</strong>로 저장된다.
      </li>
    </ul>
  <li>
    생성한 XML 파일은 코드에서 적용해야 하며 <strong>PreferenceFragmentCompat 클래스</strong>를 이용한다. 즉, <strong>상속받은 프래그먼트</strong>로 설정 화면을 준비한다.
  </li>
    <ul>
      <li>
        상속받은 프래그먼트 클래스는 <strong>onCreatePreferences() 함수를 재정의</strong>해서 작성한다.
      </li>
        <ul>
          <li>
            함수에서 <strong>setPreferencesFromResource()</strong>를 이용해 앞에서 만든 <strong>설정 XML 파일을 전달</strong>한다.
          </li>
        </ul>
    </ul>
  <li>
    생성한 프래그먼트를 액티비티에 출력하는 것은 일반적인 액티비티 프래그먼트를 이용하는 것과 차이가 없다.
  </li>
</ul>

```xml
<!-- 1. 설정 XML 파일 -->
<PreferenceScreen xmlns:app="http://schemas.android.com/apk/res-auto">
    <SwitchPreferenceCompat
        app:key="notifications"
        app:title="Enable message notifications" />
    
    <Preference
        app:key="feedback"
        app:title="Send feedback"
        app:summary="Report technical issues or suggest new features" />
</PreferenceScreen>
```

```kotlin
// 2. 설정 XML 파일 적용.
class MySettingFragment : PreferenceFragmentCompat() {
    override fun onCreatePreferences(savedInstanceState: Bundle?, rootKey: String?) {
        setPreferencesFromResource(R.xml.settings, rootKey)
    }
}
```

```xml
<!-- 3. 액티비티에서 프래그먼트 출력. -->
<androidx.fragment.app.FragmentContainerView xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:name="com.example.ch17_database.MySettingFragment"
    android:id="@+id/settingView" />
```

<h3>3-1-2. 설정 화면 구성</h3>
<ul>
  <li>
    설정 항목이 많으면 관련 있는 것끼리 <strong>묶거나</strong> 설정 화면을 <strong>여러 개로 나눌 수 있다</strong>.
  </li>
    <ul>
      <li>
        이때에는 <strong>PreferenceCategory</strong>와 <strong>Preference</strong> 태그를 이용한다.
      </li>
    </ul>
  <li>
    설정 항목을 분리할 경우에는 <strong>설정 XML</strong>과 <strong>프래그먼트</strong>를 분리하는 항목에 매칭되게 생성해야한다.
  </li>
    <ul>
      <li>
        이후 설정들을 포함하는 <strong>메인 설정 XML</strong>을 작성한다.
      </li>
      <li>
        메인 설정 XML에서 각 설정 화면은 <strong>Preference 태그</strong>로 지정한다.
      </li>
      <li>
        Preference 태그를 통해 화면을 분할한 후에는 <strong>PreferenceFragmentCompat.OnPreferenceStartFragmentCallback 인터페이스</strong>를 구현하고 <strong>onPreferenceFragment() 함수를 재정의</strong>해 작성해야 한다.
      </li>
        <ul>
          <li>
            onPreferenceStartFragment()는 <strong>설정 화면이 바뀔때마다 호출</strong>되는 함수이기 때문에 설저 화면이 바뀔 때마다 액티비티의 액션바에 출력되는 제목을 바꿀 수도 있다.
          </li>
        </ul>
    </ul>
  <li>
    설정 화면이 복잡한 경우에는 설정 화면에서 <strong>인텐트</strong>를 이용해 <strong>하위 설정 화면</strong>을 띄우는 방법으로 구현할 수 있다.
  </li>
    <ul>
      <li>
        코드에서도 가능하지만 <strong>설정 XML 등록</strong>만으로도 가능하다. (XML 설정만으로도 구현이 가능함).
      </li>
      <li>
        암시적 인텐트를 사용할 수도 있다.
      </li>
    </ul>
</ul>

```xml
<!-- 1. 항목끼리 묶기. -->
<PreferenceScreen xmlns:app="http://schemas.android.com/apk/res-auto">
    <PreferenceCategory
        app:key="a_category"
        app:title="A Setting">

        <SwitchPreferenceCompat
            app:key="a1"
            app:title="A - 1 Setting" />
        
        <SwitchPreferenceCompat
            app:key="a2"
            app:title="A - 2 Setting" />
        
    </PreferenceCategory>
    <PreferenceCategory
        app:key="B_category"
        app:title="B_Setting">

        <SwitchPreferenceCompat
            app:key="b1"
            app:title="B - 1 Setting" />
    </PreferenceCategory>
</PreferenceScreen>
```

```xml
<!-- 2. 두 화면을 포함하는 설정 화면. -->
<PreferenceScreen xmlns:app="http://schemas.android.com/apk/res-auto">
    <Preference
        app:key="a"
        app:summary="A Setting summary"
        app:title="A Setting"
        app:fragment="com.example.test17.ASettingFragment" />
    <Prefernece
        app:key="b"
        app:summary="B Setting summary"
        app:title="B Setting"
        app:fragment="com.example.test17.BSettingFragment" />
</PreferenceScreent>
```

```kotlin
// 2. 분할 설정 화면을 보여주는 액티비티 코드.
class SettingActivity : AppCompatActivity(),
    PreferenceFragmentCompat.OnPreferenceStartFragmentCallback {
    
    (... 생략 ...)
    
    override fun onPreferenceStartFragment(caller: PreferenceFragmentCompat,
                                           pref: Preference
    ): Boolean {
        // 새로운 프래그먼트 인스턴스화.
        val args = pref.extras
        val fragment = supportFragmentManager.fragmentFactory.instantiate(
            classLoader,
            pref.fragment as String)
        fragment.arguments = args
        supportFragmentManager.beginTransaction()
            .replace(R.id.setting_content, fragment)
            .addToBackStack(null)
            .commit()
        return true
    }
}
```

```xml
<!-- 3. 인텐트로 설정 화면 실행. -->
<Preference
    app:key="activity"
    app:title="Launch activity">
    
    <!-- Preference 하위에 intent 태그로 설정 화면을 지정하면 사용자가 이를 클릭했을 때 설정 화면이 실행됨. -->
    <intent
        android:targetClass="com.exmaple.test17.SomeActivity"
        android:targetPackage="com.example.test17" />

        <!-- 인텐트에 엑스트라 정보도 포함할 수 있음. -->
        <extra
            android:name="example_key"
            android:value="example_value" />
    </intent>
</Preference>
```

```xml
<!-- 4. 암시적 인텐트 사용. -->
<intent
    android:action="android.intent.action.VIEW"
    android:data="http://wwww.google.com" />
```

<h3>3-1-3. 설정 제어</h3>
<ul>
  <li>
    코드에서 설정을 제어하는 방법에 대해 알아본다.
  </li>
  <li>
    각 항목은 <strong>findPreference() 함수</strong>로 얻어야 한다.
  </li>
  <li>
    summary 속성을 자동으로 지정할 때에는 <strong>SimpleSummaryProvider</strong>를 사용한다.
  </li>
</ul>

```xml
<!-- 1. 글을 입력받는 설정. -->
<EditTextPreference
    app:key="id"
    app:title="ID 설정"
    app:isPreferenceVisible="false" />
```

```kotlin
// 2. 1번에서 설정한 app:isPreferenceVisible="false" 값을 코드에서 true로 변경한다.
override fun onCreatePreferences(savedInstanceState: Bundle?, rootKey: String?) {
    setPreferencesFromResource(R.xml.settings, rootKey)
    val idPreference: EditTextPreference? = findPreference("id")
    // 값을 true로 변경.
    idPreference?.isVisible = true

    idPreference?.summary="code summary"
    idPreference?.title="code title"
}
```

```xml
<!-- 3. 설정 XML 예. -->
<EditTextPreference
    app:key="id"
    app:title="ID 설정" />

<ListPreference
    app:key="color"
    app:title="색상 선택"
    android:entries="@array/my_color"
    app:entryValues="@array/my_color_values" />
```

```kotlin
// 4. 3번에서 설정한 xml 파일에서 summary가 자동으로 지정되도록한다.
// 없는 경우 'Not set'이라는 문자열이 출력된다.
val idPreference: EditTextPreference? = findPreference("id")
val colorPreference: ListPreference? = findPreference("color")

idPreference?.summaryProvider = EditTextPreference.SimpleSummaryProvider.getInstance()
colorPreference?.summaryProvider = ListPreference.SimpleSummaryProvider.getInstance()
```

```kotlin
// 5. 4번과 다르게 SummaryProvier의 하위 클래스를 만들어 코드에서 원하는 대로 summary가 지정되게 할 수도 있다.
idPreference?.summaryProvider = Preference.SummaryProvider<EditTextPreference> { preference -> 
    val text = preference.text
    if (TextUtils.isEmpty(text)) {
        "설정되지 않았습니다."
    } else {
        "설정된 ID 값은 : $text 입니다."
    }
}
````

```kotlin
// 6. 설정 항목에 이벤트를 추가할 수 있으며 이벤트를 처리해야 하는 경우 setOnPreferenceClickListener()
//    함수로 이벤트 핸들러를 지정한다.
idPreference?.setOnPreferenceClickListener { preference ->
    Log.d("kkang", "preference key : ${preference.key}")
    true
}
```

<h3>3-1-4. 설정한 값 가져오기</h3>
<ul>
  <li>
    프리퍼런스를 이용하면 설정한 내용이 XML 파일로 <strong>자동 저장</strong>되지만, 설정값을 가져올 때에는 <strong>PreferenceManager.getDefaultSharePreferences() 함수</strong>를 이용한다.
  </li>
</ul>

```xml
<!-- 1. 가져오려는 설정 값을 가진 XML 파일 예 -->
<!-- 사용자가 입력한 값은 id 키값으로 저장된다.-->
<EditTextPreference
    app:key="id"
    app:title="ID 설정" />
```

```kotlin
// 2. 설정값 가져오기.
val sharedPreferences = PreferenceManager.getDefaultSharedPreferences(activity)
val id = sharedPreferences.getString("id", "")
```

<h3>3-1-5. 설정 변경 순간 감지</h3>
<ul>
  <li>
    설정이 변경되는 것을 감지하는 것에는 <strong>Preference.OnPrefernceChangeListener</strong>를 이용하는 것과 <strong>SharedPreferences.OnSharedPreferenceChangeListener</strong>를 이용하는 방법 두 가지가 있다.
  </li>
    <ul>
      <li>
        Preference.OnPreferenceChangeListener는 <strong>각 프리퍼런스 객체</strong>마다 이벤트 핸들러를 직접 지정하여 객체의 설정 내용이 변경되는 순간의 이벤트를 처리한다.
      </li>
      <li>
        SharedPreferences.OnSharedPreferenceChangeListener는 모든 설정 객체의 변경을 <strong>하나의 이벤트 핸들러</strong>에서 처리한다.
      </li>
        <ul>
          <li>
            이 경우 설정 프래그먼트 클래스에서 <strong>SharedPreferences.OnSharedPreferenceChangeListener</strong>를 구현하고 <strong>추상함수 onSharedPreferenceChanged()를 재정의</strong>해야한다.
          </li>
          <li>
            이벤트 감지가 더 이상 필요하지 않을 때에는 <strong>unregisterOnSharedPreferenceChangeListener() 함수</strong>를 통해 <strong>이벤트 등록을 해제</strong>한다.
          </li>
        </ul>
    </ul>
</ul>

```kotlin
// 1. 프리퍼런스를 이용한 이벤트 처리.
idPreference?.setOnPreferenceChangeListener { preference, newValue ->
    Log.d("kkang", "preference key : ${preference.key}, newValue : $newValue")
    true
}
```

```kotlin
// 2. 공유된 프리퍼런스를 이용해 이벤트 처리.
class MySettingFragment : PreferenceFragmentCompat(), SharedPreferences.OnSharedPreferenceChangeListener {
    (... 생략 ...)
    override fun onSharedPreferenceChanged(sharedPreferences: SharedPreferences, key: String?) {
        if (key == "id") {
            Log.i("kkang", "newValue : " + sharedPreferences?.getString("id", ""))
        }
    }
    
    override fun onResume() {
        super.onResume()
        preferenceManager.sharedPreferences?.registerOnSharedPreferenceChangeListener(this)
    }

    override fun onPause() {
        super.onPause()
        preferenceManager.sharedPreferences?.unregisterOnSharedPreferenceChangeListener(this)
    }
}
```

<br><br>

<h1>4. 개선된 할 일 목록 앱 만들기</h1>
<ul>
  <li>
    도서 p542의 실습을 따라한다.
  </li>
</ul>