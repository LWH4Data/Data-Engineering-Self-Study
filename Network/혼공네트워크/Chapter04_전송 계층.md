<h1>1. 전송 계층 개요: IP의 한계와 포트</h1>
<ul>
  <li>
    네트워크 계층의 IP는 <strong>신뢰할 수 없는 통신</strong>과 <strong>비연결형 통신</strong>을 수행한다는 한계가 있다.
  </li>
  <li>
    네트워크 계층과 응용 계층 사이에 위치한 전송 계층은 신뢰할 수 있는 통신과 연결형 통신을 가능하게 하여 <strong>IP의 한계를 극복</strong>하고, <strong>포트 번호</strong>를 통해 응용 계층의 애플리케이션 프로세스들을 식별한다.
  </li>
</ul>

<br>

<h2>1-1. 신뢰할 수 없는 통신과 비연결형 통신</h2>
<ul>
  <li>
    IP는 신뢰할 수 없는(비신뢰성) 프로토콜(unreliable protocol)이자 비연결형 프로토콜(connectionless protocol)이다.
  </li>
    <ul>
      <li>
        위의 이유가 전송 계층이 존재하는 이유이기도 하다.
      </li>
    </ul>
  <li>
    신뢰할 수 없는 통신이란 IP 프로토콜이 <strong>패킷이 수신지까지 제대로 전송되었다는 보장</strong>을 하지 않는 특징을 의미한다.
  </li>
    <ul>
      <li>
        패킷 데이터 손실, 중복 패킷 전송, 순차적으로 패킷 도착 등을 보장하지 않는다.
      </li>
      <li>
        이러한 전송 특성을 <strong>최선형 전달(best effort delivery)</strong>이라고도 부른다. (최선은 다하지만 보장은 하지 않음).
      </li>
    </ul>
  <li>
    비연결형 통신은 송수신 호스트 간에 <strong>사전 연결 수립</strong> 작업을 거치지 않는 특징을 의미한다.
  </li>
  <li>
    IP가 이렇게 신뢰와 보장이 없는 이유는 <strong>성능</strong> 때문이다. 위와 같은 정보를 확인하는 것들이 모두 부하이기 때문이다.
  </li>
    <ul>
      <li>
        예를 들어 금융과 같은 신뢰성이 중요한 경우도 있으나 전화 등 스트리밍의 경우 일부 패킷에 손실이 발생하여도 크게 영향이 없으며 실시간이 더 중요하다.
      </li>
    </ul>
</ul>

<br>

<h2>1-2. IP의 한계를 보완하는 전송 계층</h2>
<h3>1-2-1. 전송 계층은 연결형 통신을 가능하게 한다.</h3>
<ul>
  <li>
    연결형 통신을 지원하는 대표적인 전송 프로토콜로 <strong>TCP</strong>가 있다.
  </li>
    <ul>
      <li>
        TCP는 두 호스트가 정보를 주고받기 전에 가상의 회선을 설정하듯 연결을 수립한다.
      </li>
      <li>
        송수신하는 동안에는 연결을 유지하고, 끝나면 연결을 종료할 수 있다.
      </li>
      <li>
        즉 호스트간에 메시지를 주고받기 전 호스트 사이에 메시지 전송로(회선)를 설정하고 해당 전송로로 메시지를 주고받는다.
      </li>
    </ul>
  <li>
    다만 항상 TCP와 같은 신뢰성을 보장하는 것이 좋은 것은 아니다. 떄로는 비교적 높은 성능이 우성시되는 경우도 있으며 이때에는 전송 계층에 <strong>UDP</strong>라는 프로토콜을 사용한다.
  </li>
</ul>

<h3>둘째, 전송 계층은 신뢰성 있는 통신을 가능하게 한다.</h3>
<ul>
  <li>
    TCP를 활용하면 패킷이 수신지까지 올바른 순서로 전달되는 것을 보장하기 위해 <strong>재전송</strong>을 통한 오류 제어, 흐름 제어, 혼잡 제어 등 다양한 기능들을 제공하여 <strong>신뢰성을 보장</strong>한다.
  </li>
</ul>

<br>

<h2>1-3. 응용 계층과의 연결 다리, 포트</h2>
<ul>
  <li>
    전송 계층이 네트워크 계층의 한계를 극복하도록 한다면 포트는 응용 계층과의 <strong>연결 다리의 역할</strong>을 한다.
  </li>
</ul>

<h3>1-3-1. 포트의 정의</h3>
<ul>
  <li>
    패킷은 단순히 수신지 호스트까지 전달만 되는 것이 아니라 도착 후에는 수신 대상이 되는 <strong>특정 애플리케이션 프로세스</strong>까지 전달이 되어야 한다.
  </li>
  <li>
    패킷이 실행 중인 특정 애플리케이션까지 전달되려면 패킷에 <strong>특정 애플리케이션을 식별</strong>할 수 있는 정보가 필요하며 이 정보를 <strong>포트(port)</strong>라고 한다.
  </li>
</ul>

