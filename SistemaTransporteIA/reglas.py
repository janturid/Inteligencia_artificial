from experta import *

class Ruta(Fact):
    """Representa una conexión entre dos estaciones"""
    origen = Field(str, mandatory=True)
    destino = Field(str, mandatory=True)
    costo = Field(int, mandatory=True)

class MejorRuta(Fact):
    """Guarda la mejor ruta encontrada"""
    origen = Field(str, mandatory=True)
    destino = Field(str, mandatory=True)
    costo_total = Field(int, mandatory=True)
    ruta = Field(list, mandatory=True)

class SistemaTransporte(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.rutas = []
        self.costo_minimo = float('inf')
        self.mejor_ruta = []

    def declare_route(self, origen, destino, costo):
        """Declarar una ruta en el sistema"""
        self.declare(Ruta(origen=origen, destino=destino, costo=costo))

    def encontrar_mejor_ruta(self, inicio, objetivo):
        """Encuentra la mejor ruta desde inicio a objetivo"""
        def buscar_ruta(actual, objetivo, costo_actual, ruta_actual):
            if actual == objetivo:
                if costo_actual < self.costo_minimo:
                    self.costo_minimo = costo_actual
                    self.mejor_ruta = ruta_actual
                return
            
            for origen, destino, costo in self.rutas:
                if origen == actual and destino not in ruta_actual:
                    buscar_ruta(destino, objetivo, costo_actual + costo, ruta_actual + [destino])

        # Registrar todas las rutas declaradas
        for hecho in self.facts.values():
            if isinstance(hecho, Ruta):
                self.rutas.append((hecho["origen"], hecho["destino"], hecho["costo"]))

        # Ejecutar la búsqueda
        buscar_ruta(inicio, objetivo, 0, [inicio])

        # Mostrar resultados
        if self.mejor_ruta:
            print(f"Mejor ruta: {' -> '.join(self.mejor_ruta)}")
            print(f"Costo total: {self.costo_minimo}")
        else:
            print("No se encontró una ruta.")
