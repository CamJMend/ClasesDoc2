class VistaAdmin:
    def mostrar_menu(self):
        print("1. Gestionar Citas")
        print("2. Gestionar Horarios")
        print("3. Asignar Citas")
        print("4. Visualizar Citas")
        opcion = input("Seleccione una opción: ")
        return opcion

    def gestionar_citas(self, citas):
        for cita in citas:
            print(f"Fecha: {cita['fecha']}, Hora: {cita['hora']}, Motivo: {cita['motivo']}, Estado: {cita['estado']}")