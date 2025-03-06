class Cita:
    def __init__(self, fecha, hora, motivo, estado, id_cita, id_medico, id_paciente):
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.estado = estado
        self.id_cita = id_cita
        self.id_medico = id_medico
        self.id_paciente = id_paciente

    def create_dictionary(self):
        return {
            "fecha": self.fecha,
            "hora": self.hora,
            "motivo": self.motivo,
            "estado": self.estado,
            "id_cita": self.id_cita,
            "id_medico": self.id_medico,
            "id_paciente": self.id_paciente
        }