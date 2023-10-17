def f(x, y, mod):
    a = 0
    m = 1
    if y == 1:
        return 0
    a += 1
    while (m * x % mod) != y:
        a += 1
        m = (m * x) % mod
    return a


def power(x, e, n):
    m = 1
    while e > 0:
        if e & 1:
            m = (m * x) % n
        x = (x * x) % n
        e >>= 1
    return m


def verify(g, q, p, m, x, y):
    z1 = power(q, x, p)
    z2 = power(x, y, p)
    z = power(g, m, p)
    if (z1 * z2) % p == z:
        return True
    else:
        return False


if __name__ == "__main__":
    p, g, q = map(int, input().split())
    m, x, y = map(int, input().split())
    a = f(g, q, p)
    r = f(g, x, p)

    if verify(g, q, p, m, x, y):
        print("YES")
    else:
        print("NO")
    print(a)
    print(r)
