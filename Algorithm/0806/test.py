word = input()


def word_pop(word):
    list_word = list(word)
    word_save = list(word)
    empty_list = []

    for _ in range(len(list_word)):
        empty_list.append(list_word.pop())
       
    if word_save == empty_list:
        return 1
    else:
        return 0

print(word_pop(word))