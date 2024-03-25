class Fruta:
    def __init__(self, id, nombre, precio_unitario, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
        self.costo_total = precio_unitario * cantidad

def main():
    N = int(input("Ingrese el número de frutas: "))
    frutas = []

    for i in range(N):
        id = i + 1
        nombre = input(f"Ingrese el nombre de la fruta {id}: ")
        precio_unitario = float(input(f"Ingrese el precio unitario de la fruta {id}: "))
        cantidad = int(input(f"Ingrese la cantidad de la fruta {id}: "))
        frutas.append(Fruta(id, nombre, precio_unitario, cantidad))

    costo_total = sum(fruta.costo_total for fruta in frutas)

    print(f"\nCosto total del salpicón: ${costo_total:.2f}\n")

    frutas_ordenadas = sorted(frutas, key=lambda x: x.costo_total, reverse=True)
    print("Frutas en orden descendente de costo:")
    for fruta in frutas_ordenadas:
        print(f"ID: {fruta.id}, Nombre: {fruta.nombre}, Costo Total: ${fruta.costo_total:.2f}")

    fruta_mas_barata = min(frutas, key=lambda x: x.precio_unitario)
    print(f"\nLa fruta más barata es: {fruta_mas_barata.nombre} (ID: {fruta_mas_barata.id})")

if __name__ == "__main__":
    main()
