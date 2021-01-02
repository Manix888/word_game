import random
word = input('> ').lower()  # ввод слова
rus_dict = open('word_rus.txt', 'r', encoding='utf-8')  # открытие словаря
rus_dict = rus_dict.readlines()  # чтение
rus_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'э', 'ю', 'я']

answer_letter = word[-1]  # буква, на которую должно начинаться ответное слово
check_letter = rus_alphabet[
    rus_alphabet.index(answer_letter) + 1]  # буква, которая находится следующей по алфавиту от {answer_letter}

first_words = ['абажур', 'баба-яга', 'вабик', 'габардин', 'даба', 'евангелик', 'ёкание', 'жабник', 'забавник', 'ибер',
               'йеменец', 'кабалист', 'лабардан', 'мавзолей', 'набалдашник', 'оазис', 'пава', 'рабкрин', 'саадак',
               'табак-самосад', 'уанстеп', 'фабианец', 'хабанера', 'цадик', 'чабан', 'шабат', 'щавель', 'эбонит',
               'юань', 'ябедник']


def check_index(let1, word2):  # функция проверки позиции
    index1 = rus_alphabet.index(let1)
    index2 = rus_alphabet.index(word2[0])
    if index1 > index2:
        return True
    elif index1 < index2:
        return False
    else:
        if word2 in first_words:
            return None
        else:
            return False


indexes = []  # переменная с индексами
for letter in [answer_letter, check_letter]:  # бинарный поиск
    l = -1
    r = 34007
    while l + 1 < r:
        mid = (l + r) // 2
        if check_index(letter, rus_dict[mid]) is True:  # если индекс 1 буквы больше 2
            l = mid
        elif check_index(letter, rus_dict[mid]) is False:  # иначе
            r = mid
        else:
            break
    indexes.append(r)

letter_dict = rus_dict[indexes[0]:indexes[1]]
ans = ''
for i in range(len(letter_dict) if len(letter_dict) < 25 else 25):
    ans += f'{random.choice(letter_dict)}'
print(f'Ответы:\n{ans}')
