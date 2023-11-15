def pow_mod(x, i, mod):
    s = 1
    while i != 0:
        s = (s * x) % mod
        i -= 1
    return s

def modj(x, y):
    z = x - y
    while z < 0:
        z += p
    return z % p

def modx(x, y):
    while x < 0 or y < 0:
        x += p
        y += p
    x %= p
    y %= p
    sum = 0
    while x != 0:
        if x & 1:
            sum = (sum + y) % p
        y = y << 1
        x = x >> 1
    return sum

def modc(x, y):
    y = pow_mod(y, p - 2, p)
    z = modx(x, y)
    return z

def a_x(a, x):
    sum = a[1]
    for i in range(2, t + 1):
        sum = (sum + a[i] * pow_mod(x, i - 1, p)) % p
    return sum

def solve():
    for i in range(1, t + 1):
        k = i
        while k <= t and abs(A[k][i]) < 1e-10:
            k += 1
        if k <= t:
            for j in range(i, t + 2):
                A[i][j], A[k][j] = A[k][j], A[i][j]

            for j in range(i + 1, t + 1):
                c = modc(p - A[j][i], A[i][i])
                for k in range(i, t + 2):
                    A[j][k] = (A[j][k] + modx(c, A[i][k])) % p
        else:
            print("系数矩阵奇异，线性方程组无解或有无数解")
            return False

    for i in range(t, 0, -1):
        a[i] = A[i][t + 1]
        for j in range(t, i, -1):
            a[i] = modj(a[i], modx(a[j], A[i][j]))
        a[i] = modc(a[i], A[i][i])
    return True

# 主程序
t, w, p = map(int, input().split())
a = [0] * (t + 2)
x = [0] * (t + 3)
y = [0] * (t + 3)

for i in range(1, t + 1):
    x[i], y[i] = map(int, input().split())

x[t + 1] = int(input())

A = [[0] * (t + 3) for _ in range(t + 2)]

for i in range(1, t + 1):
    for j in range(1, t + 1):
        A[i][j] = pow_mod(x[i], j - 1, p)
    A[i][t + 1] = y[i]

if solve() != True:
    exit(-1)

print(f"{a[1]}")
y[t + 1] = a_x(a, x[t + 1])
print(f"{y[t + 1]}")
