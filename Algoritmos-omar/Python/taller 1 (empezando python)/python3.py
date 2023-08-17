print("Ejercicio #7");

edadMeses = 0;
edadAños = 0;
hemoglobina = 0;
sexo = 0;

hemoglobina = int(input("Digite su nivel de hemoglobina"));
edad = int(input("Es menor de un año? 1.Si 2.No"));

if edad == 1 :
    edadMeses = int(input("Digite su edad en meses"));
    if edadMeses <= 1 :
        if hemoglobina >= 13 :
            print("Resultado Negativo");
        else : 
            print("Resultado Positivo");
    elif edadMeses <= 6 :
        if hemoglobina >= 10 :
            print("Resultado Negativo");
        else : 
            print("Resultado Positivo");
    elif edadMeses <= 12 :
        if hemoglobina >= 11 :
            print("Resultado Negativo");
        else : 
            print("Resultado Positivo");
elif edad == 2 :
    edadAños = int(input("Digite su edad en años"));
    if edadAños <= 15 :
        if edadAños <= 5 :
            if hemoglobina <= 11.5 :
                print("Resultado Negativo");
            else :
                print("Resultado Positivo");
        elif edadAños <= 10 :
            if hemoglobina <= 12.6 :
                print("Resultado Negativo");
            else :
                print("Resultado Positivo");
        elif edadAños <= 15 :
            if hemoglobina <= 13 :
                print("Resultado Negativo");
            else :
                print("Resultado Positivo");
    else :
        sexo = int(input("Digite su sexo 1.MASCULINO 2.FEMENINO"));
        if sexo == 1 :
            if hemoglobina >= 14 :
                print("Resultado Negativo");
            else :
                print("Resultado Positivo");
        elif sexo == 2 :
            if hemoglobina >= 12 :
                print("Resultado Negativo");
            else :
                print("Resultado Positivo");
print("GRACIAS POR CONSULTAR :D");

