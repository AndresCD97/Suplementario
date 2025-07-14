actividades = ["Natación", "Gimnasio", "Tenis", "Yoga"]

cupos_disponibles = [13, 15, 14, 12] #cupos disponibles iniciales

mis_reservas = []

def cliente_nombre():
    nombre = input("Ingrese nombre: ").strip()
    if nombre:
        return nombre
    print("El valor para nombre no puede estar vacío.")
    return cliente_nombre()

def mostrar_actividades():
    print("\nActividades disponibles:")
    for i, actividad in enumerate(actividades):
        print(f"{i + 1}. {actividad} (Cupos disponibles: {cupos_disponibles[i]})")

def reservar_actividad():
    nombre = cliente_nombre()
    apellido = input("Ingrese apellido: ").strip()
    mostrar_actividades()

    try:
        opcion = int(input("Seleccione la actividad (número): "))
        if 1 <= opcion <= len(actividades):
            indice = opcion - 1
            if cupos_disponibles[indice] > 0:
                cupos_disponibles[indice] -= 1
                reserva = f"{nombre} {apellido} reservó {actividades[indice]}"
                mis_reservas.append(reserva)
                print("Reserva confirmada")
            else:
                print("No hay cupos disponibilidad de cupos")
        else:
            print("Error, ingrese valor valido")
    except ValueError:
        print("Entrada no válida. Debe ser un número.")

def ver_reservas():
    print("\n Lista de reservas:")
    if mis_reservas:
        for r in mis_reservas:
            print("-", r)
    else:
        print("No hay reservas")

def menu():
    llave = True
    while llave:
        print("\nCentro de deportivo")
        print("1. Reservar una actividad")
        print("2. Ver reservas")
        print("3. Salir del sistema")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            reservar_actividad()
        elif opcion == "2":
            ver_reservas()
        elif opcion == "3":
            print("END")
            llave = False
        else:
            print("ERROR, ingrese opcion valida")

menu()
