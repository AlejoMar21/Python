#Problema: Ecuaciones de física (Parte I)
#Uno de las aplicaciones más comunes de la programación es el desarrollo de operaciones en actividades científicas. 
#Por ejemplo, en física, se suelen escribir programas para el cálculo eficiente de ecuaciones, para un análisis y manejo efectivo 
#de los resultados.En esta actividad vamos a considerar un problema básico de física que describe el movimiento con las llamadas 
#ecuaciones cinemáticas. Inicialmente, queremos poder calcular rápidamente la posición final de un objeto que se desplaza horizontalmente 
#a una aceleración constante (movimiento uniformemente acelerado).


#Podemos calcular este valor a partir de algunos parámetros iniciales que describen el problema. Estos parámetros iniciales son:


#La velocidad inicial v0 del objeto en dirección del recorrido.
#La posición inicial x0. En este caso el recorrido solo se dará en una dirección de forma horizontal.
#La aceleración a que se mantiene constante en todo el recorrido.
#El tiempo t o duración del recorrido.

#Se conoce que la posición de un objeto uniformemente acelerado puede ser calculada por la siguiente ecuación:


#x=x0+v0t+12at2


#En este ejercicio usted deberá crear un programa que realice lo siguiente:


#1 Obtener de la entrada del programa los parámetros iniciales, línea por línea y en el orden descrito en la sección ⌨️ Entrada.
#2 Convertir cada valor de texto obtenido de la entrada en un valor numérico decimal.
#3 Utilizar los valores numéricos en una expresión matemática y obtener el valor de la posición final.
#4 Reportar el resultado de la operación con el formato numérico descrito en la sección 🖥️ Salida.
#La entrada será provista por UNCode en la forma de casos de prueba de texto. Esta entrada deberá ser recibida en su programa con instrucciones que incluyan la función input.

#Su programa deberá recibir de la entrada 4 líneas con los valores de x0, v0, a y t respectivamente.

#Línea 1: cadena de texto con la posición inicial x0 en m
#Línea 2: cadena de texto con la velocidad inicial v0 en m/s
#Línea 3: cadena de texto con la aceleración a en m/s2
#Línea 4: cadena de texto con el tiempo t en s

#Tenga en cuenta que cada una de estas líneas es obtenida como cadenas de texto con un formato que puede ser convertido a un valor decimal con la función float. No olvide realizar la conversión del tipo de dato en su programa.

#La salida será capturada por UNCode y comparada con la salida esperada de cada caso de prueba. Esta salida deberá ser generada por su programa con instrucciones que incluyan la función print.
#En este ejercicio el programa deberá imprimir exactamente 1 línea con la respuesta del ejercicio. Esta respuesta deberá tener este formato exacto:
'La posición final es {x} metros.'
#Donde {x} corresponde a la posición calculada en metros, que deberá ser presentada con un formato que muestre exactamente dos dígitos decimales


### 💻  Ejemplo: Ejercicios de física (I)  💻 ###
##################################################

## 👇 Escriba su código DEBAJO de esta línea 👇 ##


# 1) Obtener de la entrada del programa los parámetros iniciales.


x0 = input()
v0 = input()
a = input()
t = input()


# 2) Convertir cada valor de texto obtenido de la entrada en un valor numérico decimal.
x0=float(x0)
v0=float(v0)
a=float(a)
t=float(t)



# 3) Utilizar los valores numéricos en una expresión matemática y obtener el valor de la posición final.


x = x0+v0*t+(1/2)*a*(t**2)


# 4) Reportar el resultado de la operación con dos dígitos decimales.

print(f"La posición final es { x :.2f} metros.")



## ☝️ Escriba su código ENCIMA de esta línea ☝️ ##