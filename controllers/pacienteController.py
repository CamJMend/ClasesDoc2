from model.DAO.citaDAO import AddCitaDAO

class PacienteController:
    def __init__(self):
        self.cita_dao = AddCitaDAO()

    def agendar_cita(self, fecha, hora, motivo, id_paciente):
        return self.cita_dao.agregar_cita(fecha, hora, motivo, id_paciente)

    def ver_estado_cita(self, cita_id):
        return self.cita_dao.obtener_cita_por_id(cita_id)