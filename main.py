import random
from colorama import init, Fore

init(autoreset=True)

# Russian
rus_dict = open('word_rus.txt', 'r', encoding='utf-8')
rus_dict = rus_dict.readlines()
rus_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'э', 'ю', 'я']
# English
eng_dict = open('word_eng.txt', 'r', encoding='utf-8')
eng_dict = eng_dict.readlines()  # чтение
eng_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

first_words = ['абажур', 'баба-яга', 'вабик', 'габардин', 'даба', 'евангелик', 'ёкание', 'жабник', 'забавник', 'ибер',
               'йеменец', 'кабалист', 'лабардан', 'мавзолей', 'набалдашник', 'оазис', 'пава', 'рабкрин', 'саадак',
               'табак-самосад', 'уанстеп', 'фабианец', 'хабанера', 'цадик', 'чабан', 'шабат', 'щавель', 'эбонит',
               'юань', 'ябедник', 'aachen', 'babble', 'cab', 'dab', 'each', 'faber', 'gab', 'habakkuk', 'iain', 'jab',
               'kabul', 'lab', 'maastricht', 'naafi', "o'clock", 'pablo', 'qatar', 'rabat', 'sabbath', 'tab',
               'ubiquitous', 'vacancies', 'wad', 'xavier', 'yacht', 'zabaglione']

while True:
    word = input('> ').lower()  # ввод слова
    answer_letter = word[-1]  # буква, на которую должно начинаться ответное слово
    language = ''
    if answer_letter in rus_alphabet:
        language = 'rus'
    else:
        language = 'eng'

    check_letter = ''
    if language == 'eng':
        check_letter = 'a'
        if answer_letter != 'z':
            check_letter = eng_alphabet[
                eng_alphabet.index(
                    answer_letter) + 1]  # буква, которая находится следующей по алфавиту от {answer_letter}
    else:
        if answer_letter in ['ъ', 'ы', 'ь']:
            answer_letter = word[-2]
        check_letter = 'а'
        if answer_letter != 'я':
            check_letter = rus_alphabet[
                rus_alphabet.index(
                    answer_letter) + 1]  # буква, которая находится следующей по алфавиту от {answer_letter}


    def check_index(let1, word2, lang):  # функция проверки позиции
        if lang == 'rus':
            index1 = rus_alphabet.index(let1)
            index2 = rus_alphabet.index(word2[0])
        else:
            index1 = eng_alphabet.index(let1)
            index2 = eng_alphabet.index(word2[0])

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
        if language == 'eng':
            right = 65135
        while left + 1 < right:
            mid = (left + right) // 2
            if language == 'rus':
                check_answer = check_index(letter, rus_dict[mid], language)
            else:
                check_answer = check_index(letter, eng_dict[mid], language)
            if check_answer is True:  # если индекс 1 буквы больше 2
                left = mid
            elif check_answer is False:  # иначе
                right = mid
            else:
                break
            iterations += 1
        indexes.append(right)

    letter_dict = None
    if language == 'eng':
        if answer_letter == 'z':
            indexes[1] = 65135
        letter_dict = eng_dict[indexes[0]:indexes[1]]
    else:
        if answer_letter == 'я':
            indexes[1] = 34007
        letter_dict = rus_dict[indexes[0]:indexes[1]]
    ans = ''

    for i in range(len(letter_dict) if len(letter_dict) < 15 else 15):
        choice = random.choice(letter_dict)
        if len(choice) <= 6:
            ans += Fore.GREEN + f'{choice}'
        elif len(choice) <= 10:
            ans += Fore.YELLOW + f'{choice}'
        else:
            ans += Fore.RED + f'{choice}'
        letter_dict.remove(choice)

    if language == 'rus':
        print(f'Решения:\n{ans}')
        print(f'Поиск слов выполнен за ' + Fore.GREEN + f'{iterations}' + Fore.RESET + ' итераций бинарного поиска\n')
        if input('Продолжить (Y/N)? > ').lower() in ['n', 'н']:
            break
    else:
        print(f'Answers:\n{ans}')
        print(f'Word search was performed in ' + Fore.GREEN + f'{iterations}' + Fore.RESET +
              ' binary search iterations\n')
        if input('Continue (Y/N)? > ').lower() in ['n', 'н']:
            break
