рост = int(input('Введите ваш рост в см: '))
вес = int(input('Введите ваш вес в кг: '))
имт = вес/((рост/100)**2)
if имт <=16:
    print('Выраженный дефицит массы тела')
if имт >16 and имт <18.5:
    print('Недостаточная масса тела')
if имт>18.5 and имт<24.99:
    print('Норма')
if имт>25 and имт<30:
    print('Избыточная масса тела')
if имт>30 and имт<35:
    print('Ожирение первой степени')
if имт>35 and имт<40:
    print('Ожирение второй степени')
if имт>40:
    print('Ожирение третьей степени')
