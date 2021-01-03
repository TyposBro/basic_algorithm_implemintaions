from base_expansion import base_expansion as be


def mod_exp(n, exp, mod):
    """Return remainder"""

    e = __be_helper(exp)
    x = 1
    p = n % mod
    for i in e:
        if i == 1:
            x = (x * p) % mod
        p = (p*p) % mod
    return x


def __be_helper(exp):
    e = [int(i) for i in str(be(exp))]
    e.reverse()
    return e


if __name__ == "__main__":
    a = int(input("num: "))
    b = int(input("exp: "))
    c = int(input("mod: "))
    print(mod_exp(a, b, c))
