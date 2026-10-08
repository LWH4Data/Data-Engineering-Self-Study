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
        </ul>
    </ol>
</ul>