import csv
import math

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

def mean(data):
    length = len(data)
    total =0
    for i in data:
        total += int(i)
    mean = total/length
    return mean

data = data[0]

squaredList = []
for i in data:
    a = int(i)-mean(data)
    a = a**2
    squaredList.append(a)

sumOfSquares = 0
for i in squaredList:
    sumOfSquares = sumOfSquares + i
result = sumOfSquares/len(data)
standardDeviation = math.sqrt(result)
print(standardDeviation)





