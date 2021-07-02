import pandas as pd  # IMPORTANTE

# Variables de prueba
nombreArchivo = 'https://raw.githubusercontent.com/anfejaramillo/OpenAccess/main/datos_p79.csv'
nombres = ['Rachel', 'grey']
departamentos = ['Ventas']

def hallarAsociados (nombres, departamentos, nombreArchivo):
    
    # Si no ingresan valores en los parámetros NOMBRE y DEPARTAMENTO o ingresa mal el nombre del archivo
    cantidad_nombres = len(nombres)
    cantidad_departamentos = len(departamentos)
    
    if cantidad_nombres == 0 and cantidad_departamentos == 0:
        mensaje_error = 'Error, introduzca al menos un criterio de busqueda'
        return mensaje_error
    elif nombreArchivo != 'https://raw.githubusercontent.com/anfejaramillo/OpenAccess/main/datos_p79.csv':
        
        mensaje_error = 'Error leyendo el archivo.'
        return mensaje_error
    else:
        pass
    
    
    # Si ingresan valores en los parámetros NOMBRE y DEPARTAMENTO
    # Primero debemos convertir la primer letra en Mayúscula para que pueda ubicar los registros en el df
    posicion = 0
    while cantidad_nombres > 0:
        Mayus = nombres[posicion][0].upper()
        resto = nombres[posicion][1:]
        palabranueva = Mayus+resto
        nombres[posicion]=palabranueva
        cantidad_nombres -= 1
        posicion += 1

    # Se crea el DataFrame con el csv
    base = pd.read_csv(nombreArchivo)
    df = pd.DataFrame(base, columns=('nombre_usuario','Identificador','contrasena_uso_unico','nombre_1','nombre_2','departamento','ubicacion','correo'))
    
    # aplico el Try/Except para realizar la búsqueda de los registros según los parámetros y convierto en
    # listas las columnas a utilizar
    try:
        busqueda = df.query('departamento == @departamentos or nombre_1 == @nombres or nombre_2 in @nombres' )
        nombre1 = list(busqueda.nombre_1)
        nombre2 = list(busqueda.nombre_2)
        correo1 = list(busqueda.correo)

        cantidad_regristros = len(nombre1)

        # Inicio proceso de identificación de cada asesor

        if cantidad_regristros > 0:
            pos = 0
            asesores = ''

            #While para crear comentario por cada asesor

            while cantidad_regristros > 0:

                nombre_1_asesor = nombre1[pos]
                nombre_2_asesor = nombre2[pos]
                correo_asesor = correo1[pos]

                asesores += f'{nombre_1_asesor} {nombre_2_asesor}:{correo_asesor}. '
                cantidad_regristros -= 1
                pos += 1

            mensaje_inicial = 'Por favor comunicate con alguno de los siguientes contactos: '
            mensaje = mensaje_inicial + asesores
        
        # Else para definir resultado cuando no localice ningún registro
        else:
            mensaje_no = 'No encontramos asociados para tu solicitud.'
            return mensaje_no
        
     # except para definir resultado cuando no localice ningún registro    (Por si acaso)
    except:

        mensaje_no = 'No encontramos asociados para tu solicitud.'
        return mensaje_no
    
    return mensaje


print(hallarAsociados(nombres, departamentos, nombreArchivo))
