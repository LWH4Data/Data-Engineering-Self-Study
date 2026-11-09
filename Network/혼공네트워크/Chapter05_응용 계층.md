<h1>1. DNS와 자원</h1>
<ul>
  <li>
    메시지를 주고받고자 하는 대상을 파악하기 위해서는 IP 주소 외에도 <strong>도메인 네임</strong>을 사용할 수 있다.
  </li>
  <li>
    송수신하고자 하는 정보를 식별하기 위한 방법으로는 <strong>위치 기반의 식별자인 URL</strong>과 <strong>이름 기반의 식별자인 URN</strong>이 있다.
  </li>
</ul>

<br>

<h2>1-1. 도메인 네임과 네임 서버</h2>
<ul>
  <li>
    호스트를 특정하는 데 IP를 사용할 수 있지만 IP 주소만을 사용하면 통신하고자 하는 <strong>모든 호스트의 IP 주소를 기억</strong>하는 것이 부담되고 호스트 IP 주소는 <strong>언제든 바뀔 수 있다는 문제</strong>가 있다.
  </li>
  <li>
    위와 같은 문제로 일반적으로 사용자는 상대 호스트를 특정하기 위해 IP 주소보다는 <strong>도메인 네임(domain name)</strong>을 많이 사용한다.
    <ul>
      <li>
        도메인 네임이란 호스트의 IP 주소와 대응되는 <strong>문자열 형태</strong>의 호스트 특정 정보이다.
      </li>
      <li>
        도메인 네임과 IP 주소는 <strong>네임 서버(name server)</strong>에서 관리하고, 도메인 네임을 관리하는 네임 서버는 <strong>DNS 서버</strong>라고도 부른다.
      </li>
    </ul>
  </li>
  <li>
    도메인 네임은 IP 주소에 비해 기억하기 쉽고 IP 주소가 바뀌어도 도메인 네임은 그대로이기에 활용하기 편리하다.
  </li>
  <li>
    도메인 네임은 <strong>점(.)</strong>을 기준으로 계층적으로 분류된다.
    <ul>
      <li>
        최상단에는 <strong>루트 도메인(root domain)</strong>이 있다. 일반적으로 알고 있는 도메인 네임의 <strong>마지막 부분</strong>을 의미한다.
      </li>
      <li>
        루트 도메인 이후에는 <strong>최상위 도메인(TLD; Top-Level Domain)</strong>이 있고 그 후에 또 도메인들이 나열된다.
      </li>
      <li>
        예를 들어 www.example.com이라면 최상위 도메인은 com이다.
        <ul>
          <li>
            최상위 도메인은 다양하고 대표적으로 com, net, org, kr(대한민국), jp(일본), cn(중국), us(미국) 등이 있다.
          </li>
        </ul>
      </li>
    </ul>
  </li>
  <li>
    정확히는 루트 도메인(.)이 가장 마지막에 붙지만 일반적으로 이를 생략하여 표기한다. 따라서 'www.google.com'이나 'www.google.com.'' 둘 모두 동일하게 접속된다.
  </li>
  <li>
    최상위 도메인의 하부 도메인은 <strong>2단계 도메인(second-level domain)</strong>이라고 한다.
  </li>
  <li>
    도메인 네임의 단계는 일반적으로 3~5 단계 정도이며 도메인 네임을 모두 포함하는 도메인 네임을 <strong>전체 주소 도메인 네임(FQDN; Fully-Qualified Domain Name)</strong>이라 한다.
    <ul>
      <li>
        FQDN은 전체를 명시하여 호스트를 나타낼 수 있기 때문에 <strong>호스트 네임(host name)</strong>이라 부르기도 한다.
      </li>
    </ul>
  </li>
  <li>
    계층적인 도메인 네임을 효율적으로 관리하기 위해 네임 서버 또한 <strong>계층적인 형태</strong>를 이룬다.
  </li>
  <li>
    네임 서버는 <strong>여러 개</strong> 존재하며 <strong>전 세계 여러 군데</strong>에 위치해 있다.
  </li>
  <li>
    위처럼 계층적이고, 분산된 도메인 네임(Domain Name)에 대한 관리 체계(System)를 도메인 네임 시스템(Domain Name System), 줄여서 <strong>DNS</strong>라고 부른다.
    <ul>
      <li>
        DNS는 호스트가 이런 도메인 네임 시스템을 이용할 수 있도록 하는 <strong>애플리케이션 계층 프로토콜</strong>을 의미하기도 한다.
      </li>
      <li>
        즉 DNS는 계층적이고 분산된 도메인 네임에 대한 <strong>관리 체계</strong>이며 이를 관리하는 <strong>프로토콜</strong>이다.
      </li>
    </ul>
  </li>
</ul>

<h4>개인 전화번호부와 같은 hosts 파일</h4>
<ul>
  <li>
    호스트는 호스트마다 <strong>hosts 파일</strong>을 가지고 있으며 이는 <strong>도메인 네임과 IP 주소의 대응 관계</strong>를 담은 파일로 이를 통해 <strong>도메인 네임에 대응하는 IP 주소를 식별</strong>할 수 있다.
  </li>
  <li>
    MAC OS 혹은 리눅스는 /etc/hosts에 위치하고, Window OS의 경우 %SystemRoot%\System32\drivers\etc\hosts에 위치한다.
  </li>
  <li>
    단, hosts 파일 하나만으로는 네트워크 세성에 있는 모든 호스트의 도메인 네임, IP 주소 쌍을 기억하기 어렵기 때문에 별도의 서버가 있는 것이다.
  </li>
</ul>

<h4>서브 도메인이란 무엇인가요?</h4>
<ul>
  <li>
    서브 도메인(subdomain)이란 <strong>다른 도메인이 포함된 도메인</strong>을 의미한다.
  </li>
  <li>
    예를 들어 google.com의 서브 도메인들로는 다음이 있다.
    <ul>
      <li>
        main.google.com
      </li>
      <li>
        www.google.com
      </li>
      <li>
        scholar.google.com
      </li>
      <li>
        drive.google.com
      </li>
    </ul>
  </li>
</ul>

<br>

<h2>1-2. 계층적 네임 서버</h2>
<ul>
  <li>
    IP 주소를 모르는 상태에서 도메인 네임에 대응되는 IP 주소를 알아내는 과정을 흔히 도메인 네임을 <strong>풀이(resolve)</strong>한다고 표현하며 영어로는 <strong>resolving한다</strong>라고도 한다.
  </li>
  <li>
    IP 주소를 알아내는 과정에서 다양한 네임 서버들이 사용되는데 중요한 네임 서버의 유형은 크게 네 가지가 있다.
    <ul>
      <li>
        <strong>로컬 네임 서버(local name server)</strong>
        <ul>
          <li>
            클라이언트와 맞닿아 있는 서버로 클라이언트가 도메인 네임을 통해 IP 주소를 알아내고자 할 때 <strong>가장 먼저 찾게 되는 네임 서버</strong>이다.
          </li>
          <li>
            로컬 네임 서버의 주소는 일반적으로 <strong>ISP</strong>에서 할당해 주는 경우가 많다.
            <ul>
              <li>
                ISP에서 할당해 주는 로컬 네임 서버가 아닌 <strong>공개 DNS 서버(public DNS Server)</strong>를 이용할 수도 있다.
              </li>
            </ul>
          </li>
        </ul>
      </li>
      <li>
        <strong>루트 네임 서버(root name server)</strong>
        <ul>
          <li>
            로컬 네임 서버가 대응되는 IP 주소를 모른다면 루트 네임 서버에 해당 도메인 네임을 질의하게 된다.
          </li>
          <li>
            루트 네임 서버는 루트 도메인을 관장하는 네임 서버로, 질의에 대해 TLD 네임 서버의 IP 주소를 반환할 수 있다.
          </li>
        </ul>
      </li>
      <li>
        <strong>TLD(최상위 도메인) 네임 서버</strong>
        <ul>
          <li>
            TLD 네임 서버는 TLD를 관리하는 네임 서버이다.
          </li>
          <li>
            TLD 네임 서버는 질의에 대해 TLD의 하위 도메인인 네임을 관리하는 네임 서버 주소를 반환할 수 있다.
          </li>
        </ul>
      </li>
      <li>
        <strong>책임 네임 서버(authoritative name server)</strong>
        <ul>
          <li>
            책임 네임 서버는 특정 도메인 영역(name)을 관리하는 네임 서버로, 자신이 관리하는 도메인 영역의 질의에 대해서 다른 네임 서버에 넘기지 않고 바로 답할 수 있는 네임 서버이다.
            <ul>
              <li>
                쉽게 말해 로컬 네임 서버가 <strong>마지막으로 질의하는 네임 서버</strong>이다.
              </li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
  </li>
  <li>
    로컬 네임 서버가 네임 서버들에게 질의하는 방법에는 크게 <strong>재귀적 질의</strong>와 <strong>반복적 질의</strong> 두 가지가 있다.
    <ul>
      <li>
        재귀적 질의(recursive query)는 <strong>'클라이언트 &rarr; 로컬 네임 서버 &rarr; 루트 네임 서버 &rarr; TLD 네임 서버 &rarr; 다음 단계 서버'</strong>로 질의하는 과정을 반복하여 최종 응답 결과를 <strong>역순으로 전달</strong>받는 방식이다.
      </li>
      <li>
        반복적 질의(iterative query)란 <strong>로컬 네임 서버</strong>가 <strong>반복적</strong>으로 루트 네임 서버, TLD 네임 서버, 책엠 네임 서버에 질의하고 최종 결과를 클라이언트에 알려 주는 방식이다.
      </li>
    </ul>
  </li>
  <li>
    로컬 네임 서버가 도메인을 통해 IP를 얻는 과정에는 단계가 많아 요청이 많아지면 <strong>루트 네임 서버에 과부하</strong>가 걸릴 수 있다.
    <ul>
      <li>
        실제로는 네임 서버들이 기존에 응답받은 결과를 임시로 저장했닫가 추후 같은 질의에 이를 활용하는 경우가 많으며 이를 <strong>DNS 캐시(DNS cache)</strong>라고 한다.
      </li>
      <li>
        DNS 캐시를 저장하는 용도로 사용되는 서버도 있다.
      </li>
      <li>
        DNS 캐시는 영원히 남는 것은 아니며 <strong>TTL(Time To Live)</strong>이라는 값과 함께 저장되며 이 값은 <strong>캐시될 수 있는 시간</strong>을 의미한다.
      </li>
    </ul>
  </li>
