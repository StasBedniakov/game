print('Компьютер угадает Ваше число. \nДля этого давай договоримся в каких пределах может быть число: ')
number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))

if number1 > number2:
    left_border = number2
    right_border = number1 + 1
else:
    left_border = number1
    right_border = number2 + 1
print(left_border, right_border)
while True:
    guess_number = (right_border + left_border) // 2
    print('Ваше число:', guess_number, '?')
    print('Если Ваше число: \nбольше нажмите 1, \nменьше нажмите 2, \nравно нажмите 3:')
    print(left_border, right_border)
    answer = int(input('Ваш выбор: '))
    while (answer != 1) and (answer != 2) and (answer != 3):
        print('Пожалуйста проверьте правильность ввода!')
        print('Я предполагаю, что Ваше число:', guess_number)
        print('Если Ваше число: \nбольше нажмите 1, \nменьше нажмите 2, \nравно нажмите 3')
        answer = int(input())
    if answer == 1:
        left_border = guess_number
    elif answer == 2:
        right_border = guess_number
    else:
        print('Компьютер угадал! Компьютер молодец.')
        break

