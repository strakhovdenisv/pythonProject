def gen_bin(M, prefix=""):
    if M==0:
        print(prefix)
        return
    gen_bin(M-1, prefix+"0")
    gen_bin(M-1, prefix+"1")


def generate_number(N:int, M:int, prefix=None):
    """ Генерирует ысе числа (с лидирующими незначающими нулями)
        в N-ричной системе счисления (N <= 10)
        длины Ь
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()

# только для двоичной СС:
gen_bin(3)

# для произвольной СС:
generate_number(3,3)
