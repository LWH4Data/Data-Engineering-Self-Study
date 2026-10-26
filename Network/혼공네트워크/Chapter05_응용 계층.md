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
  </li>
    <ul>
      <li>
        도메인 네임이란 호스트의 IP 주소와 대응되는 <strong>문자열 형태</strong>의 호스트 특정 정보이다.
      </li>
      <li>
        도메인 네임과 IP 주소는 <strong>네임 서버(name server)</strong>에서 관리하고, 도메인 네임을 관리하는 네임 서버는 <strong>DNS 서버</strong>라고도 부른다.
      </li>
    </ul>
  <li>
    도메인 네임은 IP 주소에 비해 기억하기 쉽고 IP 주소가 바뀌어도 도메인 네임은 그대로이기에 활용하기 편리하다.
  </li>
  <li>
  <li>
    도메인 네임은 <strong>점(.)</strong>을 기준으로 계층적으로 분류된다.
  </li>
    <ul>
      <li>
        최상단에는 <strong>루트 도메인(root domain)</strong>이 있다. 일반적으로 알고 있는 도메인 네임의 <strong>마지막 부분</strong>을 의미한다.
      </li>
      <li>
        루트 도메인 이후에는 <strong>최상위 도메인(TLD; Top-Level Domain)</strong>이 있고 그 후에 또 도메인들이 나열된다.
      </li>
      <li>
        예를 들어 www.example.com이라면 최상위 도메인은 com이다.
      </li>
        <ul>
          <li>
            최상위 도메인은 다양하고 대표적으로 com, net, org, kr(대한민국), jp(일본), cn(중국), us(미국) 등이 있다.
          </li>
        </ul>
    </ul>
  <li>
    정확히는 루트 도메인(.)이 가장 마지막에 붙지만 일반적으로 이를 생략하여 표기한다. 따라서 'www.google.com'이나 'www.google.com.'' 둘 모두 동일하게 접속된다.
  </li>
  <li>
    최상위 도메인의 하부 도메인은 <strong>2단계 도메인(second-level domain)</strong>이라고 한다.
  </li>
  <li>
    도메인 네임의 단계는 일반적으로 3~5 단계 정도이며 도메인 네임을 모두 포함하는 도메인 네임을 <strong>전체 주소 도메인 네임(FQDN; Fully-Qualified Domain Name)</strong>이라 한다.
  </li>
    <ul>
      <li>
        FQDN은 전체를 명시하여 호스트를 나타낼 수 있기 때문에 <strong>호스트 네임(host name)</strong>이라 부르기도 한다.
      </li>
    </ul>
  <li>
    계층적인 도메인 네임을 효율적으로 관리하기 위해 네임 서버 또한 <strong>계층적인 형태</strong>를 이룬다.
  </li>
  <li>
    네임 서버는 <strong>여러 개</strong> 존재하며 <strong>전 세계 여러 군데</strong>에 위치해 있다.
  </li>
  <li>
    위처럼 계층적이고, 분산된 도메인 네임(Domain Name)에 대한 관리 체계(System)를 도메인 네임 시스템(Domain Name System), 줄여서 <strong>DNS</strong>라고 부른다.
  </li>
    <ul>
      <li>
        DNS는 호스트가 이런 도메인 네임 시스템을 이용할 수 있도록 하는 <strong>애플리케이션 계층 프로토콜</strong>을 의미하기도 한다.
      </li>
      <li>
        즉 DNS는 계층적이고 분산된 도메인 네임에 대한 <strong>관리 체계</strong>이며 이를 관리하는 <strong>프로토콜</strong>이다.
      </li>
    </ul>
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

<h4>서브 도메인이란 무엇인가요?</h4>
<ul>
  <li>
    서브 도메인(subdomain)이란 <strong>다른 도메인이 포함된 도메인</strong>을 의미한다.
  </li>
  <li>
    예를 들어 google.com의 서브 도메인들로는 다음이 있다.
  </li>
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
</ul>

<br>

