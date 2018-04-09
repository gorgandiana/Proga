
import re

with open ("Птицы - Класс птицы - Виды птиц.html",encoding = "utf-8") as f:
        text = f.read()
c = re.sub('Птиц', 'Рыб', text) 
c1 = re.sub('птиц', 'рыб', c) 
c2 = re.sub('Птицей', 'Рыбой', c1) 
c3 = re.sub('птицей', 'рыбой',c2)
   
with open ("text.txt","w", encoding = "utf-8") as t:
        t.write(c3)
#с функциями ничего не работает:(
