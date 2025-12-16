import string

def word_frecuency(text):
    "Retorna un diccionario con las palabras y su frecuencia en el texto"
    frequencies = {}
    
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
        
    return frequencies