</ul>

<br>

<h2>1-3. 자원을 식별하는 URI</h2>
<ul>
  <li>
    송수신하고자 하는 정보를 식별하기 위한 방법에는 <strong>URI</strong>가 있다. 
    <ul>
      <li>
        URI를 식별 정보 기준으로 분류한 개념들에는 <strong>URL</strong>과 <strong>URN</strong>이 있다.
      </li>
    </ul>
  </li>
  <li>
    상기한 URI, URL, URN을 이해하기 위해서는 자원(resource)이 무엇인지 이해해야 한다. <strong>자원</strong>이란 <strong>네트워크상의 메시지를 통해 주고받는 대상</strong>을 의미한다.
    <ul>
      <li>
        예를 들면 HTML 파일, 이미지나 동영상, 텍스트 파일 등이 모두 해당한다.
      </li>
    </ul>
  </li>
  <li>
    오늘날 인터넷 환경을 이루는 대부분의 통신은 <strong>HTTP를 기반</strong>으로 이루어지고, 자원이라는 용어는 <strong>HTTP 요청 메시지의 대상</strong>이라고도 표현한다.
  </li>
  <li>
    네트워크상에서 자원을 주고받기 위해서는 자원을 식별할 수 있어야하며 이렇게 <strong>자원을 식별</strong>할 수 있는 정보를 <strong>URI(Uniform Resource Identifier)</strong>라고 부른다.
    <ul>
      <li>
        <strong>위치</strong>를 이용해 자원을 식별하는 경우를 <strong>URL(Uniform Resource Locator)</strong>이라 한다.
      </li>
      <li>
        <strong>이름</strong>을 이용해 자원을 식별하는 경우를 <strong>URN(Uniform Resource Name)</strong>이라 한다.
      </li>
    </ul>
  </li>
</ul>

<h3>1-3-1. URL</h3>
<ul>
  <li>
    오늘날 인터넷 환경에서 자원 식별에 더 많이 사용되는 방법은 URL이다.
  </li>
  <li>
    예를 들어 'foo://www.example.com:8042/over/there?name=ferret#nose'의 형식은 다음과 같다.
    <ul>
      <li>
        foo &rarr; scheme
        <ul>
          <li>
            URL의 첫 부분으로 <strong>자원에 접근하는 방법</strong>을 의미하며 일반적으로 사용할 <strong>프로토콜</strong>이 명시된다.
          </li>
          <li>
            HTTP를 사용할 때에는 http://를, HTTPS를 사용할 때에는 https://를 명시한다.
          </li>
        </ul>
      </li>
      <li>
        www.example.com:8042 &rarr; authority
        <ul>
          <li>
            authority는 <strong>호스트를 특정할 수 있는 정보</strong>, 예를 들어 IP 주소 혹은 도메인 네임이 명시되면 <strong>콜론(:) 뒤에 포트 번호</strong>를 덧붙일 수도 있다. 
          </li>
        </ul>
      </li>
      <li>
        /over/there? &rarr; path
        <ul>
          <li>
            path에는 <strong>자원이 위치한 경로</strong>가 명시된다. 
          </li>
          <li>
            자원의 위치는 <strong>슬래시(/)</strong>를 기준으로 <strong>계층적으로 표현</strong>되고, 최상위 경로 또한 슬래시로 표현된다.
          </li>
        </ul>
      </li>
      <li>
        ?name=ferret &rarr; query
        <ul>
          <li>
            path까지만을 활용해서 자원의 위치를 식별할 수도 있지만, 더 많은 정보가 필요할 때도 있다. 이때 <strong>쿼리 문자열(query string)</strong>을 사용한다. 쿼리 문자열은 <strong>쿼리 파라미터(query parameter)</strong>라고도 부른다.
          </li>
          <li>
            쿼리 문자열은 <strong>물음표(?)</strong>로 시작되는 <strong>&lt;키=값&gt;</strong> 형태의 데이터이며 <strong>앰퍼센트(&)</strong>를 사용해 여러 쿼리 문자열을 연결할 수도 있다.
          </li>
        </ul>
      </li>
      <li>
        #nose &rarr; fragment
        <ul>
          <li>
            <strong>자원의 한 조각</strong>을 가리키기 위한 정보이다. 흔히 HTML 파일과 같은 자원에서 특정 부분을 가리키기 위해 사용한다.
          </li>
        </ul>
      </li>
    </ul>
  </li>
</ul>

<h3>1-3-2. URN</h3>
<ul>
  <li>
    자원의 위치가 변하면 기존 URL로는 자원을 식별할 수가 없다. 그러나 <strong>URN</strong>은 <strong>고유한 이름</strong>을 붙이는 이름 기반 식별자로 <strong>자원의 위치와 무관하게 자원을 식별</strong>할 수 있다는 장점이 있다.
  </li>
  <li>
    다만 URL만큼 널리 사용되는 방식은 아니다.
  </li>
</ul>

<h4>DNS 레코드 타입</h4>
<ul>
  <li>
    네임 서버는 <strong>DNS 자원 레코드(DNS resource record)</strong>라 불리는 정보를 저장하고 관리한다.
  </li>
  <li>
    이러한 레코드는 도메인 네임을 구입한 뒤, 웹 사이트에 도메인 네임을 적용시킬 때 자주 접하게 된다. 예를 들어 IP 주소 1.2.3.4인 호스트를 접속 가능한 웹 서비스로 만든 경우 도메인 네임에 IP 주소를 매핑한다.
    <ul>
      <li>
        도메인 레코드를 추가하여 네임 서버에 IP가 도메인 네임에 매핑되었음을 알린다.
      </li>
    </ul>
  </li>
  <li>
    각 레코드에는 <strong>레코드 유형</strong>이 정해져 있기 때문에 레코드의 유형이 달라지면 레코드의 이름과 값의 의미가 달라진다.
  </li>
</ul>

<br><br>

<h1>2. HTTP</h1>
<ul>
  <li>
    HTTP에는 다음과 같은 중요한 네 가지 특성이 있다.
    <ul>
      <li>
        HTTP는 요청과 응답을 기반으로 동작한다.
      </li>
      <li>
        미디어 독립적이다.
      </li>
      <li>
        상태를 유지하지 않는다.
      </li>
      <li>
        지속 연결을 지원한다.
      </li>
    </ul>
  </li>
</ul>

<br>

<h2>2-1. HTTP의 특성</h2>
<ul>
  <li>
    HTTP(Hypertext Transfer Protocol)는 응용 계층에서 정보를 주고받는 데 사용되는 프로토콜이다.
  </li>
</ul>

