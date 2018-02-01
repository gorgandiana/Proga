word = input('Введите слово: ')
vowels = ['а','о','у','ю','э','я','ы','е','и','ё']    #после каждой гласной должна выводится "с" и та гласная
for vowel in word:
    if vowel in vowels:
        vowel = vowel+'с'+vowel
        print(vowel,end='')
    else:
            print(vowel,end='')
    
   
 
