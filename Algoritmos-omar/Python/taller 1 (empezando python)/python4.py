print("Ejercicio #8");

promedio = 0;
descuento = 0;
tipoAlumno = '';

uniCursar = 0;
colegiatura = 0;
desCurso = 0;
totalPagar = 0;

tipoAlumno = int(input("Digite 1.Alumno Preparatoria 2.Alumno Profesional"));
promedio = float(input("Digite su promedio"));

if tipoAlumno == 1 :
    if promedio >= 9.5 :
        uniCursar = 55;
        colegiatura = (uniCursar / 5) * 180;
        desCurso = colegiatura * 0.25;
        totalPagar = colegiatura - desCurso;
        print("Total a pagar por colegiatura de preparatoria: " + totalPagar + "$" + " Recibiste un descuento: " + desCurso);
    elif promedio >= 9 : 
        uniCursar = 50;
        colegiatura = (uniCursar / 5) * 180;
        desCurso = colegiatura * 0.10;
        totalPagar = colegiatura - desCurso;
        print("Total a pagar por colegiatura de preparatoria: " + totalPagar + "$" + " Recibiste un descuento: " + desCurso);
    elif promedio > 7 : 
        uniCursar = 50;
        colegiatura = (uniCursar / 5) * 180;
        print("Total a pagar por colegiatura de preparatoria: " + totalPagar + "$" + " no recibiste descuento" + " Materias perdidas de 0 a 3");
    elif promedio <= 7 :
        uniCursar = 45 ;
        colegiatura = (uniCursar / 5) * 180;
    print("Total a pagar por colegiatura de preparatoria: " + totalPagar + "$" + " no recibiste descuento" + " Materias perdidas es de 4 o mas");
elif tipoAlumno == 2 :
    if promedio >= 9.5 :
        uniCursar = 55;
        colegiatura = (uniCursar / 5) * 300;
        desCurso = colegiatura * 0.20;
        totalPagar = colegiatura - desCurso;  
        print("Total a pagar por colegiatura de preparatoria: " + totalPagar + "$" + " Recibiste un descuento: " + desCurso);
    else :
        uniCursar = 55;
        colegiatura = (uniCursar / 5) * 300;
        print("Total a pagar por colegiatura de preparatoria: " + totalPagar + "$" + " No recibiste descuento");
else :
    print("Solo puede digitar 1 o 2");



