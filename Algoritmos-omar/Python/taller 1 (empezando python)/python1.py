print("Ejercicio #5")

precioKilo = float(input("Digite el precio por kilo de las manzanas"))
numKilos = float(input("Digite cuantos kilos de manzana compro"))
descuento = 0
precioPagar = 0
cliente = ""
if numKilos <= 2 : 
    descuento = 0
    precioPagar = precioKilo * numKilos
    cliente = "0%"
elif numKilos <= 5 :
    descuento = precioKilo - (precioKilo * 0.1)
    precioPagar = descuento * numKilos
    cliente = "10%"
elif numKilos <= 10 :
    descuento = precioKilo - (precioKilo * 0.15)
    precioPagar = descuento * numKilos
    cliente = "15%"
else : 
    descuento = precioKilo - (precioKilo * 0.20)
    precioPagar = descuento * numKilos
    cliente = "20%"

print("Precio a pagar: " + str(precioPagar) + "Descuento: " + str(cliente))


    