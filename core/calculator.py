from decorators import cache_decorator

functions = {
    '+' : lambda x, y: x + y,
    '-' : lambda x, y: x - y, 
    '*' : lambda x, y: x * y,
    '/' : lambda x, y: x / y if y != 0 else None,
    '**' : lambda x, y: x**y
}

@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    try:
        result = functions[operation](a,b)
    except KeyError:
        return 'Введена некорректная операция'
    else:
        return result

while(True):
    if __name__ == '__main__':
        try:
            a = int(input('Введите число: ')) # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
            b = int(input('Введите число: '))
        except ValueError:
            print("Ошибка ввода данных. Выход")
        else:
            operation = input('Введите операцию')
            print('Результат: ', calculator(a, b, operation))
    
    
