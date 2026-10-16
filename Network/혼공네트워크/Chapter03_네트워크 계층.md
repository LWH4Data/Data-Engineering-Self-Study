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