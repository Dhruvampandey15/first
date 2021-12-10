a, b, c, d = input().split(" ")
a = int(a) # location 1
b = int(b) # rate 1
c = int(c) # location 2
d = int(d) # rate 2


def calcWin(a, b, c, d):
    if a > c:
        while(c < a and b < d):
            a = a + b
            c = c + d
            if a == c:
                return True
    elif a < c:
        while(a < c and d < b):
            a = a + b
            c = c + d
            if a == c:
                return True
    elif a == c:
        return True

    return False


if calcWin(a, b, c, d):
    print("YES")
else:
    print("NO")
