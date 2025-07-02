# La escuela ECAPMA de la UNAD está desarrollando un estudio para verificar el cambio climático en su ciudad. Para esto, le ha pedido su ayuda en la construcción de un programa que solicite las temperaturas de los últimos 15 días, las cuales debe almacenar lista y debe mostrar el promedio de temperaturas.
temperaturas = []
dia = 0
while dia < 15:
    try:
        dato = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
        temperaturas.append(dato)
        dia += 1
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número (use punto como decimal).")
# Cálculo del promedio
promedio = sum(temperaturas) / len(temperaturas)
# Resultados
print("\nTemperaturas registradas:", temperaturas)
print(f"Promedio de los últimos 15 días: {promedio:.2f} °C")