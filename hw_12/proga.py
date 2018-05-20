#Программа должна обходить всё дерево папок,
#начинающееся с той папки, где она находится,
#и сообщать следующую информацию (далее - по вариантам):
#в какой папке лежит больше всего файлов.
import os
start_path = '.'
max = 0
for root, dirs, files in os.walk(start_path):
    print('Где мы сейчас', root)
    print('Папки на этом уровне', dirs)
    print('Файлы на этом уровне', files) 
    number_files = len(files) 
    print(number_files)
    
    if len(files)> max:
        max = len(files)
        folder = root
print(folder)       
print('Папка с наибольшим количеством файлов')

