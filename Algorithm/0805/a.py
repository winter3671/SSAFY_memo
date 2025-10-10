word = input()
lower_word = word.lower()

word_list = [0] * 26
gap = ord('a')   # 0 = ord('a') - gap

for i in range(0, 26):
    for j in range(len(lower_word)):
        if ord(lower_word[j]) - gap == i:
            word_list[i] += 1

count = 0

for i in range(1, len(word_list)):
    if max(word_list) == word_list[i]:
        count += 1

    if count == 2:
        break

if count == 2:
    print('?')
else:
    print((chr(word_list.index(max(word_list))+gap)).upper())