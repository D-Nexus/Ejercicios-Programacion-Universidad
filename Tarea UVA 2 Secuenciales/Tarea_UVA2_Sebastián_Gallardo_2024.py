# Librerias
import math
# Entradas
print('*** Kiwi ayuda al Coyote ***')
print('Ingrese los siguiente datos: \n')
#función para evaluar si los datos son validos
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

def calcular_coordenadas(xi, yi, vx, vy, t):
    #Calcula las coordenadas (x, y) de un proyectil en un tiempo t.
    xt = xi + vx * t
    yt = yi + vy * t - (4.9 * t**2)  # Incluye el efecto de la gravedad
    return xt, yt

def mostrar_coordenadas_tiempo(xi, yi, vx, vy):
    #Muestra las coordenadas del proyectil en tiempos específicos.
    tiempos = [0.1, 0.2, 0.3] #tiempos
    print('En tiempo 0 el proyectil se encuentra en:', round(xi, 5), round(yi, 5))
    for t in tiempos:
        xt, yt = calcular_coordenadas(xi, yi, vx, vy, t)
        print(f'En tiempo {t} el proyectil se encuentra en:', round(xt, 5), round(yt, 5))

def calcular_tiempo_impacto(vy, yi):
    #Calcula el tiempo estimado de impacto del proyectil.
    d = vy**2 - (4 * -4.9 * yi)  # Discriminante de la fórmula cuadrática
    tiempo_estimado = (-vy - math.sqrt(d)) / (2 * -4.9)
    return tiempo_estimado

#Entradas        
xc = pedir_float('Coordenada x del Correcaminos: ', lambda x: x > 0)
v = pedir_float('Velocidad inicial de lanzamiento (kms/h): ', lambda x: 10 <= x <= 200)
a = pedir_float('Ángulo de lanzamiento, expresado (grados): ', lambda x: 1 <= x <= 89)
xi = pedir_float('Coordenada x del lanzamiento (Coyote): ', lambda x: 0 <= x < xc)
yi = pedir_float('Coordenada y del lanzamiento (Coyote): ', lambda x: x >= 0)

# Conversión de unidades
a_radianes = (a * math.pi) / 180  # Conversión a radianes
v_conversion = (v * 10) / 36  # Conversión de km/h a m/s

# Componentes de velocidad
vx = v_conversion * math.cos(a_radianes)
vy = v_conversion * math.sin(a_radianes)

# Cálculo del tiempo de impacto estimado
tiempo_estimado = calcular_tiempo_impacto(vy, yi)

# Coordenada del impacto y fallo
xt7 = xi + (vx * tiempo_estimado)
fallo_impacto = xt7 - xc

print('\nValores ajustados:')
print('Velocidad =', round(v_conversion, 5), 'm/s')
print('Ángulo de lanzamiento =', round(a_radianes, 5), 'radianes')
print('vx =', round(vx, 5), 'm/s')
print('vy =', round(vy, 5), 'm/s')
print('\nEvaluación del lanzamiento:')
print('Tiempo de impacto estimado:', round(tiempo_estimado, 5),'s')

# Mostrar coordenadas a tiempo específico
mostrar_coordenadas_tiempo(xi, yi, vx, vy)

# Calcular coordenadas justo antes del impacto
tiempos_antes_impacto = [tiempo_estimado - 0.3, tiempo_estimado - 0.2, tiempo_estimado - 0.1]
for t in tiempos_antes_impacto:
    xt, yt = calcular_coordenadas(xi, yi, vx, vy, t)
    print(f'En tiempo {round(t, 5)} el proyectil se encuentra en:', round(xt, 5), round(yt, 5))

print('Proyectil impacta en coordenada x:', round(xt7, 5))
print('Se falló al Correcaminos por:', round(fallo_impacto, 5),'m')



       




