class Vehiculo:
    def __init__(self, matricula, modelo, potenciaCV):
        self.matricula = matricula
        self.modelo = modelo
        self.potencia = potenciaCV
        print("metodo constructor vehiculo disparado")

    def getMatricula(self) -> str:
        return self.matricula
    
    def getModelo(self) -> str:
        return self.modelo
    
    def getPotenciaCV(self) -> int:
        return self.potenciaCV


class Taxi(Vehiculo):
    def __init__(self, numeroLicencia):
        self.numeroLicencia = numeroLicencia
        print("el metodo de la subclase taxi se ha disparado")

    def setNumeroLicencia(self):
       pass 

    def getNumeroLicencia(self) -> int:
        return self.numeroLicencia


class Autobus(Vehiculo):
    def __init__(self, numeroPlazas):
        self.numeroPlazas = numeroPlazas
        print("el metodo de la subclase autobus se ha disparado")

    def setNumeroPlazas(self):
        pass

    def getNumeroPlazas(self) -> int:
        return self.numeroPlazas
    

miTaxi = Taxi(12345)
print("licencia del taxi: ", miTaxi.getNumeroLicencia())

miBus = Autobus(3)
print("el numero de plazas de mi autobus es: ", miBus.getNumeroPlazas())