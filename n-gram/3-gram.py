import codecs

def count_n_words(n):
    if (len(words) >= n):
        for i in range (n - 1, len(words) - 1):
            key = words[i - 1] + ' _ ' + words[i]
            if (n == 3):
                key = words[i - 2] + ' _ ' + key
            if (key in c[n - 2]):
                c[n - 2][key] += 1
            else:
                c[n - 2][key] = 1

file =  codecs.open('all_word_segmented_news.u8.txt', 'r', 'utf-8')

c = [{},{}]

for line in file:
    line = line.replace(' _ ', ' ')
    words = line.split(' ')
    count_n_words(2)
    count_n_words(3)

n = 0
for c33 in c[1]:
    c33_split = c33.split(' _ ')
    c33_join = c33_split[0] + ' _ ' + c33_split[1]
    n += 1
    print(str(n) + ' ' + c33 + ': ' + str(c[1][c33] * 1.0 / c[0][c33_join]))