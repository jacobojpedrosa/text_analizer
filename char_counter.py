def contador_caracteres(texto):
   
    caracteres_excluidos = [',', '.', '(', ')', ' ']
    
    cantidad_valida = 0
    
    for caracter in texto: #mira si esta excluido
        if caracter not in caracteres_excluidos:
            #Si no está excluido, incrementa el contador
            cantidad_valida += 1
            
    return cantidad_valida

