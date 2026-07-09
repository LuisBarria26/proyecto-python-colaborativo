def imprimir_cuento():
    nombre = input("Ingresa el nombre del protagonista: ")
    lenguaje = input("¿Qué lenguaje aprendió?: ")
    herramienta = input("¿Qué herramienta aprendió?: ")

    print("\n--- Cuento ---")
    print("Había una vez un estudiante llamado", nombre + ".")
    print(nombre, "aprendió", herramienta, "y", lenguaje + ".")
    print("Con esfuerzo terminó su proyecto exitosamente.")
    print("Finalmente,", nombre, "compartió su proyecto con otros desarrolladores.")
    print("Desde ese día,", nombre, "siguió aprendiendo y colaborando en nuevos proyectos de software.")

imprimir_cuento()
