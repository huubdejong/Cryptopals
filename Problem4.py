import operator

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
    scores = []
    for i in range(256):
        input_bytes = bytearray.fromhex(string_in)
        decoded_bytes = [input_bytes[j] ^ i for j in range(len(input_bytes))]
        cur_score = score_bytes(decoded_bytes)
        scores.append([cur_score, bytearray(decoded_bytes), string_in, chr(i)])
    
    sorted_guesses = sorted(scores, key=operator.itemgetter(0), reverse=True)
    #for line in sorted_guesses[:5]:
        #print(line[1].decode("utf-8"))
    return sorted_guesses[:1]
    #print("Best guess: " + str(best_key) + ", gives: " + decoded.decode("utf-8"))



with open("strings.txt") as f:
    lines = f.readlines()

all_guesses = []
for line in lines: 
    all_guesses += find_key(line)

best_guesses = sorted(all_guesses, key=operator.itemgetter(0), reverse=True)[0:10]
for guess in best_guesses:
    try:
        print(guess[1].decode())
    except:
        print("This string does not get XOR'ed to an ascii string")
    print(guess[2] + ", " + guess[3])

    