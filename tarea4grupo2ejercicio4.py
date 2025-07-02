# Construir una función que reciba como parámetro el año de nacimiento de una persona y calcule si esa persona es mayor de edad o no.
from datetime import date
def edad_y_mayoria(año: int, mes: int, dia: int) -> tuple[int, bool]:
    hoy = date.today()
    nacimiento = date(año, mes, dia)
    edad = hoy.year - nacimiento.year
    if hoy < date(hoy.year, mes, dia):
        edad -= 1
    return edad, edad >= 18
try:
    año = int(input("Ingresa tu año de nacimiento (ej. 2008): "))
    mes = int(input("Ingresa tu mes de nacimiento (1-12): "))
    dia = int(input("Ingresa tu día de nacimiento (1-31): "))
    edad, mayor = edad_y_mayoria(año, mes, dia)
    print(f"\nTienes {edad} años.")
    if mayor:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")
except ValueError:
    print("Por favor, ingresa solo números enteros válidos.")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")