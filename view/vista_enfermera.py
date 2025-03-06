class VistaEnfermera:
    def mostrar_menu(self):
        print("1. Actualizar Estado de Cita")
        print("2. Registrar Signos Vitales")
        print("3. Asistir Médico")
        opcion = input("Seleccione una opción: ")
        return opcion

    def actualizar_estado_cita(self, cita):
        print(f"Cita actualizada: {cita['fecha']} - {cita['estado']}")