word = input('Введите слово или фразу на английском: ')
cons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
word = word.lower()
for con in word:
    if con in cons:
        con = con+'aig'
        print(con,end='')
    else:
        print(con,end='')

