from colorama import Fore, Back, Style
import doors, riddles
from difflib import SequenceMatcher
import time
import sys
from rich.console import Console
import time

start_time = time.time()

console = Console()

console.print('\n')

def welcome_message():
    console.print('\n' * 50)
    console.print('[blue][on blue]Дед мороз потерял подарки![/blue][/on blue]')
    console.print('[blue]Помогите ему найти их! Они находятся за дверьми, однако, вас ждут загадки![/blue]')
    console.print('[black]Нажмите Enter, чтобы начать![/black]')

    waiting()

def waiting():
    input()
    console.print('\n')
    game()

def door_chooser(chosen_door):
    best_similarity = 0
    best_index = None

    for i, door_name in enumerate(doors.possible_doors):
        similarity = SequenceMatcher(None, chosen_door.lower(), door_name.lower()).ratio()
        if similarity > best_similarity:
            best_similarity = similarity
            best_index = i

    return best_index if best_similarity > 0.6 else None

def similarity(chosen_door, b):
    return SequenceMatcher(None, chosen_door, b).ratio()

def game():
    if not doors.doors_amount:
        console.print('[green]Поздравляем! Все двери пройдены![/green]')
        game_over()

    console.print('[blue]Выберите дверь![/blue]')
    console.print('[yellow]Доступные двери:[/yellow]')
    for i, door_name in enumerate(doors.doors_amount):
        console.print(f'{i + 1}. {door_name}')

    chosen_door = str(input('Введите название: ')).lower()

    door_index = door_chooser(chosen_door)

    if door_index is not None:
        console.print(f'[green]Вы выбрали дверь: {doors.doors_amount[door_index]}[/green]')
        riddle_chooser(door_index)
    else:
        console.print('[red]Не удалось найти подходящую дверь. Попробуйте ещё раз![/red]')
        game()


def riddle_chooser(door_index):
    match doors.possible_doors[door_index]:
        case 'снеговик':
            riddles.snowman()
        case 'снегурочка':
            riddles.snegurochka()
        case 'волшебник':
            riddles.wizard()
        case 'снежинка':
            riddles.snowflake()
    
    # Удаляем элементы из обоих списков синхронно
    del doors.possible_doors[door_index]
    del doors.doors_amount[door_index]
    console.print('[green]Дверь успешно пройдена![/green]')
    time.sleep(1)
    game()

def game_over():
    console.print('\n')
    console.print('[bold][red]Дед мороз:[/bold][/red]' + '[bold][blue] Спасибо за то что помог мне найти подарки![/bold][/blue]')
    console.print('[bold][red]Дед мороз:[/bold][/red]' + '[bold][blue] Ну, а мне пора уходить, до свидания![/bold][/blue]')
    console.print('\n')
    console.print('[bold][green]ИГРА ОКОНЧЕНА![/bold][/green]')
    console.print(f'Вы потратили {time.time() - start_time} секунд')
    sys.exit()

if len(sys.argv) > 1:
    if sys.argv[1] == 'debug':
        game_over()
else:
    welcome_message()