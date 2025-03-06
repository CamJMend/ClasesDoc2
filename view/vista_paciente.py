class VistaPaciente:
    def mostrar_menu(self):
        print("1. Agendar Cita")
        print("2. Ver Estado de Cita")
        opcion = input("Seleccione una opción: ")
        return opcion

    def agendar_cita(self):
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        hora = input("Ingrese la hora (HH:MM): ")
        motivo = input("Ingrese el motivo de la cita: ")
        return {'fecha': fecha, 'hora': hora, 'motivo': motivo}

    def ver_estado_cita(self, cita):
        print(f"Estado de la cita: {cita['estado']}")