<h3>2-1-1. 요청-응답 기반 프로토콜</h3>
<ul>
  <li>
    HTTP는 클라이언트와 서버가 서로 <strong>HTTP 요청 메시지</strong>와 <strong>HTTP 응답 메시지</strong>를 주고받는 구조로 동작한다.
    <ul>
      <li>
        HTTP 요청 메시지와 HTTP 응답 메시지는 <strong>메시지 형태</strong>가 다르다.
      </li>
    </ul>
  </li>
  <li>
    개발자 도구에서 <strong>[Network] 탭</strong>을 보면 해당 웹 사이트에서 주고받는 자원들을 확인할 수 있다.
    <ul>
      <li>
        여기서 임의의 자원을 클릭하면 <strong>HTTP 요청 메시지 헤더(Request Headers)</strong>와 <strong>HTTP 응답 메시지 헤더(Response Headers)</strong>를 볼 수 있다.
      </li>
    </ul>
  </li>
</ul>

<h3>2-1-2. 미디어 독립적 프로토콜</h3>
<ul>
  <li>
    HTTP는 주고받을 <strong>자원의 특성과 무관</strong>하게 그저 자원을 <strong>주고받을 수단(인터페이스)</strong>의 역할만을 수행한다.
    <ul>
      <li>
        실제로 HTTP를 통해 HTML, JPEG, PNG, JSON, XML, PDF 등 다양한 종류의 자원을 주고받을 수 있다.
      </li>
    </ul>
  </li>
  <li>
    HTTP에서 메시지로 주고받는 자원의 종류를 <strong>미디어 타입(media tpye)</strong>이라 부른다. 혹은 <strong>MIME 타입(Multipurpose Internet Mail Extensions Type)</strong>이라고도 부른다.
    <ul>
      <li>
        HTTP는 주고받을 미디어 타입에 특별히 제한을 두지 않는다.
      </li>
      <li>
        미디어 타입이란 일종의 웹 세상의 확장자와 같은 개념이다.
      </li>
      <li>
        HTTP를 통해 송수신하는 정보의 종류는 text/html(HTML), text/plain(일반 텍스트), image/png(PNG) 등으로 나타낼 수 있다. 
      </li>
    </ul>
  </li>
  <li>
    미디어 타입은 기본적으로 슬래시를 기준으로 하는 <strong>타입/서브타입(type/subtype)</strong> 형식으로 구성된다.
    <ul>
      <li>
        <strong>타입(type)</strong>은 <strong>데이터의 유형</strong>을 나타내고, <strong>서브타입(subtype)</strong>은 주어진 타입에 대한 <strong>세부 유형</strong>을 나타낸다. (type/subtype 형식).
      </li>
      <li>
        타입 목록에 대해서는 p276 참고.
      </li>
    </ul>
  </li>
  <li>
    미디어 타입에는 부가적인 설명을 위해 선택적으로 <strong>매개변수</strong>가 포함될 수 있다.
    <ul>
      <li>
        매개변수는 <strong>'타입/서브타입;매개변수=값'</strong> 형식으로 표현된다.
      </li>
    </ul>
  </li>
</ul>

<h3>2-1-3. 스테이트리스 프로토콜</h3>
<ul>
  <li>
    HTTP는 상태를 유지하지 않는 <strong>스테이트리스(stateless)</strong> 프로토콜로 통신을 하는데 있어 <strong>상태를 기억하지 않는다</strong>.
    <ul>
      <li>
        상태를 기억하지 않기 때문에 같은 요청을 여러 번 받을 때에는 불리하다.
      </li>
      <li>
        하지만 많은 클라이언트의 요청을 받을 때 모든 클라이언트의 상태를 저장하는 것이 더 부담이 되기때문에 장점으로 작용하는 경우가 많다.
      </li>
      <li>
        또한 두 개 이상의 여러 개의 서버로 구축될 수 있고 이 경우에도 상태를 기억한다면 여러 서버를 운용하기 어려워진다. (클라이언트가 특정 서버에 종속될 수 있음).
        <ul>
          <li>
            만약 한 서버에 문제가 발생하면 HTTP 통신 내역을 잃어버릴 수도 있다.
          </li>
        </ul>
      </li>
    </ul>
  </li>
  <li>
    HTTP가 처음 만들어졌을 때부터 오늘날까지 이어지는 중요한 설계 목표는 <strong>확장성(scalability)</strong>과 <strong>견고성(robustness)</strong>이며 stateless 설계는 이를 잘 보장한다.
  </li>
  <li>
    물론 HTTP의 stateless 특성을 보완하기 위한 여러 방법들도 존재한다.
  </li>
</ul>

<h3>2-1-4. 지속 연결 프로토콜</h3>
<ul>
  <li>
    HTTP는 지속적으로 발전 중인 프로토콜로 여러 버전이 존재한다.
    <ul>
      <li>
        HTTP는 TCP 상에서 동작한다. HTTP는 비연결형 프로토콜이지만 TCP는 연결형 프로토콜이므로 초기 HTTP 버전(1.0 이하)은 쓰리 웨이 핸드셰이크로 TCP 연결을 수립한 후, 요청에 대한 응답을 받으면 종료하는 식으로 동작했다.
      </li>
      <li>
        최근 HTTP 3.0은 UDP상에 동작한다.
      </li>
    </ul>
  </li>
  <li>
    최근 대중적으로 사용되는 HTTP 1.1 이상의 버전에서는 <strong>지속 연결(persistent connection)</strong>이라는 기술을 제공한다. 다른 표현으로 <strong>킵 얼라이브(keep-alive)</strong>라고도 부른다.
    <ul>
      <li>
        이는 하나의 TCP 연결상에서 여러 개의 요청-응답을 주고받을 수 있는 기술이다.
      </li>
      <li>
        해당 기술을 지원하지 않는 경우 HTTP는 매번 새롭게 연결을 수립하고 종료해야 하는 비지속 연결 방식을 이용해야 한다.
      </li>
    </ul>
  </li>
</ul>

<br>

<h2>2-2. HTTP 메시지 구조</h2>
<ul>
  <li>
    HTTP 1.1 버전의 메시지를 위주로 학습을 진행한다.
  </li>
  <li>
    HTTP 메시지는 <strong>시작 라인</strong>, <strong>필드 라인</strong>, <strong>메시지 본문</strong>으로 이루어져 있다.
    <ul>
      <li>
        필드 라인은 없거나 여러 개 있을 수 있다.
      </li>
      <li>
        필드 라인과 메시지 본문 사이에는 빈 줄 바꿈이 있다.
      </li>
    </ul>
  </li>
  <li>
    <strong>시작 라인(start-line)</strong>은 HTTP 요청 메시지일 경우 <strong>요청 라인</strong>, HTTP 응답 메시지일 경우 <strong>상태 라인</strong>이 된다.
    <ul>
      <li>
        요청 라인(request-line)의 형식은 다음과 같다.
        <ul>
          <li>
            <strong>메서드(method)</strong>는 클라이언트가 서버의 자원(요청 대상)에 대해
            <strong>수행할 작업의 종류</strong>를 의미한다.
            <ul>
              <li>
                GET, POST, PUT, DELETE 등이 있다.
              </li>
            </ul>
          </li>
          <li>
            <strong>요청 대상(request-target)</strong>은 HTTP 요청을 보낼 서버의
            <strong>자원</strong>을 의미하며 보통 (쿼리가 포함된) <strong>URI의 경
            (path)</strong>가 명시된다.
            <ul>
              <li>
                "http://www.example.com/hello?q=world"로 요청을 보낸 경우 요청 대상은
                "/hello?q=world"가 된다.
              </li>
              <li>
                하위 경로가 없더라도 요청 대상은 슬래시(/)로 표기해야 한다. 예를 들어
                "http://www.example.com"으로 요청을 하여도 요청 대상은 "/"가 된다.
              </li>
            </ul>
          </li>
          <li>
            HTTP 버전(HTTP-version)은 사용된 HTTP 버전을 의미하며 'HTTP/버전' 표기 방식을
            따른다.
          </li>
        </ul>
      </li>
      <li>
        시작 라인은 <strong>상태 라인(state-line)</strong>이 된다. 상태 라인은 HTTP 버전, 상태 코드, 이유 구문
        두 공백으로 구분된다.
        <ul>
          <li>
            상태 라인은 'HTTP 버전 (공백) 상태 코드 (공백) 이유 구문(선택적) (줄바꿈)'이다.
            <ul>
              <li>
                <strong>HTTP 버전</strong>: 사용된 HTTP의 버전을 나타낸다.
              </li>
              <li>
                <strong>상태 코드(state code)</strong>: 요청에 대한 결과를 나타내는 세 자리 정수이다.
                <ul>
                  <li>
                    클라이언트는 상태 코드를 통해 요청이 어떻게 처리되었는지 판단할 수 있다.
                  </li>
                </ul>
              </li>
              <li>
                <strong>이유 구문(reason phrase)</strong>: 상태 코드에 대한 문자열 형태의 설명이다.
              </li>
              <li>
                예를 들면 'HTTP/1.1 200 OK'와 같다.
              </li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
  </li>
  <li>
    HTTP의 <strong>필드 라인</strong>에는 <strong>0개 이상의 HTTP 헤더(HTTP header)</strong>가 명시된다. 따라서 이를 <strong>헤더 라인(header-line)</strong>이라고도 부른다.
  </li>
    <ul>
      <li>
        HTTP 헤더는 HTTP 통신에 필요한 <strong>부가 정보</strong>를 의미한다. 한 HTTP 메시지에 <strong>아주 다양한 HTTP 헤더</strong>들이 사용되는 것이 일반적이다.
      </li>
      <li>
        필드 라인에 명시되는 각 HTTP 헤더는 <strong>콜론(:)</strong>을 기준으로 <strong>헤더 이름(header-name)</strong>과 <strong>하나 이상의 헤더 값(header-value)</strong>으로 구성된다.
      </li>
    </ul>
  <li>
    HTTP 요청 혹은 응답 메시지에서 본문이 필요할 경우 <strong>메시지 본문(message-body)</strong>에 명시된다.
  </li>
    <ul>
      <li>
        존재하지 않을 수도 있으며 JSON 그리고 HTML과 같은 다양한 콘텐츠 타입이 사용될 수 있다.
      </li>
    </ul>
  <li>
    어떤 URL로 어떤 요청을 받았을 때 서버는 어떻게 응답할 것인가를 결정하며 이를 가장 잘 보여주는 문서가 API 문서이다.
  </li>
