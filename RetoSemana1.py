# Reto Semana 1

def mayor_de_cinco (numero1, numero2, numero3, numero4, numero5):
    #Comparación de numeros| se calculará cada numero con respecto al numero5 y retornará el resultado.
    if numero1 > numero5:
        numeroi = numero1 #numeroi "el número en cuestión"
        return f'El numero {numeroi} es mayor al {numero5}'
    elif numero2 > numero5:
        numeroi = numero2
        return f'El numero {numeroi} es mayor al {numero5}'
    elif numero3 > numero5:
        numeroi = numero3
        return f'El numero {numeroi} es mayor al {numero5}'
    elif numero4 > numero5:
        numeroi = numero4
        return f'El numero {numeroi} es mayor al {numero5}'
    else:
         pass
   
   
    #Identificar el numero menor | se calculará cada numero como el menor en relación a los demás y retornará el resultado.
    if numero1 < numero2 and numero1 < numero3 and numero1 < numero4:
        numeromenor = numero1 #Asigno el valor
        return f'El numero menor de entre los introducidos es el: {numeromenor}'
    elif numero2 < numero1 and numero2 < numero3 and numero2 < numero4:
        numeromenor = numero2
        return f'El numero menor de entre los introducidos es el: {numeromenor}'
    elif numero3 < numero1 and numero3 < numero2 and numero3 < numero4:
        numeromenor = numero3
        return f'El numero menor de entre los introducidos es el: {numeromenor}'
    elif numero4 < numero1 and numero4 < numero2 and numero4 < numero3:
        numeromenor = numero4
        return f'El numero menor de entre los introducidos es el: {numeromenor}'
    else: 
        pass



# Ejecuta función:

print(menor_de_cinco(1, 1, 1, 1, 1))