<h3>1-3-2. 포트의 분류</h3>
<ul>
  <li>
    전송 계층에서는 패킷 내 <strong>수신지 포트</strong>와 <strong>송신지 포트</strong>를 통해 송수신지 호스트의 애플리케이션을 식별한다.
  </li>
  <li>
    전송 계층의 핵심 프로토콜인 TCP와 UDP는 모두 포트 번호 필드인 송신지 포트 번호와 수신지 포트 번호를 포함한다.
  </li>
  <li>
    사용 가능한 포트의 수는 2의 16승(65536)개이며 번호의 범위에 따라 세 종류로 나뉜다.
  </li>
    <ul>
      <li>
        <strong>0 ~ 1023번</strong>까지의 포트 번호는 <strong>잘 알려진 포트(well known port)</strong> 혹은 <strong>시스템 포트(system port)</strong>로 범용적으로 사용되는 애플리케이션 프로토콜의 포트 번호를 의미한다. (p196).
      </li>
      <li>
        <strong>1024 ~ 49151</strong>의 포트 번호는 <strong>등록된 포트(registered port) 번호</strong>로 well known보다는 덜 범용적이지만 흔히 사용되는 애플리케이션 프로토콜에 할당된다. (p196). 
      </li>
      <li>
        <strong>49152 ~ 65535</strong>의 포트 번호는 동적 포트(dynamic port), 사설 포트(private port), 임시 포트(ephemeral port)라고 부른다. <strong>자유롭게 사용</strong>할 수 있다.
      </li>
    </ul>
  <li>
    서버로 동작하는 프로그램은 일반적으로 잘 알려진 포트와 등록된 포트로 동작하는 경우가 많다.
  </li>
  <li>
    클라이언트로서 동작하는 프로그램은 동적 포트 번호 중 임의의 번호가 할당되는 경우가 많다.
  </li>
  <li>
    IP 주소와 포트 번호가 주어지면 특정 호스트에서 실행 중인 특정 애플리케이션 프로세스를 식별할 수 있다.
  </li>
    <ul>
      <li>
        위와 같은 이유로 포트 번호는 일반적으로 <strong>'IP 주소:포트 번호'</strong> 형식으로 함께 표시되는 경우가 많다.
      </li>
    </ul>
</ul>

<h4>인터넷 할당 번호 관리 기관, IANA</h4>
<ul>
  <li>
    잘 알려진 포트와 등록된 포트는 인터넷 할당 번호 관리 기관(IANA; Internet Assigned Numbers Authority)이라는 국제 단체에 의해 할당되어 있다.
  </li>
</ul>

<br>

<h2>1-4. 포트 기반 NAT</h2>
<ul>
  <li>
    NAT은 IP 주소를 변환하는 기술로 네트워크 내부에서 사용되는 <strong>사설 IP 주소</strong>와 네트워크 외부에서 사용되는 <strong>공인 IP 주소를 변환</strong>하는 데 사용된다. 이를 위해 주로 <strong>NAT 변환 테이블</strong>을 사용한다.
  </li>
</ul>

<h3>1-4-1. NAT 변환 테이블</h3>
<ul>
  <li>
    NAT 변환 테이블에는 변환의 대상이 되는 <strong>IP 주소 쌍</strong>이 명시되어 있다.
  </li>
  <li>
    NAT 테이블의 항목을 일대일로 대응하면 <strong>사설 IP 개수만큼 공인 IP 주소</strong>를 필요로하기에 많은 사설 IP 주소를 변환하는 것에는 무리가 있다.
  </li>
    <ul>
      <li>
        따라서 다수의 사설 IP 주소를 그보다 <strong>적은 수의 공인 IP 주소</strong>로 변환한다.
      </li>
    </ul>
</ul>

<h3>1-4-2. NAPT</h3>
<ul>
  <li>
    포트 기반의 NAT를 NAPT(Network Address Port Translation) 혹은 APT(Address Port Translation)라 한다.
  </li>
  <li>
    NAPT는 포트를 활용하여 하나의 공인 IP 주소를 여러 사설 IP 주소가 공유할 수 있도록 하는 NAT의 일종이다
  </li>
    <ul>
      <li>
        NAPT는 NAT 테이블에 변환할 IP 주소쌍과 함께 포트 번호도 함꼐 기록하고 변환한다.
      </li>
      <li>
        외부 IP 주소가 같아도 포트 번호가 다르면 네트워크 내부의 호스트를 특정할 수 있다.
      </li>
      <li>
        즉 NAPT를 이용하면 네트워크 내부에서 사용할 IP 주소와 네트워크 외부에서 사용할 IP 주소를 <strong>N:1로 관리</strong>할 수 있다.
      </li>
    </ul>
</ul>

<h4>포트 포워딩</h4>
<ul>
  <li>
    포트 포워딩(port forwarding)이란 네트워크 내 <strong>특정 호스트에 IP 주소와 포트 번호를 미리 할당</strong>하고 해당 'IP 주소:포트 번호'를 통해 해당 호스트에게 패킷을 전달하는 기능이다.
  </li>
  <li>
    주로 네트워크 <strong>외부에서 네트워크 내부로 통신을 시작</strong>할 때 네트워크 내부의 서버를 외부에 서접속할 수 있게 <strong>접속 정보를 공개</strong>하기 위해 사용한다.
  </li>
</ul>

<h4>ICMP</h4>
<ul>
  <li>
    IP의 신뢰할 수 없는 전송 특성과 비연결형 전송 특성을 보완하기 위한 네트워크 계층의 프로토콜로 ICMP가 있다.
  </li>
  <li>
    ICMP(Internet Control Message Protocol)는 IP 패킷의 전송 과정에 대한 <strong>피드백 메시지</strong>를 얻기 위해 사용되는 프로토콜이다.
  </li>
  <li>
    ICMP 메시지의 종류는 크게 전송 과정에서 발생한 <strong>문제 상황에 대한 오류 보고</strong>를 하는 메시지와 네트워크에 대한 <strong>진단 정보(네트워크상의 정보 제공)</strong>에 대한 메시지 두 가지가 있다.
  </li>
  <li>
    ICMP 메시지는 <strong>타입</strong>과 <strong>코드</strong>로 정의되며 타입과 코드는 <strong>패킷 헤더</strong>에 포함되는 정보이다.
  </li>
    <ul>
      <li>
        헤더의 타입(type) 필드에는 <strong>ICMP의 유형</strong>이 번호로 명시된다.
      </li>
      <li>
        코드(code) 필드에는 <strong>구체적인 메시지 내용이 번호</strong>로 명시된다.
      </li>
      <li>
        ICMP에는 IPv4에 사용되는 ICMPv4와 IPv6에 사용되는 ICMPv6가 있다.
      </li>
    </ul>
  <li>
    ICMP는 네트워크상의 간단한 문제를 진단 및 테스트하기 위해 사용되기도 한다.
  </li>
    <ul>
      <li>
        traceroute 또는 tracert 명령어 또한 ICMP 메시지를 기반으로 동작한다.
      </li>
      <li>
        ping 또한 네트워크의 상태를 진단하는 가장 기본적인 명령어로 ICMP 기반의 명령어이다.
      </li>
    </ul>
  <li>
    유의할 점은 ICMP가 IP의 신뢰성을 보장하지는 않으며 어디까지나 도우미의 역할만 수행한다.
  </li>
    <ul>
      <li>
        IP 패킷이 수신지까지 도달하지 못하거나 ICMP 메시지를 담은 패킷이 송신지까지 되돌아오지 못하는 경우도 있다.
      </li>
    </ul>
