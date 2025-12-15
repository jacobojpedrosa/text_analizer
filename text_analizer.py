
print("Text Analizer")


def word_list(text):
    """Esta funcion divide el texto (text) en una lista de palabras manteniendo el orden"""
    list = text.split(' ')
    filtered_list = [] 
    # for item in list:
    #     if item: 
    #         filtered_list.append(item)
    filtered_list = [item for item in list if item]

    return filtered_list


    # def unique_words(text):_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    # David Jimenez _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    # """Crea un set que incluye únicamente una ocurrencia de cada palabra""" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    # pass _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# TAREA ANALIZER: # Crear un set que incluye una única ocurrencia de cada palabra.
# Def unique_words(text):
# DavidJimenez
# Crear un set que incluye unicamente una ocurrencia de cada palabra.
# pass.


def unique_words(text):          # La función llamada unique_words recibe un parámetro text. text se espera que sea una cadena de caracteres (string) con el texto a analizar.
    
    palabras = text.split( " " ) # variable llamada palabras. text.split(",") separa la cadena text en una lista usando la coma , como separador.
                                 # split(",") devuelve una lista con el texto completo en una sola posición (no separa las palabras).
    return set(palabras)         # Convierte la lista palabras en un conjunto (set) y lo devuelve.
                                 # Un set elimina elementos duplicados, de modo que de una lista como ["hola", "hola", "mundo"] se quedaría con {"hola", "mundo"}.
                                 # Pero, como antes no se han separado bien las palabras, aquí en realidad estás devolviendo un conjunto con una sola cadena: el texto entero.

resultado = unique_words("Hola hola Mundo mundo Que Dios Os Bendiga A Todos Python Mola hola")

# Llama a la función unique_words pasando como texto "hola hola mundo mundo que dios os bendiga a todos python hola".
# Como en la función se hace split(","), 
# esta llamada devuelve un set con un único elemento: la cadena completa, porque no hay comas que separen.

print(resultado) # Imprime en pantalla el valor de resultado, es decir, el set con esa cadena.

def word_frequency(text):
    # Sergio Torres
    """Retorna un diccionario con las palabras y su frecuencia en el texto"""
    pass

def longer_word(text):
    # Noemí
    """Return the longer word in the text"""
    pass

def shorter_word(text):
    # Noemí
    """Return the shorter word in the text"""
    pass

def word_filter(words, filter_words):
    # Ruben
    """Return  the words list filtered by filter_words"""
    pass

def char_counter(text):
    #Jahn
    """Return the quantity of chars in the text excluding special 
    charts like ',','.','(',')' and spaces"""
    pass

def filter_by_word_length(text,l):
    #Juan Antonio
    """Return the list of words with lenght over than l"""
    pass

def count_by_lenght(text, l):
    # Dani Gonzalez
    """Return a dict with lengths and quantities of words with this lenghts"""
    pass




if __name__ == "__main__":
    print("==Test Text Analizer==")
    print(word_list("Hola  que tal"))
    # print(len(word_list("Hola que tal")))

    assert len(word_list("Hola que tal")) == 3, "word_list failed and not returned the required quantity of words..."
    assert len(word_list("Hola  que tal")) == 3, "word_list failed and not returned the required quantity of words..."
    assert word_list("Hola que tal") == ['Hola','que','tal'], "word_list failed and not returned the required list of words..."
    assert word_list("Hola  que tal") == ['Hola','que','tal'], "word_list failed and not returned the required list of words..."

    #Angel -> Escribir los asserts de validar todas las funciones anteriores
    
    print("Todo OK")