</ul>

```text
시작 라인 (줄바꿈)
필드 라인 (줄바꿈)
(줄 바꿈)
메시지 본문
```

```text
< HTTP 상태와 헤더 예 >
GET /example-page HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; rv:109.0) Gecko/20100101
Firefox/118.0
Accept: text/html
```

<h2>2-3. HTTP 메서드</h2>
<ul>
  <li>
    HTTP에서 자주 사용되는 메서드는 GET, HEAD, POST, PUT, PATCH, DELETE 이다. (자세한 것은 p284 참고).
  </li>
</ul>

<h3>2-3-1. GET - 가져다주세요</h3>
<ul>
  <li>
    <strong>GET 메서드</strong>는 <strong>특정 자원을 조회</strong>할 때 사용되는 메서드이다. 자원은 HTML, JSON, 이미지 파일, 일반 텍스트 등 다양한 것들이 될 수 있다.
  </li>
  <li>
    GET은 가장 흔히 사용되는 메서드 중 하나이며 웹 브라우저에서도 빈번하게 사용된다.
  </li>
  <li>
    요청을 위해 사용되는 것은 요청 라인의 <strong>'요청 대상'</strong>과 <strong>'Host 헤더'</strong> 이다.
  </li>
</ul>

```http
# 1. 요청 메시지===========
GET /example-page HTTP/1.1
Host: www.example.com
Accept: *

# 2. 응답 메시지===========
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

# HTML 문서를 응답받은 예제
<!DOCTYPE html>
<html>
<head>
  <title>Example Page</title>
</head>
<body>
  <h1>Hello, World</h1>
</body>
</html>

# 3. GET 메서드는 요청 메시지 본문보다 쿼리 문자열을 사용함.
GET /index.html?name1=value1&name2=value2 HTTP/1.1
HostL www.example.com
Accept: *
```

<h3>2-3-2. HEAD - 헤더만 가져다주세요</h3>
<ul>
  <li>
    HEAD 메서드는 사실상 GET 메서드와 동일한 역할을 한다. 유일한 차이점은 응답 메시지에 <strong>메시지 본문이 포함되지 않는다는 것</strong> 이다.
  </li>
    <ul>
      <li>
        즉 HEAD 메서드는 서버 요청에 대한 응답으로 <strong>응답 메시지의 헤더</strong>만을 반환한다.
      </li>
    </ul>
</ul>

```http
# 1. 요청 메시지==========
HEAD /example-page HTTP/1.1
Host: www.example.com
Accept: *

# 2. 응답 메시지==========
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234
```

<h3>2-3-3. POST - 처리해 주세요</h3>
<ul>
  <li>
    POST 메서드는 서버로 하여금 <strong>특정 작업을 처리</strong>하도록 요청하는 메서드이며 <strong>범용성이 매우 넓은 메서드</strong>이다.
  </li>
  <li>
    처리할 대상은 흔히 <strong>메시지 본문</strong>으로 명시된다.
  </li>
  <li>
    범용성이 넓기는 하지만 주로 클라이언트가 <strong>서버에 새로운 자원을 생성</strong>하고자 할 때 사용된다.
  </li>
  <li>
    성공적으로 POST 요청이 처리되어 새로운 자원이 생성되면 서버는 응답 메시지의 <strong>Location 헤더</strong>를 통해 새로 생성된 자원의 위치를 클라이언트에게 알려줄 수 있다.
  </li>
</ul>

```http
# 1. 응답 메시지============
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: 100
Date: Mon, 14 Oct 2024 16:35:00 PST
Location: /posting/1

{
    "id": 1,
    "Title": "오늘도 즐거운 날입니다."
    "Contents": "재미있는 글 보고 가세요~"
}
```

<h3>2-3-4. PUT - 덮어써 주세요</h3>
<ul>
  <li>
    PUT 메서드는 <strong>덮어쓰기</strong>를 요청하는 메서드이다.
  </li>
    <ul>
      <li>
        요청 자원이 없다면 메시지 본문으로 <strong>자원을 새롭게 생성</strong>한다.
      </li>
      <li>
        이미 자원이 존재한다면 메시지 본문으로 <strong>자원을 완전히 대체</strong>한다.
      </li>
    </ul>
</ul>

<h3>2-3-5. PATCH - 일부 수정해 주세요</h3>
<ul>
  <li>
    PUT 메서드가 완전한 대체에 가깝다면 PATCH 메서드는 <strong>부분적 수정</strong>에 가깝다.
  </li>
    <ul>
      <li>
        예를 들어 Title과 Contents가 있는데 Title만 보내는 경우 PUT은 Contents 자체가 없어지지만, PATCH는 Contents는 유지한 채로 Title만 수정된다.
      </li>
    </ul>
</ul>

<h3>2-3-6. DELETE - 삭제해 주세요</h3>
<ul>
  <li>
    DELETE 메서드는 <strong>특정 자원을 삭제</strong>하고 싶을 때 사용하는 메서드이다.
  </li>
</ul>

```http
# 1. 요청 메시지============
DELETE /texts/a.txt HTTP/1.1
Host: example.com
```

<br>

<h2>2-4. HTTP 상태 코드</h2>
<ul>
  <li>
    상태 코드는 <strong>요청에 대한 결과</strong>를 나타내는 세 자리 정수이며 200, 201, 304, 404, 505 등 다양한 종류가 존재한다.
  </li>
  <li>
    상태 코드의 종류는 <strong>백의 자리 수</strong>를 기준으로 유형을 구분할 수 있다.
  </li>
    <ul>
      <li>
        100번대: 정보성 상태 코드
      </li>
      <li>
        200번대: 성공 상태 코드
      </li>
      <li>
        300번대: 리다이렉션 상태 코드
      </li>
      <li>
        400번대: 클라이언트 에러 상태 코드
      </li>
      <li>
        500번대: 서버 에러 상태 코드
      </li>
    </ul>
</ul>

<h3>2-4-1. 200번대: 성공 상태 코드</h3>
<ul>
  <li>
    200번대 상태 코드는 <strong>요청이 성공</strong>했음을 의미한다. 주로 사용되는 상태 코드는 200(OK), 201(Created), 202(Accepted), 204(No Content)이다.
  </li>
    <ul>
      <li>
        200(OK): 요청이 성공함.
      </li>
      <li>
        201(Created): 요청 성공, 자원이 생성됨.
      </li>
      <li>
        202(Accepted): 요청 성공, 아직 요청한 작업을 끝내지 못함.
      </li>
      <li>
        204(No Content): 요청 성공, 메시지 본문으로 표시할 데이터가 없음.
      </li>
    </ul>
