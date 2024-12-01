from reglas import SistemaTransporte

def main():
    # Crear el motor de conocimiento
    motor = SistemaTransporte()

    # Inicializar el motor
    motor.reset()

    # Declarar las rutas del sistema de transporte
    motor.declare_route("A", "B", 5)
    motor.declare_route("A", "C", 10)
    motor.declare_route("B", "D", 15)
    motor.declare_route("C", "D", 5)
    motor.declare_route("D", "E", 10)
    motor.declare_route("C", "E", 20)

    # Ejecutar el motor y buscar la mejor ruta
    motor.encontrar_mejor_ruta("A", "E")

if __name__ == "__main__":
    main()
