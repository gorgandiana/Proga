import random

def hint():
    d = {}
    with open("words_hints1.csv", 'r', encoding='utf-8') as f:
        for line in f:
             word, hint = line.strip().split(" ", maxsplit=1)
             d[word] = hint
    return d


def programm(dictionary):
    tries = 0
    key = random.choice(list(dictionary))
    print("Привет!Поиграем? Я буду загадывать слова, а ты, используя подсказки, будешь их угадывать:)\n\
Подсказка:", dictionary[key]," ...")
    attemp = input("Загаданное слово: ")
    while attemp.lower() != key :      
        print("Ответ неправильный")
        attemp = input("Загаданное слово: ")
        tries += 1
    if attemp.lower() == key:
        print("Правильный ответ!")    


programm(hint())
