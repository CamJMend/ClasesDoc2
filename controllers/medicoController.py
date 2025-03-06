from model.DAO.medicoDAO import MedicoDAO

class MedicoController:
    def __init__(self):
        self.medico_dao = MedicoDAO()

    def aceptar_cita(self, cita_id):
        self.medico_dao.aceptar_cita(cita_id)

    def ver_citas_agendadas(self, medico_id):
        return self.medico_dao.ver_citas_agendadas(medico_id)

    def cancelar_cita(self, cita_id):
        self.medico_dao.cancelar_cita(cita_id)
