# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Condicionales anidados
numero_1 = 7
numero_2 = -2

# Verifique si el numero_1 es mayor a 5
#   --> En caso afirmativo, verifique si el numero_2
#       es positivo

if numero_1 > 5:
    if numero_2 > 0:
        print("Resp = 1")
    else:
        print("Resp = 2")
else:
    if numero_2 > 5:
        print("Resp = 3")
    else:
        print("Resp = 4")


# Verifique la calificación de un estudiante según su
# puntaje en un examen
puntaje = 70

# Si el puntaje es mayor igual a 90 --> imprimir A
# Si el puntaje es mayor igual a 80 --> imprimir B
# Si el puntaje es mayor igual a 70 --> imprimir C
# Si el puntaje es mayor igual a 60 --> imprimir D
# Si el puntaje es menor a  60      --> imprimir F

if puntaje >= 90:
    puntaje_1 = "A"
elif puntaje >= 80:
    puntaje_2 = "B"
elif puntaje >= 70:
    puntaje_3 = "C"
elif puntaje >= 60:
    puntaje_4 = "D"
else:
    puntaje_5 = "F"
# Debe imprimir en pantalla la calificacion
# Utilizar "if" anidados

if puntaje >= 90:
    print("El puntaje es:", puntaje_1,"(",puntaje,")")
elif puntaje >= 80:
    print("El puntaje es:", puntaje_2,"(",puntaje,")")
elif puntaje >= 70:
    print("El puntaje es:", puntaje_3,"(",puntaje,")")
elif puntaje >= 60:
    print("El puntaje es:", puntaje_4,"(",puntaje,")")
else:
    print("El puntaje es:", puntaje_5,"(",puntaje,")")