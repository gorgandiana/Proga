
import re
def openfile():
    with open ("Птицы - Класс птицы - Виды птиц.html",encoding = "utf-8") as f:
        text = f.read()
    result = re.sub('Птиц', 'Рыб', result) 
    result = re.sub('птиц', 'рыб', result) 
    result = re.sub('Птицей', 'Рыбой', result) 
    result = re.sub('птицей', 'рыбой',result)
   
    with open ("text.txt","w", encoding = "utf-8") as t:
        t.write(result)

