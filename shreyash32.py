a = input().lower()
b = input().lower()

soln = []

n = len(a) if len(a) < len(b) else len(b)

for i in range(n):
    for j in range(n):
            if a[i] == b[j]:
                soln.append(a[i])
                break
            break

try:
    for k in range(j, len(b)):
        i += 1
        if a[i] == b[k]:
            soln.append(a[i])
            j = k
except:
    pass

print(soln)