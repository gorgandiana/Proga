

def read():
    with open(str(input('Введите название файла на английском: ')), encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        return words


def spl(words):
    count = 0
    for word in words:
        if word.startswith("un") != 0:
            count = count + 1
    return count

def pol(words):
    count2 = 0   #сколько слов на un имеет больше букв чем мы ввели
    pln = int(input('Введите число: '))
    for word in words:
      if (word.startswith("un") != 0)and(len(word) > pln):
          count2 = count2 + 1
    return count2
    

words = read()
a=spl(words)
b=pol(words)
print('Всего слов(un):')
print(a)
print('Процент слов:')
print(b/a*100)
