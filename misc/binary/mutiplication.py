from base_expansion import base_expansion as be


def bin_multiply(num1, num2):
    """
    Return binary multiplication
    """
    a = _helper(num1)
    b = _helper(num2)
    res = 0
    for i, second in enumerate(b):
        if second == 1:
            res += a[i]*10**(i+1)
    return res


def _helper(num):
    a = [int(i) for i in str(be(num1, 2))]
    a.reverse()
    return a


if __name__ == "__main__":
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    print(bin_multiply(num1, num2))
