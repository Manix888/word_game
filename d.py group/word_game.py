import discord
import random
import datetime
from discord.ext import commands, tasks


# Код
class Word_game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.cog_name = ["Игра_в_слова"]
        self.check.start()
        self.game = {  # Данные игры
            'on': None,
            'channel': None,
            'last_word': None,
            'last_time': None,
            'stats': {
                f'{self.bot.user.id}': 0
            }
        }
        self.rus_dict = open('word_rus.txt', 'r', encoding='utf-8').readlines()
        self.rus_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
                             'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'э', 'ю', 'я']
        self.first_words = ['абажур', 'баба-яга', 'вабик', 'габардин', 'даба', 'евангелик', 'ёкание', 'жабник',
                            'забавник', 'ибер', 'йеменец', 'кабалист', 'лабардан', 'мавзолей', 'набалдашник', 'оазис',
                            'пава', 'рабкрин', 'саадак', 'табак-самосад', 'уанстеп', 'фабианец', 'хабанера', 'цадик',
                            'чабан', 'шабат', 'щавель', 'эбонит', 'юань', 'ябедник']

    @commands.group()
    async def word_game(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title='Игра в слова',
                                  description='Бот начинает играть в слова с участниками сервера.\n'
                                              f'Играть можно только в '
                                              f'{self.bot.get_channel(707145989068292166).mention}!\n\n'  
                                              # ID канала в котором можно играть в слова
                                              '`.word_game start` - Начало игры\n`.word_game stop` - Окончание игры\n'
                                              '`.word_game prompt` - Подсказка\n`.word_game stats` - Статистика',
                                  color=0x00FFE8, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)

    @word_game.command()
    async def start(self, ctx):
        if self.game['on']:
            await ctx.send('Игра в слова уже запущена!')
        else:
            self.game['on'] = True
            a = random.choice(self.rus_alphabet)
            while a in ['ъ', 'ы', 'ь']:
                a = random.choice(self.rus_alphabet)
            word = self.word_search(a)
            self.game['last_word'] = word.rstrip()
            await ctx.send('**Игра в слова запущена! Начинаем!**')
            await ctx.send(word)
            self.game['last_time'] = datetime.datetime.now()
            self.game['channel'] = ctx.channel.id
            print(self.game)

    @word_game.command()
    async def stop(self, ctx):
        if self.game['on']:
            self.game['on'] = None
            await ctx.send('Игра в слова закончилась')
            await ctx.send(embed=self.search_stats())
            self.game['stats'] = {'731049397684535346': 0}

    @word_game.command()
    async def prompt(self, ctx):
        if self.game['on']:
            new_word = self.word_search(self.game['last_word'])
            await ctx.reply(f'Вот возможный ответ: ||{new_word}||')

    @word_game.command()
    async def stats(self, ctx):
        if self.game['on']:
            await ctx.send(embed=self.search_stats())

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.game['on']:
            if message.channel.id in [707145989068292166,
                                      709199971504619581]:  # Тут каналы, в которых можно играть в слова
                if message.author.id != self.bot.user.id:
                    if (len(message.content.split())) == 1:
                        index = -1
                        if self.game['last_word'][index] in ['ъ', 'ы', 'ь']:
                            index = -2
                        if self.game['last_word'][index] == (message.content)[0]:
                            new_word = self.word_search(message.content)
                            self.game['last_word'] = new_word.rstrip()
                            await message.channel.send(new_word)  # бот пишет ответное слово
                            self.game['last_time'] = datetime.datetime.now()
                            self.game['stats']['731049397684535346'] += 1
                            if str(message.author.id) not in self.game['stats']:
                                self.game['stats'][str(message.author.id)] = 1
                            elif str(message.author.id) in self.game['stats']:
                                self.game['stats'][str(message.author.id)] += 1

    @tasks.loop(seconds=10.0)
    async def check(self):  # Цикл, проверяющий последнее время отправки сообщения
        # Если прошло больше 5 минут, то игра заканчивается
        # Может криво работать
        if self.game['on'] is True:
            diff = datetime.datetime.now() - self.game['last_time']
            if diff.seconds // 60 == 5:
                channel = self.bot.get_channel(self.game['channel'])
                await channel.send('Игра в слова автоматически закончилась из-за неактива')
                self.game['on'] = None
                await channel.send(embed=self.search_stats())
                self.game['stats'] = {f'{self.bot.user.id}': 0}

    def search_stats(self):  # Поиск статистики
        e = discord.Embed(title="Статистика игры",
                          description=f"Таблица лидеров:")
        leaders = sorted(self.game['stats'], key=lambda score: self.game['stats'][score],
                         reverse=True)
        position = 1
        for leader in leaders:
            leader = self.bot.get_user(int(leaders[position - 1]))  # Сортировка 4360
            leader_score = self.game['stats'][str(leader.id)]
            e.add_field(name=f"{position} место:", value=f"{leader.mention} | очки: **{leader_score}**",
                        inline=False)
            position += 1
        return e

    def word_search(self, word):  # Логика поиска
        answer_letter = word[-1]  # буква, на которую должно начинаться ответное слово
        if answer_letter in ['ъ', 'ы', 'ь']:
            answer_letter = word[-2]
        check_letter = 'а'
        if answer_letter != 'я':
            check_letter = self.rus_alphabet[
                self.rus_alphabet.index(
                    answer_letter) + 1]  # буква, которая находится следующей по алфавиту от {answer_letter}

        def check_index(let1, word2):  # функция проверки позиции
            index1 = self.rus_alphabet.index(let1)
            index2 = self.rus_alphabet.index(word2[0])
            if index1 > index2:
                return True
            elif index1 < index2:
                return False
            else:
                if word2 in self.first_words:
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
                if check_index(letter, self.rus_dict[mid]) is True:  # если индекс 1 буквы больше 2
                    left = mid
                elif check_index(letter, self.rus_dict[mid]) is False:  # иначе
                    right = mid
                else:
                    break
                iterations += 1
            indexes.append(right)

        if answer_letter == 'я':
            indexes[1] = 34007
        letter_dict = self.rus_dict[indexes[0]:indexes[1]]
        choice = random.choice(letter_dict)
        return choice


def setup(client):
    client.add_cog(Word_game(client))
