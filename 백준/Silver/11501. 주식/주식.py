# 뒤에 입력되는 최대값을 기준으로 계산해야 하는 그리디 문제
# 문제에서 주어진 값들을 뒤로 세어 뒤에서 입력되는 값 중 최대값을 구함

T = int(input())
for _ in range(T):
    n = int(input())
    price = list(map(int, input().split()))
    
    profit = 0      # 이익
    maxPrice = 0    # 주식의 최대 가격
    
    # 뒤에 입력된 최대값을 확인하기 위해 뒤에서부터 셈
    for i in range(n-1, -1, -1):
        # 최대값 확인
        if price[i] > maxPrice:
            maxPrice = price[i]
        # 현재 가격이 현재 최대 가격보다 작으면 차익 실현
        else:
            profit += maxPrice - price[i]
    print(profit)