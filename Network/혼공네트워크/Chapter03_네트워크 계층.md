<h1>1. LAN을 넘어서는 네트워크 계층</h1>
<ul>
  <li>
    네트워크 계층에서는 <strong>IP 주소</strong>를 이용해 송수신지 대상을 지정하고, 다른 네트워크에 이르는 경로를 결정하는 <strong>라우팅</strong>을 통해 다른 네트워크와 통신한다.
  </li>
</ul>

<br>

<h2>1-1. 데이터 링크 계층의 한계</h2>
<ul>
  <li>
    물리 계층과 데이터 계층만으로 LAN을 넘어 통신을 하는 것은 다음 두 가지 이유로 어렵다.
  </li>
    <ol>
      <li>
        첫째, 물리 계층과 데이터 링크 계층만으로는 다른 네트워크까지의 도달 <strong>경로</strong>를 파악하기 어렵다.
      </li>
        <ul>
          <li>
            LAN에 속한 호스트끼리만 통신하지 않고 네트워크에서는 패킷들이 <strong>수많은 네트워크 장비</strong>를 거쳐 <strong>다양한 경로</strong>를 통해 이동한다.
          </li>
          <li>
            패킷이 이동할 <strong>최적의 경로</strong>를 결정하는 것을 <strong>라우팅(routing)</strong>이라 한다.
          </li>
            <ul>
              <li>
                물리 계층과 데이터 링크 계층의 장비로는 라우팅을 수행할 수 없다.
              </li>
            </ul>
          <li>
            라우팅을 수행하는 대표적인 장비로는 <strong>라우터(router)</strong>가 있다.
          </li>
        </ul>
      <li>
        둘째, MAC 주소만으로는 모든 네트워크에 속한 <strong>호스트의 위치</strong>를 특정하기 어렵다.
      </li>
        <ul>
          <li>
            모든 호스트가 모든 네트워크에 속한 모든 호스트의 MAC 주소를 서로 알고 있기 어려우며 따라서 MAC 주소만으로 세상의 모든 호스트를 특정할 수 없다.
          </li>
            <ul>
              <li>
                네트워크를 통해 정보를 주고받는 과정은 택배의 송수신과 같고, MAC 주소는 개인 정보로 볼 수 있다.
              </li>
            </ul>
          <li>
            수신인 역할을 하는 것이 MAC이라면 <strong>수신지</strong>의 역할을 하는 것이 <strong>IP 주소</strong>이다.
          </li>
            <ul>
              <li>
                네트워크에서도 <strong>MAC 주소와 IP 주소</strong>를 함께 사용하고 기본적으로 <strong>IP 주소를 우선</strong>으로 활용한다.
              </li>
            </ul>
          <li>
            MAC 주소를 물리 주소라고 보르는 것처럼 IP 주소는 <strong>논리 주소</strong>라고도 부른다.
          </li>
            <ul>
              <li>
                MAC 주소는 일반적으로 NIC마다 할당되는 고정된 주소이지만 IP 주소는 <strong>호스트에 직접 할당</strong>이 가능하다.
              </li>
              <li>
                IP는 <strong>DHCP(Dynamic Host Configuration Protocol)</strong>라는 특정 프로토콜을 통해 자동으로 할당받거나 사용자가 직접 할당할 수 있다.
              </li>
              <li>
                한 호스트가 <strong>복수의 IP 주소</strong>를 갖는 것도 가능하다.
              </li>
            </ul>
        </ul>
    </ol>
  <li>
    즉, 물리 계층과 데이터 링크 계층만으로는 네트워크 간의 통신이 어려우며 이 때문에 <strong>네트워크 계층</strong>이 다른 네트워크와의 통신을 가능하도록 한다.
  </li>
    <ul>
      <li>
        IP 주소를 이용해 수신지 수소를 설정.
      </li>
      <li>
        해당 수신지까지의 최적의 경로를 결정하는 라우팅을 활용.
      </li>
    </ul>
</ul>

<br><br>

<h2>1-2. 인터넷 프로토콜</h2>
<ul>
  <li>
    네트워크 계층에서 가장 핵심적인 프로토콜을 하나 꼽으면 IPv4와 IPv6 두 가지 버전이 있는 <strong>인터넷 프로토콜(IP; Internet Protocol)</strong>이다.
  </li>
    <ul>
      <li>
        주로 IP 주소를 이야기할 대에는 IPv4를 의미한다.
      </li>
    </ul>
</ul>

<h3>1-2-1. IP 주소 형태</h3>
<ul>
  <li>
    IP 주소는 <strong>4바이트(32비트)</strong>로 주소를 표현한다.
  </li>
    <ul>
      <li>
        각 숫자당 <strong>8비트로(1바이트)</strong>로 표현되기에 <strong>0~255 범위</strong> 안에 있는 <strong>네 개의 10진수</strong>로 표기된다.
      </li>
      <li>
        각 10진수는 <strong>점(.)</strong>으로 구분되는데 점으로 구분된 각 8비트(0~255 범위의 10진수)를 <strong>옥텟(octet)</strong>이라 한다.
      </li>
      <li>
        예를 들면 192.168.1.1인 IPv4가 있다.
      </li>
    </ul>
</ul>

