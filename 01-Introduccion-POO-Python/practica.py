class Persona:
    def __init__(self, nombre:str, documento:str):
        self.nombre = nombre
        self.documento = documento
        
        def __str__(self)-> str:
            return f"{self.nombre}, se creo esta persona con el documento{self.documento}"

class CuentaBancaria: #En las clases se pone la primera de cada palabra en mayuscula
    def __init__(self, titular: Persona, saldo=0):
        self.titular = titular
        self._saldo = saldo

    def saldo(self)->int:
        return self._saldo
    
    def depositar(self, monto: float):
        if monto > 0:
            self._saldo += monto
            print(f"Se depositó un monto de {monto} y mi saldo actual es de {self._saldo}.")
        else:
            print("El monto a depositar debe ser mayor que cero.")
        
        def retirar(self,monto:float)->None: #Minuscula para los metodos
            if monto <= self._saldo:
                self._saldo -= monto
                print(f"Se retiró un monto de {monto} y mi saldo actual es de {self._saldo}.")
            else:
                print("No se puede retirar el monto es mayor al saldo disponible.")

class CuentaAhorro(CuentaBancaria): #A la clase hija le paso la clase padre
    def __init__(self, titular: str, saldo:float=0, interes: float=0.01):
        super().__init__(titular, saldo)
        self.interes = interes
        
    def calcular_interes(self):
        ganancia = self._saldo * self.interes
        self._saldo += ganancia
        print(f"Interes aplicado. Saldo actual: {self._saldo}.")

class CuentaCorriente(CuentaBancaria): #A la clase hija le paso la clase padre
    def __init__(self, titular: str, saldo:float=0, limite_de_sobre_giro: float=0.01):
        super().__init__(titular, saldo)
        self.limite_de_sobre_giro = limite_de_sobre_giro
        
    def retirar_cuenta_corriente(self, monto: float):
        if monto <= self._saldo + self.limite_de_sobre_giro:
            self._saldo -= monto
            print(f"Se retiró un monto de {monto} y mi saldo actual es de {self._saldo}.")
        else:
            print(f"El monto a retirar excede el límite de sobregiro.")

class Banco:
    def __init__(self, nombre: str)->list:
        self.nombre = nombre
        self.cuentas = []

    def crear_cuenta(self, titular, cuenta: CuentaBancaria, tipo = "ahorros"):
        if tipo == "ahorros":
            cuenta = CuentaAhorro(titular)
        else:
            cuenta = CuentaCorriente(titular)
        self.cuentas.append(cuenta)
        print(f"Cuenta creada para {titular.nombre} con saldo inicial de {cuenta.saldo()}.")
        return cuenta

    def mostrar_cuentas(self):
        if not self.cuentas:
            print("No hay cuentas registradas.")
        else:
            for i,cuenta in enumerate(self.cuentas, 1):
                print(f"{i}.{cuenta}")

while True: 
    print("Bienvenido al sistema bancario") 
    print("1. Crear cuenta")
    print("2. Mostrar cuentas")