# По условиям: на вход нам приходит строка, содержащая только символы скобок. 
# Следующие символы скобочек: ( ) { } [ ]. 
# Необходимо написать функцию, которая проверит такую строку и вернет в результате true или false 
# — в зависимости от того, является ли данная последовательность скобок валидной или нет. 

def isValidBracketRow(stroka): 
    """ Фунциия проверяет валидность последовательности скобочек в строке. 
        Возвращает логическую переменную. 
    """
    stack = [] 
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for i in range(len(stroka)) :
        current = stroka[i]
        if (isClosedBracket(current)) :
            if brackets[current] != stack.pop() :
                return(False)
        else :
            stack.append(current)


def isClosedBracket(simvol) :
    if (simvol.find(')', ']', '}')) > -1 :
        return(simvol.find(')',']','}'))

print(isValidBracketRow(input('Введите строку из символов [] {} (): ')))