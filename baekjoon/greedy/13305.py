n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

total = 0
min = costs[0]
for i in range(n-1):
    if costs[i] < min:
        min = costs[i]
    total += min * roads[i]
print(total)