from colorama import Fore, Back, Style
from difflib import SequenceMatcher
from rich.console import Console
import random

console = Console()

def similarity(users_answer, real_answer):
    return SequenceMatcher(None, users_answer, real_answer).ratio()

score = ['снеговик', 'снегурочка', 'волшебник', 'снежинка']

def snowman():

    if 'снеговик' not in score:
        score.append('снеговик')

    real_answer = 'снежинка'

    snowmans_riddle = '''
    Я белый, мягкий, вечно танцую.
    Я в небе рождаюсь, но на землю я лечу. 
    Кто я такой, от холода не таю?
    Если меня найдёшь, скажи, не подведу!
    '''

    print(Fore.BLUE + Style.BRIGHT + 'Отгадай загадку!' + Style.RESET_ALL)

    print(Fore.WHITE + Back.WHITE + snowmans_riddle + Style.RESET_ALL)
    users_answer = str(input('Введите ответ: '))


    answer_is_correct = False
    while not answer_is_correct:        
        if similarity(users_answer, real_answer) > 0.8:
            print(Fore.GREEN + 'Правильно! Отлично!' + Style.RESET_ALL)
            answer_is_correct = True
            score.pop(score.index('снеговик'))
        else:
            print(Fore.RED + 'Неправильно! Попробуй ещё раз!' + Style.RESET_ALL) # <- prints endlessly
            users_answer = str(input('Введите ответ: '))
    


def snegurochka():

    if 'снегурочка' not in score:
        score.append('снегурочка')

    snegurochka_riddle = '''
    Я светлая и красивая, на праздник я всегда сияю. Без меня Новый год не засияет — что я такое?
    '''

    print(Fore.BLUE + Style.BRIGHT + 'Отгадай загадку!' + Style.RESET_ALL)

    print(Fore.WHITE + Back.WHITE + snegurochka_riddle + Style.RESET_ALL)

    real_word = ['Г', 'И', 'Р', 'Л', 'Я', 'Н', 'Д', 'А']
    guessed_word = ['Г', '_', '_', '_', 'Я', '_', '_', '_']

    while guessed_word != real_word:
        input_letter = str(input('Введите букву: ')).upper()

        if input_letter in real_word:
            indices = [i for i, letter in enumerate(real_word) if letter == input_letter]
            for index in indices:
                guessed_word[index] = input_letter    
            print(Fore.YELLOW + ''.join(guessed_word) + Style.RESET_ALL)
        else:
            print(Fore.RED + 'Неправильная буква. Попробуйте ещё раз!' + Style.RESET_ALL)
        
    
    if guessed_word == real_word:
        print(Fore.GREEN + 'Правильно! Отлично!' + Style.RESET_ALL)
        score.pop(score.index('снегурочка'))
        
def wizard():
    if 'волшебник' not in score:
        score.append('волшебник')

    console.print('[yellow]Волшебник загадал число от 1 до 100. Попробуй угадать![/yellow]')

    secret_number = random.randint(1, 100)
    guess = None

    while guess != secret_number:
        guess = int(input('Введите ваше предположение: '))

        if guess < secret_number:
            console.print('[yellow]Больше![/yellow]')
        elif guess > secret_number:
            console.print('[yellow]Меньше![/yellow]')
        else:
            console.print('[green]Правильно! Отлично![/green]')
            score.pop(score.index('волшебник'))

def snowflake():

    if 'снежинка' not in score:
        score.append('снежинка')

    print(Fore.CYAN + Style.BRIGHT + 'Найди отличающуюся снежинку!' + Style.RESET_ALL)

    print(Fore.CYAN + Style.BRIGHT + '''
      1 | ❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄
      2 | ❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄
      3 | ❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄
      4 | ❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄
      5 | ❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❅❄
    ''')

    users_answer = input('Введите позицию снежинки:')
    answer_is_correct = False
    while not answer_is_correct:
        if users_answer == '5.29':
            console.print('[green]Правильно! Отлично![/green]')
            answer_is_correct = True
            score.pop(score.index('снежинка'))
        else:
            console.print('[red]Неправильно! Попробуй ещё раз![/red]')
            users_answer = (input('Введите позицию снежинки (пример: 2.23 (2 ряд 23 колонка)):'))
