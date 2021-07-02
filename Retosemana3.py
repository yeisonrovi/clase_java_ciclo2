# GENERADOR DE ACRÓNIMOS
def constructorDeAcronimos(cadena):

    cadena = cadena.upper()
    palabras = cadena.split()
    cantidades = len(palabras)
    posicion = 0
    texto = ""
    acronimo = "El acronimo del texto introducido es: "
    contador = 1

    if cantidades == 0:
        mensaje_error = 'El texto introducido esta vacío y por tanto no hay acronimo'
        return mensaje_error

    while cantidades > 0:
        
        word = palabras[posicion]
        letra = word[0]

        cantidades = cantidades - 1
        posicion = posicion + 1
        texto = texto + f'La primera letra de la palabra {contador} es {letra}. '
        acronimo = acronimo + letra
        contador = contador+1
    
    mensaje = texto + acronimo
    
    return mensaje

print(constructorDeAcronimos('HOLA MUNDO'))

