import codecs

file =  codecs.open('all_word_segmented_news.u8.txt', 'r', 'utf-8')

c2 = {}
c3 = {}

for line in file:
    line = line.replace(' _ ', ' ')
    words = line.split(' ')
    if (len(words) >= 2):
        for i in range (1, len(words) - 1):
            key = words[i - 1] + ' _ ' + words[i]
            if (key in c2):
                c2[key] += 1
            else:
                c2[key] = 1
    if (len(words) >= 3):
        for i in range (2, len(words) - 1):
            key = words[i - 2] + ' _ ' + words[i - 1] + ' _ ' + words[i]
            if (key in c3):
                c3[key] += 1
            else:
                c3[key] = 1

n = 0
for c33 in c3:
    c33_split = c33.split(' _ ')
    c33_join = c33_split[0] + ' _ ' + c33_split[1]
    n += 1
    print(str(n) + ' ' + c33 + ': ' + str(c3[c33] * 1.0 / c2[c33_join]))