</ul>

<h3>2-4-2. 300번대: 리다이렉션 상태 코드</h3>
<ul>
  <li>
    300번대 상태 코드는 <strong>리다이렉션(redirection)</strong>과 관련된 상태 코드이다.
  </li>
  <li>
    리다이렉션이란 클라이언트가 요청한 <strong>자원이 다른 곳</strong>에 있을 때, 클라이언트의 요청을 <strong>다른 곳으로 이동</strong>시키는 것을 의미한다.
  </li>
    <ul>
      <li>
        클라이언트가 요청한 자원이 다른 URL에 있는 경우 서버는 응답 메시지의 <strong>Location 헤더</strong>를 통해 <strong>요청한 자원이 위치한 URL</strong>을 안내할 수 있다. 이후 해당 위치로 즉시 재요청을 보내 URL에 대한 응답을 받게 된다.
      </li>
    </ul>
  <li>
    리다이렉션의 유형으로는 크게 <strong>영구적인 리다이렉션</strong>과 <strong>일시적인 리다이렉션</strong>이 있다.
  </li>
    <ul>
      <li>
        <strong>영구적인 리다이렉션(permanent redirection)</strong>은 자원이 <strong>완전히 새로운 곳</strong>으로 이동하여 경로가 <strong>영구적으로 재지정</strong>되는 것을 의미한다.
      </li>
        <ul>
          <li>
            이 경우 기존의 URL에 요청 메시지를 보내면 항상 새로운 URL로 리다이렉트 된다.
          </li>
          <li>
            서버가 도메인을 이전하는 등 웹 사이트의 큰 개편이 있을 때 이런 영구적인 리다이렉션을 접할 수 있다.
          </li>
          <li>
            대표적인 상태 코드로 <strong>301(Moved Permanently)</strong>과 <strong>308(Permanent Redirect)</strong>이 있다.
          </li>
            <ul>
              <li>
                301은 클라이언트가 보내는 두 번째 요청의 메서드가 첫 번째 메서드와 달리 바뀔 수 있다는 애매한 점이 있다.
              </li>
              <li>
                308은 301의 애매한 점을 보완하여 두 번째 메서드가 첫 번째 메서드와 달리 바뀔 수 없다.
              </li>
            </ul>
        </ul>
      <li>
        <strong>일시적인 리다이렉션(temporary redirection)</strong>은 자원의 위치가 <strong>임시로 변경</strong>되었거나 <strong>임시로 사용할 URL이 필요</strong>한 경우 주로 사용된다.
      </li>
        <ul>
          <li>
            이번에 이동한 주소가 <strong>다음번에도 올바른 목적지라는 보장</strong>이 없기 때문에 원래 URL 주소를 기억하고 있어야 한다.
          </li>
          <li>
            일시적인 리다이렉션과 관련한 상태 코드는 302(Found), 303(See Other), 307(Temporary Redirect)이 있다.
          </li>
            <ul>
              <li>
                <strong>302(Found)</strong>는 요청한 자원이 <strong>임시로 다른 곳으로 이동</strong>했음을 나타낸다. 이때 두 번째 요청의 메서드가 바뀔 수 있다.
              </li>
              <li>
                <strong>307(Temporary Redirect)</strong>는 302의 애매함을 보완하여 <strong>두 번째 메서드가 바뀌지 않는다</strong>.
              </li>
              <li>
                <strong>303(See Other)</strong>은 두 번째 메서드가 바뀌기는 하지만 이동할 주소를 <strong>GET</strong> 또는 <strong>HEAD</strong>로만 조회하도록 한다.
              </li>
            </ul>
        </ul>
    </ul>
  <li>
    리다이렉션은 클라이언트가 요청한 자원이 다른 곳에 있을 때 요청을 다른 곳으로 이동시킨다. 이때 다른 곳이란 <strong>URL</strong>이 될 수도 있고 혹은 <strong>캐시</strong>가 될 수도 있다.
  </li>
</ul>

<h3>2-4-3. 400번대: 클라이언트 에러 상태 코드</h3>
<ul>
  <li>
    400번대 상태 코드는 <strong>클라이언트에 의한 에러</strong>가 있음을 알려주는 상태 코드이다.
  </li>
    <ul>
      <li>
        서버가 처리할 수 없는 형태로 요청이 오는 경우.
      </li>
      <li>
        존재하지 않는 자원에 대해 요청을 보내는 경우.
      </li>
    </ul>
  <li>
    <strong>400(Bad Request)</strong>은 <strong>클라이언트의 요청이 잘못</strong>되었음을 아렬 주는 상태 코드이다.
  </li>
  <li>
    <strong>401(Unauthorized)</strong> 상태 코드는 특정 자원에 접근하기 위한 <strong>인증</strong>이 필요할 때의 상태 코드이다.
  </li>
    <ul>
      <li>
        서버 상태 코드 401(Unauthorized)는 반드시 <strong>WWW-Authenticate라는 헤더</strong>를 통해 인증 방법을 알려 주어야 한다.
      </li>
      <li>
        만약 클라이언트의 <strong>권한이 충분하지 않다면</strong> 상태 코드 <strong>403(Forbidden)을 응답</strong>한다. 즉 자원에 접근할 권한이 없음을 의미한다.
      </li>
    </ul>
  <li>
    401(Unauthorized)는 인증(Authentication)으로 <strong>자신이 누구인지를 증명</strong>하는 것을 의미한다.
  </li>
    <ul>
      <li>
        주의할 점은 403(Forbidden)은 <strong>권한 부여(Authorization)</strong>으로 인증된 주체에게 <strong>작업을 허용하는 것</strong>을 의미하며 <strong>인가</strong>라고도 부른다.
      </li>
    </ul>
  <li>
    <strong>404(Not Found)</strong>는 접근하고자 하는 자원이 <strong>존재하지 않음</strong>을 알리는 상태 코드이다. 혹은 자원이 존재하더라도 <strong>공개하지 않는 자원</strong>에 대해 404(Not Found)를 응답하는 경우도 있다.
  </li>
  <li>
    어떤 URI(URL)에 어떤 메서드로 요청 받았을 때 서버가 어떻게 행동(응답)해야 하는지 설계하는 것은 개발자의 몫이며 이때 구현되지 않은 메서드로 요청을 보낸다면 <strong>상태 코드 405(Method Not Allowed)</strong>를 통해 <strong>메서드의 미지원</strong>을 알릴 수 있다.
  </li>
</ul>

<h3>2-4-4. 500번대: 서버 에러 상태 코드</h3>
<ul>
  <li>
    500번대 상태 코드의 원인은 <strong>서버</strong>이다. 즉 클라이언트가 올바르게 요청을 보냈을지라도 발생할 수 있는 서버 에러에 대한 상태 코드이다.
  </li>
  <li>
    <strong>500(Internal Server Error)</strong>은 <strong>서버의 예기치 못한 상황</strong>으로 인해 요청을 처리할 수 없음을 의미한다.
  </li>
    <ul>
      <li>
        다소 포괄적인 표현이며 서버 내 에너를 통칭하기도 한다.
      </li>
    </ul>
  <li>
    <strong>502(Bad Gateway)</strong>는 클라이언트와 서버 사이에 위치한 <strong>중간 서버의 통신 오류</strong>를 나타내는 상태 코드이다.
  </li>
  <li>
    <strong>503(Service Unabailable)</strong>은 현재 <strong>서비스를 일시적으로 이용할 수 없음</strong>을 의미한다.
  </li>
</ul>

