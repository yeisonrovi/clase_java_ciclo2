# SISTEMA DE ARBOL DE DECISIONES PARA VIABILIDAD DE PRESTAMO

# Variables

informacion = {
    'id_prestamo' : 'RETOS2_003',
    'casado' : 'No',
    'dependientes' : '0',
    'educacion' : 'No Gradudado',
    'independiente' : 'No',
    'i_d' : 3748 ,
    'i_c' : 1668 ,
    'c_p' : 110 ,
    'p_p' : 360 ,
    'historia_credito': 1,
    'tipo_propiedad':'Semiurbano'
}

def prestamo(informacion):
    # Posibles resultados
    aprobado = {
        'id_prestamo': informacion['id_prestamo'],
        'aprobado' : True
    }
    rechazado = {
        'id_prestamo': informacion['id_prestamo'],
        'aprobado' : False
    }

    # Manejo previo de valores

    informacion['independiente'] = informacion['independiente'].upper()
    informacion['dependientes'] = str(informacion['dependientes'])
    informacion['casado'] = informacion['casado'].upper()
    informacion['educacion'] = informacion['educacion'].upper()
    informacion['tipo_propiedad'] = informacion['tipo_propiedad'].upper()

    # Arbol de Decisiones:
    if informacion['historia_credito'] > 0:
        if informacion['i_c'] > 0 and (informacion['i_c']/9) > informacion['c_p']:
            return aprobado
        elif informacion['dependientes'] == '3+' and informacion['independiente'] == 'SI':
            if informacion['i_c']/12 > informacion['c_p']:
                return aprobado
            else:
                return rechazado
        elif informacion['c_p'] < 200:
                return aprobado
        else:
            return rechazado
    else:
        if informacion['independiente'] == 'SI':
            if informacion['casado'] == 'NO' and (informacion['dependientes'] == '2' or informacion['dependientes'] == '3+'):
                if informacion['i_d'] / 10 > informacion['c_p'] or informacion['i_c'] / 10 > informacion['c_p']:
                    if informacion['c_p'] < 180:
                        return aprobado
                    else:
                        return rechazado
                else:
                    return rechazado
            else:
                return rechazado
        elif (informacion['tipo_propiedad'] == 'URBANO' or informacion['tipo_propiedad'] == 'RURAL') and (informacion['dependientes'] == '1' or informacion['dependientes'] == '0'):
            if informacion['educacion'] == 'GRADUADO':
                if informacion['i_d'] / 11 > informacion['c_p'] and informacion['i_c'] / 11 > informacion['c_p']:
                    return aprobado
                else:
                    return rechazado
            else:
                return rechazado
        else:
            return rechazado

                
