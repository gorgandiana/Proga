import random

def first_phrase():
    with open('nouns_1.txt','r',encoding='utf-8')as f:
        nouns_1 = f.readlines()
        noun_1 = random.choice(nouns_1)
#существительное 3 слога
    with open ('verbs.txt','r',encoding='utf-8') as f:
        verbs = f.readlines()
        verb = random.choice(verbs)
#глагол 2 слога
    return noun_1.replace('\n','') + ' ' + verb.replace('\n','') + '.'
print(first_phrase())


def second_phrase():
    with open ('nouns_2.txt','r',encoding='utf-8')as f:
        nouns_2 = f.readlines()
        noun_2 = random.choice(nouns_2)
#существительное 3 слога
    with open ('pronouns.txt','r',encoding='utf-8')as f:
        pronouns = f.readlines()
        pronoun = random.choice(pronouns)
#местоимение 2 слога
    with open ('verbs.txt','r',encoding='utf-8') as f:
        verbs = f.readlines()
        verb = random.choice(verbs)
#глагол 2 слога
    return noun_2.replace('\n','') + ' ' + pronoun.replace('\n','') + ' ' + verb.replace('\n','')
print(second_phrase())


def third_phrase():
    with open ('adjectives.txt','r',encoding='utf-8')as f:
        adjectives = f.readlines()
        adjective = random.choice(adjectives)
#прилагательное 2 слога
    with open('nouns_1.txt','r',encoding='utf-8')as f:
        nouns_1 = f.readlines()
        noun_1 = random.choice(nouns_1)
#существительное 3 слога
    return adjective.replace('\n','') + ' ' + noun_1.replace('\n','') + '.'
print(third_phrase())

def fourth_phrase():
    with open ('nouns_2.txt','r',encoding='utf-8')as f:
        nouns_2 = f.readlines()
        noun_2 = random.choice(nouns_2)
#существительное 3 слога
    with open ('pronouns.txt','r',encoding='utf-8')as f:
        pronouns = f.readlines()
        pronoun = random.choice(pronouns)
#местоимение 2 слога
    with open ('verbs.txt','r',encoding='utf-8') as f:
        verbs = f.readlines()
        verb = random.choice(verbs)
#глагол 2 слога
    return noun_2.replace('\n','') + ' ' + pronoun.replace('\n','') + ' ' + verb.replace('\n','')
print(second_phrase())


def fifth_phrase():
    with open('names.txt','r',encoding='utf-8')as f:
        names = f.readlines()
        name = random.choice(names)
#существительное 3 слога
    marks = [".", "?", "!", "..."]
    mark = random.choice(marks)
    return 'Привет, ' + name.replace('\n','') + mark
print(fifth_phrase())

        
    
       
    

