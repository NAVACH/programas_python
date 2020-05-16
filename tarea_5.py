cantdepro=0
cantdecadapro=0
totdepro=0
totdecompra=0
leche=100
pleche=20
huevo=100
phuevo=18.5
sabritas=100
psabritas=12.5
coca=100
pcoca=25
cantdeleche=0
cantdehuevo=0
lechem=0
huevom=0
sabritasm=0
cocam=0
total=0
totalcash=0
costoleche=0
costohuevo=0
costosabritas=0
costococa=0
totalstockleche=0
totalstockhuevo=0
totalstocksabritas=0
totalstockcoca=0
lechemenos=0
huevomenos=0
sabritasmenos=0
cocamenos=0
persona=0
porcentaje1=int(0)
porcentaje2=int(0)
porcentaje3=int(0)
porcentaje4=int(0)

print(" ####BIENVENIDO#### ")
sistema=input("Ingresa venta:  si/no   ")
    
while(sistema !="no"):
    print("*********para terminar compra presiona n*************")
    producto=input("Ingresa nombre de producto: ")
    lechemenos=leche-lechem
    huevomenos=huevo-huevom
    sabritasmenos=sabritas-sabritasm
    cocamenos=coca-cocam
    if (producto=="leche" or producto=="huevo" or producto=="sabritas" or producto=="coca"):
        #LECHE
        if (producto == "leche"):
            
            if lechemenos>=1:  
                cantdeleche=int(input("ingresa la natidad de unidades:  "))
                porleche1=leche/100*50
                costoleche=pleche*cantdeleche
                lechem=cantdeleche+0  
            elif(lechemenos==0):
                print("*****PRODUCTO AGOTADO*****")
            continue
        #HUEVO
        elif(producto== "huevo"):
            
            if huevomenos>=1:
                cantdehuevo=int(input("ingresa la cantidad de huevo por unidad:  "))
                costohuevo=phuevo*cantdehuevo
                huevom=cantdehuevo+0
            elif (huevomenos==0):
                print("***PRODUCTO AGOTADO***")
            continue
        #SABRITAS
        elif(producto=="sabritas"):
            
            if sabritasmenos>=1:
                cantdesabritas=int(input("ingresa la cantidad de sabritas por unidad:  "))
                costosabritas=psabritas*cantdesabritas
                sabritasm=cantdesabritas+0
            elif(sabritasmenos==0):
                print("*****PRODUCTOAGOTADO*****")
            continue
        #COCA
        elif(producto=="coca"):
            
            if cocamenos>=1:   
                cantdecoca=int(input("ingresa cantidad de coca por unidad:   "))
                costococa=pcoca*cantdecoca
                cocam=cantdecoca+0
            elif(cocamenos==0):
                print("****PRODUCTO AGOTADO****")
            continue 
                
    else:   
            total=lechem+huevom+sabritasm+cocam
            totalcash=costoleche+costohuevo+costosabritas+costococa
            porcentaje1=leche/100*lechemenos
            porcentaje2=huevo/100*huevomenos
            porcentaje3=sabritas/100*sabritasmenos
            porcentaje4=coca/100*cocamenos
            print("cantidad por producto", "leche= ",pleche, " huevo= ", phuevo,  "sabritas= ", psabritas, "coca= ", pcoca)
            print("total de leche: ", lechem , " cantidad de huevo: ", huevom , " cantidad de sabritas: ", sabritasm , " cantidad de coca: ", cocam )
            print("cantidad total de unidades/productos", total)
            print("cantidad total a pagar en efectivo: ", totalcash)

            print("porcentaje de leche es:", porcentaje1)
            print("porcentaje de huevo es:", porcentaje2)
            print("porcentaje de sabritas es:", porcentaje3)
            print("porcentaje de coca es:", porcentaje4)
            print("***Fin de su compra GRACIAS***")
            if(porcentaje1==50):
                print("leche mitad en existencia")
            elif(porcentaje1<=25):
                print("leche producto escaso")
            if(porcentaje2==50):
                    print("HUEVO mitad en existencia")
            elif(porcentaje2<=25):
                print("HUEVO producto escaso")
            if(porcentaje3==50):
                print("SABRITAS mitad en existencia")
            elif(porcentaje3<=25):
                print("SABRITAS producto escaso")
            if(porcentaje4==50):
                print("COCA mitad en existencia")
            elif(porcentaje4<=25):
                print("COCA producto escaso")
    persona=persona+1
    
        
##CIERRE DE TIENDA........stock, totsl de clientes, productos vendidos
    respuesta=input("CIERRE DE TIENDA------(si/no)")
    if (respuesta=="no"):
        sistema=input("Continuar compra (si/no)?:  ")
        continue
        
    elif (respuesta=="si"):

        print("****STOCK****")
        print("la cantidad de stock es: " )
        #PRODUCTO_VENDIDO
        print("leche=", lechemenos)
        print("huevo=", huevomenos)
        print("sabritas=", sabritasmenos)
        print("coca=", cocamenos)
        #CLIENTES
        print("****CLIENTES****")
        print("la cantidad de clientes HOY: " )
        print(persona)
        #TOTALVENTA
        print("cocas vendidas:_ ", cocam, " cantidad de huevo vendido:_ ", huevom )
        print("sabritas vendidas:_ ",sabritasm , " cantidad de leche vendido:_ ", lechem)
        #TOTALCASH
        print("cantidad vendida:_ ", totalcash)
    break
        
    

   

            
        
        
        





    