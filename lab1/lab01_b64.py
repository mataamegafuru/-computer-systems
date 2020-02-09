def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def to_b64 (num):
    count = 0
    count2 = 0
    bits = text_to_bits(num)
    print(len(bits)/6)
    bysix = [[]]
    for i in bits:
        if ((count2 == 0 and count == 6) or (count2 != 0 and count == 5)):
            bysix.append([])
            count = 0
            count2 += 1
            bysix[count2].append(i)
        else:
            bysix[count2].append(i)
            count += 1
    for i in range(len(bysix)):
        bysix[i] = ''.join(map(str, bysix[i]))
    add = 0
    if len(bysix[len(bysix) - 1]) != 6:
        add = 6 - len(bysix[len(bysix) - 1])
        bysix[len(bysix) - 1] += '0' * add

    print(bysix)
    pull = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    cod = ''
    for i in bysix:
        cod += pull[int(i, 2)]
    cod += '=' * (int(add / 2))
    print(cod)
    return cod


file_name = input("Enter file name: ")
with open(file_name, 'r', encoding='utf-8') as text:
    with open('your_file_inb64.txt', 'w') as text2:
        string = text.read()
        base64 = to_b64(string)
        text2.write(base64)
        print(len(string), len(base64))
