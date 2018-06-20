#(5 баллов). Для каждого файла сделайте следующее:
#восстановите исходный текст (очистите от тегов и знаков ударения) и
#сохраните его в новый файл с тем же названием, но расширением .txt и в
#кодировке «cp1251». В первой строке нового файла
#напишите название новости, взяв его из тега <title>.

import re

def open_text():
    with open ('news (2)/news/itartass1.html', 'r', encoding='utf-8') as file:
        text = file.read()
        splited_text = text.split('\n')
    return text, splited_text
def re_sub():
    result = re.sub('`','', text)
    result_1 = re.sub('><','', result)
    return result_1
    print(result_1)
def main():
    text, splited = open_text()
    result = re_sub()
    result_1 = re_sub()


if __name__ == '__main__':
    main()
