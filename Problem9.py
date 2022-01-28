
txt = "YELLOW SUBMARINE"


def PKCS7_padding(bytes_in: bytes, block_size: int):
    out = bytearray(bytes_in)
    offset = block_size - (len(bytes_in) % block_size)
    print(bytes(offset))
    for i in range(offset):
        out.append(offset)
        print(out)
    return out


print(PKCS7_padding(bytes(txt, "utf-8"), 20))
