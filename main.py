import re
import string
frequency = {}
abrirDocumento = open('AgregarTexto.txt', 'r')
listaPalabras = abrirDocumento.read().lower()
calcularTamaño = re.findall(r'\b[a-z]{1,20}\b', listaPalabras)
 
for palabra in calcularTamaño:
    contador = frequency.get(palabra,0)
    frequency[word] = contador + 1
     
repeticion = frequency.keys()
 
for palabra in repeticion:
    print (palabra, frequency[words])