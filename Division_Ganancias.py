#Problema: División de las ganancias

#Escriba un programa que solucione el siguiente problema algebraico.

#Decide poner un puesto de venta de tamales en una feria local con 6
#de sus amigos. Preparar un tamal tiene un valor de 3$
#,por lo que entre todos deciden vender los tamales a 5$
#para tener un margen de ganancias apropiado. De antemano acuerdan que las ganancias de las ventas serán divididas entre los 7
#de manera equitativa y sin partes d ecimales, y el dinero que sobre será guardado para ser usado en una celebración después del evento.


#Por ejemplo, si el dinero recolectado al final del evento, descontando el dinero invertido en cocinar los tamales vendidos (es decir, la ganancia neta) es de 25$
#, se podría dar 3$v#a cada uno de los amigos y quedarían 4$
#para la celebración.


#¿Cuánto dinero le corresponde a cada persona y cuánto dinero queda para la reunión?

#⌨️ Entrada

#¿Cómo funciona la entrada en UNCode?
#La entrada será provista por UNCode en la forma de casos de prueba de texto. Esta entrada deberá ser recibida en su programa con instrucciones que incluyan la función input.

#El programa recibirá un único valor de entrada.


#- ventas: número entero entre 0 y 300 que representa el número total de tamales vendido.

#🖥️ Salida

#¿Cómo funciona la salida en UNCode?
#La salida será capturada por UNCode y comparada con la salida esperada de cada caso de prueba. Esta salida deberá ser generada por su programa con instrucciones que incluyan la función print.

#El programa debe imprimir en la salida dos líneas.

#- monto_integrante: el monto de dinero que le corresponde a cada integrante del grupo.
#- monto_sobrante: el monto de dinero sobrante y depositado para la celebración después del evento.

### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 6 líneas de código)

# Entrada del programa (~ 1 línea).
ventas = int(input())                     # Reemplace 'None' por el código necesario. 


# Operaciones matemáticas (~ 3 líneas).
costo_tamal = 3
precio_venta = 5
num_personas = 7

ganancia_neta = ventas * (precio_venta - costo_tamal)
monto_integrante = ganancia_neta // num_personas
monto_sobrante = ganancia_neta % num_personas

# Salida del programa (~ 2 líneas).
print(monto_integrante)          # Indique el primer resultado en esta línea.
print(monto_sobrante)            # Indique el segundo resultado en esta línea.