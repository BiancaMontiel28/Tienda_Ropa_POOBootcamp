class Producto:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    def mostrar_info(self):
        print(f"Nombre: {self._nombre}, Precio: {self._precio}, Cantidad: {self._cantidad}")

    def obtener_precio(self):
        return self._precio

    def reducir_cantidad(self, cantidad):
        self._cantidad -= cantidad


class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self._talla}")


class RopaHombre(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)


class RopaMujer(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)


class Carrito:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, prenda, cantidad):
        if cantidad <= prenda._cantidad:
            self._productos.append((prenda, cantidad))
            prenda.reducir_cantidad(cantidad)
            print(f"Agregado al carrito: {cantidad} x {prenda._nombre}")
        else:
            print("No hay suficiente stock para agregar al carrito.")

    def calcular_total(self):
        total = sum(prenda.obtener_precio() * cantidad for prenda, cantidad in self._productos)
        return total

    def mostrar_resumen(self):
        print("\nResumen de compra:")
        for prenda, cantidad in self._productos:
            print(f"{cantidad} x {prenda._nombre} a {prenda.obtener_precio()} cada uno.")
        print(f"Total a pagar: {self.calcular_total()}")


class Inventario:
    def __init__(self):
        self._prendas = []

    def agregar_prenda(self, prenda):
        self._prendas.append(prenda)

    def mostrar_inventario(self):
        for i, prenda in enumerate(self._prendas):
            print(f"{i + 1}. ", end="")
            prenda.mostrar_info()
            print()


# Función principal
def main():
    # Crear el inventario
    inventario = Inventario()
    inventario.agregar_prenda(RopaHombre("Camisa de Hombre", 25.00, 50, "M"))
    inventario.agregar_prenda(RopaHombre("Pantalón de Hombre", 30.00, 30, "L"))
    inventario.agregar_prenda(RopaHombre("Chaqueta de Hombre", 55.00, 20, "L"))
    inventario.agregar_prenda(RopaMujer("Falda de Mujer", 28.00, 15, "S"))
    inventario.agregar_prenda(RopaMujer("Blusa de Mujer", 22.00, 40, "M"))
    inventario.agregar_prenda(RopaMujer("Vestido de Mujer", 45.00, 10, "M"))
    inventario.agregar_prenda(RopaHombre("Zapatos de Hombre", 60.00, 25, "42"))
    inventario.agregar_prenda(RopaMujer("Zapatos de Mujer", 50.00, 20, "38"))

    # Mostrar el inventario
    inventario.mostrar_inventario()

    # Crear el carrito
    carrito = Carrito()

    # Interacción con el usuario para seleccionar productos
    while True:
        indice_compra = int(input("Seleccione un producto para comprar (número, 0 para finalizar): ")) - 1
        if indice_compra == -1:
            break
        cantidad_compra = int(input("Ingrese la cantidad a comprar: "))
        carrito.agregar_producto(inventario._prendas[indice_compra], cantidad_compra)

    # Mostrar resumen de la compra
    carrito.mostrar_resumen()

# Ejecutar el programa
if __name__ == "__main__":
    main()