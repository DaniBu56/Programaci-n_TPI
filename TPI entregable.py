#TPI Programación 1
#Alumno: Burgos Daniela

import csv

# CSV
def cargar_paises():
    paises = []
    try:
        with open("Datos_paises.csv", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                paises.append({
                    "nombre": fila["nombre"].lower(),
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"].lower()
                })
    except FileNotFoundError:
        print("Error: No se encontró el archivo CSV.")
    return paises

def guardar_paises(paises):
    with open("Datos_paises.csv", "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(paises)

# OPCION 1: Agregar un país
def agregar_pais(paises):
    nombre = input("Nombre del país: ").strip().lower()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return
    if any(p["nombre"] == nombre for p in paises):
        print("Error: El país ya existe.")
        return
    try:
        poblacion = int(input("Población: "))
        superficie = int(input("Superficie: "))
        if poblacion < 0 or superficie <= 0:
            print("Error: Valores inválidos.")
            return
    except ValueError:
        print("Error: Debe ingresar números enteros.")
        return
    continente = input("Continente: ").strip()
    paises.append({"nombre": nombre, "poblacion": poblacion,
                   "superficie": superficie, "continente": continente})
    guardar_paises(paises)  #csv
    print("País agregado correctamente.")

# OPCION 2: Actualizar datos país de población y superficie
def actualizar_pais(paises):
    nombre = input("Nombre del país a actualizar: ").strip().lower()
    for p in paises:
        if p["nombre"] == nombre:
            try:
                nueva_poblacion = int(input("Nueva población: "))
                nueva_superficie = int(input("Nueva superficie: "))
                if nueva_poblacion < 0 or nueva_superficie <= 0:
                    print("Valores inválidos")
                    return
                p["poblacion"] = nueva_poblacion
                p["superficie"] = nueva_superficie
                guardar_paises(paises) 
                print("Datos actualizados correctamente")
                return
            except ValueError:
                print("Debe ingresar números enteros")
                return
    print("Error: País no encontrado")

# OPCION 3: Buscar un país por nombre
def buscar_pais(paises):
    nombre = input("Nombre del país a buscar: ").strip().lower()
    encontrados = [p for p in paises if nombre in p["nombre"]]
    if encontrados:
        for p in encontrados:
            print(f"País: {p['nombre']}")
            print(f"Población: {p['poblacion']}")
            print(f"Superficie: {p['superficie']} km²")
            print(f"Continente: {p['continente']}")
    else:
        print("Error: País no encontrado.")

# OPCION 4: Filtrar países
def filtrar_paises(paises):
    if not paises:
        print("No hay datos cargados.")
        return
    print("Filtrar por: 1.Continente  2.Rango de población  3.Rango de superficie")
    opcion = input("Elija criterio: ")
    if opcion == "1":
        cont = input("Continente: ").strip().lower()
        filtrados = [p for p in paises if p["continente"].lower() == cont]
    elif opcion == "2":
        try:
            minimo = int(input("Población mínima: "))
            maximo = int(input("Población máxima: "))
            filtrados = [p for p in paises if minimo <= p["poblacion"] <= maximo]
        except ValueError:
            print("Error: Debe ingresar números enteros.")
            return
    elif opcion == "3":
        try:
            minimo = int(input("Superficie mínima: "))
            maximo = int(input("Superficie máxima: "))
            filtrados = [p for p in paises if minimo <= p["superficie"] <= maximo]
        except ValueError:
            print("Error: Debe ingresar números enteros.")
            return
    else:
        print("Error: Opción inválida.")
        return
    print("Países filtrados:")
    for p in filtrados:
        print(f"País: {p['nombre']}")

# OPCION 5: Ordenar países
def clave_nombre(pais): return pais["nombre"]
def clave_poblacion(pais): return pais["poblacion"]
def clave_superficie(pais): return pais["superficie"]

def ordenar_paises(paises):
    if not paises:
        print("No hay datos cargados.")
        return
    print("Ordenar por: 1.Nombre  2.Población  3.Superficie")
    opcion = input("Elija criterio: ")
    if opcion == "1":
        paises.sort(key=clave_nombre)
    elif opcion == "2":
        paises.sort(key=clave_poblacion)
    elif opcion == "3":
        paises.sort(key=clave_superficie)
    else:
        print("Error: Opción inválida.")
        return
    print("Lista ordenada:")
    for p in paises:
        print(f"País: {p['nombre']} | "
              f"Población: {p['poblacion']} | "
              f"Superficie: {p['superficie']} km² | "
              f"Continente: {p['continente']}")

# OPCION 6: Estadísticas

def clave_poblacion(pais):
    return pais["poblacion"]

def clave_superficie(pais):
    return pais["superficie"]

def mostrar_estadisticas(paises):
    if not paises:
        print("No hay datos cargados.")
        return
    poblaciones = [p["poblacion"] for p in paises]
    superficies = [p["superficie"] for p in paises]
    continentes = {}
    for p in paises:
        c = p["continente"].lower()
        continentes[c] = continentes.get(c, 0) + 1
# Visualización
    mayor_poblacion = max(paises, key=clave_poblacion)
    menor_poblacion = min(paises, key=clave_poblacion)

    print("Estadísticas:")
    print("País con mayor población:")
    print(f"País: {mayor_poblacion['nombre']} | "
          f"Población: {mayor_poblacion['poblacion']} | "
          f"Superficie: {mayor_poblacion['superficie']} km² | "
          f"Continente: {mayor_poblacion['continente']}")
    
    print("País con menor población:")
    print(f"País: {menor_poblacion['nombre']} | "
          f"Población: {menor_poblacion['poblacion']} | "
          f"Superficie: {menor_poblacion['superficie']} km² | "
          f"Continente: {menor_poblacion['continente']}")

    print("Promedio población:", sum(poblaciones)//len(poblaciones))
    print("Promedio superficie:", sum(superficies)//len(superficies))
    print("Cantidad de países por continente:", continentes)

# Menú principal
def menu():
    paises = cargar_paises()  # para CSV
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar país")
        print("2. Actualizar país")
        print("3. Buscar país")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Salir")
        opcion = input("Elija una opción: ")
        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_paises(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "7":
            print("Fin del programa.")
            break
        else:
            print("Error: Opción inválida.")

# Bloque principal
menu()