from itertools import count


# Homewock 9.1
def popular_words (text, words):
    text = text.lower() # приводим строку в нижний регистр
    listWord = text.split() # создаем список слов для поиска популярных
    result = {}
    for i in words: #  цикл который ищет совпадения по словам, считает их кал и передает в result
        result[i] = listWord.count(i)
    return result


# Homewock 9.2
def difference  (*args):
    if not args: # проверка если в args елементы
        return 0
    minimum = min(args) #  поиск минимального и максимального числа
    maximum = max(args)

    return round (maximum - minimum, 1) # округление и возвращение промежутка между мин и макс




print("Homeworck 9.1")

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

print("Homeworck 9.2")

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')

