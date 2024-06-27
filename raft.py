
n = input("Enter how many sheeps you have: ")
k = input("Enter how many time you need to cross the river: ")
k = int(k)
list= []
for i in range(int(n)):
    number = input("Enter the sheep weight: ")
    list.append(int(number))

array = []
array = list.copy()

result = 0
margin = 100000
index = 0
goal = 0
allSum = 0
results = []

for i in range(len(array)):
    allSum += array[i]


while k > 0:
    allSum -= result
    result = 0
    margin = 100000
    goal = allSum / k
    for j in range(len(array)):
        for i in range(len(array)):
            if abs(goal - (result + array[i])) < margin:
                margin = abs(goal - (result + array[i]))
                index = i
        if goal - result != margin:
            result += array[index]
            array[index] = 0
            index = 0

    results.append(result)
    k-=1

k = 0
for i in range(len(results)):
    if results[i] > k:
        k = results[i]

print(k)