<h3>1-2-2. IP의 기능</h3>
<ul>
  <li>
    IP의 기능은 다양하지만 대표적인 기능에는 크게 <strong>IP 주소 지정</strong>과 <strong>IP 단편화</strong>가 있다. (두 기능 모두 RFC 791에 명시되어 있다).
  </li>
    <ul>
      <li>
        IP 주소 지정(IP addressing)은 IP 주소를 바탕으로 <strong>송수신 대상을 지정</strong>하는 것을 의미한다.
      </li>
      <li>
        IP 단편화(IP fragmmentation)는 전송하고자 하는 패킷의 크기가 MTU라는 최대 전송 단위보다 클 경우, 이를 MTU 크기 이하의 <strong>복수의 패킷으로 나누는 것</strong>을 의미한다.
      </li>
        <ul>
          <li>
            MTU(Maximum Transmission Unit)란 한 번에 전송 가능한 IP 패킷의 최대 크기를 의미한다.
          </li>
          <li>
            MTU 크기는 일반적으로 1500바이트이고, MTU 크기 이하로 나누어진 패킷은 수신지에 도착하여 다시 재조합된다.
          </li>
        </ul>
    </ul>
</ul>

<h4>RFC 문서</h4>
<ul>
  <li>
    RFC(Request for Comments) 문서는 네트워크/인터넷 관련 신기술 제안, 의견 등을 남긴 문서이다.
  </li>
  <li>
    영향력이 있는 RFC 문서에는 번호가 부여되며 <strong>RFC + RFC 번호</strong>는 폐지되거나 수정되지 않아 검색해서 찾기도 용이하다.
  </li>
</ul>

