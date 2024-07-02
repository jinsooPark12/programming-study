n = int(input()) # 분해합의 값 입력

for i in range(1, n+1):     # 해당 분해합의 생성자 찾기
    num = sum((map(int, str(i))))   # i의 각 자리수의 합
    num_sum = i + num       # 분해합 = 생성자 + 각 자리수의 합
    # i가 가장 작은 수부터 차례로 들어가므로 처음 구해진 분해합이 입력값과 같을 때가 가장 작은 생성자임
    if num_sum == n:
        print(i)
        break
    if i == n:          # 생성자 i와 입력값이 같다면 생성자 X
        print(0)