from model.Objects.paciente import Paciente

class ControllerPaciente:
    def __init__(self):
        self.modelo = Paciente()

    def agendar_cita(self, fecha, hora, motivo):
        return self.modelo.agendar_cita(fecha, hora, motivo)

    def obtener_estado_cita(self, cita_id):
        return self.modelo.obtener_estado_cita(cita_id)