</ul>

<br><br>

<h1>2. TCP와 UDP</h1>
<ul>
  <li>
    네트워크 계층에서 가장 중요한 프로토콜이 IP라면, 전송 계층에서 가장 중요한 프로토콜은 <strong>TCP</strong>와 <strong>UDP</strong>이다.
  </li>
    <ul>
      <li>
        TCP(Transmission Control Protocol)는 신뢰할 수 있는 통신을 위한 <strong>연결형 프로토콜</strong>이다.
      </li>
      <li>
        UDP(User Datagram Protocol)는 TCP보다 신뢰성은 떨어지지만 비교적 빠른 통신이 가능한 <strong>비연결형 프로토콜</strong>이다.
      </li>
    </ul>
  <li>
    TCP가 통신의 시작과 끝맺는 과정, 오류 제어를 위한 재전송, 흐름 제어, 혼잡 제어 등의 기능이 더 많아 학습할 내용이 더 많다.
  </li>
</ul>

<br>

<h2>2-1. TCP 통신 단계와 세그먼트 구조</h2>
<ul>
  <li>
    TCP 통신을 크게 세 단계로 나누면 <strong>연결 수립</strong>, <strong>데이터 송수신(재전송을 통한 오류 제어, 흐름 제어, 혼잡 제어)</strong>, <strong>연결 종료</strong>라 구분할 수 있다.
  </li>
  <li>
    TCP 연결 수립과 종료를 이해하기 위해서는 가장 먼저 <strong>MSS</strong>라는 TCP의 세그먼트 구조를 이해해야한다.
  </li>
  <li>
    MSS는 Maximum Segment Size의 약자로, TCP로 전송할 수 있는 <strong>최대 페이로드 크기</strong>를 의미한다.
  </li>
    <ul>
      <li>
        MTU는 헤더 크기까지 포함하지만 MSS는 TCP 헤더 크기를 제외한다는 차이가 있다.
      </li>
    </ul>
  <li>
    TCP의 기본 동작을 이해하기 위한 세그먼트 헤더의 필드들은 다음과 같다.
  </li>
    <ul>
      <li>
        <strong>송신지 포트(source port)와 수신지 포트(destination port)</strong>: 송신지 또는 수신지 애플리케이션을 식별하는 포트 번호.
      </li>
      <li>
        <strong>순서 번호(sequence number)</strong>: 순서 번호가 명시되는 필드. 송수신되는 세그먼트의 올바른 순서를 보장하기 위해 세그먼트 데이터의 첫 바이트에 부여되는 번호이다.
      </li>
      <li>
        <strong>확인 응답 번호(acknowledgment number)</strong>: 상대 호스트가 보낸 세그먼트에 대한 응답. 다음으로 수신하기를 기대하는 순서 번호가 명시된다.
      </li>
      <li>
        <strong>제어 비트(control bits)</strong>: 플래그 비트(flag bits)라고도 부르며 현재 세그먼트에 대한 부가 정보를 나타낸다.
      </li>
      <li>
        <strong>윈도우(window)</strong>: 수신 윈도우의 크기가 명시된다. 수신 윈도우란 한 번에 수신하고자 하는 데이터의 양을 나타낸다.
      </li>
    </ul>
</ul>

<h3>2-1-1. 제어 비트</h3>
<ul>
  <li>
    <strong>제어 비트</strong>는 기본적으로 <strong>8비트</strong>로 구성되며 각 자리의 비트는 각기 다른 의미를 가진다. 자주 언급되는 세 개의 제어 비트는 다음과 같다.
  </li>
    <ul>
      <li>
        <strong>ACK</strong>: 세그먼트의 승인을 나타내기 위한 비트
      </li>
      <li>
        <strong>SYN</strong>: 연결을 수립하기 위한 비트
      </li>
      <li>
        <strong>FIN</strong>: 연결을 종료하기 위한 비트
      </li>
    </ul>
</ul>

<h3>2-1-2. 순서 번호와 확인 응답 번호</h3>
<ul>
  <li>
    <strong>순서 번호 필드</strong>와 <strong>확인 응답 번호 필드</strong>는 TCP의 <strong>신뢰성을 보장</strong>하기 위해 사용되는 중요한 필드로 한 쌍으로 묶어 기억하는 것이 좋다.
  </li>
  <li>
    순서 번호 필드의 순서 번호는 세그먼트의 올바른 <strong>송수신 순서를 보장</strong>하기 위한 번호로, 세그먼트 데이터의 <strong>첫 바이트</strong>에 부여되는 번호이다.
  </li>
  <li>
    SYN 플래그가 1로 설정되어 연결이 시작되면 1로 설정된 세그먼트의 경우 순서 번호는 무작위 값이되며 이를 <strong>초기 순서 번호(ISN; Initial Sequence Number)</strong>라고 한다.
  </li>
    <ul>
      <li>
        초기 순서 번호로 시작한 뒤에 데이터를 송신하는 동안 순서 번호는 <strong>'초기 순서 번호 + 송신한 바이트 수'</strong>가 된다.
      </li>
      <li>
        순서 번호는 세그먼트상에서 <strong>32비트(4바이트)</strong>로 표현된다. 만약 표현 가능한 수를 넘어선다면 <strong>0부터 다시 증가</strong>한다.
      </li>
    </ul>
  <li>
    순서 번호는 TCP 세그먼트의 순서를 나타내기 위한 정보이다.
  </li>
  <li>
    확인 응답 번호 필드에 명시되는 <strong>확인 응답 번호</strong>는 <strong>순서 번호에 대한 응답</strong>이다.
  </li>
    <ul>
      <li>
        즉 수신자가 다음으로 받기를 기대하는 순서 번호이다. 일반적으로 순서 번호 + 1로 설정한다.
      </li>
    </ul>
  <li>
    확인 응답 번호 값을 보내기 위해서는 제어 비트에서 승인을 나타내는 비트인 <strong>ACK 플래그를 1</strong>로 설정해야 한다.
  </li>
