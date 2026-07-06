from operaciones import suma, resta, multiplicacion, division
from cuento import imprimir_cuento

print("=== Operaciones Matemáticas ===")
print("Suma:", suma(10, 5))
print("Resta:", resta(10, 5))
print("Multiplicación:", multiplicacion(10, 5))
print("División:", division(10, 5))

print("\n" + "="*30)  # línea agregada

print("\n=== Cuento ===")
imprimir_cuento()
