#Unidades de medida

#En primer lugar, hemos identificado que en muchos escenarios de la vida real los valores que manejamos no están expresados en las mismas unidades de medida. En este caso, el programa va a obtener los parámetros en las siguientes unidades:

#- La posición inicial x0 en metros (m).
#- La velocidad inicial v0 en kilómetros por hora (km/h).
#- La aceleración a en metros sobre segundo al cuadrado (m/s2).
#- El tiempo t en segundos (s).

#Dado que la velocidad está dada en kilometros por hora, es necesario antes calcular algunas conversiones entre unidades de medida. Tenga en cuenta las siguientes equivalencias:


#1 km=1000 m↔1 m=11000 km
#1 h=3600 s↔1 s=13600 h
#1 km/h=13.6 m/s↔1 m/s=3.6 km/h

#¿Cómo funciona la entrada en UNCode?
#La entrada será provista por UNCode en la forma de casos de prueba de texto. Esta entrada deberá ser recibida en su programa con instrucciones que incluyan la función input.

#Su programa deberá recibir de la entrada 4 líneas con los valores de x0, v0, a y t respectivamente.


#Línea 1: cadena de texto con la posición inicial x0 en m
#Línea 2: cadena de texto con la velocidad inicial v0 en km/h
#Línea 3: cadena de texto con la aceleración a en m/s2
#Línea 4: cadena de texto con el tiempo t en s

#Tenga en cuenta que cada una de estas líneas es obtenida como cadenas de texto con un formato que puede ser convertido a un valor decimal con la función float. No olvide realizar la conversión del tipo de dato en su programa.

#¿Cómo funciona la salida en UNCode?
#La salida será capturada por UNCode y comparada con la salida esperada de cada caso de prueba. Esta salida deberá ser generada por su programa con instrucciones que incluyan la función print.

#En este ejercicio el programa deberá imprimir exactamente 1 línea con la respuesta del ejercicio. Esta respuesta deberá tener este formato exacto:


'La posición final es de {x} m y la velocidad es de {v} km/h'


#- {x} corresponde a la posición final calculada en metros (m), que deberá ser presentada con un formato que muestre exactamente 2 dígitos decimales.
#- {v} corresponde a la velocidad final calculada en kilómetros por hora (km/h), que deberá ser presentada con un formato que muestre exactamente 3 dígitos decimales.

##################################################
#### 💻 Tarea: Ejercicios de física (II)  💻 ####
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



# 3) Realizar las operaciones matemáticas para las conversiones de unidad de medida necesarias.

v0=v0*(1/3.6)



# 4) Utilizar los valores numéricos en las expresiones matemáticas de cada ecuación y obtener el valor de:


#     i. Posición final 
x = x0+v0*t+(1/2)*a*(t**2)


#     ii. Velocidad final.
v = v0+(a*t)
v= v*3.6

# 5) Reportar el resultado de la operación con el formato solicitado.


print(f'La posición final es de {x:.2f} m y la velocidad es de {v:.3f} km/h')


## ☝️ Escriba su código ENCIMA de esta línea ☝️ ##