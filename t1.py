#пример с сайта питона 
def fib(n):
    """ Выводит строку с последовательностью Фибоначи в пределе N значения """
    a, b = 0, 1
    while a < n :
        print(a, end=' ')
        a, b = b, a+b 
    print()


#отработка ошибки ввода
while True:      
    try:
        fib(int(input('Величина последоовательности фибоначи: '))) 
        print('Ok...')
    except ValueError: 
        print('Не то пальто')
    else:
        print('Done')
        break

