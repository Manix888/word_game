import random
from colorama import init, Fore

init(autoreset=True)
rus_dict = open('word_rus.txt', 'r', encoding='utf-8')  # открытие словаря
rus_dict = rus_dict.readlines()  # чтение
rus_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'э', 'ю', 'я']

first_words = ['абажур', 'баба-яга', 'вабик', 'габардин', 'даба', 'евангелик', 'ёкание', 'жабник', 'забавник', 'ибер',
               'йеменец', 'кабалист', 'лабардан', 'мавзолей', 'набалдашник', 'оазис', 'пава', 'рабкрин', 'саадак',
               'табак-самосад', 'уанстеп', 'фабианец', 'хабанера', 'цадик', 'чабан', 'шабат', 'щавель', 'эбонит',
               'юань', 'ябедник']


while True:
    word = input('> ').lower()  # ввод слова
    answer_letter = word[-1]  # буква, на которую должно начинаться ответное слово
    if answer_letter in ['ъ', 'ы', 'ь']:
        answer_letter = word[-2]
    check_letter = 'а'
    if answer_letter != 'я':
        check_letter = rus_alphabet[
            rus_alphabet.index(answer_letter) + 1]  # буква, которая находится следующей по алфавиту от {answer_letter}


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


    iterations = 0
    indexes = []  # переменная с индексами
    for letter in [answer_letter, check_letter]:  # бинарный поиск
        left = -1
        right = 34007
        while left + 1 < right:
            mid = (left + right) // 2
            if check_index(letter, rus_dict[mid]) is True:  # если индекс 1 буквы больше 2
                left = mid
            elif check_index(letter, rus_dict[mid]) is False:  # иначе
                right = mid
            else:
                break
            iterations += 1
        indexes.append(right)

    if answer_letter == 'я':
        indexes[1] = 34007
    letter_dict = rus_dict[indexes[0]:indexes[1]]
    ans = ''

    for i in range(len(letter_dict) if len(letter_dict) < 10 else 10):
        choice = random.choice(letter_dict)
        if len(choice) <= 6:
            ans += Fore.GREEN + f'{choice}'
        elif len(choice) <= 10:
            ans += Fore.YELLOW + f'{choice}'
        else:
            ans += Fore.RED + f'{choice}'
        letter_dict.remove(choice)

    print(f'Решение:\n{ans}')
    print(f'Поиск слов выполнен за ' + Fore.GREEN + f'{iterations}' + Fore.RESET + ' итераций бинарного поиска\n')
    if input('Продолжить (Y/N)? > ').lower() in ['n', 'н']:
        break
