#ejercicio 4
#pedir edades y sexo de N numero de personas, seguir censando hasta que se ingrese por tecldo "no"
#imprimir cuantas menores de edad
#cuantos mujeres mayores de edad
#cuantos hombres menores de edad
#cuantos hombres mayores de edad
#si el sexo diferente de "masculino" imprimir "erroneo" y terminar el programa
#cuando llegue a 5 hombres mayores de edad imprimir "se ha censado 5 hombres hasta el momento" y continuar programa
#cuando llegue a 5 mujeres mayores de edad imprimir "se ha censado 5 mujeres hasta el momento" y continuar programa
#imprimir numero de personas censadas
hommay=0
hommen=0
mujmay=0
mujmen=0
sum=0
cen=input("se registra persona?: ")
while(cen!="no"):
    edad=int(input("Ingresa edad: "))
    sexo=input("ingresa sexo femenino/masculino: ")
    if (sexo == "masculino" or sexo=="femenino"):
        if (sexo=="masculino" and edad>17):
            hommay=hommay+1
            if hommay==5:
                print("5 hombres mayores de edad imprimir se ha censado 5 hombres hasta el momento")
                continue
            elif(sexo=="masculino" and edad<=17):
                hommen=hommen+1        
            if(sexo=="femenino" and edad>17):
                mujmay=mujmay+1
                mujmay==5
                print("5 mujeres mayores de edad imprimir se ha censado 5 hombres hasta el momento")
                continue
            elif(sexo=="femenino" and edad<=17):
                mujmen=mujmen+1
        sum=sum+1
    else:
        print("XXXsexo no especificadoXXX")
        break
        cen=input("ingresa persona nuevamente?: ")
print("personas censadas: ", sum)
print("hombres mayores de edad: ", hommay, "_____" " Hombres menores: ", hommen)
print("mujeres menores: ", mujmay,  " ____ " " mujeres menores: ", mujmen)
    
                
                






