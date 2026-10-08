
# Ejercicio 1: Ficha de cliente

class Cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Cedula: {self.cedula}\n"
                f"Telefono: {self.telefono}")


# Creamos dos clientes diferentes
cliente1 = Cliente("Juan Perez", "5123456", "0981123456")
cliente2 = Cliente("Maria Lopez", "6234567", "0972234567")

# Mostramos sus fichas
print("=== CLIENTE 1 ===")
print(cliente1)

print("\n=== CLIENTE 2 ===")
print(cliente2)
