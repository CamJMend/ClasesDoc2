from model.Objects.cita import Cita

class Paciente:
    def __init__(self):
        self.citas = []

    def agendar_cita(self, fecha, hora, motivo):
        nueva_cita = Cita(
            id=len(self.citas) + 1,
            fecha=fecha,
            hora=hora,
            motivo=motivo,
            estado='Pendiente'
        )
        self.citas.append(nueva_cita)
        return nueva_cita

    def obtener_estado_cita(self, cita_id):
        for cita in self.citas:
            if cita.id == cita_id:
                return cita.estado
        return None