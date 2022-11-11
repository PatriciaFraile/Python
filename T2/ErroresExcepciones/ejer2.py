'''Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa 
se bloquee y además explica en un mensaje al usuario la causa y/o solución:
colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
colores['blanco']'''

try:
    colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
    colores['blanco']
except KeyError:
    print('No se encuentra el blanco')