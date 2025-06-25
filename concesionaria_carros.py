class Carro:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca
        self.disponible = True

    def marcar_vendido(self):
        if self.disponible:
            self.disponible = False
            print(f"El auto {self.modelo} ha sido vendido")
        else:
            print(f"El auto {self.modelo} no está disponible")


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carros_comprados = []

    def comprar_carro(self, carro):
        if carro.disponible:
            carro.marcar_vendido()
            self.carros_comprados.append(carro)
            print(f"{self.nombre} ha comprado el {carro.modelo}")
        else:
            print(f"El carro {carro.modelo} no está disponible")


class Concesionario:
    def __init__(self):
        self.carros = []
        self.clientes = []

    def agregar_carro(self, carro):
        self.carros.append(carro)
        print(f"El carro {carro.modelo} ha sido agregado")

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"El cliente {cliente.nombre} ha sido agregado")

    def mostrar_carros_disponibles(self):
        print("Carros disponibles:")
        for carro in self.carros:
            if carro.disponible:
                print(f"{carro.modelo} hecho por {carro.marca}")


# Crear carros
carro1 = Carro("Civic", "Honda")
carro2 = Carro("Corolla", "Toyota")
carro3 = Carro("Mustang", "Ford")

# Crear cliente
cliente1 = Cliente(input("Tu nombre es: "))

# Crear concesionario
concesionario = Concesionario()
concesionario.agregar_carro(carro1)
concesionario.agregar_carro(carro2)
concesionario.agregar_carro(carro3)
concesionario.agregar_cliente(cliente1)

# Mostrar carros disponibles
concesionario.mostrar_carros_disponibles()

# Realizar compra
cliente1.comprar_carro(carro2)

# Mostrar carros disponibles nuevamente
concesionario.mostrar_carros_disponibles()

