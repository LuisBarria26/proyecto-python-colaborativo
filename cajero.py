# Diccionario donde se guardan los usuarios
usuarios = {}

print("===================================")
print("      💰 CAJERO AUTOMÁTICO 💰")
print("===================================")

# Preguntar si tiene usuario
while True:

    respuesta = input("¿Ya tienes un usuario? (SI/NO): ").strip().upper()

    if respuesta == "NO":

        print("\n===== CREAR USUARIO =====")

        nuevo_usuario = input("Ingrese un nombre de usuario: ")

        while nuevo_usuario in usuarios:
            print("Ese usuario ya existe.")
            nuevo_usuario = input("Ingrese otro nombre de usuario: ")

        nuevo_pin = input("Cree un PIN de 4 dígitos: ")

        usuarios[nuevo_usuario] = {
            "pin": nuevo_pin,
            "saldo": 1000,
            "historial": []
        }

        print("\n✅ Usuario creado correctamente.")
        print("Ahora inicie sesión.")
        break

    elif respuesta == "SI":
        break

    else:
        print("Respuesta inválida. Escriba SI o NO.")

# ==========================
# INICIO DE SESIÓN
# ==========================

while True:

    usuario = input("\nUsuario: ")

    if usuario not in usuarios:
        print("❌ Usuario incorrecto.")
        continue

    pin = input("PIN: ")

    if pin != usuarios[usuario]["pin"]:
        print("❌ Contraseña incorrecta.")
        continue

    print(f"\n✅ Bienvenido {usuario}")
    break

# ==========================
# MENÚ DEL CAJERO
# ==========================

opcion = 0

while opcion != 5:

    print("\n========== MENÚ ==========")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Ver historial")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:

        print(f"\nSu saldo actual es: ${usuarios[usuario]['saldo']:.2f}")

    elif opcion == 2:

        deposito = float(input("Ingrese el monto a depositar: $"))

        if deposito > 0:

            usuarios[usuario]["saldo"] += deposito

            usuarios[usuario]["historial"].append(
                f"Depósito: +${deposito:.2f}"
            )

            print("✅ Depósito realizado correctamente.")

        else:

            print("Monto inválido.")

    elif opcion == 3:

        retiro = float(input("Ingrese el monto a retirar: $"))

        if retiro > 0 and retiro <= usuarios[usuario]["saldo"]:

            usuarios[usuario]["saldo"] -= retiro

            usuarios[usuario]["historial"].append(
                f"Retiro: -${retiro:.2f}"
            )

            print("✅ Retiro realizado correctamente.")

        elif retiro > usuarios[usuario]["saldo"]:

            print("❌ Fondos insuficientes.")

        else:

            print("Monto inválido.")

    elif opcion == 4:

        print("\n===== HISTORIAL =====")

        if len(usuarios[usuario]["historial"]) == 0:

            print("No existen movimientos registrados.")

        else:

            for movimiento in usuarios[usuario]["historial"]:
                print(movimiento)

    elif opcion == 5:

        print("\nGracias por utilizar el Cajero Automático.")

    else:

        print("Opción no válida.")
