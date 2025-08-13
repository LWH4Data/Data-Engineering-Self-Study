<h1>1. 소개</h1>
<ul>
  <li>
    소프트웨어 인프라는 <strong>수평적 확장</strong>이 용이함.<br>→ Nginx는 <strong>HTTP, TCP, UDP 프로토콜</strong>을 활용하여 부하분산을 한다. (수평적 확장).
  </li>
    <ul>
      <li>
        <strong>수평적 확장 (horizontal scaling)</strong>: 증가하는 부하에 대해 동일한 시스템을 추가 투입하는 방법.
      </li>
    </ul>
  <li>
    웹 서비스 아키텍처 중에는 상태 정보를 메모리 혹은 공용 데이터베이스에 저장하는 <strong>스테이스리스(stateless)</strong> 애플리케이션 계층을 채택한다.<br>→ 단, 세션에 저장되는 값이 많으면 <strong>네트워크 부하가 증가</strong>한다.<br>→ 이 경우 세션을 <strong>로컬에 저장</strong>하는 방법을 활용할 수 있다.<br>→ 이로인해 <strong>지능적 부하분산</strong>이 필요해진다.<br>→ Nginx는 <strong>쿠키값</strong> 혹은 <strong>라우팅을 추적</strong>하는 솔루션을 제공한다.<br>→ 이번 장에서는 Nginx를 통해 <strong>부하를 분산</strong>하여 <strong>세션을 유지</strong>하는 법을 배운다.
  </li>
  <li>
    애플리케이션을 운영할 때 <strong>업스트림 서버의 상태를 감지</strong>하는 것이 중요하다.
  </li>
    <ul>
      <li>
        업스트림 서버란 프록시 서버 뒤의 실제 구동되는 서버를 의미한다.
      </li>
      <li>
        업스트림 서버에 문제가 있다면 주로 timeout 문제가 생기며 애플리케이션이 구동하지 못한다.
      </li>
    </ul>
  <li>
    Nginx에서는 업스트림 서버 확인을 위해 <strong>두 가지 서비스를 제공</strong>한다.
  </li>
    <ul>
      <li>
        <strong>passive</strong>
      </li>
        <ul>
          <li>
            오픈 소스 Nginx 제공.
          </li>
          <li>
            유저의 <strong>요청이 들어온 시점</strong>에 업스트림 서버의 상태를 확인한다.
          </li>
          <li>
            <strong>서버의 부하</strong>가 적은 방식이다.
          </li>
        </ul>
      <li>
        <strong>active</strong>
      </li>
        <ul>
          <li>
            Nginx 플러스에서 제공
          </li>
          <li>
            유저의 요청과 상관없이 로드 밸런서(e.g. Nginx)가 <strong>주기적으로</strong> 업스트림 서버의 상태를 확인한다.
          </li>
          <li>
            <strong>사용자 요청이 들어오기 전</strong>에 업스트림 서버의 상태를 확인할 때 필요가 있을 때 사용한다.
          </li>
        </ul>
    </ul>
</ul>

<br><br>

<h1>2. HTTP 부하분산</h1>
<ul>
  <li>
    두 대 이상의 HTTP 서버로 부하 분산을 구현한다.
  </li>
  <li>
    Nginx의 <strong>upstream 블록</strong>과 <strong>http 모듈</strong>을 활용한다.
  </li>
  <li>
    <strong>HTTP upstream 모듈</strong>을 통해 HTTP 프로토콜 요청에 대한 부하분산 방식 정의<br>→ 부하분산을 위한 <strong>목적지 풀(pool, 여러대의 서버를 지칭)</strong>은 유닉스 소켓, IP 주소, 서버 호스트네임 혹은 이들의 조합으로 주어진다.<br>→ 각 업스트림 대상은 <strong>server 지시자</strong>로 설정한다.<br>→ <strong>매개변수</strong>를 지정할 수 있으며 플러스는 고급 매개변수 또한 제공한다.
  </li>
</ul>

```Nginx
# upstream 모듈을 통해 업스트림 서버 지정.
upstream backend {

      # 부하가 분산될 첫 번째 서버로 weight=1이다.
      # weight의 default 값이 1이기에 생략 가능.
      server 10.10.12.45:80           weight=1; # weight은 매개변수

      # 부하가 분산될 두 번째 서버로 weight=2이며 따라서 첫 번째 서버보다 두 배 
      # 많은 요청을 받는다.
      server app.example.com:80       weight=2;

      # 위의 두 대의 서버 모두 연결이 불가한 경우 backup으로 지정한 서버에 연결된다.
      server spare.example.com:80     backup;
}
server {
      location / {
          proxy_pass http://backend;
    }
}
```

<br><br>

