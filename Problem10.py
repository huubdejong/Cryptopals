import base64
from Crypto.Cipher import AES
import binascii

file = """I'm back and I'm ringin' the bell 
A rockin' on the mike while the fly girls yell 
In ecstasy in the back of me 
Well that's my DJ Deshay cuttin' all them Z's 
Hittin' hard and the girlies goin' crazy 
Vanilla's on the mike, man I'm not lazy. 

I'm lettin' my drug kick in 
It controls my mouth and I begin 
To just let it flow, let my concepts go 
My posse's to the side yellin', Go Vanilla Go! 

Smooth 'cause that's the way I will be 
And if you don't give a damn, then 
Why you starin' at me 
So get off 'cause I control the stage 
There's no dissin' allowed 
I'm in my own phase 
The girlies sa y they love me and that is ok 
And I can dance better than any kid n' play 

Stage 2 -- Yea the one ya' wanna listen to 
It's off my head so let the beat play through 
So I can funk it up and make it sound good 
1-2-3 Yo -- Knock on some wood 
For good luck, I like my rhymes atrocious 
Supercalafragilisticexpialidocious 
I'm an effect and that you can bet 
I can take a fly girl and make her wet. 

I'm like Samson -- Samson to Delilah 
There's no denyin', You can try to hang 
But you'll keep tryin' to get my style 
Over and over, practice makes perfect 
But not if you're a loafer. 

You'll get nowhere, no place, no time, no girls 
Soon -- Oh my God, homebody, you probably eat 
Spaghetti with a spoon! Come on and say it! 

VIP. Vanilla Ice yep, yep, I'm comin' hard like a rhino 
Intoxicating so you stagger like a wino 
So punks stop trying and girl stop cryin' 
Vanilla Ice is sellin' and you people are buyin' 
'Cause why the freaks are jockin' like Crazy Glue 
Movin' and groovin' trying to sing along 
All through the ghetto groovin' this here song 
Now you're amazed by the VIP posse. 

Steppin' so hard like a German Nazi 
Startled by the bases hittin' ground 
There's no trippin' on mine, I'm just gettin' down 
Sparkamatic, I'm hangin' tight like a fanatic 
You trapped me once and I thought that 
You might have it 
So step down and lend me your ear 
'89 in my time! You, '90 is my year. 

You're weakenin' fast, YO! and I can tell it 
Your body's gettin' hot, so, so I can smell it 
So don't be mad and don't be sad 
'Cause the lyrics belong to ICE, You can call me Dad 
You're pitchin' a fit, so step back and endure 
Let the witch doctor, Ice, do the dance to cure 
So come up close and don't be square 
You wanna battle me -- Anytime, anywhere 

You thought that I was weak, Boy, you're dead wrong 
So come on, everybody and sing this song 

Say -- Play that funky music Say, go white boy, go white boy go 
play that funky music Go white boy, go white boy, go 
Lay down and boogie and play that funky music till you die. 

Play that funky music Come on, Come on, let me hear 
Play that funky music white boy you say it, say it 
Play that funky music A little louder now 
Play that funky music, white boy Come on, Come on, Come on 
Play that funky music"""


def PKCS7_padding(bytes_in: bytes, block_size: int):
    out = bytearray(bytes_in)
    offset = block_size - (len(bytes_in) % block_size)
    for i in range(offset):
        out.append(offset)
    return bytes(out)


def xor_bytes(input_bytes, key_bytes):
    out = b''
    for i in range(len(input_bytes)):
        out += bytearray([input_bytes[i] ^ key_bytes[i % len(key_bytes)]])
    return out


def CBC_encrypt(text_bytes, IV, key):
    cipher = AES.new(key, AES.MODE_ECB)
    out = b''
    out += cipher.encrypt(xor_bytes(text_bytes[:16], IV))
    for i in range(16, len(text_bytes), 16):
        out += cipher.encrypt(xor_bytes(out[i-16:i], text_bytes[i:i+16]))
    return out


def CBC_decrypt(cipher_bytes, IV, key):
    cipher = AES.new(key, AES.MODE_ECB)
    l = len(cipher_bytes)
    out = xor_bytes(cipher.decrypt(cipher_bytes[-16:l]), cipher_bytes[-32:-16])
    for i in range(32, l, 16):
        out = xor_bytes(cipher.decrypt(
            cipher_bytes[l - i: l - i + 16]), cipher_bytes[l - i - 16:l - i]) + out
    out = xor_bytes(cipher.decrypt(cipher_bytes[:16]), IV) + out
    return out


#plaintext = base64.b64decode(file)
# print(plaintext)
key = "YELLOW SUBMARINE"
cipher = AES.new(key, AES.MODE_ECB)
plaintext = bytes(file, "utf-8")
s = CBC_encrypt(plaintext, b'\x00\x00\x00\x00\x00\x00\x00\x00', key)
print(s)

print(CBC_decrypt(s, b'\x00\x00\x00\x00\x00\x00\x00\x00', key))


input_bytes = bytearray.fromhex("1c0111001f010100061a024b53535009181c")
key_bytes = bytearray.fromhex("686974207468652062756c6c277320657965")

print(binascii.hexlify(xor_bytes(input_bytes, key_bytes)))