<h2>1-2. 계층적 네임 서버</h2>
<ul>
  <li>
    IP 주소를 모르는 상태에서 도메인 네임에 대응되는 IP 주소를 알아내는 과정을 흔히 도메인 네임을 <strong>풀이(resolve)</strong>한다고 표현하며 영어로는 <strong>resolving한다</strong>라고도 한다.
  </li>
  <li>
    IP 주소를 알아내는 과정에서 다양한 네임 서버들이 사용되는데 중요한 네임 서버의 유형은 크게 네 가지가 있다.
  </li>
    <ul>
      <li>
        <strong>로컬 네임 서버(local name server)</strong>
      </li>
        <ul>
          <li>
            클라이언트와 맞닿아 있는 서버로 클라이언트가 도메인 네임을 통해 IP 주소를 알아내고자 할 때 <strong>가장 먼저 찾게 되는 네임 서버</strong>이다.
          </li>
          <li>
            로컬 네임 서버의 주소는 일반적으로 <strong>ISP</strong>에서 할당해 주는 경우가 많다.
          </li>
            <ul>
              <li>
                ISP에서 할당해 주는 로컬 네임 서버가 아닌 <strong>공개 DNS 서버(public DNS Server)</strong>를 이용할 수도 있다.
              </li>
            </ul>
        </ul>
      <li>
        <strong>루트 네임 서버(root name server)</strong>
      </li>
        <ul>
          <li>
            로컬 네임 서버가 대응되는 IP 주소를 모른다면 루트 네임 서버에 해당 도메인 네임을 질의하게 된다.
          </li>
          <li>
            루트 네임 서버는 루트 도메인을 관장하는 네임 서버로, 질의에 대해 TLD 네임 서버의 IP 주소를 반환할 수 있다.
          </li>
        </ul>
      <li>
        <strong>TLD(최상위 도메인) 네임 서버</strong>
      </li>
        <ul>
          <li>
            TLD 네임 서버는 TLD를 관리하는 네임 서버이다.
          </li>
          <li>
            TLD 네임 서버는 질의에 대해 TLD의 하위 도메인인 네임을 관리하는 네임 서버 주소를 반환할 수 있다.
          </li>
        </ul>
      <li>
        <strong>책임 네임 서버(authoritative name server)</strong>
      </li>
        <ul>
          <li>
            책임 네임 서버는 특정 도메인 영역(name)을 관리하는 네임 서버로, 자신이 관리하는 도메인 영역의 질의에 대해서 다른 네임 서버에 넘기지 않고 바로 답할 수 있는 네임 서버이다.
          </li>
            <ul>
              <li>
                쉽게 말해 로컬 네임 서버가 <strong>마지막으로 질의하는 네임 서버</strong>이다.
              </li>
            </ul>
        </ul>
    </ul>
  <li>
    로컬 네임 서버가 네임 서버들에게 질의하는 방법에는 크게 <strong>재귀적 질의</strong>와 <strong>반복적 질의</strong> 두 가지가 있다.
  </li>
    <ul>
      <li>
        재귀적 질의(recursive query)는 <strong>'클라이언트 &rarr; 로컬 네임 서버 &rarr; 루트 네임 서버 &rarr; TLD 네임 서버 &rarr; 다음 단계 서버'</strong>로 질의하는 과정을 반복하여 최종 응답 결과를 <strong>역순으로 전달</strong>받는 방식이다.
      </li>
      <li>
        반복적 질의(iterative query)란 <strong>로컬 네임 서버</strong>가 <strong>반복적</strong>으로 루트 네임 서버, TLD 네임 서버, 책엠 네임 서버에 질의하고 최종 결과를 클라이언트에 알려 주는 방식이다.
      </li>
    </ul>
  <li>
    로컬 네임 서버가 도메인을 통해 IP를 얻는 과정에는 단계가 많아 요청이 많아지면 <strong>루트 네임 서버에 과부하</strong>가 걸릴 수 있다.
  </li>
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
</ul>

<br>

<h2>1-3. 자원을 식별하는 URI</h2>
<ul>
  <li>
    송수신하고자 하는 정보를 식별하기 위한 방법에는 <strong>URI</strong>가 있다. 
  </li>
    <ul>
      <li>
        URI를 식별 정보 기준으로 분류한 개념들에는 <strong>URL</strong>과 <strong>URN</strong>이 있다.
      </li>
    </ul>
  <li>
    상기한 URI, URL, URN을 이해하기 위해서는 자원(resource)이 무엇인지 이해해야 한다. <strong>자원</strong>이란 <strong>네트워크상의 메시지를 통해 주고받는 대상</strong>을 의미한다.
  </li>
    <ul>
      <li>
        예를 들면 HTML 파일, 이미지나 동영상, 텍스트 파일 등이 모두 해당한다.
      </li>
    </ul>
  <li>
    오늘날 인터넷 환경을 이루는 대부분의 통신은 <strong>HTTP를 기반</strong>으로 이루어지고, 자원이라는 용어는 <strong>HTTP 요청 메시지의 대상</strong>이라고도 표현한다.
  </li>
  <li>
    네트워크상에서 자원을 주고받기 위해서는 자원을 식별할 수 있어야하며 이렇게 <strong>자원을 식별</strong>할 수 있는 정보를 <strong>URI(Uniform Resource Identifier)</strong>라고 부른다.
  </li>
    <ul>
      <li>
        <strong>위치</strong>를 이용해 자원을 식별하는 경우를 <strong>URL(Uniform Resource Locator)</strong>이라 한다.
      </li>
      <li>
        <strong>이름</strong>을 이용해 자원을 식별하는 경우를 <strong>URN(Uniform Resource Name)</strong>이라 한다.
      </li>
    </ul>
</ul>

