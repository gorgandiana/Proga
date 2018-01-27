def words_from_text(fname):
    with open(fname, encoding = 'utf-8') as f:
        text = f.read()
    symbols_to_remove = """,.:;'()-"""
    for s in symbols_to_remove:
        text = text.replace(s, '')
        words = text.split()
        return words
def word_count(words):
    count = {}
    for x in words:
        if x in count:
            count[x] +=1
        else:
            count[x] = 1
    return count

words = words_from_text('dochka.txt')
#print(words[:20])
count = word_count(words)
print(count['оправдание'])
