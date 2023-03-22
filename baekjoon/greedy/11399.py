peopleNum = int(input())
#리스트를 입력받는다
exTimes = list(map(int, input().split()))
# print(exTimes)
#리스트를 정렬한다
exTimes.sort()
#리스트 순회하며 지금까지의 값에 현재 값을 더한 값을 더하여 누적
total = 0
cul = 0
for i in exTimes:
    cul += i
    total += cul
print(total)