<h4>HTTP의 발전: HTTP/0.9에서 HTTP/3.0 까지</h4>
<ul>
  <li>
    HTTP/0.9
  </li>
    <ul>
      <li>
        지금은 거의 사용하지 않는 <strong>초창기 HTTP 버전</strong>이다.
      </li>
      <li>
        사용가능한 메서드는 <strong>GET</strong> 하나였으며 요청 메시지는 한 줄로 구성되어 있었다.
      </li>
    </ul>
  <li>
    HTTP/1.0
  </li>
    <ul>
      <li>
        HTTP/1.0부터는 <strong>HEAD</strong>와 <strong>POST</strong> 같은 GET 이외의 메서드가 도입되었다.
      </li>
      <li>
        <strong>헤더</strong>가 지원되기 시작하여 더 다양한 정보블 주고받을 수 있게 되었다.
      </li>
      <li>
        여전히 <strong>지속 연결(persistent connection)</strong>을 지원하지 않아 HTTP 메시지를 주고받을 때 <strong>연결 수립과 종료를 반복</strong>하였다.
      </li>
    </ul>
  <li>
    HTTP/1.1
  </li>
    <ul>
      <li>
        HTTP/1.1부터 <strong>지속 연결</strong>이 공식적으로 지원되었다.
      </li>
      <li>
        특정 요청에 대한 응답이 수신되기 전에 다음 요청을 보낼 수 있는 파이프라이닝 기능과 협상 기능 등 다양한 기능 및 사용 가능한 헤더가 추가되어 <strong>오늘날까지 널리 사용되는 버전</strong>이다.
      </li>
    </ul>
  <li>
    HTTP/2.0
  </li>
    <ul>
      <li>
        HTTP/2.0은 HTTP/1.1의 효율과 성능을 높이기 위한 버전이다.
      </li>
      <li>
        송서신 효율을 높이기 위해 <strong>헤더를 압축</strong>하여 전송한다.
      </li>
      <li>
        이전 버전에는 텍스트 기반의 메시지를 송수신하였지만 HTTP/2.0부터는 <strong>바이너리 데이터 기반</strong>의 메시지를 송수신한다.
      </li>
      <li>
        클라이언트가 요청하지 않았더라도 미래에 필요할 것으로 예상되는 자원을 미리 전송해 주는 <strong>서버 푸시(server push)</strong> 기능을 제공한다.
      </li>
      <li>
        HTTP/1.1까지 고질적인 문제였던 HOL 블로킹(Head-Of-Line blocking) 문제를 완화한 버전이다.
      </li>
        <ul>
          <li>
            HOL 블로킹이란 같은 큐에 대기하여 순차적으로 처리되는 여러 패킷이 있을 때, 첫 번째 패킷의 처리 지연으로 인해 <strong>나머지 패킷들의 처리도 모두 지연</strong>되는 문제를 의미한다.
          </li>
          <li>
            HTTP/2.0은 이 문제에 있어 <strong>멀티플렉싱(multiplexing) 기법</strong>을 도입해 완화하였다. 이는 요청과 응답을 주고받는 단위는 하나의 <strong>스트림</strong>에서 이루어지고 이런 스트림을 <strong>동시에 독립적으로 송수신 가능</strong>하며 일정한 순서를 유지할 필요가 없는 방법이다.
          </li>
        </ul>
    </ul>
  <li>
    HTTP/3.0
  </li>
    <ul>
      <li>
        지금까지 언급한 HTTP 버전들은 모두 TCP를 기반으로 동작하지만 <strong>HTTP/3.0</strong>은 <strong>UDP</strong>를 기반으로 동작한다.
      </li>
        <ul>
          <li>
            정확히는 UDP를 기반으로 구현된 <strong>QUIC(Quick UDP Internet Connections) 프로토콜</strong>이다.
          </li>
        </ul>
      <li>
        속도 측면에서 TCP에 비해 빠르다는 장점이 있으며 현재 빠르게 성장하고 있다.
      </li>
    </ul>
</ul>

<br><br>

<h1>3. HTTP 헤더와 HTTP 기반 기술</h1>
<ul>
  <li>
    이번 절에서는 필드 라인에 대해 학습한다.
  </li>
    <ul>
      <li>
        필드 라인에는 다양한 HTTP 헤더들이 명시된다.
      </li>
    </ul>
</ul>

<br>

<h2>3-1. HTTP 헤더</h2>
<ul>
  <li>
    HTTP 헤더의 종류는 매우 많기 때문에 도서에서는 <strong>HTTP 요청</strong> 시 주로 사용되는 헤더, <strong>HTTP 응답</strong> 시 주로 사용되는 해더, <strong>HTTP 요청과 응답 모두</strong>에서 자주 활용되는 헤더순으로 설명한다.
  </li>
</ul>

<h3>3-1-1. 요청 시 활용되는 HTTP 헤더</h3>
<ul>
  <li>
    HTTP 요청 시 주로 활용되는 헤더는 'Host', 'User-Agent', 'Referer', 'Authorization' 헤더가 있다.
  </li>
  <li>
    <strong>Host</strong>는 요청을 보내는 <strong>호스트</strong>를 나타내는 헤더이다.
  </li>
    <ul>
      <li>
        호스트는 주로 <strong>도메인 네임</strong>으로 명시되며 <strong>포트 번호</strong>가 포함될 수 있다.
      </li>
    </ul>
  <li>
    <strong>User-Agent</strong>는 웹 브라우저와 같이 <strong>HTTP 요청을 시작</strong>하는 클라이언트 측의 프로그램을 의미한다.
  </li>
    <ul>
      <li>
        <strong>User-Agent 헤더</strong>에는 <strong>요청 메시지 생성</strong>에 관여한 <strong>클라이언트 프로그램</strong>과 관련된 다양한 정보가 명시된다.
      </li>
      <li>
        예를 들어 운영체제, 브라우저 종류 및 버전, 렌더링 엔진과 같은 정보가 해당한다.
      </li>
    </ul>
  <li>
    <strong>Referer 헤더</strong>에는 클라이언트가 요청을 보낼 때 <strong>머무르고 잇던 URL</strong>을 명시한다.
  </li>
    <ul>
      <li>
        Referer를 통해 클라이언트의 <strong>유입 경로</strong>를 파악해 볼 수 있다.
      </li>
    </ul>
  <li>
    <strong>Authorization 헤더</strong>는 클라이언트의 <strong>인증 정보</strong>를 담는 헤더이다.
  </li>
    <ul>
      <li>
        <strong>인증 타입(type)</strong>과 인증을 위한 <strong>정보(credentials)</strong>가 차례로 명시된다.
      </li>
      <li>
        가장 기본적은 HTTP 인증 타입은 Basic으로 <strong>username:password 구조</strong>를 사용한다. 이 값은 <strong>Base64 인코딩</strong>을 하여 인증 정보(credential)로 삼는다.
      </li>
    </ul>
</ul>

```text
# 1. Host 예시
GET /hypertext/WWW/TheProject.html HTTP/1.1
Host: info.cern.ch
...

# 2. User-Agent 예시
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.9) Gecko/20100101 Firefox/109.9

# 3. Referer 예시
Referer: https://en.wikipedia.org/

# 4. Authorization 헤더 예시
Authorization: <type> <credentials>
```

<h3>3-1-2. 응답 시 활용되는 HTTP 헤더</h3>
<ul>
  <li>
    HTTP 응답 시 주로 활용되는 헤더는 'Server', 'Allow', 'Retry-After', 'Location', 'WWW-Authenticate' 헤더이다.
  </li>
  <li>
    <strong>Server 헤더</strong>는 요청을 처리하는 <strong>서버 측</strong>의 소프트웨어와 관련된 정보를 명시한다.
  </li>
  <li>
    <strong>Allow 헤더</strong>는 클라이언트에게 <strong>허용된 HTTP 메서드 목록</strong>을 알려 주기 위해 사용된다.
  </li>
    <ul>
      <li>
        상태 코드 <strong>405(Method Not Allowed)</strong>는 요청한 메서드를 지원하지 않음을 의미하며 Allow 헤더가 함께 사용된다.
      </li>
    </ul>
  <li>
    <strong>Retry-After</strong>는 자원을 사용할 수 있는 <strong>날짜</strong> 혹은 <strong>시각</strong>을 나타낸다.
  </li>
  <li>
    <strong>Location 헤더</strong>는 클라이언트에게 <strong>자원의 위치</strong>를 알려 주기 위해 사용되는 헤더로 주로 <strong>리다이렉션</strong>이 발생했을 때나 <strong>새로운 자원이 생성</strong>되었을 때 사용된다.
  </li>
    <ul>
      <li>
        상태 코드 503(Service Unavailable)은 현재는 요청을 처리할 수 없으나 추후 가능할 수도 있다는 상태 메시지로 함께 사용된다.
      </li>
    </ul>
  <li>
    <strong>WWW-Authenticate</strong>는 요청한 자원에 대한 유효한 인증이 없을 때 응답하는 코드인 <strong>401(Unauthorized)</strong>과 함께 사용된다.
  </li>
    <ul>
      <li>
        WWW-Authenticate 헤더는 자원에 접근하기 위한 <strong>인증 방식</strong>을 설명하는 헤더이다.
      </li>
      <li>
        실제로는 <strong>보안 영역(realm)</strong>이나 인증에 사용될 <strong>문자집합(charset)</strong> 등도 함께 알려줄 수 있다.
      </li>
      <li>
        Authorization과 WWW-Authenticate 헤더를 통해 인증되지 않은 클라이언트가 HTTP 인증(Basic 인증)을 수행하는 과정을 p313 에서 참고.
      </li>
    </ul>
