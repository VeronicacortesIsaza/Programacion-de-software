class Persona:
    def __init__(self, nombre:str, documento:str):
        self.nombre =  nombre
        self.documento = documento

    def __str__(self) -> str:
        return f"{self.nombre}, se creo esta persona con el documneto {self.documento}"
    
class CuentaBancaria:
    def __init__(self, titutar: Persona, saldo: int = 0):
        self.titutar = titutar
        self._saldo = saldo
         
    def saldo(self) -> int:
        return self._saldo
    
    def depositar(self, monto: float) -> None:
        if monto > 0:
            self._saldo += monto
            print(f"Se depósito un monto de {monto} y mi saldo actual {self._saldo}")
        else:
            print("El monto debe ser positivo")

    def retirar(self, monto: float) -> None:
        if monto <= self._saldo:
            self._saldo -= monto
            print(f"Se retira del saldo {self._saldo} el monto de {monto}")
        else:
            print(f"no se puede retirar un monto mayor al saldo de la cuenta")

    def __str__(self) -> str:
        return f"Cuenta de {self.titutar.nombre} - Documento: {self.titutar.documento} - Saldo: ${self._saldo}"

        
class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo = 0, interes: float = 0.02):
        super().__init__(titular, saldo)
        self.interes = interes

    def calcular_interes(self):
        ganancia = self._saldo * self.interes
        self._saldo += ganancia
        print(f"interes aplicado y su nuevo saldo es {self._saldo}")


class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo = 0, limite_de_sobregiro: float = 500):
        super().__init__(titular, saldo)
        self.limite_de_sobregiro = limite_de_sobregiro

    def retirar(self, monto: float):
        if monto <= self._saldo + self.limite_de_sobregiro:
            self._saldo -= monto 
            print(f"Se retira del saldo {self._saldo} el monto de {monto}")
        else:
            print(f"no se puede retirar un monto mayor al saldo de la cuenta")


class Banco:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.cuentas = []

    def crear_cuentar(self, titular, tipo="ahorros") -> list:
        if tipo == "ahorro":
            cuenta = CuentaAhorro(titular)
        else:
            cuenta = CuentaCorriente(titular)
        self.cuentas.append(cuenta)
        print(f"cuenta brancaria {self.nombre}")
        return cuenta
    
    def mostrar_cuentas(self):
        if not self.cuentas:
            print("No tengo cuentas registradas")
        else:
            for i, cuenta in enumerate(self.cuentas, 1):
                print(f"{i}.{cuenta}")



banco = Banco(nombre="Banco ITM")
while True:
    print("\n--- MENU ---")
    print("1. crear una persona y una cuenta")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Aplicar interes a una cuenta de ahorros")
    print("5. Mostrar cuentas")
    print("6. Salir")
    while True:
        opcion = input("Elige una opción (1-6): ")
        if opcion.isdigit():  
            opcion = int(opcion)  
            if 1 <= opcion <= 6:
                print("Opción válida:", opcion) 
                break  
            else:
                print("El número debe estar entre 1 y 6.")
        else:
            print("Debes ingresar un número válido.")
    if opcion == 1:
        nombre = input("Ingrese el nombre de la persona ")
        documento = input("ingrese el documento de la persona ")
        persona = Persona(nombre=nombre,documento=documento)
        
        while True:
            print("\nQue tipo de cuenta quiere crear")
            tipo = input("Escriba ahorros o corriente ").lower().strip()
            if tipo in ["ahorros", "corriente"]:
                banco.crear_cuentar(persona,tipo)
                break
            else:
                print("Tipo de cuenta no válido. Intente nuevamente.")
    elif opcion == 2:
        if not banco.cuentas:
            print("No hay cuentas disponibles para depositar")
            continue
        for i, cuenta in enumerate(banco.cuentas, 1):
            print(f"{i}. {cuenta}")
        seleccion = input("Seleccione la cuenta para depositar: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(banco.cuentas):
            monto = float(input("Ingrese el monto a depositar: "))
            banco.cuentas[int(seleccion) - 1].depositar(monto)
        else:
            print("Seleccion invalida")
    elif opcion == 3:
        if not banco.cuentas:
            print("No hay cuentas disponibles para retirar")
            continue
        for i, cuenta in enumerate(banco.cuentas, 1):
            print(f"{i}. {cuenta}")
        seleccion = input("Seleccione la cuenta para retirar: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(banco.cuentas):
            monto = float(input("Ingrese el monto a retirar: "))
            banco.cuentas[int(seleccion) - 1].retirar(monto)
        else:
            print("Seleccion invalida")
    elif opcion == 4:
        if not banco.cuentas:
            print("No hay cuentas disponibles para aplicar interes")
            continue
        for i, cuenta in enumerate(banco.cuentas, 1):
            print(f"{i}. {cuenta}")
        seleccion = input("Seleccione la cuenta para aplicar interes: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(banco.cuentas):
            cuenta_selecionada = banco.cuentas[int(seleccion) - 1]
            if isinstance(cuenta_selecionada, CuentaAhorro):
                cuenta_selecionada.calcular_interes()
            else:
                print("Solo las cuentas de ahorros permiten aplicar interés.")
        else:
            print("Seleccion invalida")
    elif opcion == 5:
        banco.mostrar_cuentas()
    elif opcion == 6:
        print("Gracias por usar nuestra aplicacion")
        break
    else:
        print("Opcion no valida")