# Создаём список букв
print('Шифр Цезаря')
abc ='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
while True:
    string = input('Введите текст:   ')
    if string == '0':
        break
    dec = int(input('Введите 1 для зашифровки, -1 для расшифровки:   '))
    n = int(input('Введите шаг смещения:    '))
    out = ''    #строка вывода
    for i in range(len(string)):
        try:
            index = abc.index(string[i])
            out += abc[(index+n*dec)%33]
        except ValueError:
                try:
                    index = b_abc.index(string[i])
                    out += b_abc[(index+n*dec)%33]
                except ValueError:
                    out += string[i]
    print(out)