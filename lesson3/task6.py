def int_func(word):
    return word.title()


def string_of_words(strings):
    words = strings.split()
    for index, word in enumerate(words):
        words[index] = int_func(word)
    return " ".join(words)


string = input('Введите строку слов: ')
result = string_of_words(string)
print(f'Каждое введенное слово начинается с заглавной буквы: {result}')
