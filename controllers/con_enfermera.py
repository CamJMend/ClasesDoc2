from model.Objects.enfermera import Enfermera

class ControllerEnfermera:
    def __init__(self):
        self.modelo = Enfermera()

    def agregar_cita(self, fecha, hora, motivo):
        nueva_cita = {
            'id': len(self.modelo.citas) + 1,
            'fecha': fecha,
            'hora': hora,
            'motivo': motivo,
            'estado': 'Pendiente'
        }
        return self.modelo.agregar_cita(nueva_cita)

    def actualizar_estado_cita(self, cita_id, estado):
        return self.modelo.actualizar_estado_cita(cita_id, estado)

    def obtener_citas(self):
        return self.modelo.citas