a = input().lower()
b = input().lower()

soln = []

index1 = -9
index2 = -9

for i, x in enumerate(list(a)):
    for j, y in enumerate(list(b)):
        if x == y:
            index1 = i
            index2 = j
            soln.append(x)
            break
        break


for l in range(index1, len(a)):
    print(a[l])
    for k in range(index2, len(b)):
        print(b[k])
        if a[l] == b[k]:
            soln.append(b[k])
            break
    index2 = k + 1
            

soln.pop(-1)

print(soln)