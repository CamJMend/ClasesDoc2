class VistaMedico:
    def mostrar_menu(self):
        print("1. Revisar Citas")
        print("2. Aceptar Citas")
        print("3. Gestionar Citas")
        print("4. Actualizar Estado de Consulta")
        opcion = input("Seleccione una opción: ")
        return opcion

    def revisar_citas(self, citas):
        for cita in citas:
            print(f"Fecha: {cita['fecha']}, Hora: {cita['hora']}, Motivo: {cita['motivo']}, Estado: {cita['estado']}")

    def actualizar_estado_consulta(self, consulta):
        print(f"Consulta actualizada: {consulta['fecha']} - {consulta['estado']}")