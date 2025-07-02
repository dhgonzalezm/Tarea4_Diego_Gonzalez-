# Para el ingreso a la montaña rusa, el parque mundo locura valida que la persona tenga una altura igual o superior a 1.20 y le han solicitado su ayuda para construir un programa que solicite la altura de n personas y muestre un mensaje indicando si la persona puede ingresar o no a la atracción. Después de la validación de cada persona, se debe preguntar si desea registrar una nueva persona, el programa finaliza cuando el usuario responda que no desea registrar más.
altura_minima = 1.20        # metros
persona = 1                 # contador opcional
print("Bienvenido al registro de la montaña rusa Mundo Locura\n")
while True:
    # 1) Pedir la altura
    try:
        altura = float(input(f"Altura de la persona #{persona}: "))
    except ValueError:
        print("Entrada no válida. Usa números y punto decimal (ej.: 1.58).\n")
        continue                         # Repite esta iteración
    # 2) Evaluar la altura
    if altura >= altura_minima:
        print("Puede ingresar a la atracción.\n")
    else:
        print("No cumple con la altura mínima. Lo sentimos.\n")
    # 3) Preguntar si se registra otra persona
    continuar = input("¿Registrar otra persona? (s/n): ").strip().lower()
    if continuar not in ("s", "si", "sí"):
        break
    persona += 1
    print()  # Línea en blanco para separar registros
print("\n Registro finalizado. ¡Disfruta tu visita!")