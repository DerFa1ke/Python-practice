#пример 1 
def fib(n):
    a, b = 0, 1
    while a < n :
        print(a, end=' ')
        a, b = b, a+b 
    print()
fib(1000)

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











# #пример 2 
# fruits = ['Banana', 'Apple', 'Lime']
# loud_fruits = [fruits.upper() for fruits in fruits]
# print(loud_fruits)
# print(list(enumerate(fruits)))

# #пример 4 
# print("Hello, I'm Python!")
# name = input('Type ur name\n') 
# print('Hi, %s.' % name)

