# Librerias
import math
# Entradas
print('*** Kiwi ayuda al Coyote ***')
print('Ingrese los siguiente datos: \n')
def pedir_float(mensaje, condicion):
    while True:
        try:
            valor = float(input(mensaje))
            if condicion(valor):
                return valor
            else:
                print('Error, ingrese un valor válido.')
        except ValueError:
            print('Error, ingrese un número.')

xc = pedir_float('Coordenada x del Correcaminos: ', lambda x: x > 0)
v = pedir_float('Velocidad inicial de lanzamiento (kms/h): ', lambda x: 10 <= x <= 200)
a = pedir_float('Ángulo de lanzamiento, expresado (grados): ', lambda x: 1 <= x <= 89)
xi = pedir_float('Coordenada x del lanzamiento (Coyote): ', lambda x: 0 <= x < xc)
yi = pedir_float('Coordenada y del lanzamiento (Coyote): ', lambda x: x >= 0)

#angulo en radianes y velocidad a m/s
a_radianes = (a * math.pi)/180 #Conversion a radianes
v_conversion = (v * 10 )/36 #Conversion a m/s
#Descomponer velocidad en coseno y seno
vx = v_conversion * math.cos(a_radianes)
vy = v_conversion * math.sin(a_radianes)
#Las coordenadas (x,y) en el tiempo 0.1
xt1 = xi + (vx * 0.1)
yt1 = yi + (vy * 0.1) - (4.9 * (0.1**2))
#Las coordenadas (x,y) en el tiempo 0.2
xt2 = xi + vx * 0.2
yt2 = yi + vy * 0.2 - (4.9 * (0.2**2))
#Las coordenadas (x,y) en el tiempo 0.3
xt3 = xi + vx * 0.3
yt3 = yi + vy * 0.3 - (4.9 * (0.3**2))
#Tiempo estimado
d = vy**2 - (4 * -4.9 * yi)
tiempo_estimado = (-vy - math.sqrt(d))/(2 * -4.9)
#Tiempo 3s antes del impacto
tiempo_impacto1 = tiempo_estimado - 0.3
tiempo_impacto2 = tiempo_estimado - 0.2
tiempo_impacto3 = tiempo_estimado - 0.1
#Las coordenadas (x,y) en el tiempo 0.1 antes del impacto
xt4 = xi + (vx * tiempo_impacto1)
yt4 = yi + (vy * tiempo_impacto1) - (4.9 * (tiempo_impacto1**2))
#Las coordenadas (x,y) en el tiempo 0.1 antes del impacto
xt5 = xi + (vx * tiempo_impacto2)
yt5 = yi + (vy * tiempo_impacto2) - (4.9 * (tiempo_impacto2**2))
#Las coordenadas (x,y) en el tiempo 0.1 antes del impacto
xt6 = xi + (vx * tiempo_impacto3)
yt6 = yi + (vy * tiempo_impacto3) - (4.9 * (tiempo_impacto3**2))
#La coordenada x, del impacto
xt7 = xi + (vx * tiempo_estimado)
#Fallo del impacto
fallo_impacto = xt7 - xc
print('\nValores ajustados:')
print('Velocidad =',round(v_conversion,5),'m/s')
print('Ángulo de lanzamiento =',round(a_radianes,5),'radianes')
print('vx =',round(vx,5),'m/s')
print('vy =',round(vy,5),'m/s')
print('\nEvaluación del lanzamiento: ')
print('Tiempo de impacto estimado:',round(tiempo_estimado,5))
print('En tiempo 0 el proyectil se encuentra en: ',round(xi,5),round(yi,5))
print('En tiempo 0.1 el proyectil se encuentra en: ',round(xt1,5),round(yt1,5))
print('En tiempo 0.2 el proyectil se encuentra en: ',round(xt2,5),round(yt2,5))
print('En tiempo 0.3 el proyectil se encuentra en: ',round(xt3,5),round(yt3,5))
print('En tiempo',round(tiempo_impacto1,5),'el proyectil se encuentra en:',round(xt4,5),round(yt4,5))
print('En tiempo',round(tiempo_impacto2,5),'el proyectil se encuentra en:',round(xt5,5),round(yt5,5))
print('En tiempo',round(tiempo_impacto3,5),'el proyectil se encuentra en:',round(xt6,5),round(yt6,5))
print('Proyectil impacta en coordenada x:',round(xt7,5))
print('Se falló al Correcaminos por:',round(fallo_impacto,5))



       




