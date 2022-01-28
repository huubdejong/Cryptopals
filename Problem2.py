bhex = "0123456789abcdef"
bits = ['0000', '0001','0010', '0011', '0100','0101', '0110', '0111', '1000','1001']


def hex_dig_to_bin(c):
    if c.isdigit():
        return bits[int(c)]
    if c == 'a': return "1010"
    if c == 'b': return "1011"
    if c == 'c': return "1100"
    if c == 'd': return "1101"
    if c == 'e': return "1110"
    if c == 'f': return "1111"

def hex_to_bin(s):
    out = ""
    for c in s:
        out += hex_dig_to_bin(c)
    return out

def bin_to_hex(s):
    i = 0
    out = ""
    while i < len(s):
        val = 0
        for j in range(4):
            #print(2**(5-j))
            val += int(s[i+j])*(2**(3-j))
            #print(val)
        out += bhex[val]
        i += 4
    return out

def XOR(d1, d2):
    if d1 != d2: return "1"
    return "0"

def string_XOR(s1, s2):
    s1 = hex_to_bin(s1)
    s2 = hex_to_bin(s2)
    out = ""
    for i in range(len(s1)):
        out += str(XOR(s1[i],s2[i]))
    return bin_to_hex(out)

print(string_XOR("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"))
    
