def main():
    a, b = bin(int(input("Enter A:\n"))), bin(int(input("Enter B:\n")))
    print(' '*10 + f"A = {'0' * (64 - len(a) + 2)}{a[2:]}\n" + ' '*10 + f"B = {'0' * (64 - len(b) + 2)}{b[2:]}")
    b, minusB, k = prepare(a, b)
    print(' '*10 + f"B = {'0' * (64 - len(bin(b)) + 2)}{bin(b)[2:]}\n" + ' '*9 + f"-B = {'0' * (64 - len(bin(minusB)) + 2)}{bin(minusB)[2:]}\n")
    cel, ost = algorithm(str(a), b, minusB, k)
    print("CORRECT OST")
    print(' '*10 + '0'*(64 - len(bin(ost)) + 2) + bin(ost)[2:])
    print(f"{int(a, 2)} / {b >> k} = {cel}.{bin(ost)[2:]}")
    
    def prepare(a: str, b: str) -> tuple:
    k = len(a) - len(b)
    # посчитали разницу длин делимого и делителя
    b = int(b,2) << k
    minusB = (int('1'*64, 2) ^ b) + 1
    return b, minusB, k
    
    def shift_left(a: str) -> str:
    a = int(a, 2) << 1
    return bin(a)[0:2] + bin(a)[3:] if len(str(bin(a))) - 2 == 64 else '0' * (64 - len(bin(a)) + 2) + bin(a)[2:]
    
    def algorithm(a: str, b: int, minusB: int, k: int):
    print("A + (-B):")
    print(' '*10 + '0' * (64 - len(a) + 2) + a[2:] + '\n'+ ' '*10 + '0' * (64 - len(bin(minusB)) + 2) + bin(minusB)[2:])
    a = bin(int(a,2) + minusB)[-64:] # 5.1
    print(' ' * 10 + '_'*64 + '\n' + ' '*10 + a)
    res = '0' if int(a,2) >> 63 == 1 else '1' # 5.2
    for i in range(k): # 5.6
        print("A << 1:")
        a = shift_left(a) # 5.3
        print(' '*10 + a[-64:])
        if res[i] == '1': # 5.4
            print("A + (-B):")
            print(' '*10 + '0' * (64 - len(a) + 2) + a[2:] + '\n'+ ' '*10 + '0' * (64 - len(bin(minusB)) + 2) + bin(minusB)[2:])
            a = str(bin(int(a,2) + minusB))[-64:] # a = a + minus
            print(' ' * 10 + '_'*64 + '\n' + ' '*10 + a)
            res += '0' if int(a,2) >> 63 == 1 else '1' # 5.5
        else:             # 5.4
            print("A + B:")
            print(' '*10 + '0' * (64 - len(a) + 2) + a[2:] + '\n'+ ' '*10 + '0' * (64 - len(bin(b)) + 2) + bin(b)[2:])
            a = str(bin(int(a,2) + b))[-64:] # a = a + b
            print(' ' * 10 + '_'*64 + '\n' + ' '*10 + a)
            res += '0' if int(a,2) >> 63 == 1 else '1' # 5.5

    if int(a,2) >> 63 == 1: # 6.1
        a = str(bin(int(a,2) + b))[-64:]
    print('\n' + ' '*10 + '0'*(64 - len(a) + 2) + a[2:])
    return res, int(a,2) >> k # 6.2
    
    
    if __name__ == '__main__':
    main()