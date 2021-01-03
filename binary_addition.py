from base_expansion import base_expansion as be


def binary_addition(num1, num2):
    a = _helper(num1)
    b = _helper(num2)
    c = 0
    res = []
    length = len(a) if len(a) > len(b) else len(b)

    for i in range(length-1):
        d = (_get(a, i)+_get(b, i)+c)//2
        elem = _get(a, i)+_get(b, i)+c-2*d

        res.append(elem)
        c = d
    res.append(c)
    res = [str(i) for i in res]
    res.reverse()
    res = "".join(res)
    return res


def _helper(num):
    a = [int(i) for i in str(be(num, 2))]
    a.reverse()
    return a


def _get(l, idx, default=0):
    try:
        return l[idx]
    except IndexError:
        return default


if __name__ == "__main__":

    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
    res = binary_addition(num1, num2)
    print(res)