</ul>

```text
# 1. Server 헤더 예시
Server: Apache/2.4.1 (Unix)

# 2. Allow 헤더 예시
Allow: POST, OPTIONS

# 3. Retry-After 헤더 예시
Retry-After: Fri, 23 Aug 2024 09:00:00 GMT
Retry-After: 120
```

<h4>영역(region)이란?</h4>
<ul>
  <li>
    WWW-Authenticate 헤더에서 realm은 보안이 적용될 영역을 의미한다.
  </li>
  <li>
    영역이 달라지면 요구되는 권한도 달라질 수 있다.
  </li>
</ul>

<h3>3-1-3. 요청과 응답 모두에서 활용되는 HTTP 헤더</h3>
<ul>
  <li>
    <strong>Date</strong>는 메시지가 <strong>생성된 날짜</strong>와 <strong>시각</strong>에 관련된 정보를 담은 헤더이다.
  </li>
  <li>
    <strong>Connection 헤더</strong>는 클라이언트의 요청과 응답 간의 <strong>연결 방식</strong>을 설정하는 헤더이다.
  </li>
    <ul>
      <li>
        HTTP의 <strong>지속 연결 프로토콜</strong>이 Connection에 명시되는 대표적인 연결 방식이다.
      </li>
      <li>
        <strong>Connection: keep-alive 헤더</strong>를 통해 상대방에게 <strong>지속 연결을 희망</strong>함을 알릴 수 있다.
      </li>
      <li>
        반대로 <strong>Connection: close</strong>를 통해 연결 종료를 희망함을 알릴 수 있다.
      </li>
    </ul>
  <li>
    <strong>Content-Length 헤더</strong>는 본문의 바이트 단위 크기(길이)를 나타낸다.
  </li>
  <li>
    Content-Type, Content-Language, Content-Encoding과 같은 헤더들은 전송하려는 메시지 본문의 <strong>표현 방식</strong>을 설명하는 헤더이다.
  </li>
    <ul>
      <li>
        이 헤더들은 표현 헤더(representation header)의 일종이라고도 부른다.
      </li>
      <li>
        <strong>Content-Type 헤더</strong>는 메시지 본문에 사용된 미티어 타입을 나타낸다.
      </li>
      <li>
        <strong>Content-Language 헤더</strong>는 메시지 본문에 사용된 자연어를 명시한다.
      </li>
        <ul>
          <li>
            첫 번째 서브 태그는 언어 코드로 <strong>특정 언어</strong>를 의미하는 언어 코드가 명시된다.
          </li>
          <li>
            두 번째 서브 태그는 국가 코드로 <strong>특정 국가</strong>를 의미하는 국가 코드가 명시된다.
          </li>
          <li>
            예를 들어 ko-KR은 한국에서 사용하는 한국어를 의미한다.
          </li>
        </ul>
      <li>
        <strong>Content-Encoding 헤더</strong>는 메시지 본문을 압축하거나 변환한 방식이 명시된다.
      </li>
        <ul>
          <li>
            HTTP를 통해 송수신되는 데이터는 전송 속도 개선을 위해 종종 압축이나 변환이 되며 이를 위해 존재하는 헤더이다.
          </li>
        </ul>
    </ul>
</ul>

```text
# 1. Date 헤더 예시.
Date: Tue, 15 Nov 1994 08:12:31 GMT

# 2. Connection 헤더 예시
Connection: keep-alive
Connection: close

# 3. Content-Encoding 헤더 예시
Content-Encoding: gzip
Content-Encoding: compress
Content-Encoding: deflate
Content-Encoding: br

# 여러 인코딩이 사용된 경우 적용된 순서대로 명시한다.
Content-Encoding: deflate, gzip
```

<br>

<h2>3-2. 캐시</h2>
<ul>
  <li>
    클라이언트가 같은 자원을 요청하는 요청을 지속적으로 보내는 경우 <strong>HTTP 캐시</strong>를 활용해 응답받은 내용을 사본으로 임시로 저장하여 활용한다.
  </li>
    <ul>
      <li>
        캐시(cache)란 불필요한 대역폭 낭비와 응답 지연을 방지하기 위해 정보의 사본을 임시로 저장하는 기술이다.
      </li>
      <li>
        정보의 사본을 임시로 저장하는 것 자체를 캐시(cache)한다 혹은 캐싱(caching)한다라고도 표현한다.
      </li>
      <li>
        캐시를 활용하면 불필요한 대역폭 낭비를 줄일 수 있고, 더 빠르게 데이터에 접근할 수 있다.
      </li>
    </ul>
  <li>
    <strong>웹 브라우저</strong>에 저장되는 캐시를 개인 <strong>전용 캐시(private cache)</strong>, 클라이언트와 서버 사이에 위치한 <strong>중앙 서버</strong>에 저장되는 캐시를 <strong>공용 캐시(public cache)</strong>라고 한다.
  </li>
  <li>
    캐시에 저장된 사본 데이터가 최신 원본 데이터의 최신 상태를 유지하고 있는지를 <strong>캐시 신선도(cache freshness)</strong>라 표현한다.
  </li>
    <ul>
      <li>
        캐시 신선도를 유지하는 가장 기본적인 방법은 캐시된 데이터에 <strong>유효 기간</strong>을 설정하는 방법이다.
      </li>
      <li>
        유효 기간을 부여하는 방법으로는 <strong>응답 메시지의 Expires 헤더(날짜)</strong>와 <strong>Cache-Control 헤더의 Max-Age 값(초)</strong>을 이용할 수 있다.
      </li>
    </ul>
  <li>
    캐시의 <strong>유효 기간이 만료</strong>된 경우 클라이언트는 캐시된 자원이 <strong>여전히 최신 상태의 정보인지 재검사</strong>를 진행한다.
  </li>
    <ul>
      <li>
        <strong>날짜</strong>를 기반으로 재검사하는 방식은 클라이언트가 <strong>If-Modified-Since 헤더</strong>를 통해 서버에게 특정 시점 이후로 원본 데이터가 원경 되었는지 묻는 방법이다. 명시된 시점 이후로 원본에 변경이 있다면 새 자원으로 응답하도록 서버에 요청한다.
      </li>
      <li>
        서버 입장에서 If-Modified-Since 헤더가 포함된 요청 메시지를 수신한 경우 서버의 <strong>자원 상태</strong>는 크게 다음 세 가지이다.
      </li>
        <ul>
          <li>
            요청받은 자원이 변경되었다면 <strong>상태 코드 200(OK)</strong>과 함께 <strong>새로운 자원</strong>을 반환한다.
          </li>
          <li>
            요청받은 자원이 변경되지 않았다면 서버는 메시지 없는 <strong>상태 코드 304(Not Modified)</strong>를 통해 클라이언트에게 자원이 변경되지 않았음을 알림.
          </li>
            <ul>
              <li>
                즉 캐시된 자원이 있으니 캐시된 자원을 사용하라는 것을 의미한다.
              </li>
            </ul>
          <li>
            요청받은 자원이 삭제되었다면 <strong>상태 코드 404(Not Found)</strong>를 통해 요청한 자원이 존재하지 않음을 알린다.
          </li>
        </ul>
      <li>
       서버는 상태 코드 304(Not Modified)를 통한 자원의 변경 여부뿐만 아니라 <strong>Last-Modified 헤더</strong>를 통해 <strong>자원의 마지막 시점</strong>도 클라이언트에 알려 줄 수 있다.
      </li>
      <li>
        <strong>엔티티 태그(Entity Tag, Etag)</strong>를 사용하는 방법은 자원의 <strong>버전(version)</strong>을 식별하기 위한 정보이다.
      </li>
        <ul>
          <li>
            Etag와 일치하는 자원이 있는지 확인할 때에는 <strong>If-None-Match</strong>를 이용한다.
          </li>
        </ul>
      <li>
        Etag를 이용하는 경우에도 서버의 자원은 하래 셋 중 하나의 상황을 따른다.
      </li>
        <ul>
          <li>
            요청한 자원이 <strong>변경된 경우</strong> Etag 값도 변경된 것이기에 <strong>상태 코드 200(OK)</strong>과 함께 변경된 데이터와 Etag 값을 응답한다.
          </li>
          <li>
            요청한 <strong>자원이 변경되지 않은 경우</strong> Etag도 변경되지 않은 것이기에 <strong>304(Not Modified)</strong>를 응답한다.
          </li>
          <li>
            요청한 자원이 <strong>삭제</strong>된 경우 <strong>상태 코드 404(Not Found)</strong>를 응답한다.
          </li>
        </ul>
    </ul>
