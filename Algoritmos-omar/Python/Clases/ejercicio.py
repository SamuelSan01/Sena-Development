class Productos:
    def __init__(self, fechaCaducidad, numeroLote):
        self.fechaCaducidad = fechaCaducidad
        self.numeroLote = numeroLote
        print("la clase Productos se ha disparado")

    def fechaCaducidad(self) -> str:
        return self.fechaCaducidad
    
    def numeroLote(self) -> int:
        return self.numeroLote
    

class ProductosCongelados(Productos):
    def __init__(self, fechaCaducidad, numeroLote, temperaturaCongelacion):
      super().__init__(fechaCaducidad, numeroLote)
      self.temperaturaCongelacion = temperaturaCongelacion
      print("la clase Productos congelados se ha disparado")

      def temperaturaCongelacion(self) -> int:
       return self.temperaturaCongelacion
      

class CongeladosPorAire(ProductosCongelados):
    def __init__(self, fechaCaducidad, numeroLote, temperaturaCongelacion, ):
       super().__init__(fechaCaducidad, numeroLote, temperaturaCongelacion)
       self.temperaturaCongelacion = temperaturaCongelacion
       print("la subclase Congelados por aire se ha disparado")


class CongeladosPorAgua(ProductosCongelados):
    def __init__(self, fechaCaducidad, numeroLote, temperaturaCongelacion):
       super().__init__(fechaCaducidad, numeroLote, temperaturaCongelacion)
       self.temperaturaCongelacion = temperaturaCongelacion
       print("la subclase Congelados por agua se ha disparado")


class CongeladosPorNitrogeno(ProductosCongelados):
    def __init__(self, fechaCaducidad, numeroLote, temperaturaCongelacion):
       super().__init__(fechaCaducidad, numeroLote, temperaturaCongelacion)
       self.temperaturaCongelacion = temperaturaCongelacion
       print("la subclase Congelados por nitrogeno se ha disparado")


class ProductosFrescos(Productos):
    def __init__(self,fechaCaducidad, numeroLote,):
      super().__init__(fechaCaducidad, numeroLote)
      print("la clase Productos frescos se ha disparado")


class ProductosRefrigerados(Productos):
    def __init__(self,fechaCaducidad, numeroLote,):
      super().__init__(fechaCaducidad, numeroLote)
      print("la clase Productos refrigerados se ha disparado")


miProducto = CongeladosPorAgua('11-01-2006',273872,10)
print(miProducto.fechaCaducidad.numeroLote)