</ul>

<br>

<h2>2-2. TCP 연결 수립과 종료</h2>
<ul>
  <li>
    TCP는 통신 이전에는 <strong>연결을 수립</strong>하고, 통신 이후에는 <strong>연결을 종료</strong>한다.
  </li>
</ul>

<h3>2-2-1. 연결 수립: 쓰리 웨이 핸드셰이크</h3>
<ul>
  <li>
    TCP의 연결 수립은 <strong>쓰리 웨이 핸드셰이크(three-way handshake)</strong>라는 세 개의 단계로 이루어진다. (p214의 테이블 참고).
  </li>
  <li>
    처음 연결을 시작하는 호스트의 연결 수립 과정을 <strong>액티브 오픈(active open)</strong>이라 한다.
  </li>
    <ul>
      <li>
        주로 서버-클라이언트 관계에서 <strong>클라이언트</strong>에 의해 수행된다.
      </li>
    </ul>
  <li>
    연결 요처을 받으면 요청에 따라 연결을 수립해 주는 호스트도 있으며 이 호스트의 연결 수립 과정을 <strong>패시브 오픈(passive open)</strong>이라 한다.
  </li>
</ul>

<h3>2-2-2. 연결 종료</h3>
<ul>
  <li>
    데이터 송수신이 끝나면 연결을 종료하며 이 과정은 <strong>송수신 호스트</strong>가 각자 한 번씩 <strong>FIN</strong>과 <strong>ACK</strong>를 주고받으며 이루어진다.
  </li>
    <ul>
      <li>
        '송신 호스트(FIN) &#8593; 수신 호스트(ACK) &#8593; 수신 호스트(FIN) &#8593; 송신 호스트(ACK)' 네 개의 단계로 이루어지기 때문에 포 웨이 핸드셰이크(four-way handshake)라고 부르기도 한다.
      </li>
    </ul>
  <li>
    <strong>액티브 클로즈(active close)</strong>는 먼저 연결을 종료하려는 호스트에 의해 수행된다.
  </li>
  <li>
    <strong>패시브 클로즈(passive close)</strong>는 연결 종료 요청을 받아들이는 호스트에 의해 수행된다.
  </li>
</ul>

<br>

<h2>2-3. TCP 상태</h2>
<ul>
  <li>
    TCP는 연결형 통신과 신뢰할 수 있는 통신을 유지하기 위해 다양한 <strong>상태(state)</strong>를 유지한다.
  </li>
    <ul>
      <li>
        여기서 상태란 현재 <strong>어떤 통신 과정</strong>에 있는지를 나타내는 정보이다.
      </li>
      <li>
        TCP가 상태를 유지하고 활용한다는 점에서 <strong>스테이트풀(stateful) 프로토콜</strong>이라고도 불린다.
      </li>
    </ul>
  <li>
    상태에는 크게 연결이 수립되지 않은 상태, 연결 수립 과정에서 주로 보이는 상태, 연결 종료 과정에서 보이는 상태 세 가지로 나눌 수 있다. (p216).
  </li>
</ul>

<h3>2-3-1. 연결이 수립되지 않은 상태</h3>
<ul>
  <li>
    아직 연결 수립이 이루어지기 전의 호스트는 주로 <strong>CLOSED</strong>나 <strong>LISTEN</strong> 상태를 유지하고 있다.
  </li>
    <ul>
      <li>
        CLOSED: 아무런 연결이 없는 상태.
      </li>
      <li>
        LISTEN: 일종의 연결 대기 상태.
      </li>
    </ul>
  <li>
    일반적으로 서버로서 동작하는 패시브 오픈 호스트는 LISTEN 상태를 유지한다.
  </li>
    <ul>
      <li>
        LISTEN 상태란 쓰리 웨이 핸드셰이크의 첫 번째 단계에서 액티브 오픈 호스트의 <strong>SYN 세그먼트</strong>를 기다리는 상태이다.
      </li>
    </ul>
</ul>

<h3>2-3-2. 연결 수립 상태</h3>
<ul>
  <li>
    TCP 연결 수립 과정에서는 주로 SYN-SENT, SYN-RECEIVED, ESTABLISHED 상태를 볼 수 있다.
  </li>
    <ul>
      <li>
        <strong>SYN-SENT</strong>: 액티브 오픈 호스트가 SYN 세그먼트를 보낸 뒤 이에 대한 응답인 SYN + ACK 세그먼트를 기다리는 상태.
      </li>
      <li>
        <strong>SYN-RECEIVED</strong>: 패시브 오픈 호스트가 SYN + ACK 세그먼트를 보낸 뒤 그에 대한 ACK 세그먼트를 기다리는 상태.
      </li>
      <li>
        <strong>ESTABLISHED</strong>: 연결이 확립되었음을 나타내는 상태이며 데이터를 송수신 할 수 있는 상태를 의미한다.
      </li>
        <ul>
          <li>
            쓰리 웨이 핸드셰이크 과정에서 두 호스트가 마지막 ACK 세그먼트를 주고받으면 ESTABLISHED 상태로 접어든다.
          </li>
        </ul>
    </ul>
</ul>

