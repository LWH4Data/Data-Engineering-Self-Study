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
        <strong>0 ~ 1023번</strong>까지의 포트 번호는 <strong>잘 알려진 포트(well known port)<strong> 혹은 <strong>시스템 포트(system port)</strong>로 범용적으로 사용되는 애플리케이션 프로토콜의 포트 번호를 의미한다. (p196).
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
    
  </li>
</ul>