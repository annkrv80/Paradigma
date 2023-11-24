import os

field = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def building_field(field):
    print('-------------')
    for i in range(3):
        print('|', field[0 + i * 3], '|', field[1 + i * 3], '|', field[2 + i * 3], '|')
        print('-------------')


def game_move(token):
    valid = False
    while not valid:
        player_move = int(input(f'Куда поставить {token}? '))
        try:
            player_move = int(player_move)
        except:
            print('Некорректный ввод. Введите число')
            continue
        if 1 <= player_move <= 9:
            if str(field[player_move - 1]) not in 'XO':
                field[player_move - 1] = token
                valid = True
            else:
                print('Эта клетка уже занята')
        else:
            print('Введите число от 1 до 9')


def check_win(field):
    win_combination = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                       (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for e in win_combination:
        if field[e[0]] == field[e[1]] == field[e[2]]:
            return field[e[0]]
    return False


count = 0
win = False
while not win:
    building_field(field)
    if count % 2 == 0:
        game_move('X')
    else:
        game_move('O')
    count += 1
    if count > 4:
        tmp = check_win(field)
        if tmp:
            print(f'{tmp}, выиграл!')
            win = True
            break
        if count == 9:
            print('Ничья!')
            break


building_field(field)

# При написании кода процедурная, структурная парадигма.
# Процедурная парадигма основана на вызове процедур.
# Внутри процедур использована структурная парадигма, код структурирован, не используется "goto".
