#Problema: Transformando cadenas de texto

#Realizar un programa que reciba una cadena de texto, aplique una serie de transformaciones, siguiendo las reglas escritas a continuación; y al final imprima el resultado obtenido.


#- Todos los caracteres deben de estar completamente en minúscula.
#- Las vocales 'a', 'e' y 'o' deben de ser reemplazadas por el carácter 'i'.
#- De igual manera, se deberán reemplazar sus versiones con acento ('Á', 'á', 'É', 'é', 'Ó' y 'ó') por el carácter 'í'.

#¿Cómo funciona la entrada en UNCode?
#La entrada será provista por UNCode en la forma de casos de prueba de texto. Esta entrada deberá ser recibida en su programa con instrucciones que incluyan la función input.

#El programa recibirá un único valor de entrada.

#- cadena: cadena de texto con el texto original.

#¿Cómo funciona la salida en UNCode?
#La salida será capturada por UNCode y comparada con la salida esperada de cada caso de prueba. Esta salida deberá ser generada por su programa con instrucciones que incluyan la función print.

#El programa debe imprimir en la salida una única línea:


#- cidini: cadena de texto con el resultado del procesamiento de la cadena original con las reglas especificadas en el enunciado.

### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 11 líneas de código)

# Entrada del programa (~ 1 línea).
cadena = input()          # Reemplace 'None' por el código necesario. 

# Operaciones en cadenas de texto (~ 9 líneas)
cadena = cadena.lower()
cadena = cadena.replace('a', 'i').replace('e', 'i').replace('o', 'i')
cadena = cadena.replace('á', 'í').replace('é', 'í').replace('ó', 'í')

# Salida del programa (~ 1 línea).
print(cadena)