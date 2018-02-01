i = input('Введите число ')
my_min = int(i)
my_max = int(i)
s = int(i)    #сумма всех введенных чисел
k = 1        #количество введенных чисел

while i != "":
    i = input('Введите число ')
    if i != "":
        s = s + int(i)
        k = k +1
        if int(i) > my_max:
            my_max = int(i)
        if int(i) < my_min:
            my_min = int(i)
   
print('Среднее арифметическое')
print(int(s)/k)        
print('max=')
print(my_max)
print('min=:')
print(my_min)
