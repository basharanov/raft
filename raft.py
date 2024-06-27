a = [52, 17946,27160, 387, 17346, 27505, 20816, 20577, 10961, 6021, 5262, 28278, 24163, 931, 11003, 19738, 17914, 1683, 10320, 10475]
b = [26,10,30,7,4,5] #82
c = [13,9,1,34,23,12,5] # 97
d = [4, 5, 7, 11, 2, 9, 18, 7] #63 (v minalata programa nqmashe 4 a beshe 2)

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