<h3>2-3-3. 연결 종료 상태</h3>
<ul>
  <li>
    TCP 연결을 종료하는 과정에서는 주로 FIN-WAIT-1, CLOSE-WAIT, FIN-WAIT-2, LAST-ACK, TIME-WAITE, CLOSED 상태를 볼 수 있다.
  </li>
    <ul>
      <li>
        <strong>FIN-WAIT-1</strong>: 일반적인 TCP 연결 종료의 첫 단계이다. FIN 세그먼트로서 연결 종료 요청을 보낸 액테브 클로즈 호스트가 FIN-WAIT-1 상태가 된다.
      </li>
      <li>
        <strong>CLOSE-WAIT</strong>: 종료 요청인 FIN 세그먼트를 받은 패시브 클로즈 호스트가 그에 대한 응답으로 ACK 세그먼트를 보낸 후 대기하는 상태이다.
      </li>
      <li>
        <strong>FIN-WAIT-2</strong>: FIN-WAIT-1 상태에서 ACK 세그먼트를 받게 되면 FIN-WAIT-2 상태가된다. 상대 호스트의 FIN 세그먼트를 기다린다.
      </li>
      <li>
        <strong>LAST-ACK</strong>: CLOSE-WAIT 상태에서 FIN 세그먼트를 전송한 뒤 이에 대한 ACK 세그먼트를 기다리는 상태이다.
      </li>
      <li>
        <strong>TIME-WAIT</strong>: 액티브 클로즈 호스트가 FIN 세그먼트를 수신한 뒤, 이에 대한 ACK 세그먼트를 전송한 후에 되는 상태이다.
      </li>
        <ul>
          <li>
            패시브 클로즈 호스트가 마지막 ACK 세그먼트를 수신하면 바로 CLOSED 상태로 전이되는 것과 반대로 <strong>일정 시간을 기다린 뒤</strong>에 CLOSED 상태로 전이한다.
          </li>
        </ul>
    </ul>
  <li>
    <strong>CLOSING 상태</strong>는 보통 <strong>동시에 연결을 종료</strong>하려 할 때 전이되는 상태이다.
  </li>
    <ul>
      <li>
        예를 들어 이미 받은 요청에 대한 ACK 세그먼트는 보냈지만, 자신의 FIN 세그먼트에 대한 ACK를 받지 못하는 경우가 해당한다.
      </li>
      <li>
        이 경우 ACK 세그먼트를 수신하면 각자 TIME-WAIT 상태로 접어든 뒤에 종료하게 된다.
      </li>
    </ul>
  <li>
    TCP의 다양한 상태는 맥OS나 리눅스에서 netstat을 통해 확인할 수 있다.
  </li>
</ul>

<h4>TIME-WAIT 상태가 필요한 이유</h4>
<ul>
  <li>
    가장 중요한 이유는 상대 호스트가 받았어야 할 마지막 ACK 세그먼트가 <strong>올바르게 전송되지 않았을 수 있기 때문</strong>이다.
  </li>
    <ul>
      <li>
        올바르게 전송하지 못하였다면 재전송을 해야하기 때문에 이를 기다린다.
      </li>
    </ul>
  <li>
    또 다른 이유는 한 연결을 종료하고 다른 연결을 수립하는 과정 사이에 대기 시간이 없다면 <strong>서로 다른 연결의 패킷들이 혼란을 야기</strong>할 수 있다.
  </li>
</ul>

<br>

<h2>2-4. UDP 데이터그램 구조</h2>
<ul>
  <li>
    <strong>UDP</strong>는 비연결형 통신을 수행하는 신뢰할 수 없는 프로토콜이며 연결 수립 및 해제, 재전송을 통한 오류 제어, 혼잡 제어, 흐름 제어 등을 하지 않으며 TCP처럼 상태도 유지하지 않아 <strong>스테이트리스(stateless)프로토콜</strong>의 일종이라고도 한다.
  </li>
  <li>
    UDP 데이터그램의 구조는 송신지 포트, 수신지 포트, 길이, 체크섬 네 가지로 단순하다.
  </li>
    <ul>
      <li>
        <strong>송신지 포트와 수신지 포트</strong>: 송수신지의 포트 번호가 담긴다.
      </li>
      <li>
        <strong>길이</strong>: 헤더를 포함한 UDP 데이터그램의 바이트가 담긴다.
      </li> 
      <li>
        <strong>체크섬</strong>: 데이터그램 전송 과정에서 오류가 발생했는지 검삭하기 위한 필드이다.
      </li>
        <ul>
          <li>
            <strong>데이터그램이 훼손</strong>되었는지를 나타내는 정보로 수신지까지 잘 도달했는지를 나타내는 신뢰성/비신뢰성과는 관련이 없다.
          </li>
        </ul>
    </ul>
  <li>
    UDP는 패킷을 빠르게 마구 던지는 형식이기 때문에 이 과정에서 패킷이 손실되거나 순서가 바뀔 수도 있다.
  </li>
</ul>

<br><br>

<h1>3. TCP의 오류, 흐름, 혼잡 제어</h1>
<ul>
  <li>
    TCP의 연결 수립과 연결 종료 사이의 데이터 송수신에서 이루어지는 오류 제어, 흐름 제어, 혼잡 제어에 대해 학습한다.
  </li>
</ul>

<br>

<h2>3-1. 오류 제어: 재전송 기법</h2>
<ul>
  <li>
    TCP는 오류 제어를 위해 잘못된 세그먼트를 재전송하는 <strong>재전송 기반 오류 제어</strong>를 활용한다.
  </li>
</ul>