<h3>1-2-3. IPv4</h3>
<ul>
  <li>
    IPv4 패킷은 프레임 페이로드로 <strong>데이터 필드</strong>에 명시된다.
  </li>
  <li>
    IPv4 패킷은 생각하게 복잡하게 생겼는데 핵심이 되는 부분은 <strong>식별자</strong>, <strong>플래그</strong>, <strong>단편화 오프셋</strong>, <strong>TTL</strong>, <strong>프로토콜</strong>, <strong>송신지 IP 주소</strong>, <strong>수신지 IP 주소</strong> 총 7개이다. (p134).
  </li>
    <ol>
      <li>
        식별자
      </li>
        <ul>
          <li>
            식별자(identifier)는 <strong>패킷에 할당된 번호</strong>이다.
          </li>
          <li>
            쪼개어져서 전달되는 IPv4 패킷들을 <strong>수신지에서 재조합</strong>할 때 어떤 메시지에서부터 쪼개졌는지 인식하기 위해 사용한다.
          </li>
        </ul>
      <li>
        플래그
      </li>
        <ul>
          <li>
            플래그(flag)는 총 세 개의 비트로 구성된 필드로 <strong>첫 번째 비트</strong>는 예약된 비트로 <strong>항상 0</strong>이며 현재 사용되지 않는다.
          </li>
            <ul>
              <li>
                그 중하나는 <strong>DF(Don't Fragment)</strong> 비트로 이 비트가 1인 경우 <strong>IP 단편화</strong>를 수행하지 않았음을 의미한다.
              </li>
              <li>
                다른 한 비트는 <strong>MF(More Fragment)</strong>로 단편화된 패킷이 <strong>더 있는지</strong>를 나타낸다.
              </li>
                <ul>
                  <li>
                    0인 경우 마지막 패킷임을 의미하며, 1인 경우 아직 쪼개진 패킷이 남아있음을 의미한다.
                  </li>
                </ul>
            </ul>
        </ul>
      <li>
        단편화 오프셋
      </li>
        <ul>
          <li>
            <strong>단편화 오프셋(fragment offset)</strong>은 패킷이 단편화되기 전에 초기 데이터에서 <strong>몇 번째로 떨어진 패킷</strong>인지를 나타낸다.
          </li>
          <li>
            단편화되어 전송되는 패킷들이 순서대로 도착하지 않을 수 있어 재조립할 때 활용한다.
          </li>
        </ul>
      <li>
        TTL
      </li>
        <ul>
          <li>
            TTL은 Time To Live로 <strong>패킷의 수명</strong>을 의미한다.
          </li>
          <li>
            호스트끼리 통신할 때 여러 라우터를 거칠 수 있으며 <strong>하나의 라우터</strong>를 거칠 때마다 <strong>TTL에서 1을 차감</strong>한다.
          </li>
            <ul>
              <li>
                TTL 값이 0으로 떨어진 패킷은 폐기한다.
              </li>
              <li>
                패킷이 폐기되면 패킷을 송신한 호스트에게 <strong>시간 초과(Time Exceeded)</strong> 메시지가 전송되며 이를 알려주는 프로토콜은 ICMP이다.
              </li>
            </ul>
          <li>
            패킷이 호스트 또는 라우터에 한 번 전달되는 것을 <strong>홉(hop)</strong>이라 한다.
          </li>
            <ul>
              <li>
                즉 TTL이 라우터를 거쳐 TTL이 1감소하는 것은 hop마다 감소한다고 볼 수도 있다.
              </li>
            </ul>
          <li>
            TTL은 <strong>무의미한 패킷</strong>이 네트워크상에 지속적으로 남아있는 것을 방지한다.
          </li>
        </ul>
      <li>
        프로토콜
      </li>
        <ul>
          <li>
            IP 패킷의 프로토콜은 <strong>상위 계층의 프로토콜</strong>이 무엇인지 나타내는 필드이다.
          </li>
            <ul>
              <li>
                예를 들어 TCP는 6번, UDP는 17번이다.
              </li>
            </ul>
        </ul>
      <li>
        송신지 IP 주소와 수신지 IP 주소 
      </li>
        <ul>
          <li>
            송신지 IP 주소(Source IP Address)와 수신지 IP 주소(Destination IP Address)에서는 이름 그대로 각 주소를 알 수 있다.
          </li>
        </ul>
    </ol>
</ul>

<h3>1-2-4. IPv6</h3>
<ul>
  <li>
    할당 가능한 IPv4 주소의 수는 2의 32승으로 43억 개이지만 전 세계 사람들이 다수의 기기를 사용한다면 쉽게 <strong>고갈</strong>될 수 있으며 이러한 이유로 IPv6가 등장한다.
  </li>
  <li>
    IPv6는 <strong>16바이트(128비트)</strong>로 주소를 표현할 수 있으며 이론상으로 <strong>2의 128승개의 주소</strong>를 할당가능하다.
  </li>
    <ul>
      <li>
        <strong>콜론(:)</strong>으로 구분된 <strong>8개의 그룹</strong>의 <strong>16진수</strong>로 표기된다.
      </li>
    </ul>
  <li>
    IPv6 패킷의 구조는 IPv4의 구조보다 단순하며 주요 필드로는 다음 <strong>헤더</strong>, <strong>홉 제한</strong>, <strong>송신지 IP 주소</strong>, <strong>수신지 IP 주소</strong> 네 개가 있다. (p137).
  </li>
    <ol>
      <li>
        다음 헤더
      </li>
        <ul>
          <li>
            다음 헤더(next header) 필든는 <strong>상위 계층의 프로토콜</strong>을 가리키거나 <strong>확장 헤더</strong>를 가리킨다.
          </li>
            <ul>
              <li>
                IPv6에는 기본 헤더와 <strong>확장 헤더(extension header)</strong>가 있으며 <strong>추가적인 헤더 정보</strong>가 필요할 경우 기본 헤더에 확장 헤더를 추가하여 헤더를 갖는다.
              </li>
              <li>
                확장 헤더는 기본 헤더와 페이로드 데이터 사이에 위치한다.
              </li>
              <li>
                또한 확장 헤더는 하나가 아니라 꼬리를 물듯 <strong>여러 개</strong>를 가질 수 있다.
              </li>
            </ul>
          <li>
            확장 헤더의 종류는 다양하며 상황에 맞는 다양한 정보를 운반할 수 있다. 대표적인 헤더들은 다음과 같다.
          </li>
            <ul>
              <li>
                홉 간 옵션(Hop-by-Hop Options): 수신지에서만 패킷을 검사하도록하는 수신지 옵션(Destination Options).
              </li>
              <li>
                라우팅(Routing): 라우팅 관련 정보를 운반하는 라우팅
              </li>
              <li>
                단편화를 위한 단편(Fragment)
              </li>
              <li>
                암호화와 인증을 위한 ESP(Encapsulating), AH(Authentication Header)
              </li>
            </ul>
        </ul>
      <li>
        홉 제한
      </li>
        <ul>
          <li>
            홉 제한(hop limit) 필드는 IPv4 패킷의 TTL 필드와 비슷하게 <strong>패킷의 수명</strong>을 나타내는 필드이다.
          </li>
        </ul>
      <li>
        송신지 IP 주소와 수신지 IP 주소
      </li>
        <ul>
          <li>
            송신지 주소(source address)와 수신지 주소(destination address)를 통해 IPv6 주소 지정이 가능하다.
          </li>
        </ul>
    </ol>
  <li>
    IPv4 헤더 길이는 가변적이나 IPv6 기본 헤더는 <strong>40바이트로 고정적</strong>이다.
  </li>
</ul>

<h4>IPv6의 단편화</h4>
<ul>
  <li>
    IPv6는 IPv4와 달리 기본 헤더에 단편화 관련 필드가 없고 <strong>단편화 확장 헤더</strong>를 통해 단편화가 이루어진다.
  </li>
  <li>
    단편화 확장 헤더에도 다음 헤더가 있다.
  </li>
    <ul>
      <li>
        기본 헤더처럼 단편화 확장 헤더에도 다음 헤더 필드가 있는 것은 <strong>또 다른 확장 헤더</strong> 또는 <strong>상위 프로토콜</strong>을 가리키기 위함이다.
      </li>
    </ul>
  <li>
    예약됨(reserved)과 예약(res) 필드는 0으로 설정되어 사용하지 않는다.
  </li>
  <li>
    단편화 오프셋(fragment offset), M 플래그(M flag), 식별자(identification) 필드는 각각 IPv4의 단편화 오프셋, MF 플래그, 식별자 필드와 같은 역할을 수행한다.
  </li>
    <ul>
      <li>
        역할은 마찬가지로 단편화 오프셋은 현재 단편화된 위치를 나타낸다.
      </li>
      <li>
        M 플래그는 1일 경우 더 많은 단편화된 패킷이 남아있음을, 0인 경우 마지막 패킷임을 나타낸다.
      </li>
      <li>
        식별자는 동일한 메시지에서부터 단편화된 패킷임을 식별하기 위해 사용된다.
      </li>
    </ul>
</ul>

<br>

<h2>1-3. ARP</h2>
<ul>
  <li>
    기본적으로 상대 호스트의 IP 주소는 알지만, MAC 주소는 알지 못하는 상황이 있을 수 있으며 이럴 때 ARP를 사용한다.
  </li>
  <li>
    <strong>ARP(Address Resolution Protocol)</strong>는 <strong>IP 주소를 통해 MAC 주소</strong>를 알아내는 프로토콜로 동일 네트워크 내에 있는 소수신 대상의 IP 주소를 통해 MAC 주소를 알아낼 수 있다.
  </li>
  <li>
    ARP의 동작 과정은 다음과 같다.
  </li>
    <ol>
      <li>
        ARP 요청
      </li>
        <ul>
          <li>
            발신 호스트는 우선 네트워크 내의 모든 호스트에게 브로드캐스트 메시지를 보내며 이 메시지가 <strong>ARP 요청(ARP Request)이라는 패킷</strong>이다.
          </li>
        </ul>
      <li>
        ARP 응답
      </li>
        <ul>
          <li>
            모든 호스트가 ARP 요청 메시지를 받지만, 수신 대상 호스트를 제외한 나머지 호스트들은 자신의 IP가 아니기 때문에 이를 무시한다.
          </li>
          <li>
            수신 대상 호스트는 자신의 MAC 주소를 담은 메시지를 발신 호스트에게 전송하며 이 유니캐스트 메시지는 <strong>ARP 응답(ARP Reply)이라는 ARP 패킷</strong>이다.
          </li>
        </ul>
    </ol>
</ul>

<h4>ARP 패캇</h4>
<ul>
  <li>
    ARP 요청과 응답 과정에서는 ARP 패킷이 전송된다. (구조는 p141).
  </li>
    <ul>
      <li>
        ARP 패킷의 구조 중 <strong>오퍼레이션 코드(Opcode; Operation Code)</strong>는 <strong>ARP 패킷 유형</strong>을 나타낸다. ARP 요청이라면 1, ARP 응답이라면 2로 설정된다.
      </li>
      <li>
        송신지 하드웨어 주소(Sender Hardware Address)와 수신지 하드웨어 주소(Target Hardware Address)를 활용한다.
      </li>
        <ul>
          <li>
            <strong>이더넷 프레임</strong>의 수신지 MAC 주소에는 <strong>브로드캐스트</strong> 메시지임을 나타내는 ff:ff:ff:ff:ff:ff가 명시된다.
          </li>
            <ul>
              <li>
                이는 MAC 주소를 모르니까 일단 브로드캐스트로 보냄을 의미한다.
              </li>
            </ul>
          <li>
            ARP 요청 패킷의 수신지 하드웨어 주소에는 00:00:00:00:00:00이 명시된다.
          </li>
            <ul>
              <li>
                이는 브로드캐스트로 받은 수신지가 ARP 패킷의 IP가 자신과 일치하면 그 안의 MAC 주소를 자신의 주소로 채우기 위함이다. 그후 다시 ARP 응답을 요청자에게 보낸다.
              </li>
            </ul>
        </ul>
      <li>
        ARP 테이블 갱신
      </li>
        <ul>
          <li>
            ARP를 활용할 수 있는 모든 호스트는 <strong>ARP 테이블(ARP Table)</strong>이라는 정보를 유지한다.
          </li>
          <li>
            ARP 체이블이란 IP 주소와 그에 맞는 MAC 주소 테이블을 대응하는 표이다.
          </li>
            <ul>
              <li>
                앞선 과정을 통해 알아낸 MAC 주소를 IP 주소와 함께 저장해 두고 재사용하며 따라서 이후에는 이미 주소를 아는 경우에 한하여 브로드캐스트 ARP 요청 패킷을 재전송할 필요가 없어진다.
              </li>
            </ul>
        </ul>
    </ul>
  <li>
    ARP는 <strong>동일 네트워크 내</strong>에 있는 호스트의 IP 주소를 통해 MAC 주소를 알아내는 프로토콜이다 만약 다른 네트워크의 호스트에 전달하는 것이 목적이라면 각 <strong>'송신지 - 라우터 A - 라우터 B - ... - 수신지'마다 ARP 요청 - ARP 응답 과정</strong>을 거쳐가며 최종 목적지를 찾는다.
  </li>
    <ul>
      <li>
        실제로는 ARP 이외에도 라우팅 프로토콜 등을 포함하여 진행한다.
      </li>
    </ul>
  <li>
    핵심은 다음 두 가지이다.
  </li>
    <ul>
      <li>
        ARP는 <strong>동일 네트워크</strong>에 속한 호스트의 MAC 주솔르 알아내기 위해 사용하는 프로토콜이다.
      </li>
      <li>
        다른 네트워크에 속한 호스트에게 패킷을 보내야 할 경우<strong> 네트워크 외부로 나가기 위한 장비(라우터)의 MAC 주소</strong>를 알아내어 패킷을 전송한다.
      </li>
    </ul>
</ul>

<h4>IP 단편화를 피하는 방법</h4>
<ul>
  <li>
    IP 단편화는 데이터가 여러 패킷으로 쪼개져 전송해야할 <strong>패킷의 헤더</strong>들이 많아지고, 이는 곧 <strong>트래픽 증가</strong>와 <strong>대역폭 낭비</strong>로 이어질 수 있으며 받는 쪽에서도 <strong>IP 패킷들을 하나로</strong> 합쳐야하는 부하가 있어 <strong>되도록 하지 않는 것</strong>이 좋다.
  </li>
  <li>
    IP 단편화를 피하기 위해서는 IP 패킷을 주고받는 <strong>모든 호스트의 처리 가능한 MTU 크기</strong>를 고려해야 한다.
  </li>
    <ul>
      <li>
        이렇게 IP 단편화 없이 주고받을 수 있는 최대크기를 <strong>경로 MTU(Path MTU)</strong>라고 한다. 즉 경로 MTU만큼의 데이터만 주고받으면 단편화는 발생하지 않는다.
      </li>
    </ul>
  <li>
    경로 MTU를 구하고 해당 크기만큼만 송수신하여 IP 단편화를 회피하는 기술을 <strong>경로 MTU 발견(Path MTU discovery)</strong>이라 한다.
  </li>
  <li>
    오늘날 네트워크에서는 대부분 경로 MTU 발견을 지원하며 경로 MTU 발견은 기본적으로 DF 플래그를 설정한 채 동작한다.
  </li>
    <ul>
      <li>
        예를 들어 어떤 호스트가 MTU 크기를 넘은 IP 패킷을 받았는데 해당 IP 패킷에 DF 플래그가 설정되어 있다면 IP 패킷을 전달한 호스트에게 DF 플래그가 설정되어 있어 <strong>단편화 처리가 불가능함을 알린다</strong>.
      </li>
      <li>
        이 메시지를 전달 받은 송신자 호스트는 IP 패킷을 점차 줄이며 이 과정에서 경로 MTU를 알게 된다.
      </li>
    </ul>
</ul>

<br><br>

<h1>2. IP 주소</h1>
<ul>
  <li>
    하나의 IP 주소는 크게 <strong>네트워크 주소</strong>와 <strong>호스트 주소</strong>로 이루어진다.
  </li>
    <ul>
      <li>
        네트워크 주소는 호스트가 속한 <strong>특정 네트워크를 식별</strong>하는 역할을 한다.
      </li>
      <li>
        호스트 주소는 네트워크 내의 <strong>특정 호스트를 식별</strong>하는 역할을 한다.
      </li>
    </ul>
</ul>

<br>

<h2>2-1. 네트워크 주소와 호스트 주소</h2>
<ul>
  <li>
    네트워크 주소는 네트워크 ID, 네트워크 식별자(network identifier) 등으로 부르기도 하고 호스트 주소는 호스트 ID, 호스트 식별자(host identifier) 등으로 부르기도 한다.
  </li>
  <li>
    호스트 주소 공간을 크게 할당하면 호스트가 할당되지 않은 다수의 IP 주소가 낭비되고, 반대로 무조건 호스트 주소 공간을 작게 할당하면 호스트가 사용할 IP 주소가 부족해 질 수 있는데 이러한 문제를 해결하기 위해 생긴 개념이 <strong>IP 주소의 클래스(class)</strong> 이다.
  </li>
</ul>

<br>

<h2>2-2. 클래스풀 주소 체계</h2>
<ul>
  <li>
    클래스는 <strong>네트워크의 크기</strong>에 따라 IP 주소를 분류하는 기준이다. 필요한 호스트 IP 개수에 따라 네트워크 크기를 가변적으로 조정한다.
  </li>
  <li>
    클래스를 기반으로 IP 주소를 관리하는 주소 체계를 <strong>클래스풀 주소 체계(classful addressing)</strong>라고 한다.
  </li>
    <ul>
      <li>
        클래스 A는 네트워크 주소에 1옥텟만 할당되고 주소가 비트 0으로 시작된다. 따라서 2^7개의 A 클래스 네트워크와 2^24(16,777,216)개의 호스트 주소를 가질 수 있다.
      </li>
      <li>
        클래스 B는 네트워크 주소가 10으로 시작하고 2옥텟으로 구성되며 호스트 주소도 2옥텟으로 구성된다. 이론상 2^14개의 B 클래스 네트워크와 2^16개의 호스트 주소를 가질 수 있다.
      </li>
        <ul>
          <li>
            IP 주소의 최솟값은 128.0.0.0이고 최댓값은 191.255.255.255 이다. (네트워크주소 앞의 비트가 10으로 고정되었기 때문).
          </li>
        </ul>
      <li>
        C 클래스의 네트워크 주소는 110으로 시작하고 3옥텟으로 구성되며 호스트 주소는 1옥텟으로 구성된다. 이론상 2^21개의 C 클래스 네트워크 주소와 2^8개의 호스트 주소를 가질 수 있다.
      </li>
        <ul>
          <li>
            IP 주소의 최솟값은 192.0.0.0이고 최댓값은 223.255.255.255이다.
          </li>
        </ul>
      <li>
        D는 멀티캐스트를 위해, E는 특수한 목적을 위해 예약된 클래스이기 때문에 별도의 목적으로 사용된다.
      </li>
    </ul>
  <li>
    단, 호스트 주소가 전부 0인 IP 주소는 <strong>네트워크 자체</strong>를 의미하는 네트워크 주소로 사용되고, 전부 1인 주소는 <strong>브로드캐스트</strong>를 위한 주소로 사용되기 때문에 <strong>모두 호스트 주소로 할당할 수는 없다</strong>.
  </li>
    <ul>
      <li>
        따라서 A, B, C 클래스에서도 전체 호스트 주소의 개수에서 -2를 해 주어야 한다.
      </li>
    </ul>
</ul>

<br>

<h2>2-3. 클래스리스 주소 체계</h2>
<ul>
  <li>
    클래스풀 주소 체계는 결국 클래스별 네트워크의 크기가 고정되어 있어 다수의 IP 주소가 낭비될 가능성이 있다는 문제가 있다.
  </li>
  <li>
    클래스리스 주소 체게(classless addressing)는 <strong>클래스 개념 없이(classless)</strong> 네트워크의 영역을 나누어 호스트에게 IP 주소 공간을 할당하는 방식으로 오늘날 주로 사용된다.
  </li>
</ul>

<h3>2-3-1. 서브넷 마스크</h3>
<ul>
  <li>
    클래스리스 주소 체계는 클래스풀처럼 클래스로 네트워크와 호스트를 구분지을 수 없기 때문에 <strong>서브넷 마스크</strong>를 이용한다.
  </li>
  <li>
    <strong>서브넷 마스크(subnet mask)</strong>는 IP 주소상에서 <strong>네트워크 주소는 1</strong>로 그리고 <strong>호스트 주소는 0</strong>으로 표기한 <strong>비트열</strong>을 의미한다.
  </li>
  <li>
    서브넷 마스크를 이용해 크래스를 원하는 크기로 더 잘게 쪼개어 사용하는 것을 <strong>서브네팅(subneting)</strong>이라 한다.
  </li>
  <li>
    서브네트워크는 IP 주소의 네트워크 주소로 구분 가능한 <strong>네트워크의 부분 집합</strong>이다. (줄여서 서브넷이라 부르기도 한다).
  </li>
  <li>
    A, B, C 클래스를 각각 서브넷 마스크로 표현하면 다음과 같다.
  </li>
    <ul>
      <li>
        A 클래스: 255.0.0.0(11111111.00000000.00000000.00000000)
      </li>
      <li>
        B 클래스: 255.255.0.0(11111111.11111111.00000000.00000000)
      </li>
      <li>
        C 클래스: 255.255.255.0(11111111.11111111.11111111.00000000)
      </li>
    </ul>
</ul>

<h4>서브네팅: 비트 AND 연산</h4>
<ul>
  <li>
    서브넷 마스크를 이용해 네트워크 주소와 호스트 주소를 구분 짓는 방법은 단순히 IP 주소와 서브넷 마스크를 <strong>비트 AND 연산</strong>하면 된다.
  </li>
    <ul>
      <li>
        비트 AND 연산(bitwise AND operation)이란 피연산자가 모두 1인 경우에는 1, 아닌 경우에는 0이 되는 연산이다.
      </li>
    </ul>
</ul>

<h4>서브넷 마스크 표기: CIDR 표기법</h4>
<ul>
  <li>
    서브넷 마스크를 표기하는 방법에는 크게 다음 두 가지가 있다.
  </li>
    <ul>
      <li>
        서브넷 마스크를 10진수로 직접 표기하는 방법.
      </li>
      <li>
        IP 주소/서브넷 마스크상의 1의 개수 형식으로 표현하는 방법.
      </li>
    </ul>
  <li>
    위의 두 가지 중 IP 주소/서브넷 마스크상의 1의 개수로 표현하는 형식을 <strong>CIDR 표기법(CIDR; Classless Inter-Dormain Routing notation)</strong>이라 한다.
  </li>
    <ul>
      <li>
        IP 주소와 서브넷 마스크를 함께 표현할 수 있는 간단한 표기로 많이 활용된다.
      </li>
    </ul>
  <li>
    예를 들면 192.168.0.2/25인 CIDR은 다음과 같다.
  </li>
    <ul>
      <li>
        IP주소: 11000000.10101000.00000000.00000010
      </li>
      <li>
        서브넷 마스크: 11111111.11111111.11111111.10000000
      </li>
    </ul>
</ul>

<br>

<h2>2-4. 공인 IP 주소와 사설 IP 주소</h2>
<ul>
  <li>
    전 세계에는 고유한 IP 주소가 있고 이를 공인 IP 주소라한다. 그리고 고유하지 않은 IP 주소도 존재한다. 
  </li>
</ul>

<h3>2-4-1. 공인 IP 주소</h3>
<ul>
  <li>
    공인 IP 주소(public IP address)는 전 세계에서 <strong>고유한 IP 주소</strong>이다.
  </li>
    <ul>
      <li>
        네트워크 간의 통신에서 인터넷을 이용할 때 사용하는 IP가 해당한다.
      </li>
      <li>
        ISP나 공인 IP 주소 할당 기관을 통해 할당받을 수 있다.
      </li>
    </ul>
</ul>

<h3>2-4-2. 사설 IP 주소와 NAT</h3>
<ul>
  <li>
    사설 IP 주소(private IP address)는 <strong>사설 네트워크에서 사용</strong>하기 위한 IP 주소이다.
  </li>
    <ul>
      <li>
        사설 네트워크는 외부 네트워크에 공개되지 않은 네트워크를 의미한다.
      </li>
      <li>
        우리가 사용하는 모든 네트워크 기기의 IP 주소를 전부 별도로 신청하지는 않는다. 이는 <strong>LAN 내의 많은 호스트</strong>는 <strong>사설 IP 주소</strong>를 사용하기 때문이다.
      </li>
    </ul>
  <li>
    IP 주소 공간 중에서는 사설 IP 주소로 사용하도록 특별히 예약된 IP 주소 공간이 있으며 다음과 같다.
  </li>
    <ul>
      <li>
        10.0.0.0/8 (10.0.0.0 - 10.255.255.255)
      </li>
      <li>
        172.16.0.0/12 (172.16.0.0 - 172.31.255.255)
      </li>
      <li>
        192.168.0.0/16 (192.168.0.0 - 192.168.255.255)
      </li>
    </ul>
  <li>
    사설 IP 주소의 할당 주체는 일반적으로 <strong>라우터</strong>이다.
  </li>
  <li>
    사설 IP 주소는 해당 호스트가 속한 <strong>사설 네트워크상에서만 유효</strong>하기 때문에 다른 네트워크상의 <strong>사설 IP 주소와 중복</strong>되어도 된다.
  </li>
  <li>
    사설 IP 주소를 사용하는 호스트가 외부 네트워크와 통신하기 위해서는 <strong>NAT(Network Address Translation)</strong>을 사용한다.
  </li>
    <ul>
      <li>
        NAT은 IP 주소를 변환하는 기술이며 주로 '<strong>네트워크 내부 사설 IP → 네트워크 외부 공인 IP</strong>'로 변환할 때 사용한다.
      </li>
      <li>
        NAT을 통해 사설 IP 주소를 사용하는 여러 호스트는 <strong>적은 수의 공인 IP 주소를 공유</strong>할 수 있다.
      </li>
      <li>
        대부분의 라우터와 (가정용) 공유기는 NAT 기능을 내장하고 있고 이를 통해 외부와 통신을 한다.
      </li>
    </ul>
  <li>
    window의 경우 'cmd - ipconfig'를 통해 사설 IP를 확인할 수 있고, 구글이나 네이버를 통해 공인 IP를 확인할 수 있다.
  </li>
</ul>

<br>

<h2>2-5. 정적 IP 주소와 동적 IP 주소</h2>
<ul>
  <li>
    호스트에 IP를 할당할 때 수작업을 통한 정적 할당 혹은 DHCP를 통한 동적 할당을 주로 사용한다.
  </li>
</ul>

<h3>2-5-1. 정적 할당</h3>
<ul>
  <li>
    정적 할당이란 수작업을 통해 호스트에 직접 IP 주소를 부여하는 방법이다. 이렇게 할당된 IP 주소를 <strong>정적 IP 주소(static IP address)</strong>라고 부른다.
  </li>
  <li>
    운영체제의 네트워크 설정을 통해 부여할 IP 주소, 서브넷 마스크, 게이트웨이(라우터) 주소, DNS 주소를 입력하여 호스트에 정적 IP 부여가 가능하다.
  </li>
  <li>
    IP 주소 할당에서의 라우터의 의미는 기본 게이트웨이(첫 번째 홉)를 의미한다.
  </li>
</ul>

<h4>기본 게이트웨이</h4>
<ul>
  <li>
    게이트웨이(gateway)의 일반적인 의미는 서로 다른 네트워크를 연결하는 하드웨어적/소프트웨어적 수단을 의미한다.
  </li>
  <li>
    그 중 기본 게이트웨이(default gateway)는 호스트가 속한 네트워크 외부로 나가기 위한 <strong>기본적인 첫 경로(첫 번째 홉)</strong>를 의미한다.
  </li>
    <ul>
      <li>
        기본 게이트웨이는 <strong>네트워크 외부와 연결된 라우터(공유기)의 주소</strong>를 의미하는 경우가 많다.
      </li>
    </ul>
</ul>

<h3>2-5-2. 동적 할당과 DHCP</h3>
<ul>
  <li>
    IP 주소를 정적으로만 할당하면 늘어나는 호스트 수로 인해 관리가 어려워지는 문제가 발생한다.
  </li>
  <li>
    동적 할당은 정적 할당과 달리 IP 주소를 직접 일일이 입력하지 않고 호스트에 IP 주소가 동적으로 할당되며 이렇게 할당된 IP 주소를 <strong>동적 IP 주소(dynamic IP address)</strong>라 한다.
  </li>
    <ul>
      <li>
        동적 IP 주소는 사용되지 않을 경우 회수되고, 할당받을 때마다 다른 주소를 받을 수 있다.
      </li>
    </ul>
  <li>
    IP 동적 할당에 사용되는 대표적인 프로토콜은 <strong>DHCP(Dynamic Host Configuration Protocol)</strong>이다.
  </li>
    <ul>
      <li>
        DHCP는 응용 계층에 속하지만 네트워크 계층의 개념을 이해하는 데에도 많은 도움이 된다.
      </li>
    </ul>
  <li>
    DHCP를 통한 IP 주소 할당은 <strong>IP 주소를 할당받고자하는 호스트(클라이언트)</strong>와 해당 호스트에게 IP 주소를 제공하는 <strong>DHCP 서버(DHCP server)</strong>간에 메시지를 주고받음으로써 이루어진다.
  </li>
    <ul>
      <li>
        일반적으로 DHCP 서버 역할은 <strong>라우터</strong>가 수행하지만, 특정 호스트에 DHCP 서버 기능을 추가할 수도 있다.
      </li>
    </ul>
  <li>
    DHCP로 할당받은 IP 주소는 사용할 기간(임대 기간)이 정해져 있으며 일반적으로 수 시간에서 수일로 설정한다.
  </li>
    <ul>
      <li>
        임대 기간이 끝난 IP 주소는 다시 DHCP 서버로 반납된다. 그래서 DHCP를 통해 IP 주소를 할당받는 것을 <strong>IP 주소를 임대한다</strong>라고 표현하기도 한다.
      </li>
      <li>
        cmd - ipconfig /all을 통해 확인할 수 있다.
      </li>
    </ul>
  <li>
    IP 주소를 할당받는 과정에서 클라이언트와 DHCP 서버 간에 주소 주고받는 메시지의 종류는 크게 네 가지가 있다. (순서대로 주고 받는다).
  </li>
    <ol>
      <li>
        DHCP Discover(클라이언트 → DHCP 서버)
      </li>
        <ul>
          <li>
            DHCP Discover 메시지를 통해 DHCP 서버를 찾으며 이 메시지는 <strong>브로드캐스트로 전송</strong>된다.
          </li>
          <li>
            DHCP Discover 메시지를 전송하는 시점에서는 아직 클라이언트 IP 주소를 할당 받지 못했기 때문에 <strong>송신지 IP 주소는 0.0.0.0으로 설정</strong>된다.
          </li>
        </ul>
      <li>
        DHCP Offer(DHCP 서버 → 클라이언트)
      </li>
        <ul>
          <li>
            DHCP Discover 메시지를 받은 DHCP 서버는 클라이언트에게 DHCP Offer 메시지를 보낸다.
          </li>
          <li>
            DHCP Offer 메시지에는 클라이언트에게 할당할 IP 주소를 포함하여 서브넷 마스크, 임대 기간 등의 정보 또한 포함된다.
          </li>
        </ul>
      <li>
        DHCP Request(클라이언트 → DHCP 서버)
      </li>
        <ul>
          <li>
            클라이언트가 DHCP Offer 메시지를 받았고, 전달받은 IP 주소를 사용해도 되는가에 대해 DHCP Request로 응답한다.
          </li>
        </ul>
      <li>
        DHCP ACK(DHCP 서버 → 클라이언트)
      </li>
        <ul>
          <li>
            DHCP 서버는 마지막으로 DHCP ACK 메시지를 보낸다. 이는 최종 승인과 같은 의미이다.
          </li>
        </ul>
    </ol>
  <li>
    IP 주소 사용 기간이 모두 끝나면 IP 주소가 DHCP 서버에 반납되어 원칙적으로는 다시 위의 과정을 반복해야 한다. 하지만 임대 기간이 끝나기 전 임대 기간을 연장할 수 있으며 이를 <strong>임대 갱신(lease renewal)</strong>이라 한다.
  </li>
    <ul>
      <li>
        임대 갱신은 IP 주소의 임대 기간이 끝나기 전에 기본적으로 두 차레 자동으로 수행된다.
      </li>
      <li>
        자동으로 수행되는 과정에서 임대 개싱 과정이 모두 실패한다면 IP 주소는 DHCP 서버로 반납된다.
      </li>
    </ul>
</ul>

<h4>예약 주소:0.0.0.0 vs 127.0.0.1</h4>
<ul>
  <li>
    p166의 테이블과 같이 특수한 목적을 위해 예약된 IP 주소들이 있다.
  </li>
  <li>
    <strong>루프백 주소(loopback address)</strong>는 자기 자신을 가리키는 주소로 가장 일반적으로 사용되는 주소는 <strong>127.0.0.1</strong>이고, <strong>로컬호스트(localhost)</strong>라고도 부른다.
  </li>
    <ul>
      <li>
        전송된 패킷이 자기 자신에게 되돌아온다. 따라서 주로 테스트나 디버깅 용도로 사용된다.
      </li>
    </ul>
  <li>
    0.0.0.0/8은 인터넷 표준 공식 문서(RFC 6890)에 따르면 <strong>'이 네트워크의 이 호스트(This host on thos network)를 지칭하도록 예약되었다'</strong>라고 명시되어 있다.
  </li>
    <ul>
      <li>
        주로 아직 IP 주소를 할당받지 못하였을 때 임시로 사용하는 경우가 많다.
      </li>
    </ul>
  <li>
    0.0.0.0/0은 모든 임의의 IP 주소를 의미한다.
  </li>
    <ul>
      <li>
        이 주소는 패킷이 이동할 경로를 결정하는 라우팅에서 활용되며 디폴트 라우트를 나타내기 위해 사용된다.
      </li>
      <li>
        <strong>디폴트 라우트(default route)</strong>란 패킷을 어떤 IP로 전달할지 결정하기 어려울 경우 기본적으로 패킷을 전달할 경로를 의미한다.
      </li>
    </ul>
</ul>

<br><br>

<h1>3. 라우팅</h1>
<ul>
  <li>
    라우터의 핵심 기능은 패킷이 이동할 <strong>최적의 경로를 설정</strong>한 뒤 해당 경로로 <strong>패킷을 이동</strong>시키는 것이며 이를 <strong>라우팅</strong>이라 한다.
  </li>
  <li>
    라우팅은 어려운 주제이기에 도서에서는 라우팅의 분류에 초점을 맞추어 <strong>라우팅 테이블</strong>이 만들어지는 방법과 프로토콜에 따라 라우팅을 분류하는 것에대해 배운다.
  </li>
</ul>

<br>

<h2>3-1. 라우터</h2>
<ul>
  <li>
    네트워크 계층의 장비로 라우터만 알아도 무리가 없을 정도로 라우터는 네트워크 계층의 핵심 기능을 담당한다.
  </li>
    <ul>
      <li>
        L3 스위치(L3 switch)로 불리는 장치도 있으나 오늘날에는 라우터와 상당히 유사하기에 구분하지 않는 경우도 있고 따라서 도서에서는 라우터만을 다룬다.
      </li>
    </ul>
  <li>
    일반적으로 가정 환경에서는 <strong>공유기</strong>가 라우터의 역할을 대신한다.
  </li>
    <ul>
      <li>
        공유기를 홈 라우터(home router)라 부르기도 한다.
      </li>
      <li>
        사실 공유기는 라우터 기능뿐만 아니라 NAT 기능, DHCP 서버 기능, 보안을 위한 방화벽 등 다양한 장치의 기능이 함축되어 있다.
      </li>
    </ul>
</ul>