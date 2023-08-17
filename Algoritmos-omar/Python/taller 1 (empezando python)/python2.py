print("Ejercicio #6");

capital = 0;
prestamo = 0;
presupuesto = 0;
computo = 5000;
mobiliario = 2000;
insumos = 0;
incentivos = 0;

capital = float(input("Digite el saldo actual de la capital"));

if capital < 0 : 
    prestamo = 10000 + capital;
    presupuesto = 10000 - computo - mobiliario;
    insumos = presupuesto / 2;
    incentivos = presupuesto / 2;
elif capital > 0 : 
    prestamo = 20000 - capital;
    presupuesto = 20000
    insumos = presupuesto / 2;
    incentivos = presupuesto / 2;
elif capital > 20000 :
    prestamo = 0;
    presupuesto = capital - computo - mobiliario;
    insumos = presupuesto / 2;
    incentivos = presupuesto / 2;

print("Insumos: " + str(insumos) + "Incentivos: " + str(incentivos) + "Prestamo: " + str(prestamo));