<h1>3. TCP 부하분산</h1>
<ul>
  <li>
    두 대 이상의 부하를 TCP 서버로 분산하는 것을 구현한다.
  </li>
  <li>
    Nginx의 upstream블록과 stream 모듈을 활용한다.
  </li>
  <li>
    Nginx의 기본 설정 파일 conf.d는 http 블록에 포함되기에 TCP를 활용하기 위해서는 stream.conf.d라는 별도의 폴더를 생성하고 저장하는 편이 좋다.
  </li>
    <ul>
      <li>
        nginx.conf 파일의 stream 블록에 생성한 stream.conf.d/*.conf;를  추가하여 추적하게 한다.
      </li>
    </ul>
</ul>

```nginx
stream {

      # 3306 포트로 TCP 요청을 받아 읽기 전용 복제본(read replica) 두 대로 구성된 
      # MySQL 서버로 부하를 분산한다.
      upstream mysql_read {
              server read1.example.com:3306     weight=5;
              server read2.example.com:3306;
              server 10.10.12.34:3306           backup;
      }
      server {
              listen 3306;
              proxy_pass mysql_read;
      }
}
```

<ul>
  <li>
    Nginx에서 TCP 부하분산은 <strong>stream 모듈</strong>을 활용한다.
  </li>
    <ul>
      <li>
        stream 모듈의 기본 형식(부하분산 포함)은 <strong>http와 유사</strong>하다.
      </li>
    </ul>
  <li>
    <strong>http</strong>는 OSI 7계층 중 7계층인 <strong>애플리케이션 계층(application layer)</strong>을, <strong>stream</strong>은 4계층인 <strong>전송 계층(transport layer)</strong>에서 동작한다. 
  </li>
    <ul>
      <li>
        동작하는 계층은 다르지만 서로 <strong>호환이 가능</strong>하다. 단, <strong>http는 HTTP 프로토콜</strong>에, <strong>stream은 패킷 전달과 부하분산</strong>에 중점을 둔다고 이해하면 된다.
      </li>
    </ul>
  <li>
    stream을 이용할 경우 TCP 연결과 관련된 <strong>여러 프록시 속성</strong>들(SSL/TLS 인증서 제한, 타임아웃, 킵얼라이브 시간 등)을 설정할 수 있다. 이중 일부 옵션은 Nginx 변수를 값으로 사용할 수 있다.
  </li>
    <ul>
      <li>
        Nginx 플러스의 TCP 고급 기능들에 대해서는 2.10 능동적 헬스체크에서 소개한다.
      </li>
    </ul>
</ul>

<br><br>

<h1>4. UDP 부하분산</h1>

```nginx
# UDP 프로토콜을 사용해 NTP(네트워크 타임 프로토콜, Network Time Protocol) 서버 두 대로 전달.
stream {
      upstream ntp {
            server ntp1.example.com:123 weight=2;
            server ntp2.example.com:123;
      }

      server {
              # udp: 부하분산 설정 매개변수.
              # reuseport: 부하분산 과정에서 클라이언트와 서버가 패킷을 여러번 주고 받는 경우 설정.
              listen 123 udp reuseport; 
              proxy_pass ntp;
      }
}
```

<ul>
  <li>
    UDP 부하분산이 적용된 대표적인 서비스들은 OpenVPN, Voice Internet Protocol, 가상 데스크톱 환경, Datagram Transport Layer Security가 있다.
  </li>
  <li>
    DNS를 통해 여러 A 레코드 주소나 SRV 레코드를 갖고 있으면 되지 않나?<br> → UDP는 DNS, NTP, QUIC, HTTP/3, VoIP 등 네트워크 기반 시스템에서 사용하는 많은 서비스의 근간<br> → Nginx의 UDP 부하분산<br> → <strong>DNS의 부하 분산</strong>의 기능을 한다.
  </li>
  <li>
    UDP 부하분산은 TCP와 마찬가지로 <strong>stream 모듈</strong>을 사용하며 형식도 유사하다.
  </li>
    <ul>
      <li>
        차이점은 <strong>UDP</strong>는 <strong>listen 지시자</strong>를 통해 UDP 데이터그램을 처리할 <strong>소켓을 지정</strong>한다.
      </li>
      <li>
        또한 TCP에는 없는 부하분산 매개변수들이 존재한다.
      </li>
        <ul>
          <li>
            <strong>proxy_response</strong>
          </li>
            <ul>
              <li>업스트림 서버로부터 수신할 것으로 예상되는 <strong>응답의 크기</strong>를 지정한다. 
              </li>
              <li>
                지정값이 없다면 proxy_timeout의 제한값으로 설정되며 해당 제한값에 도달할 때까지 <strong>무제한 응답처리</strong>를 한다.
              </li>
            </ul>
          <li>
            <strong>proxy_timeout</strong>
          </li>
            <ul>
              <li>
                연결을 닫기 전까지 목적지 서버로의 읽기, 쓰기, 작업 완료를 <strong>기다리는 시간을 지정</strong>한다.
              </li>
            </ul>
          </li>
          <li>
            <strong>reuseport</strong>
          </li>
            <ul>
              <li>
                Nginx가 <strong>워커 프로세스별</strong>로 개별 수신 소켓을 만들어 사용한다. 
              </li>
              <li>
                커널은 Nginx로 보내는 연결들을 <strong>워커 프로세스 단위로 분산</strong> → 클라이언트와 서버가 주고받는 여러 패킷을 <strong>동시에 처리</strong>.
              </li>
              <li>
                리눅스 커널 3.9, BSD, 프리 BSD 12 이상 버전에서만 가능하다.
              </li>
            </ul>
          </li>
        </ul>
    </ul>
</ul>

<br><br>

<h1>5. 부하분산 알고리즘</h1>
