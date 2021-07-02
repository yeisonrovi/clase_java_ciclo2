# Variables
productos_vendidos = {'producto1' : {'nombre' : 'Llave', 'precio' : 1500, 'iva' : 0, },'producto2' : { 'nombre' : 'Cemento','precio' : 60500,'iva' : 0.15,},'producto3' : {'nombre' : 'Tornillos','precio' : 22500,'iva' : 0.19, }}

def reporte_ferreteria(productos):
    # Manejo de variables previo
    productos_vendidos = dict(productos)
    items = list(productos_vendidos.keys())
    detalle = list(productos_vendidos.values())
    # Productos
    nombreproducto1 = detalle[0]['nombre']
    nombreproducto2 = detalle[1]['nombre']
    nombreproducto3 = detalle[2]['nombre']
    # Total Precios
    total_precio = detalle[0]['precio'] + detalle[1]['precio'] + detalle[2]['precio']
    # Total Impuestos
    total_impuestos = detalle[0]['iva']*detalle[0]['precio'] + detalle[1]['iva']*detalle[1]['precio'] + detalle[2]['iva']*detalle[2]['precio']
    # Reporte productos
    mensaje = f'Los productos reportados son: {nombreproducto1} , {nombreproducto2} , {nombreproducto3}'
    
    reporte = {
     "precio_total" : total_precio,
     "impuestos_total" : total_impuestos,
     "reporte" : mensaje
     }

    return reporte

print(reporte_ferreteria({'producto1' : {'nombre' : 'Llave', 'precio' : 1500, 'iva' : 0, },'producto2' : { 'nombre' : 'Cemento','precio' : 60500,'iva' : 0.15,},'producto3' : {'nombre' : 'Tornillos','precio' : 22500,'iva' : 0.19, }}))