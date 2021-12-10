def bullshit():
    try:
        s = input().lower()
        chararr = []
        for a in s:
            chararr.append(ord(a))

        tmp = chararr[-1]
        ind = -1
        for i, e in reversed(list(enumerate(chararr))):
            if e < tmp:
                ind = i
                break
            else:
                tmp = e
        if ind == -1:
            raise Exception
        repl = 100000

        for j in range(ind, len(chararr)):
            if chararr[j] > chararr[ind] and chararr[j] < repl:
                repl = chararr[j]
                repli = j

        chararr[ind], chararr[repli] = chararr[repli], chararr[ind]

        sortedarr = chararr[:ind+1]
        subarr = chararr[ind+1:]
        subarr.sort()
        sortedarr = sortedarr + subarr

        finalarr = []
        for x in sortedarr:
            finalarr.append(chr(x))

        finalstr = ''.join(finalarr)

        print(finalstr)
    except:
        print("no answer")

n = int(input())
for i in range(n):
    bullshit()
