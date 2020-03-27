
# алгоритм
# сдвиг
# сумма
# перевод в двоичную СС
# подбор битности регистра (Я ХОТЕЛ ЭТО СДЕЛАТЬ...)


def main():
    a = ten2two(int(input("Enter A:\n")))
    b = ten2two(int(input("Enter B:\n")))
    res = algorithm(a, b)
    print(f"{a} x {b} = {res}")


def ten2two(num: int) -> int:
    return int(bin(num), 2)


def sum_reg(c: int, a: int) -> int:
    a = a << 32
    return c + a


def shift_right(num: int) -> int:
    return num >> 1


def algorithm(a: int, c: int) -> int:
    reg_b = '0'*(32 - len(str(bin(c))[2:])) + str(bin(c))[2:]
    for i in range(32):
        print(f"B = {reg_b[31 - i]}\n" + ' ' * 10 + f"C = {'0' * (64 - len(str(bin(c))[2:])) + str(bin(c))[2:]}")
        if reg_b[31-i] == '1':
            c = sum_reg(c, a)
            print(' '*7 + "+\n" + ' '*10 + f"A = {'0'*(64 - len(str(bin(a))[2:])) + str(bin(a))[2:]}\n" + ' '*14 + '_'*64)
        c = shift_right(c)
        print("C >> 1")
        print(' '*10 + f"C = {'0' * (64 - len(str(bin(c))[2:])) + str(bin(c))[2:]}\n")

    return c



























if __name__ == '__main__':
    main()