i = input('Введите число ')
mymin = int(i)
mymax = int(i)
s = int(i)    #сумма всех введенных чисел
k = 1        #количество введенных чисел

while i != "":
    i = input('Введите число ')
    if i != "":
        s = s + int(i)
        k = k +1
        if int(i) > mymax:
            mymax = int(i)
        if int(i) < mymin:
            mymin = int(i)
   
print('Среднее арифметическое')
print(int(s)/k)        
print('max=')
print(mymax)
print('min=:')
print(mymin)
