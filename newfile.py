# realizar ejercicio
# Moises Ovalles V-27726153 seccion 91
# La Isla del Drama
# Está por terminar la primera temporada del Reality Show llamado “La Isla delDrama”; razón por la cual se debe iniciar el proceso de selección de los nuevos participantes para la segunda temporada.La selección es realizada por tres jueces que emiten una puntuación entre 0.0 y 10.0, por cada candidato que realice la audición.
#El problema es que son tantos los candidatos para la audición que la empresa productora desea que usted realice un programa que procese una lista de candidatos evaluados que contiene la siguiente información:
#NOMBRE DEL CANDIDATO Y LAS 3 PUNTUACIONES DE LOS JUECES.
#Dicha información se encuentra almacenada en un archivo de nombre PUNTUACIONES.TXT. Procese la información y determine e imprima por pantalla.
#✓ Porcentaje de candidatos que fueron seleccionados como participantes del reality show.
#✓ Promedio de la puntuación definitiva obtenida por los candidatos que pasaron a ser participantes.
#✓ Un mensaje que indique si es necesario o no una segunda etapa de selección.
#Consideraciones:
#✓ La puntuación definitiva de un candidato es el promedio de las 3 puntuaciones emitidas por los jueces.
#✓ Un candidato es seleccionado como participante si la puntuación definitiva es mayor o igual a 7.5 puntos.
#✓ Se necesita una segunda etapa de selección, si la cantidad de candidatos seleccionados es menor a 20 o es mayor a 24.
arch = open('PUNTUACIONES.txt', 'r')
contador1 = 0
contador2 = 0
acumulador1 = 0
For registro in arch:
    linea = registro.split(' , ')
    print(linea)
    nombre = linea[0]
    print(nombre)
    nota1 = float(linea[1])
    print(nota1)
    nota2 = float(linea[2])
    print(nota2)
    nota3 = float(linea[3])
    print(nota3)
    definitiva = (nota1 + nota2 + nota3) / 3
    contador1 = contador1 + 1
    if definita >= 7.5:
        acumulador1 = acumulador1 + definitiva
        contador2 = contador2 + 1
    else:
        print('no hay candidato seleccionado')
porc = (contador2 / contador1) * 100
prom = acumulador1 / contador2
print('el % de los que fueron seleccionado con respecto al total de participante fue de:' , porc)
print('el promedio de la definitiva de aquellos que pasaron wl show fue de:' , prom)
if contador2 < 20 and contador2 > 24:
    print('se necesita otra etapa de seleccion')
else:
    print('no se necesita otra etapa de seleccion')
arch.close()
input('pulse una tecla para finalizar...')
