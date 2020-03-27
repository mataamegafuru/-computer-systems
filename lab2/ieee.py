def convert(num: float):
    sign = 0 if abs(num) > 0 else 1
    exp = 0
    while not (abs(num) > 1.0 and abs(num) < 2.0):
    # cond or cond
    # not not cond or cond
    # not not cond and not cond
        if abs(num) > 2.0:
            num /= 2
            exp += 1
        if abs(num) < 1.0:
            num *= 2
            exp -= 1
    dr = abs(num) - 1.0
    res = ""
    i = 0
    while (i < 24):
        dr *= 2
        if i <= 22:
            if (dr >= 1.0):
                res += "1"
                dr -= 1
            else:
                res += "0"
        else:
            if dr > 0.5:
                res = res[:-1] + '1'
        i+=1
    return str(sign) + bin(exp + 127)[2:] + res, sign, exp, '1' + res

def sum_ieee(s1, s2, e1, e2, m1, m2):
    shift = e1 - e2
    m2 = "0" * shift + m2
    m2 = m2[:-shift]
    print(' '*10 + m1)
    if s1 == s2:
        print(' '*7 + '+')
        m3 = bin(int (m1 ,2) + int(m2, 2))[2:]
    else:
        print(' '*7 + '-')
        m3 = bin(int (m1 ,2) - int(m2, 2))[2:]
        
    print(' '*10 + m2)
    print(' '*10 + 24*'_')
    print(' '*10 + m3)
    return m3

import math
def main():
    a, b = float(input("Enter A:\n")), float(input("Enter B:\n"))
    if abs(a) < abs(b):
        a, b = b, a 
    x1, s1, e1, m1 = convert(a)
    x2, s2, e2, m2 = convert(b)
    e3 = 0
    if e1 > e2:
        e3 = e1 
    else:
        e3 = e2
    print(str(a) + " in IEEE754: " + str(x1))
    print(str(b) + " in IEEE754: " + str(x2))
    print("Shift mantissa2 on: " + str(e1 - e2))
    m3 = sum_ieee(s1, s2, e1, e2, m1, m2)
    if len(m3) >= 24: 
        m3 = m3[:-1]
    s3 = 0
    if s1+s2 == 1:
        s3=1
    print(e3)
    print("Result: " + str(s3) + bin(e3 + 127)[2:] + m3[1:])

if __name__ == '__main__':
    main()