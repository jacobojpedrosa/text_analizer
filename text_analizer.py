
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


if __name__ == "__main__":
    print("==Test Text Analizer==")
    print(word_list("Hola  que tal"))
    # print(len(word_list("Hola que tal")))

    assert len(word_list("Hola que tal")) == 3, "word_list failed and not returned the required quantity of words..."
    assert len(word_list("Hola  que tal")) == 3, "word_list failed and not returned the required quantity of words..."
    assert word_list("Hola que tal") == ['Hola','que','tal'], "word_list failed and not returned the required list of words..."
    assert word_list("Hola  que tal") == ['Hola','que','tal'], "word_list failed and not returned the required list of words..."


    print("Todo OK")