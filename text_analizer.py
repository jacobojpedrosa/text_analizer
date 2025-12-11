
print("Text Analizer")


def word_list(text):
    """Esta funcion divide el texto en una lista de palabras manteniendo el orden"""
    return text.split(' ')


if __name__ == "__main__":
    print("==Test Text Analizer==")
    # print(word_list("Hola que tal"))
    # print(len(word_list("Hola que tal")))

    assert len(word_list("Hola que tal")) == 3, "word_list failed and not returned the required quantity of words..."
    assert word_list("Hola que tal") == ['Hola','que','tal'], "word_list failed and not returned the required list of words..."


    print("Todo OK")