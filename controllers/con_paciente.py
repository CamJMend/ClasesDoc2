from modelo.paciente import Paciente

class ControladorPaciente:
    def __init__(self, paciente):
        self.paciente = paciente

    def agendar_cita(self, fecha_hora, motivo, medico_id):
        return self.paciente.agendar_cita(fecha_hora, motivo, medico_id)

    def cancelar_cita(self, idc):
        return self.paciente.cancelar_cita(idc)
