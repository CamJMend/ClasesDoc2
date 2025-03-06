from model.Objects.medico import Medico

class ControllerMedico:
    def __init__(self):
        self.modelo = Medico()

    def agregar_cita(self, fecha, hora, motivo):
        nueva_cita = {
            'id': len(self.modelo.citas) + 1,
            'fecha': fecha,
            'hora': hora,
            'motivo': motivo,
            'estado': 'Pendiente'
        }
        return self.modelo.agregar_cita(nueva_cita)

    def obtener_citas(self):
        return self.modelo.obtener_citas()

    def aceptar_cita(self, cita_id):
        return self.modelo.aceptar_cita(cita_id)