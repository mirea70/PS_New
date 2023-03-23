diveWithMinus = input().split('-')
plus = 0
minus = 0
for plusNum in diveWithMinus[0].split('+'):
    plus += int(plusNum)
for minusArr in diveWithMinus[1:]:
    for minusNum in minusArr.split('+'):
        minus += int(minusNum)
print(plus - minus)