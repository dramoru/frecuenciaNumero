# Abro archivo y obtengo texto
with open('contabilidad.txt', encoding="utf-8") as archivo:
    texto = archivo.read()

# Obtengo la frecuencia de los caracteres
frec_caracteres: dict[str, int] = {}

for caracter in texto:
    if caracter in frec_caracteres:
        frec_caracteres[caracter] += 1
    else:
        frec_caracteres[caracter] = 1

frec_numeros: dict[str, int] = {}

for digito in range(10):
    if str(digito) in frec_caracteres:
        frec_numeros[str(digito)] = frec_caracteres[str(digito)]
    else:
        frec_numeros[str(digito)] = 0

for caracter, frecuencia in frec_numeros.items():
    print(repr(caracter) + " : " + str(frecuencia))
