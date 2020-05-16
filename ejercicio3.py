#pedir nombre de alumno
#pedir carrera
#pedir 9 calificaciones
#imprimir cuantas calificaciones son mayores a 7 y cuantas menores que 7
#sacar promedio
#si promedio es mayor o igual a 7 imprimir aprobado
#si no reprobado

nombre=input("Ingresa tu nombre: ")
carrera=input("Ingresa tu carrera: ")
cal=0
may=0
men=0
suma=0

for i in range(9):
    cal=int(input("ingresa tus calificaciones: "))

    if (cal>=7):
        may=may+1
    else:
        men=men+1
    suma=suma+cal
prom=suma/9
if prom>=7:
    print("usted esta aprobado")
else:
    print("usted esta reprobado")
    
print("Nombre de alumno ", nombre)
print("carrera de alumno ", carrera)
print("promedio de alumno ", prom)
print("calificaciones mayores a 7 ", may)
print("calificaciones menores de 7", men)



    