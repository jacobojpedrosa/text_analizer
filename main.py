import text_analizer

from text_analizer import word_list

def main_analysis(t):
    data = {}
    data['list_of_words'] = word_list(t)

    return data



if __name__ == "__main__":

    text = input("Introduce a text:")
    
    data = main_analysis(text)


    # [] -> listas
    # {} -> diccionarios y sets
    # () -> tuplas

    # {
    #  "list_of_words":['hola','que','tal'],
    #  "char_count":123,
    #  "word_count":3
    # ...
    # }