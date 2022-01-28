import base64

with open("/Users/huubdejong/Documents/Programming/Cryptopals/problem8.txt", 'r') as file:
    lines = file.readlines()

i = 0
scores = {}
for line in lines:
    l = []
    for byte in base64.b64decode(line):
        if not byte in l:
            l.append(byte)

    scores[i] = [len(l), line]
    i += 1

sorted = sorted(scores.items(), key=lambda x: x[1][0])
for i in sorted[:3]:
    print("Likely to be AES encrypted is line " +
          str(i[0]) + ": " + i[1][1])
