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
    g, q, a, k, r = map(int, input().split())

    p = 2 * q + 1
    v = pow(g, q - a, p)

    # Alice随机生成一个k
    # gama = g^k mod p
    gama = pow(g, k, p)

    # Bob选择一个随机响应r
    # Alice计算响应y
    y = (k + a * r) % q

    # Bob验证gama

    # 输出结果
    print(v)
    print(gama)
    print(y)
