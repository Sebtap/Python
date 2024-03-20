#1  Se ingresan DNI y nota de un parcial de los alumnos de un curso. El ingreso de 
#datos finaliza con un DNI negativo. Se sabe que como máximo pueden presentarse 
#a rendir 60 alumnos. Mostrar:
#a) Listado alumnos con su correspondiente DNI y la nota obtenida 
#b) La máxima nota obtenida y el DNI de los alumnos que la obtuvieron.
''''maximo=0
lista_dni=[]
lista_nota=[]
lista_nota_ordenada=[]
while True:
    dni=int(input("Ingrese dni del alumno (negativo para terminar el programa): "))
    if dni<0:
        break
    while True:
        nota_parcial=int(input("Ingrese nota del parcial del alumno: "))
        if nota_parcial<0 or nota_parcial>10:
            print("ingrese nuevamente, error al introducir nota alumno: ")
            continue
        else:
            break
    maximo+=1
    lista_dni.append(dni)
    lista_nota.append(nota_parcial)
    lista_nota_ordenada.append(nota_parcial)
    print(maximo)
    if maximo==60:
        break

lista_nota_ordenada.sort(reverse=True)

mayor_nota=lista_nota_ordenada[0]


for i in range(maximo):
    print(f"el alumno con el dni numero:{lista_dni[i]} se saco un {lista_nota[i]}")

print(f"Los dni de los alumnos con {lista_nota_ordenada[0]} que es la mayor nota son: ")
for i in range(maximo):
    if lista_nota[i]==mayor_nota:
        print(f"dni: {lista_dni[i]}")
'''

#2 Se deben ingresar los códigos de 15 productos de una empresa (números de 3 
#dígitos. Luego se ingresan las ventas realizadas durante el día. Por cada venta 
#se ingresa código de vendedor, código de artículo y cantidad.
#Los vendedores son 5 y están codificados en forma correlativa de 1001 a 1005
#Se puede recibir más de una venta de un mismo vendedor y articulo.
#El ingreso de datos finaliza con código del producto igual a 0.
#Se desea:
#a) Mostrar un listado ordenado de mayor a menor por cantidad de unidades vendidas
#CANTIDAD CODIGO
# XXX XXX
# XXX XXX
#b) Indicar el/los vendedores que realizaron menor cantidad de ventas (no de 
#unidades

''''ventas_vendedores = {1001: 0, 1002: 0, 1003: 0, 1004: 0, 1005: 0}  # Inicializar un diccionario para rastrear las ventas de cada vendedor

codigo_producto = ''
i = 0
lista_cant_unidades = []
lista_codigo_articulos = []


while codigo_producto != 0 and i < 15:
    codigo_producto = int(input("Ingrese código de producto con 3 dígitos: "))
    if codigo_producto < 100 or codigo_producto >= 1000:
        print("El código de producto debe tener 3 dígitos. Intente nuevamente...")
        continue
    if codigo_producto==0:
        break
    ventas = int(input("Ingrese cantidad de ventas realizadas durante el día: "))
    
    for _ in range(ventas):
        codigo_vendedor = int(input("Ingrese código de vendedor (1001 a 1005): "))
        if codigo_vendedor < 1001 or codigo_vendedor > 1005:
            print("El código de vendedor debe estar entre 1001 y 1005. Intente nuevamente...")
            continue
        ventas_vendedores[codigo_vendedor] += 1 #dependiendo el codigo vendedor le agrego un valor
             
        codigo_articulo = int(input("Ingrese código de artículo: "))
        cant_articulos = int(input("Ingrese la cantidad de artículos: "))
        lista_cant_unidades.append(cant_articulos)
        lista_codigo_articulos.append(codigo_articulo)

    i += 1

#contar la cantidad de datos almacenados en una lista
contador=len(lista_cant_unidades)


# Combinar y ordenar las listas en base a lista_cant_unidades
lista_combinada_ordenada = sorted(zip(lista_cant_unidades, lista_codigo_articulos), key=lambda x: x[0], reverse=True)

# Desempaquetar las listas ordenadas, separa en dos la lista combinada y la deja ordenas
lista_cant_unidades_ordenada, lista_codigo_articulos_ordenada = zip(*lista_combinada_ordenada)

print("\nLa cantidad de unidades ordenadas por su cantidad: ")
for i in range(contador):
    print(f"cantidad: { lista_cant_unidades_ordenada[i]} ",end='')
    print(f"codigo: {lista_codigo_articulos_ordenada[i]} ")
    print("")
    
print("\n")

#ordenar diccionario por cantidad de ventas
ventas_vendedores_ordenado = dict(sorted(ventas_vendedores.items(), key=lambda item: item[1],reverse=False))

for clave, valor in ventas_vendedores_ordenado.items():
    print(f"Los vendedores que menor cantidad de ventas tuvieron fueron {clave}, con {valor}")'''
    
     