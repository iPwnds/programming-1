
def spellcheck(document, valid_words):
    text = document.lower()
    text = text.replace('\n', ' ')
    text = text.split(' ')
    result = set()
    for i in text:
        if i not in valid_words:
            result.add(i)
    return result