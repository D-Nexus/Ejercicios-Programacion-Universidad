#librerias
import math
#Entradas
xc = float(input("Coordenada x del Correcaminos: "))
v = float(input("Velocidad inicial de lanzamiento (kms/h): "))
angulo = float(input("Ángulo de lanzamiento, expresado (grados): "))
x = float(input("Coordenada x del lanzamiento (Coyote): "))
y = float(input("Coordenada y del lanzamiento (Coyote): "))
print(" ") #Salto de linea
#Proceso
v_conversion = (v * 1000) / 3600 #Conversión de Kms/h --> m/s
angulo_r = angulo * math.pi / 180 #Conversión grados a radianes
vx = v_conversion * math.cos(angulo_r) #Componente horizontal velocidad(x)
vy = v_conversion * math.sin(angulo_r) #Componente vertical velocidad(y)
#tiempo 0s
t = 0
xt = round((x + vx * t),5)
yt = round((y + vy * t - 4.9 * t **2),5)
#tiempo 0.1s
t1 = 0.1
xt1 = round((x + vx * t1),5) 
yt1 = round((y + vy * t1 - 4.9 * t1 **2),5)
#tiempo 0.2s
t2 = 0.2
xt2 = round((x + vx * t2),5) 
yt2 = round((y + vy * t2 - 4.9 * t2 **2),5)
#tiempo 0.3s
t3 = 0.3
xt3 = round((x + vx * t3),5) 
yt3 = round((y + vy * t3 - 4.9 * t3 **2),5)
#tiempo estimado de impacto ecuacion de segundo grado
d = (vy)**2 - 4 * (-4.9) * y
tiempo_estimado = (-vy - math.sqrt(d)) / (2*(-4.9))
#tiempo 0.1s antes del impacto
tiempo_impacto1 = tiempo_estimado - 0.1
xt4 = round((x + vx * tiempo_impacto1),5)
yt4 = round((y + vy * tiempo_impacto1 - 4.9 * tiempo_impacto1 **2),5)
#tiempo 0.2s antes del impacto
tiempo_impacto2 = tiempo_estimado - 0.2
xt5 = round((x + vx * tiempo_impacto2),5)
yt5 = round((y + vy * tiempo_impacto2 - 4.9 * tiempo_impacto2 **2),5)
#tiempo 0.3s antes del impacto
tiempo_impacto3 = tiempo_estimado - 0.3
xt6 = round((x + vx * tiempo_impacto3),5)
yt6 = round((y + vy * tiempo_impacto3 - 4.9 * tiempo_impacto3 **2),5)
#impacto
xt7 = x + vx * tiempo_estimado
#falló de impacto al Correcaminos
fallo = xt7 - xc
#Salida
print("Valores ajustados:")
print("Velocidad =",round(v_conversion,5),"m/s")
print("Ángulo de lanzamiento =",round(angulo_r,5),"radianes") 
print("vx =",round(vx,5),"m/s")
print("vy =",round(vy,5),"m/s")
print(" ") #Salto de linea
print("Evaluación del lanzamiento:")
print("Tiempo de impacto estimado:",round(tiempo_estimado,5),"s")
print("En tiempo 0 el proyectil se encuentra en:",xt,yt)
print("En tiempo 0.1 el proyectil se encuentra en:",xt1,yt1)
print("En tiempo 0.2 el proyectil se encuentra en:",xt2,yt2)
print("En tiempo 0.3 el proyectil se encuentra en:",xt3,yt3)
print("En tiempo",round(tiempo_impacto3,5),"el proyectil se encuentra en:",xt6,yt6)
print("En tiempo",round(tiempo_impacto2,5),"el proyectil se encuentra en:",xt5,yt5)
print("En tiempo",round(tiempo_impacto1,5),"el proyectil se encuentra en:",xt4,yt4)
print("Proyectil impacta en coordenada x:",round(xt7,5))
print("Se falló al Correcaminos por:",round(fallo,5))

