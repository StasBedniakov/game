def guess_number():
    print('Компьютер угадает Ваше число. \nДля этого давай договоримся в каких пределах может быть число: ')
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))

    if number1 > number2:
        left_border = number2
        right_border = number1 + 1
    else:
        left_border = number1
        right_border = number2 + 1

    while True:
        guess_number = (right_border + left_border) // 2
        print('_' * 30)
        print('Ваше число:', guess_number, '?')
        print('Если Ваше число: \nбольше нажмите 1 \nменьше нажмите 2 \nравно нажмите 3 \nДля выхода в главное меню нажмите 0')
        print('_' * 30)
        answer = int(input('Ваш выбор: '))
        while (answer != 0) and (answer != 1) and (answer != 2) and (answer != 3):
            print('Пожалуйста проверьте правильность ввода!')
            print('Я предполагаю, что Ваше число:', guess_number)
            print('Если Ваше число: \nбольше нажмите 1, \nменьше нажмите 2, \nравно нажмите 3 \nДля выхода в главное меню нажмите 0')
            answer = int(input())
        if answer == 1:
            left_border = guess_number
        elif answer == 2:
            right_border = guess_number
        elif answer == 3:
            print('Компьютер угадал! Компьютер молодец.')
            print('_' * 30)
            press = int(input('Чтобы выйти в главное меню нажмите 0'))
            while press != 0:
                press = int(input('Чтобы выйти в главное меню нажмите 0'))
            break
        elif answer == 0:
            print('Выхожу из игры....')
            print('_' * 30)
            break
    main_menu()

def painter_menu():
    print('Приветствую Вас! Хотите чтобы я нарисовал фигуру для Вас? (Пожалуйста пишите прописью)')
    answer = input('Нарисуй: ')
    length = int(input('Введите сторону: '))
    if answer == 'квадрат':
        square(length)
    elif answer == 'треугольник':
        triangle(length)
    else:
        print('Извините, такой фигуры я пока не знаю.')


def square(length):
    for column in range(length):
        for line in range(length):
            print('*', end = ' ')
        print()
    press = int(input('Чтобы выйти в главное меню нажмите 0'))
    while press != 0:
        press = int(input('Чтобы выйти в главное меню нажмите 0'))
    main_menu()

def triangle(length):
    print('Рисунок в разработке.')
    press = int(input('Чтобы выйти в главное меню нажмите 0'))
    while press != 0:
        press = int(input('Чтобы выйти в главное меню нажмите 0'))
    main_menu()

def main_menu():
    print('_' * 10, 'Main Menu', '_' * 10)
    print('Здравствуйте! Вас приветствует компьютер. \nЕсли хотите чтобы компьютер угадал Ваше число нажмите 1 \n Если Вы хотите чтобы я нарисовал нажмите 2\nЕсли хотите выйти нажмите 0')
    print('_' * 30)
    answer = int(input('Ваши действия: '))
    if answer == 0:
        print('_' * 30)
        print('До свидания!')
    elif answer == 1:
        print('_' * 30)
        guess_number()
    elif answer == 2:
        print('_' * 30)
        painter_menu()

main_menu()