</ul>

```http
# 1. Expires 헤더를 통한 유효 기간 설정.
HTTP/1.1 200 OK
Date: Mon, 05 Feb 2024 12:00:00 GMT
Content-type: text/plain
Content-length: 100
# 유효 기간
Expires: Tue, 06 Feb 2024 12:00:00 GMT
# -- 본문 생략 --

# 2. Cache-Control 헤더를 통한 유효 기간 설정.
HTTP/1.1 200 OK
Date: Mon, 05 Feb 2024 12:00:00 GMT
Content-type: text/plain
Content-length: 100
# 유효 기간
Cache-Control: max-age=1200
# -- 본문 생략 --

# 3. If-Modified-Since를 통한 최신 상태 재점검.
GET /index.html HTTP/1.1
Host: www.example.com
If-Modified-Since: Fri, 23 Aug 2024 09:00:00 GMT

# 4. Etag를 활용한 자원 확인.
GET /index.html HTTP/1.1
Host: www.example.com
If-None-Match: "abc"
```

<br>

<h2>3-3. 쿠키</h2>
<ul>
  <li>
    HTTP는 스테이트리스 프로토콜이기 때문에 상태를 활용하기 위해 <strong>쿠키(cookie)</strong>를 활용한다. 쿠키란 <strong>서버에서 생성</strong>되어 클라이언트 측에 전달되는 데이터이다.
  </li>
    <ul>
      <li>
        쿠키는 기본적으로 &lt;이름, 값&gt; 쌍의 형태를 띠고 추가로 적용 범위와 만료 기간 등 다양한 속성을 가질 수 있다.
      </li>
    </ul>
  <li>
    서버는 쿠키를 생성하여 클라이언트에게 전송하고, 클라이언트는 전달받은 쿠키를 저장해 두었다가 추후 <strong>동일한 서버</strong>에 보내는 요청 메시지에 <strong>쿠키를 포함하여 전송</strong>한다.
  </li>
    <ul>
      <li>
        서버는 쿠키 정보를 참고해 요청이 같은 클라이언트에게서 왔는지, 로그인 상태를 유지하는지 등을 알 수 있다.
      </li>
    </ul>
  <li>
    쿠키는 각각 <strong>응답 메시지의 Set-Cookie 헤더</strong>와 <strong>요청 메시지의 Cookie 헤더</strong>를 통해 전달된다.
  </li>
    <ul>
      <li>
        응답 메시지의 Set-Cookie 헤더를 통해 <strong>쿠키의 이름</strong>, <strong>값</strong>과 더불어 세미 콜론(;)으로 구분된 속성(들)</strong>을 전달할 수 있다.
      </li>
      <li>
        한 응답 메시지에 전달할 쿠키가 여러 개라면 여러 개의 Set-Cookie를 사용하기도 한다.
      </li>
    </ul>
  <li>
    <strong>요청 메시지의 Cookie 헤더</strong> 값은 서버에 전달할 <strong>쿠키의 이름</strong>과 <strong>값</strong>을 나타내는 헤더이다.
  </li>
    <ul>
      <li>
        여러 개의 쿠키 값을 서버에 전달해야 할 때는 <strong>'Cookie: 이름=값; 이름=값;'</strong>과 같이 세미 콜론(;)을 통해 여러 쿠키의 이름-값을 나타낼 수 있다.
      </li>
    </ul>
  <li>
    쿠키는 <strong>브라우저</strong>에 저장되고 관리되며 크롬 브라우저에서 개발자 도구를 열고 '[Application] → [Storage] → [Cookies]'에서 확인할 수 있다.
  </li>
  <li>
    쿠키는 발급 받은 서버 외에 다른 서버에 전송되면 안되기 때문에 사용 가능한 <strong>도메인</strong>이 정해져 있다. 도메인은 Set-Cookie 헤더의 <strong>'domain' 속성</strong>으로 정해진다.
  </li>
    <ul>
      <li>
        같은 도메인이라도 <strong>경로별로 쿠키를 구분</strong>하여 사용하고 싶을 때가 있는데 이때에는 <strong>"path"</strong>를 활용하여 <strong>쿠키가 적용될 경로</strong>를 명시한다.
      </li>
    </ul>
  <li>
    쿠키에는 <strong>Expires/Max-Age 열</strong>이 있는데 이는 <strong>쿠키의 유효 기간</strong>을 나타낸다.
  </li>
    <ul>
      <li>
        Expires는 <strong>[요일, DD-MM-YY HH:MM:SS GMT] 형식</strong>으로 표기되는 쿠키 만료 시점을 의미한다.
      </li>
      <li>
        Max-Age는 <strong>초 단위 유효 기간</strong>을 의미한다.
      </li>
    </ul>
  <li>
    쿠키는 정보가 쉽게 노출되거나 조작될 수 있다는 <strong>보안적 한계</strong>를 가진다. 이를 보완하기 위해서 쿠키는 <strong>Secure</strong>와 <strong>HttpOnly</strong> 속성을 가진다.
  </li>
    <ul>
      <li>
        Secure는 <strong>HTTPS 프로토콜</strong>이 사용되는 경우에만 쿠키를 전송하도록 하는 속성이다.
      </li>
      <li>
        HttpOnly는 <strong>HTTP 송수신</strong>을 통해서만 쿠키를 이용하도록 제한하는 속성이다. 대표적으로 <strong>자바스크립트</strong>에서 쿠키에 접근하지 못하도록 하는 속성이다.
      </li>
    </ul>
</ul>

```http
# 1. 요청 메시지 예시.
Cookie: 이름=값; 이름=값;

# 2. 응답 메시지 예시.
HTTP/1.1 200 OK
Content-Type: text/html
Set-Cookie: name=minchul
Set-Cookie: phone=100-100
Set-Cookie: message=Hello
# ... 헤더 후략 ...
# ... 메시지 본문 생략 ...

# 3. 2번 응답 메시지를 활용한 요청 메시지
GET /next_page HTTP/1.1
Host: example.com
Cookie: name=minchul; phone=100-100; message=Hello
# ... 헤더 후략 ...
```

<h4>세션 인증</h4>
<ul>
  <li>
    쿠키를 통해 전달되는 대표적인 정보로는 <strong>세션 아이디(session id)</strong>가 있다. 
  </li>
  <li>
    세션 아이디를 이해하기 위해서는 <strong>세션 인증(session authentication)</strong>을 이해해야한다. 세션 인증은 다음의 순서로 이루어지는 <strong>인증 방식</strong>이다. 
  </li>
    <ol>
      <li>
        클라이언트는 서버에게 (아이디, 비밀번호와 같은) 인증 정보를 전송한다.
      </li>
      <li>
        인증 정보가 올바르다면, 서버는 세션 아이디를 생성해 클라이언트에게 전송한다.
      </li>
      <li>
        서버는 생성한 세션 아아디를 데이터베이스 등에 저장한다.
      </li>
      <li>
        클라이언트는 추후 요청을 보낼 때 쿠키 내에 세션 아이디를 포함하여 전송한다.
      </li>
      <li>
        서버는 쿠키 속 세션 아이디와 저장된 세션 아이디를 비교하여 클라이언트를 식별한다.
      </li>
    </ol>
</ul>

<h4>웹 스토리지: 로컬 스토리지와 세션 스토리지</h4>
<ul>
  <li>
    쿠키 이외에도 클라이언트가 저장하고 클라이언트의 상태를 추측할 수 있는 &lt;키-값&gt; 쌍 형태의 정보인 <strong>웹 스토리지(web storage)</strong>가 있다.
  </li>
  <li>
    웹 스토리지는 <strong>웹 브라우저 내의 저장 공간</strong>으로 일반적으로 <strong>쿠키보다 더 큰 데이터</strong>를 저장할 수 있다.
  </li>
    <ul>
      <li>
        쿠키는 자동으로 서버에 전송되지만, 웹 스토리지의 정보는 서버로 자동 전송되지 않으며 필요할 때 조회할 수 있다.
      </li>
      <li>
        웹 스토리지는 '[Application] → [Storage]'를 통해 확인할 수 있다.
      </li>
    </ul>
  <li>
    <strong>세션 스토리지</strong>는 <strong>세션이 유지</strong>되는 동안 유지되는 정보이고, <strong>로컬 스토리지</strong>는 별도로 삭제하지 않는 한 <strong>영구적으로 저장</strong>이 가능한 정보이다.
  </li>
</ul>