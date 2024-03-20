#1 Escribir una función que devuelva un número entero igual al de su argumento, 
#incrementado cíclicamente en 1. Por ejm. Func(1) devuelve un 2, Func(7) devuelve un 8, 
#Func(9) devuelve un 0.
''''
numero=5
def funcion(numero):
    if numero==9:
        return 0
    else:
        return numero+1

valor=funcion(numero)
print(valor)'''

#2  Escribir una función que reciba un carácter y si se trata de una letra invierta entre 
#mayúsculas y minúsculas. Es decir que si la función recibe una letra minúscula debe 
#retornar la misma letra en mayúsculas y si la recibe en mayúsculas la debe retornar en
#minúsculas. Si se recibe otro carácter no se lo modifica retornando el mismo caracter que 
#se recibió.

''''def convertir(caracter):
    if caracter>='a' and caracter<='z':
        caracter=caracter.upper()
        print(caracter)
    else:
        caracter=caracter.lower()
        print(caracter)
    
convertir('a')
convertir('B')    '''

#3 Se ingresan números enteros comprendidos entre 100 y 2000 (usar función 
#LeerYValidar). Determinar usando la función EstaDentroDelRango:
#a. Cantidad de números ingresados entre 100 y 500
#b. Cantidad de números pares ingresados entre 500 y 1200
#c. Promedio de números ingresados entre 1200 y 2000
#El ingreso de datos finaliza cuando se ingresa un número igual a 99.
#Para realizar este programa se deben realizar las siguientes funciones:
# EstaDentroDelRango: que reciba 3 enteros correspondientes a un número a validar y 
#los límites superior e inferior del rango. La función debe retornar un 1 si el número a 
#validar se encuentra dentro del rango indicado o un 0 si no lo está.
# LeerYValidar: que reciba los límites superior e inferior de un rango y retorne un 
#número que se encuentre dentro del mismo. (El ingreso de datos se realiza dentro de 
#la función). Para validar el rango utilizar la función EstaDentroDelRango realizada 
#en el punto anterior
''''aux=0;aux2=0;aux3=0;suma=0
def LeerYValidar(limiteSuperior,limiteInferior):
    global aux, aux2, aux3, suma  # Indicar que estas variables son globales
    numero=int(input("Ingrese numero comprendido entre 100 y 2000, (99 para salir del program): "))
    if numero==99:
        return 'f'
    valor=EstaDentroDelRango(numero,limiteSuperior,limiteInferior)
    print(f"El valor retornado es {valor}")
    if valor==0:
        print(f"El numero {numero} no esta dentro del rango acordado, intente nuevamente...")
    if valor == 1:
        if 100 < numero < 500:
            aux += 1
        elif 500 < numero < 1200:
            if numero % 2 == 0:
                aux2 += 1
        elif 1200 < numero < 2000:
            aux3 += 1
            suma += numero

def EstaDentroDelRango(numero,limiteSuperior,limiteInferior):
    if (numero<limiteInferior or numero>limiteSuperior):
        return 0
    else:
        return 1

while True:
    valor=LeerYValidar(2000,100)
    if valor=='f':
        break
   
promedio=suma/aux3
  
print(f"La cantidad de numeros entre 100 y 500 es: {aux}")
print(f"La cantidad de numeros pares entre 500 y 1200 es: {aux2}")
print(f"El promedio entre los numeros ingresados entre el rango 1200 y 2000 es: {promedio}")'''

#4 Se realizó un concurso de tiro al blanco. Por cada participante se ingresa un número que 
#lo identifica y el resultado de los disparos efectuados. El ingreso finaliza con un número 
#de participante negativo.
#Cada participante efectúa 10 disparos, registrándose las coordenadas X-Y de cada 
#disparo. 
# No considere disparos sobre los ejes pero sí en el centro (si es sobre los ejes las 
#coordenadas deberán volver a ingresarse).
# Para determinar el cuadrante utilizar la función CUADRANTE que reciba las dos 
#coordenadas y retorne el cuadrante al cual pertenece (1 a 4) y 0 para indicar un tiro 
#en el centro.
#Para calcular el puntaje utilizar la función PUNTAJE que reciba 5 parámetros que 
#representan la cantidad disparos en cada eje y en el centro. La función debe retornar el 
#puntaje obtenido según la siguiente escala:
# Cuadrantes 1 y 2: 50 puntos
# Cuadrantes 3 y 4: 40 puntos
# Centro: 100 puntos
#Determinar:
#a) Puntaje obtenido por cada participante, detallando cuantos disparos realizó en 
#cada cuadrante.
#b) Mostrar el número del participante ganador y el puntaje obtenido.
#c) Cantidad total de disparos en el centro (de todos los participantes)
''''cantCentro=0;maximo=float('-inf')
def cuadrante(x,y):
    if x>0:
        if y>0:
            return 1      
        elif y<0:
            return 2        
    elif x<0:
        if y<0:
            return 3        
        elif y>0:
            return 4      
    elif x==0 and y==0:
        return 0
        
def puntaje(cuad1, cuad2, cuad3, cuad4, centro):
    print(centro,cuad1,cuad2,cuad3,cuad4)
    puntos1 = 50 * cuad1 + 50 * cuad2
    puntos2 = 40 * cuad3 + 40 * cuad4
    puntos3 = 100 * centro
    puntos = puntos1 + puntos2 + puntos3
    return puntos
        
  
while True:
    i=0;cuad1=0; cuad2=0; cuad3=0; cuad4=0; centro=0
    id=int(input("Ingrese un numero que identifique al partipante (negativo para que el programa finalice): "))
    if id<0:
        break
    while i<10:
        print("Ingrese las coordenadas en X y Y del disparo: ")
        x=int(input("x="))
        y=int(input("y="))
        if (x==0 and y!=0) or (x!=0 and y==0):
            print("No se puede tomar el valor en un solo eje, ingrese las coordenadas del disparo nuevamente..")
            continue
        else:
            i=i+1
            valor=cuadrante(x,y)
            if valor==1:
                cuad1+=1     
            if valor==2:
                cuad2+=1      
            if valor==3:
                cuad3+=1   
            if valor==4:
                cuad4+=1     
            if valor==0:
                centro+=1
                cantCentro+=1
    resultado = puntaje(cuad1, cuad2, cuad3, cuad4, centro)
    if resultado>maximo:
        maximo = resultado
        ganador=id
    print(f"La cantidad de puntos del participante {id} es de {resultado} con {centro} disparos en el centro, {cuad1} cuadrante 1,  {cuad2} cuadrante2, {cuad3} cuadrante 3 y {cuad4} cuadrante 4")
    
print(f"El maximo puntaje es {maximo}puntos del participante {ganador}")
print(f"La cantidad total de disparos en el centro entre todos los participantes es de {cantCentro}")'''

