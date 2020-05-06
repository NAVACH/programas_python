nombre=str(input("ingresar Nombre: "))
carrera=str(input("Ingresar Carrera: "))
print("***Ingresa 5 calificaciones***")
cal1=float(input("Matematicas: "))
cal2=float(input("Español: "))
cal3=float(input("Ciencias Naturales: "))
cal4=float(input("Geografia: "))
cal5=float(input("Ingles: "))
prom =(cal1+cal2+cal3+cal4+cal5)/5
print("Nombre: ",nombre , '//'  "Carrera: ",carrera , '//' "Promedio: ",prom)

if prom==10:
    print("grupo de A")
if prom>=9 and prom<10:
    print("Grupo de B")
if prom<9 and prom>=8:
    print("Grupo de C")
if prom<8 and prom>=7:
    print("Grupo de D")
if prom<7 and prom>6:
    print("grupo de E")
if prom<6:
    print("Grupo de F")
else:
    print("PROMEDIO ERRONEO")


    
    