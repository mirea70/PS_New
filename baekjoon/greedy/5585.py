# 잔돈의 개수를 구하기
# 입력 받기
buyAmount = int(input())
# 1000 - 입력값
reply = 1000 - buyAmount
cnt = 0
# 500원 ~ 1엔까지 배열에 담음
list = [500, 100, 50, 10, 5, 1]
# 배열 순회하며 그 액수로 채울 수 있을 때까지 채운다
for i in list:
    while reply >= i:
        reply -= i
        # 채울 때마다 개수 셈
        cnt += 1
# 센 개수 출력
print(cnt)