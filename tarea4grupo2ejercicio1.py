# Los 20 estudiantes del profesor Juan requieren un programa que les indique si han aprobado el curso. Para esto, usted debe solicitar por cada estudiante la nota definitiva y si dicha nota es menor a 3 que muestre un mensaje indicando que no ha aprobado el curso. Si es igual 3 y menor a 4.5 debe mostrar un mensaje que informe que el estudiante ha aprobado el curso, si la nota es mayor a 4.5 muestre el mensaje que ha aprobado el curso con un desempeño superior. Después de registrar todos los estudiantes, se debe mostrar la cantidad de estudiantes que han aprobado, la cantidad de estudiantes que perdieron el curso y la cantidad de estudiantes con desempeño superior.
# Inicializamos contadores
aprobados = 0
perdidos = 0
desempeño_superior = 0
# Ciclo para 20 estduaintes.
for i in range(1, 21):
    nota = float(input(f"Ingrese la nota del estudiante {i}: "))
    if nota < 3.0:
        print("No ha aprobado el curso.")
        perdidos += 1
    elif nota < 4.5:
        print("Ha aprobado el curso.")
        aprobados += 1
    else:
        print("ha aprobado el curso con desempeño superior.")
        desempeño_superior += 1
# Resultados finales.
print("\n Resumen de resultados:")
print(f"Estudiantes que aprobaron: {aprobados}")
print(f"Estudiantes que perdieron: {perdidos}")
print(f"Estudiantes con desempeño superior: {desempeño_superior}")