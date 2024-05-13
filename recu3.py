def calculate_grade(Practica01, Practica02, Practica03, Examen, Recuperacion, Actitud):
   
    '''La función recibirá las notas de todos los apartados evaluados de cada alumno/a 
       y devolverá una nota final y un valor Verdadero/Falso en función de si ha aprobado o suspendido.

        Parámetros:
            - La función tendremos seis float con las diferentes notas de cada alumno/a (Practica01, 
            Practica02, Practica03, Examen, Recuperacion y Actitud)
        Salida:
            -La función devolvera un float con la nota final resultante y un booleano 
            con el valor True si el/la alumno/a ha aprobado o el valor False si el/la alumno/a ha suspendido.


    '''
    nota_final = ((Practica01 + Practica02 + Practica03) / 3) * 0.3 + max(Examen, Recuperacion) * 0.6 + Actitud * 0.1
    nota_final = round(nota_final,2)
    aprobado = nota_final >=5
    if aprobado:
        return(float(nota_final),':',aprobado)
    else:
        return(float(nota_final),':',aprobado)

calculate_grade(7.8,5,8.5,0,5,0)