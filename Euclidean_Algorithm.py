def gcd(num1, num2):
    """Return Greatest Common Divisor"""
    # Euclidean Algorithm for GCD
    a = max([num1, num2])
    b = min([num1, num2])

    while b != 0:
        mod = a % b
        a = b
        b = mod

    return a


def lcm(num1, num2):
    # Euclidean Algorithm for LCM
    """Return Least Common Multiple"""
    m = num1*num2
    d = gcd(num1, num2)
    return int(m/d)


if __name__ == "__main__":
    n1 = int(input("Enter the 1st number: "))
    n2 = int(input("Enter the 2nd number: "))
    print(f"Greatest Common Divisor: {gcd(n1, n2)}")
    print(f"Least Common Multiple: {lcm(n1, n2)}")
