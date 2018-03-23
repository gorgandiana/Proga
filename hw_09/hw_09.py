import re

with open ('сидеть.txt', encoding='utf-8') as f:
    text = f.read()
all_results = re.findall('Си[жд]*[еиуя]*[щлш]*[иаье]*[йягемх]*[уйо]*', text)
print(all_results)
    
