

## Dynamic Programming 
### 1주차 


### 2주차


### 3주차


### 4주차 

#### State Transition by Inaction
- "doing nothing"
  - DP에서 때때로 나타나는 패턴 중 하나
  - 같은 값을 갖는 2개의 다른 state를 나타냄 
  - 이전 state와 같은 값을 가지는 새로운 state를 갖는 방법은 아무것도 하지 않는 것
  - 예를 들면 점수를 최대화 하거나 최소화 하려고 할 때, 가장 좋은 방법은 "아무 것도 하지 않는 것"이기 때문에 이는 2개의 state(min, mix)가 동일한 값을 갖게 됨 

#### Example 188. Best Time to Buy and Sell Stock IV
- 주어진 state에 대한 문제를 해결하는 함수 
  - 각 state/decision에 어떤 정보가 필요한가?
  - 오늘 날짜(주식의 현재 가격을 조회 하기 위함)
  - 남은 거래량
  - 3가지 state variable
    - i : 날짜
    - price : 현재의 주가
    - transactionRemaining : 남은 트랜잭션 수 (주식을 팔 때마다 1씩 내려감)
    - holding : 주식을 보유하고 있지 않다면 0, 주식을 보유중인 경우 1
      - holding이 0이면 주식을 살 수 있고, 그렇지 않으면 주식을 매도 할 수 있음 
  - => 여기서 doing nothing의 의미는 주식을 사지도, 팔지도 않을 때 최대 이익일 수 있음을 의미 ⭐

  - problem : 달성 가능한 maximum profit 필요함 
    - dp(i, tR, holding) 함수 정의
    - tR 트랜잭션이 남은 i번째 날부터 시작하여 달성 가능한 최대 이익을 리턴하고, 주식이 있는지 없는지 여부를 나타내는 holding 정보를 반환 
    - 0일 째에 k거래가 남아있고 주식을 보유하지 않았기에 dp(0, k, 0)을 반환 
    - 각 state에서 hodling 여부에 따라 결정을 내림 
    - 주식을 보유하고 있다면 팔거나, 안팔 수 있음(state 2개)
      - 만약 판다면 prices[i]를 얻고, 다음 state는 (i+1, tR - 1, 0)이 됨
      - 그 다음날 1개를 판매(tR -1)하여 거래를 종료하고, 더 이상 주식을 보유하지 않게 됨 (holding = 0)
        - 총 이익은 prices[i] + dp(i+1, tR-1,0)
      - 매도하지 않고 아무것도 안한다면, 주식을 보유한채로 같은 수의 holding으로 다음 날이 됨 
        - 그렇다면 이익은 dp(i+1, tR, holding)
    - 주식을 보유하고 있지 않은 경우 2가지 옵션이 있음
      - 주식을 삼 or 주식 사지 않음
      - 주식을 구매한다면, prices[i]를 잃고, 다음 state는 (i+1, tR, 1)
        - 다음날이 되면 매도했을 때만 거래가 완료되기 때문에 holding 수는 동일하고, 주식을 보유한 상태가 됨 
        - 총 이익은 -prices[i] + dp(i+1, tR, 1) 
      - 주식을 사지 않고, 아무것도 하지 않는다면 이익은 dp(i+1, tR, holding)