<h3>3-1-1. 오류 검출과 재전송</h3>
<ul>
  <li>
    TCP 세그먼트에는 오류를 검출하는 체크섬 필드가 있으나 이는 세그먼트의 웨손 여부만 나타낼 뿐 신뢰성을 보장하지는 않는다.
  </li>
    <ul>
      <li>
        호스트는 값이 잘못되었다면 해당 패킷을 읽지 않고 폐기한다.
      </li>
    </ul>
  <li>
    TCP가 신뢰성을 제대로 보장하기 위해서는 <strong>송신 호스트</strong>가 송신한 세그먼트에 <strong>문제가 발생했음을 인지</strong>할 수 있어야 하고, 오류를 감지했자면 해당 세그먼트를 <strong>재전송</strong>할 수 있어야 한다.
  </li>
  <li>
    TCP가 오류를 검출하고 세그먼트를 재전송하는 상황은 크게 아래 두 가지가 있다.
  </li>
    <ol>
      <li>
        첫째, 중복된 ACK 세그먼트를 수신했을 때
      </li>
        <ul>
          <li>
            순차적으로 세그먼트를 보내고 그에 대한 ACK를 받은 뒤 다시 다음 순서 번호를 담은 세그먼트를 보내는 도중 수신 호스트에서 순서 번호 중에 <strong>누락</strong>이 있다면 <strong>수신 호스트는 다시 해당 패킷에 대한 ACK를 재전송</strong>한다.
          </li>
        </ul>
      <li>
        둘째, 타임아웃이 발생했을 때
      </li>
        <ul>
          <li>
            TCP 세그먼트를 송신하는 호스트는 모두 <strong>재전송 타이머(retransmission timer)</strong>라는 값을 유지한다.
          </li>
            <ul>
              <li>
                재전송 타이머의 카운트다운이 끝난 상황을 <strong>타임아웃(timeout)</strong>이라 한다.
              </li>
              <li>
                타임아웃이 발생할 때까지 ACK 세그먼트를 받지 못하면 상대 호스트에게 정상적으로 도착하지 않았다고 간주하여 세그먼트를 재전송한다.
              </li>
            </ul>
        </ul>
    </ol>
</ul>

<h4>RTT</h4>
<ul>
  <li>
    메시지를 전송한 뒤 그에 대한 답변을 답는 데까지 걸리는 시간을 <strong>RTT(Round Trip Time)</strong>라고 한다.
  </li>
  <li>
    RTT는 ping 명령어로 쉽게 조회할 수 있다.
  </li>
</ul>

<h3>3-1-2. ARQ: 재전송 기법</h3>
<ul>
  <li>
    수신 호스트의 답변(ACK)과 타임아웃 발생을 토대로 문제를 진단하고, 문제가 생긴 메시지를 재전송하는 방법을 <strong>ARQ(Automatic Repeat Request, 자동 재전송 요구)</strong>라고 한다.
  </li>
  <li>
    ARQ에는 대표적으로 세 가지 방법 <strong>Stop-and-Wait ARQ</strong>, <strong>Go-Back-N ARQ</strong>, <strong>Selective Repeat ARQ</strong>가 있다.
  </li>
</ul>

<h3>3-1-3. Stop-and-Wait ARQ</h3>
<ul>
  <li>
    <strong>Stop-and-Wait ARQ</strong>는 가장 간단한 방법으로 <strong>제대로 전달했음을 확인</strong>하기 전까지는 새로운 메시지를 보내지 않는 방식이다.
  </li>
  <li>
    오늘날 인터넷 환경에서는 자주 사용하는 방식은 아니지만 높은 신뢰성을 보장한다.
  </li>
  <li>
    하지만 송신 호스트와 수신 호스트 모두 한 번에 하나씩만 데이터를 주고받을 수 있기 때문에 <strong>네트워크 이용 효율</strong>이 낮아지고, 성능의 저하로 이어질 수 있다.
  </li>
</ul>

<h3>3-1-4. Go-Back-N ARQ</h3>
<ul>
  <li>
    Stop-and-Wait ARQ의 문제를 극복하기 위해서는 ACK 세그먼트가 도착하기 전에 여러 세그먼트를 보낼 수 있어야 한다. 이렇게 연속해서 메시지를 전송할 수 있는 기술을 <strong>파이프라이닝(pipelining)</strong>이라고 한다.
  </li>
    <ul>
      <li>
        오늘날 주로 쓰이는 Go-Back-N ARQ와 Selective Repeat ARQ가 파이프라이닝 기반으로 동작한다.
      </li>
    </ul>
  <li>
    Go-Back-N ARQ는 파이프라이닝 방식을 활용해 여러 세그먼트를 전송하고, 도중에 잘못 전송된 세그먼트가 발생할 경우 <strong>해당 세그먼트부터 다시 전송</strong>하는 방식이다.
  </li>
  <li>
    문제가 발생하는 경우 해당 세그먼크부터 다시 전송하기 때문에 'n번만의' 확인 응답이 아니라 <strong>'n번까지의'</strong> 확인 응답이라 볼 수 있다.
  </li>
    <ul>
      <li>
        이러한 점에서 Go-Back-N ARQ의 ACK 세그먼트를 <strong>누적 확인 응답(CACK; Cumulative Acknowledgment)</strong>이라고 한다.
      </li>
    </ul>
</ul>

<h4>빠른 재전송</h4>
<ul>
  <li>
    <strong>빠른 재전송(fast retransmit)</strong>이란 재전송 타이머가 만료되기 전이라도 <strong>세 번의 동일한 ACK 세그먼트</strong>가 수신되었다면 해당 세그먼트를 곧바로 재전송하는 기능이다.
  </li>
  <li>
    즉 빠른 재전송은 시간 낭비를 줄이며 빠르게 손실된 세그먼트를 재전송(retransmit)하여 성능을 높이는 기술이다.
  </li>
</ul>

<h3>3-1-5. Selective Repeat ARQ</h3>
<ul>
  <li>
    Selective Repeat ARQ는 <strong>선택적으로 재전송</strong>하는 방법이다.
  </li>
    <ul>
      <li>
        Go-Back-N ARQ와 달리 Selective Repeat ARQ는 모든 세그먼트를 재전송하지 않는다는 장점이 있다.
      </li>
      <li>
        Go-Back-N ARQ가 ACK 세그먼트 누적 확인 응답이라면, Selective Repeat ARQ의 ACK 세그먼트 <strong>개별 확인 응답(Selective Acknowledgment)</strong>이라 볼 수 있다.
      </li>
    </ul>
  <li>
    오늘날 대부분의 호스트는 TCP 통신에 Selective Repeat ARQ를 이용한다. 만약 불가하다면 그때 Go-Back-N ARQ를 사용한다.
  </li>
    <ul>
      <li>
        Selective Repeat ARQ 지원 여부는 TCP 세그먼트 헤더의 옵션 필드에 속한 <strong>SACK 허용(SACK-permitted) 필드</strong>를 통해할 수 있다.
      </li>
    </ul>
