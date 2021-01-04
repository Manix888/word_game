import random
from colorama import init, Fore

init(autoreset=True)
eng_dict = open('word_eng.txt', 'r', encoding='utf-8')  # открытие словаря
eng_dict = eng_dict.readlines()  # чтение
eng_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
                'v', 'w', 'x', 'y', 'z']

first_words = ['aachen', 'babble', 'cab', 'dab', 'each', 'faber', 'gab', 'habakkuk', 'iain', 'jab', 'kabul', 'lab', 
               'maastricht', 'naafi', "o'clock", 'pablo', 'qatar', 'rabat', 'sabbath', 'tab', 'ubiquitous', 'vacancies',
               'wad', 'xavier', 'yacht', 'zabaglione']


while True:
    word = input('> ').lower()  # ввод слова
    answer_letter = word[-1]  # буква, на которую должно начинаться ответное слово
    check_letter = 'a'
    if answer_letter != 'z':
        check_letter = eng_alphabet[
            eng_alphabet.index(answer_letter) + 1]  # буква, которая находится следующей по алфавиту от {answer_letter}


    def check_index(let1, word2):  # функция проверки позиции
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
        right = 65135
        while left + 1 < right:
            mid = (left + right) // 2
            if check_index(letter, eng_dict[mid]) is True:  # если индекс 1 буквы больше 2
                left = mid
            elif check_index(letter, eng_dict[mid]) is False:  # иначе
                right = mid
            else:
                break
            iterations += 1
        indexes.append(right)

    if answer_letter == 'z':
        indexes[1] = 65135
    letter_dict = eng_dict[indexes[0]:indexes[1]]
    ans = ''

    for i in range(len(letter_dict) if len(letter_dict) < 20 else 20):
        choice = random.choice(letter_dict)
        if len(choice) <= 6:
            ans += Fore.GREEN + f'{choice}'
        elif len(choice) <= 10:
            ans += Fore.YELLOW + f'{choice}'
        else:
            ans += Fore.RED + f'{choice}'
        letter_dict.remove(choice)

    print(f'Answers:\n{ans}')
    print(f'Word search was performed in ' + Fore.GREEN + f'{iterations}' + Fore.RESET + ' binary search iterations\n')
    if input('Continue (Y/N)? > ').lower() in ['n', 'н']:
        break
