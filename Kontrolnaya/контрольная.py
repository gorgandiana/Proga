import re
f = open('mystem.xml', encoding = 'utf-8')
text = f.read()
result = re.findall('lex', text)
mur = result.count('lex')
print(mur)
    #219 строк должно получиться
f.close() #не получается записать это в отдельный файл:(
