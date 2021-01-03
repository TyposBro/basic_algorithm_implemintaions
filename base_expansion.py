def base_expansion(num: int, base: int = 2):
    """
    return a base expansion
    """
    q = int(num)
    b = int(base)
    count = 0
    expansion = []
    while q != 0:
        expansion.append(q % b)
        q = q//b
        count += 1
    expansion.reverse()
    res = "".join(map(str, expansion))
    return int(res)


if __name__ == "__main__":

    number = input("Enter any number: ")
    base = input("Enter base: ")
    result = base_expansion(number, base)
    print(result)