</ul>

<br>

<h2>3-2. 흐름 제어: 슬라이딩 윈도우</h2>
<ul>
  <li>
    TCP의 두 번째 핵심 기능은 <strong>흐름 제어(flow control)</strong>이다. 
  </li>
    <ul>
      <li>
        호스트가 <strong>한 번에 받아서 처리할 수 있는 세그먼트의 양</strong>에는 한계가 있기 때문에 파이프라이닝을 활용하는 Go-Back-N ARQ와 Selective Repeat ARQ가 정상적으로 동작하기 위해서는 흐름 제어를 고려해야 한다.
      </li>
    </ul>
  <li>
    <strong>수신 버퍼</strong>는 수신된 세그먼트가 애플리케이션 프로세스에 의해 읽히기 전에 임시로 저장되는 공간이다.
  </li>
    <ul>
      <li>
        송신 호스트가 흐름 제어를 고려하지 않고 수신 버퍼의 크기보다 많은 데이터를 전송하면 일부 세그먼트가 처리되지 못하는 문제가 발생한다. 이와 같이 버퍼(buffer)가 넘치는(overflow) 문제 상황을 <strong>버퍼 오버플로(buffer overflow)</strong>라고 한다.
      </li>
      <li>
        수신 버퍼가 있는 것과 같이 송신할 세그먼트가 저장되는 공간인 <strong>송신 버퍼</strong>도 존재한다.
      </li>
    </ul>
  <li>
    TCP 흐름 제어란 송신 호스트가 수신 호스트의 처리 속도를 고려하며 <strong>송수신 속도를 균일하게 유지</strong>하는 것을 의미한다.
  </li>
    <ul>
      <li>
        Stop-and-Wait ARQ는 연속적으로 통신하지 않기에 필요가 없지만 Go-Back-N ARQ와 Selective Repeat ARQ는 필요하다.
      </li>
    </ul>
  <li>
    오늘날 TCP에서는 흐름 제어로 <strong>슬라이딩 윈도우(sliding window)</strong>를 사용한다.
  </li>
    <ul>
      <li>
        <strong>윈도우(window)</strong>란 송신 호스트가 파이프라이닝 할 수 있는 최대량을 의미한다. 즉 확인 응답 없이 한 번에 전송 가능한 데이터 양이다.
      </li>
    </ul>
  <li>
    송신측 윈도우는 수신 호스트가 알려 주는 수신 측 윈도우를 토대로 알 수 있다.
  </li>
  <li>
    수신 호스트는 <strong>TCP 헤더(윈도우 필드)</strong>를 통해 송신 호스트에게 자신이 받아들이고자 하는 데이터의 양을 알리면 송신 호스트는 이 정보를 바탕으로 <strong>호스트의 처리 속도에 맞춰 균일한 속도로 세그먼트를 전송</strong>한다.
  </li>
  <li>
    파이프라이닝 과정에서 송수신 윈도우는 점차 오른쪽으로 미끄러지듯 움직이며 이러한 TCP의 흐름 제어를 <strong>슬라이딩 윈도우(sliding window)</strong>라고 한다.
  </li>
</ul>

<br>

<h2>3-3. 혼잡 제어</h2>
<ul>
  <li>
    혼잡 제어에서 <strong>혼잡(congestion)</strong>이란 많은 트래픽으로 인해 패킷의 처리 속도가 늦어지거나 유실될 우려가 있는 네트워크 상황을 의미한다.
  </li>
    <ul>
      <li>
        예를 들어 하나의 라우터만 존재한다면 그것만으로도 세그먼트를 받아 처리하는데 부하가 존재하며 이 부하는 또 다른 재전송으로 이러질 수 있어 악순환이 되는 문제가 발생할 수 있다.
      </li>
      <li>
        혼잡으로 인해 전송률이 크게 떨어지는 현상을 <strong>혼잡 붕괴(congestion collapse)</strong>라고 한다.
      </li>
    </ul>
  <li>
    TCP의 <strong>혼잡 제어(congestion control)</strong>는 이와 같은 혼잡을 제어한다.
  </li>
    <ul>
      <li>
        흐름 제어의 주체가 수신 호스트라면 혼잡 제어의 주체는 <strong>송신 호스트</strong>이다.
      </li>
      <li>
        송신 호스트는 네트워크 혼잡도를 판단하고 혼잡한 정보에 맞춰 <strong>유동적으로 전송량을 조절</strong>하며 역할을 한다.
      </li>
    </ul>
  <li>
    혼잡 데어를 이해하기 위해서는 <strong>혼잡 윈도우(congestion window)</strong>에 대해 알아야한다. 혼잡 윈도우란 <strong>혼잡 없이 전송할 수 있을 법한 데이터의 양</strong>이다.
  </li>
  <li>
    수신 윈도우는 수신 호스트가 송신 호스트에게 알려주지만 혼잡 윈도우의 크기는 송신 호스트가 직접 계산해야 한다.
  </li>
    <ul>
      <li>
        혼잡 윈도우는 송신자가 자체적으로 계산해야하기 때문에 TCP 헤더에 포함되지 않는다.
      </li>
    </ul>
  <li>
    <strong>혼잡 윈도우 크기</strong>는 혼잡 제어 알고리즘을 통해 결정할 수 있으며 혼잡 제어를 수행하는 일련의 방법을 <strong>혼잡 제어 알고리즘(congestion control algorithm)</strong>이라 한다.
  </li>
  <li>
    가장 기본적인 혼잡 제어 알고리즘으로는 <strong>AIMD(Additive Increase/Multiplicative Decrease)</strong>가 있으며 아래의 과정을 반복한다.
  </li>
    <ul>
      <li>
        혼잡이 감지되지 않는다면 <strong>혼잡 윈도우</strong>를 RTT(Round Trip Time)마다 <strong>1씩 선형적으로 증가</strong>시킨다.
      </li>
      <li>
        혼잡이 감지되면 혼잡 윈도우를 절반으로 떨어뜨린다.
      </li>
    </ul>
  <li>
    AIMD는 기본적인 알고리즘이며 더 정교한 알고리즘으로 <strong>느린 시작</strong>, <strong>혼잡 회피</strong>, <strong>빠른 회복</strong> 세 가지가 있다.
  </li>
