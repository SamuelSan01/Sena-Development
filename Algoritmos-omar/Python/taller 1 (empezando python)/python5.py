print("Ejercicio #9");

num1 = 0;
num2 = 0;
num3 = 0;

num1 = float(input("Digite un primer numero"));
num2 = float(input("Digite un segundo numero"));
num3 = float(input("Digite un tercer numero"));

if num1 > num2 and num1 < num3 :
        print("Mediana es: " + str(num1));
elif num2 > num1 and num2 < num3 :
        print("Mediana es: " + str(num2));
elif num3 > num1 and num3 < num2 :
        print("Mediana es: " + str(num3));
elif num1 < num2 and num1 > num3 :
        print("Mediana es: " + str(num1));
elif num2 < num1 and num2 > num3 :
        print("Mediana es: " + num2);
elif num3 < num1 and num3 > num2 :
        print("Mediana es: " + str(num3));
    
