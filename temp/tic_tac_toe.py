import os
import random


def show(_field):
    os.system('clear')
    print(_field[1], '|', _field[2], '|', _field[3])
    print('- + - + -')
    print(_field[4], '|', _field[5], '|', _field[6])
    print('- + - + -')
    print(_field[7], '|', _field[8], '|', _field[9])


def add(_number, _tour, _field):
    _field[_number] = _tour


def next_tour(_tour):
    return 'X' if _tour == 'O' else 'O'


def check_win(_field, _tour):
    if _field[1] == _field[2] == _field[3] or \
            _field[4] == _field[5] == _field[6] or \
            _field[7] == _field[8] == _field[9] or \
            _field[1] == _field[4] == _field[7] or \
            _field[2] == _field[5] == _field[8] or \
            _field[3] == _field[6] == _field[9] or \
            _field[1] == _field[5] == _field[9] or \
            _field[3] == _field[5] == _field[7]:
        return _tour
    else:
        return None


field = {
    1: '1', 2: '2', 3: '3',
    4: '4', 5: '5', 6: '6',
    7: '7', 8: '8', 9: '9'}

tour = 'O'
how_win = None
_duo = 'N'
start = None


def duo():
    os.system('clear')
    global _duo
    global start
    _duo = input('play alone, or auto (Y/N/A): ').lower()
    if _duo == 'y':
        while start not in ('O', 'X'):
            start = input('Choose your character O/X: ').upper()
    if _duo == 'a':
        start = ''


def main():
    duo()

    global tour, how_win
    empty_field = 9
    used = []
    not_used = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    first, move = True, [1, 3, 5, 7, 9]

    while empty_field > 0:
        show(field)

        number = 0
        if _duo in ('y', 'a'):
            if tour == start:
                while number not in field or number in used:
                    number = int(input('Where add '+tour+': '))
                used.append(number)
                not_used.remove(number)
                if first:
                    if number in move:
                        move.remove(number)
            else:
                if first:
                    first = False
                    number = random.choice(move)
                else:
                    for i in not_used:
                        tmp_filed = field.copy()
                        add(i, tour, tmp_filed)
                        if check_win(tmp_filed, tour):
                            number = i
                            break
                    else:
                        for i in not_used:
                            opponent_tour = next_tour(tour)
                            tmp_filed = field.copy()
                            add(i, opponent_tour, tmp_filed)
                            if check_win(tmp_filed, opponent_tour):
                                number = i
                                break
                        else:
                            number = random.choice(not_used)
                not_used.remove(number)
                used.append(number)
        else:
            while number not in field or number in used:
                number = int(input('Where add ' + tour + ': '))
            used.append(number)

        add(number, tour, field)
        empty_field -= 1

        how_win = check_win(field, tour)
        if how_win is not None:
            break

        tour = next_tour(tour)

    end()


def end():
    show(field)
    if how_win is None:
        print('draw')
    else:
        print('winner is', tour)


def new():
    global field, how_win, tour
    field = {
        1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6',
        7: '7', 8: '8', 9: '9'}
    how_win = None
    tour = 'O'


while True:
    main()
    if not input('press enter to exit, or other key to play again: '):
        break
    new()
