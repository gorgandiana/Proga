word_count = 0
lines = []
cell = []
words = []

with open('quotes.txt', encoding = 'utf-8') as f:
    lines = f.readlines()
for line in lines:
    cells = line.split('—')
    for cell in cells:
        words = cell.split()
        for word in words:
            if len(cell)<=10 and len(word[0])<5:
                print(line)


with open('quotes.txt', encoding = 'utf-8') as f:   #не получиилось(((((((
    lines = f.readlines()
for line in lines:
    cells = line.split('—')
    for cell in cells:
             words = cell.split()
             for word in words:
                if word == 'разум':
                    print(line.count('разум'))
               
