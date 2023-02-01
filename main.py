#Importació de classes
import exercici1_B as ay
import exercici2_B as tp

#Cast input string a int i el guarda a una variable
edat = int(input("Escriu la teva edat:\n"))

#Defineix una tupla de longitud si i guarda a una variable
myTupla = (1,"Oriol",1,"DAM",4.5,"Barcelona")

#Crida les dues funcions amb arguments les variables definides
# i imprimeix el que retornen
print(ay.anyNaixement(edat))
print(tp.mostraTupla(myTupla))