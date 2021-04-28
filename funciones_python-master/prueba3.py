def lista_aleatoria (inicio, fin, cantidad):

    random_list = []
    for i in range(cantidad):
        numero = random.randrange(inicio, fin+1)
        random_list.append(numero)
    
    return random_list

