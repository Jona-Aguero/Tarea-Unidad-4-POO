
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def calcular_valor_stock(self):
        return self.precio * self.stock

    def __str__(self):
        return (f"Producto: {self.nombre}\n"
                f"Precio: {self.precio:,.0f} Gs.\n"
                f"Stock: {self.stock} unidades\n"
                f"Valor total: {self.calcular_valor_stock():,.0f} Gs.")


producto1 = Producto("Arroz", 8500, 20)
producto2 = Producto("Aceite", 15000, 12)
producto3 = Producto("Azucar", 7000, 30)

print("=== INVENTARIO DEL ALMACEN ===")

print(producto1)
print()
print(producto2)
print()
print(producto3)
