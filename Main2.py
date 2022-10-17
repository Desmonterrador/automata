doc = ("texto.txt")
palabra = input("Ingrese palabra a buscar: ")
con = 0
with open(doc, 'r') as n1:
    for linea in n1:
        palabras = linea.split()
        for i in palabras:
            if(i == palabra):
                con = con + 1
print("La palabra {palabra} aprece: ", con)