</ul>

<h4>a. 느린 시작 알고리즘</h4>
<ul>
  <li>
    <strong>느린 시작(slow start) 알고리즘</strong>은 혼잡 윈도우를 <strong>1부터 시작</strong>해 문제없이 수신된 <strong>ACK 세그먼트</strong> 하나당 1씩 증가하는 방식이다.
  </li>
  <li>
    결과적으로 혼잡 윈도우는 <strong>RTT마다 2배씩 지수적으로 증가</strong>하게 되며 AIMD보다 더 빠르게 혼잡 윈도우가 증가한다.
  </li>
  <li>
    지수적으로 증가하면 기하급수적으로 혼잡 윈도우가 커질 수 있어 <strong>느린 시작 임계치(slow start threshold)</strong>라는 값을 사용한다.
  </li>
  <li>
    혼잡 윈도우가 느린 시작 임계치 이상이 되거나 타임아웃이 발생하거나, 세 번의 중복된 ACK 세그먼트가 발생하면 다음 세 가지 중 하나의 방법을 선택한다.
  </li>
    <ul>
      <li>
        <strong>타임아웃 발생</strong> &rarr; 혼잡 윈도우 값을 1로, 느린 시작 임계치를 혼잡이 감지되었을 시점의 <strong>혼잡 윈도우 값의 절반</strong>으로 초기화한 뒤 느린 시작을 재개한다.
      </li>
      <li>
        <strong>혼잡 윈도우 >= 느린 시작 임계치</strong> &rarr; 느린 시작을 종료하고, 혼잡 윈도우를 절반으로 초기화한 뒤 혼잡 회피를 수행한다.
      </li>
      <li>
        <strong>세 번의 중복 ACK 발생</strong> &rarr; (빠른 재전송 후) 빠른 회북 수행.
      </li>
    </ul>
</ul>

<h4>b. 혼잡 회피 알고리즘</h4>
<ul>
  <li>
    <strong>혼잡 회피(congestion avoidance) 알고리즘</strong>은 RTT마다 혼잡 윈도우를 <strong>1MSS(Maximum Segment Size)</strong>씩 증가시키는 알고리즘이다.  
  </li>
  <li>
    혼잡 회피 알고리즘은 <strong>선형적</strong>으로 윈도우의 크기를 증가시킨다. 
  </li>
    <ul>
      <li>
        느린 시작 임계치를 넘어선 시점부터 혼잡이 발생할 우려가 있어 조심해서 혼잡 윈도우를 증가시키는 방식으로 볼 수 있다.
      </li>
    </ul>
  <li>
    혼잡 회피 도중 <strong>타임아웃</strong>이 발생하면 <strong>윈도우 값은 1</strong>로, 느린 시작 임계치는 혼잡이 감지된 시점의 혼잡 윈도우 값의 <strong>절반</strong>으로 초기화 한 뒤 다시 느린 시작을 수행한다.
  </li>
  <li>
    혼잡 회피 중에 <strong>세 번의 중복 ACK 세그먼트</strong>가 발생하면 혼잡 윈도우 값과 느린 시작 임계치를 대략 <strong>절반</strong>으로 떨어뜨린 뒤 <strong>빠른 회복 알고리즘</strong>을 수행한다.
  </li>
  <li>
    두 경우 모두 타임아웃이 발생한 세그먼트나 세 번의 중복 ACK 세그먼트가 발생한 세크먼트는 <strong>재전송</strong>한다.
  </li>
</ul>

<h4>c. 빠른 회복 알고리즘</h4>
<ul>
  <li>
    세 번의 중복된 ACK 세그먼트를 수신하면 빠른 재전송과 함께 빠른 회복 알고리즘이 수행된다.
  </li>
  <li>
    빠른 회복(fast recovery) 알고리즘은 세 번의 중복 ACK 세그먼트를 수신했을 때 <strong>느린 시작은 건너뛰고 혼잡 회피</strong>를 수행하는 알고리즘이다.
  </li>
    <ul>
      <li>
        말 그대로 빠르게 전송률을 회복하기 위한 알고리즘이다.
      </li>
      <li>
        빠른 회복 도중이라도 <strong>타임아웃</strong>이 발생하면 혼잡 윈도우 크기는 1로, 느린 시작 임계치는 혼잡이 감지된 시점의 절반으로 떨어뜨린 후 <strong>다시 느린 시작</strong>을 수행한다.
      </li>
    </ul>
  <li>
    중복된 ACK 세그먼트가 수신되면 <strong>빠른 회복</strong>과 <strong>함께 빠른 재전송</strong>이 수행된다는 점에서 이들을 묶어 <strong>혼잡 제어 방식의 일종</strong>으로 보기도 한다.
  </li>
</ul>

<h4>수신 윈도웅, 혼잡 윈도우</h4>
<ul>
  <li>
    수신 윈도우는 RWND(Receiver WINDow), 혼잡 윈도우는 CWND(Congestion WINDow), 느린 시작 입계치는 SSTHRESH(Slow Start THRESHold)라 부르기도 한다.
  </li>
  <li>
    각 값들은 일반적으로 운영체제에서 <strong>TCP의 상태를 관리하는 상태 변수</strong>의 형태로 존재한다.
  </li>
</ul>

<h4>ECN: 명시적 혼잡 알림</h4>
<ul>
  <li>
    
  </li>
</ul>