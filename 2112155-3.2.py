def f(x, y, mod):  # y = x^a mod
    a = 0
    m = 1
    if y == 1:
        return 0
    a += 1
    while m * x % mod != y:
        a += 1
        m *= x
        m %= mod
    return a

def pow(x, e, n):  # 计算 x^e mod n
    m = 1
    while e > 0:
        if e & 1:
            m = (m * x) % n
        x = (x * x) % n
        e = e >> 1
    return m

if __name__ == '__main__':
    # 输入参数
    g, q, v = map(int, input().split())
    r1, y1, r2, y2 = map(int, input().split())
    p = 2 * q + 1
    k1 = f(g, (pow(g, y1, p) * pow(v, r1, p)) % p, p)

    while (y1 - k1) % r1 != 0:
        y1 += q

    a = (y1 - k1) // r1

    # 输出结果
    print(a)
