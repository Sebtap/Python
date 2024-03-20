#1 Se desea desarrollar un sistema de reservas de entradas para un cine. La sala consta de 12 filas numeradas de la 1 a 
#la 12 y cada fila tiene 9 asientos numerados a partir de la fila central, con los asientos impares a la derecha y los 
#pares a la izquierda, como en el siguiente esquema:
#8 6 4 2 1 3 5 7 9 
#Para la carga, se debe mostrar al usuario un esquema con los asientos disponibles y reservados. Marcando con una 
#letra D los disponibles y una con una letra R los reservados. 
#Por cada reserva se debe solicitar la fila y el número de asiento a reservar. Si ya se encuentra reservado se debe 
#informar con un mensaje para que seleccione otro asiento. Luego de cada reserva aceptada, se debe actualizar el 
#esquema que muestra los asientos. El ingreso de datos finaliza con una fila con un número negativo.
#Al finalizar mostrar:
# la cantidad de asientos disponibles y la cantidad de asientos reservados
# los números de filas que quedaron vacías
# la o las filas con mayor cantidad de espectadores
# un listado con la cantidad de personas que se sentaron en los mismos números de butacas en el todo el cine (es 
#decir en la misma columna) ordenado de mayor a menor. Por ejemplo
#Butaca Cantidad
#  1      20
#  3      15
#  2      10

sala=[['D','D','D','D','D','D','D','D','D'],
      ['D','D','D','D','D','D','D','D','D'],
      ['D','D','D','D','D','D','D','D','D'],
      ['D','D','D','D','D','D','D','D','D'],
      ['D','D','D','D','D','D','D','D','D'],
      ['D','D','D','D','D','D','D','D','D'],
      ['D','D','D','D','D','D','D','D','D'],
      ['D','D','D','D','D','D','D','D','D'],
      ['D','D','D','D','D','D','D','D','D'],
      ['D','D','D','D','D','D','D','D','D'],
      ['D','D','D','D','D','D','D','D','D'],
      ['D','D','D','D','D','D','D','D','D']]

asientos_disponibles=9*12
asientos_reservados=0
while True:
    print("Lugares disponibles: ")
    
    # Imprimir la matriz con un salto de línea entre cada fila
    for fila in sala:
        print(' '.join(fila))  # Imprimir la fila como una cadena separada por espacios

        # Imprimir un salto de línea después de cada fila
        print()
    
    while True:
        print("Ingrese lugar a reservar: ")
        fila = int(input("Ingrese el número de fila: "))
        if fila<0:
            break
        if fila>12:
            print("No existe pruebe nuevamente.")
            continue
        columna = int(input("Ingrese el número de columna: "))
        if columna>9:
            print("No existe pruebe nuevamente.")
            continue
        if sala[fila-1][columna-1]=='R':
            print("El lugar ya esta reservado, pruebe con otro")
            continue
        elif sala[fila-1][columna-1]=='D':
            sala[fila-1][columna-1]='R'
            asientos_disponibles-=1
            asientos_reservados+=1
            print("Tu lugar fue reservado exitosamente")
            break
    if fila<0:
        break 
    
print(f"La cantidad de asientos disponibles son {asientos_disponibles} y la cantidad de asientos reservados {asientos_reservados}")
        
maxima = 0;maxima2=0
fila_maxima = None
columna_maxima=None
for i in range(12):  # Iterar sobre las filas (0 a 11)
    cantidad_espectadores = 0  # Restablecer el contador para cada fila
    for j in range(9):  # Iterar sobre las columnas (0 a 8)
        if sala[i][j] == 'R':
            cantidad_espectadores += 1
    if cantidad_espectadores > maxima:
        maxima = cantidad_espectadores
        fila_maxima = i+1   # Sumar 1 para obtener el número de fila real
        
print(f"La fila con mayor cantidad de espectadores es la {fila_maxima} con {maxima}")

lista_cantidad=[]
lista_butaca=[]
for i in range(9):
    max_espect_column=0
    for j in range(12):
        if sala[j][i]=='R':
            max_espect_column+=1
    lista_cantidad.append(max_espect_column)
    lista_butaca.append(i+1)

# Combinar y ordenar las listas en base a lista_cant_unidades
lista_combinada_ordenada = sorted(zip(lista_cantidad, lista_butaca), key=lambda x: x[0], reverse=True)

# Desempaquetar las listas ordenadas, separa en dos la lista combinada y la deja ordenas
lista_cantidad, lista_butaca = zip(*lista_combinada_ordenada)
contador=len(lista_cantidad)

print("\nLa cantidad de asientos ocupados en la misma butaca ordenadas por su cantidad: ")
for i in range(contador):
    print(f"Butaca:{lista_butaca[i]} cantidad: { lista_cantidad[i]} ",end='')
    print("")
    
print("\n")
    
