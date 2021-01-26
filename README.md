# Word game
![Python](https://img.shields.io/badge/-Python-090909?style=for-the-badge&logo=python&logoColor=F7CE43)
![Colorama](https://img.shields.io/badge/-colorama-090909?style=for-the-badge)

**Код для игры в слова**.

# Требования
- **Python**
- **Colorama**
    ``` 
    $ pip install colorama 
    ```

# Запуск
Скачиваете файлы [main.py](https://raw.githubusercontent.com/Manix888/word_game/master/main.py) и `txt` файлы [word_rus.txt](https://raw.githubusercontent.com/Manix888/word_game/master/word_rus.txt) [word_eng](https://raw.githubusercontent.com/Manix888/word_game/master/word_eng.txt) (переходите по ссылке и нажимаете `Ctrl`+`S`). Все скачанные файлы помещаете их в одну директорию (папку) и запускаете `main.py`.

# Особенности
В коде используется алгоритм [бинарного (двоичного) поиска](https://ru.wikipedia.org/wiki/Двоичный_поиск). Благодаря ему в коде вместо `34000` итераций проходит всего `30`.

Также в коде используется цветной вывод. Каждое слово подсвечено своим цветом:
- Зеленый — _короткие_ слова
- Желтый — слова _средней длины_
- Красный — _длинные_ слова

Основной код поддерживает два языка: `английский` и `русский`. Если вам нужен только один из этих языков, то просто переходите в нужную папку ([eng](https://github.com/Manix888/word_game/tree/master/eng_only) / [rus](https://github.com/Manix888/word_game/tree/master/rus_only))

# Пример работы
![Example](https://github.com/Manix888/word_game/blob/master/assets/Example.png)

# Контакты
Если у вас есть идея или у вас появилась ошибка в коде, то пишите на мой Discord:

[![Discord](https://img.shields.io/badge/-My_Discord-090909?style=for-the-badge&logo=discord&logoColor=5B72BF)](https://discordapp.com/users/692313869057785886)<br>
(**Erkin#3217**)