<h3>1-3-1. URL</h3>
<ul>
  <li>
    오늘날 인터넷 환경에서 자원 식별에 더 많이 사용되는 방법은 URL이다.
  </li>
  <li>
    예를 들어 'foo://www.example.com:8042/over/there?name=ferret#nose'의 형식은 다음과 같다.
  </li>
    <ul>
      <li>
        foo &rarr; scheme
      </li>
        <ul>
          <li>
            URL의 첫 부분으로 <strong>자원에 접근하는 방법</strong>을 의미하며 일반적으로 사용할 <strong>프로토콜</strong>이 명시된다.
          </li>
          <li>
            HTTP를 사용할 때에는 http://를, HTTPS를 사용할 때에는 https://를 명시한다.
          </li>
        </ul>
      <li>
        www.example.com:8042 &rarr; authority
      </li>
        <ul>
          <li>
            authority는 <strong>호스트를 특정할 수 있는 정보</strong>, 예를 들어 IP 주소 혹은 도메인 네임이 명시되면 <strong>콜론(:) 뒤에 포트 번호</strong>를 덧붙일 수도 있다. 
          </li>
        </ul>
      <li>
        /over/there? &rarr; path
      </li>
        <ul>
          <li>
            path에는 <strong>자원이 위치한 경로</strong>가 명시된다. 
          </li>
          <li>
            자원의 위치는 <strong>슬래시(/)</strong>를 기준으로 <strong>계층적으로 표현</strong>되고, 최상위 경로 또한 슬래시로 표현된다.
          </li>
        </ul>
      <li>
        ?name=ferret &rarr; query
      </li>
        <ul>
          <li>
            path까지만을 활용해서 자원의 위치를 식별할 수도 있지만, 더 많은 정보가 필요할 때도 있다. 이때 <strong>쿼리 문자열(query string)</strong>을 사용한다. 쿼리 문자열은 <strong>쿼리 파라미터(query parameter)</strong>라고도 부른다.
          </li>
          <li>
            쿼리 문자열은 <strong>물음표(?)</strong>로 시작되는 <strong>&lt;키=값&gt;</strong> 형태의 데이터이며 <strong>앰퍼센트(&)</strong>를 사용해 여러 쿼리 문자열을 연결할 수도 있다.
          </li>
        </ul>
      <li>
        #nose &rarr; fragment
      </li>
        <ul>
          <li>
            <strong>자원의 한 조각</strong>을 가리키기 위한 정보이다. 흔히 HTML 파일과 같은 자원에서 특정 부분을 가리키기 위해 사용한다.
          </li>
        </ul>
    </ul>
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
  </li>
    <ul>
      <li>
        도메인 레코드를 추가하여 네임 서버에 IP가 도메인 네임에 매핑되었음을 알린다.
      </li>
    </ul>
  <li>
    각 레코드에는 <strong>레코드 유형</strong>이 정해져 있기 때문에 레코드의 유형이 달라지면 레코드의 이름과 값의 의미가 달라진다.
  </li>
</ul>

<br><br>

<h1>2. HTTP</h1>
<ul>
  <li>
    HTTP에는 다음과 같은 중요한 네 가지 특성이 있다.
  </li>
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
  </li>
    <ul>
      <li>
        HTTP 요청 메시지와 HTTP 응답 메시지는 <strong>메시지 형태</strong>가 다르다.
      </li>
    </ul>
  <li>
    개발자 도구에서 <strong>[Network] 탭</strong>을 보면 해당 웹 사이트에서 주고받는 자원들을 확인할 수 있다.
  </li>
    <ul>
      <li>
        여기서 임의의 자원을 클릭하면 <strong>HTTP 요청 메시지 헤더(Request Headers)</strong>와 <strong>HTTP 응답 메시지 헤더(Response Headers)</strong>를 볼 수 있다.
      </li>
    </ul>
</ul>

<h3>2-1-2. 미디어 독립적 프로토콜</h3>
<ul>
  <li>
    HTTP는 주고받을 <strong>자원의 특성과 무관</strong>하게 그저 자원을 <strong>주고받을 수단(인터페이스)</strong>의 역할만을 수행한다.
  </li>
    <ul>
      <li>
        실제로 HTTP를 통해 HTML, JPEG, PNG, JSON, XML, PDF 등 다양한 종류의 자원을 주고받을 수 있다.
      </li>
    </ul>
  <li>
    HTTP에서 메시지로 주고받는 자원의 종류를 <strong>미디어 타입(media tpye)</strong>이라 부른다. 혹은 <strong>MIME 타입(Multipurpose Internet Mail Extensions Type)</strong>이라고도 부른다.
  </li>
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
  <li>
    미디어 타입은 기본적으로 슬래시를 기준으로 하는 <strong>타입/서브타입(type/subtype)</strong> 형식으로 구성된다.
  </li>
    <ul>
      <li>
        <strong>타입(type)</strong>은 <strong>데이터의 유형</strong>을 나타내고, <strong>서브타입(subtype)</strong>은 주어진 타입에 대한 <strong>세부 유형</strong>을 나타낸다. (type/subtype 형식).
      </li>
    </ul>
</ul>