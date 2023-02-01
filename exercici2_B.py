#Defineix funcio amb argument una tupla
def mostraTupla(myTupla):

    #Crida a la funcio len amb la tupla com a argument i guarda la sortida
    longitud =  len(myTupla)

    #Busca quantes vegades apareix un element a la tupla i guarda la sortida
    found = "Oriol" in myTupla

    #Crida a la funció count a l'objecte i calcula quantes vegades apareix l'argument 
    contador = myTupla.count(1)
    
    #Retorna les 3 variables
    return longitud,found,contador