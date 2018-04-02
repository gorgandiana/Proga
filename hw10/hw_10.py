import re
with open('archi.html', encoding='utf-8') as f:
    text = f.read()
    result = re.search('>([a-z]\w[a-z])<', text) #то что в скобочках будет печататься
    print(result.group(1)) #цифра это порядковый номер скобок
