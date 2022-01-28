
def score_bytes(array):
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(array[i]).lower(), 0) for i in range(len(array))])


def find_key(string_in):
    max_score = 0
    best_key = 0
    decoded = b''
    for i in range(256):
        input_bytes = bytearray.fromhex(string_in)
        decoded_bytes = [input_bytes[j] ^ i for j in range(len(input_bytes))]
        cur_score = score_bytes(decoded_bytes)
        if cur_score > max_score:
            max_score = cur_score
            best_key = i
            decoded = bytearray(decoded_bytes)
    print("Best guess: " + str(best_key) + ", gives: " + decoded.decode("utf-8"))

s1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
find_key(s1)

