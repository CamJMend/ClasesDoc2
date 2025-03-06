from model.DAO.citaDAO import AddCitaDAO

class AdminController:
    def __init__(self):
        self.cita_dao = AddCitaDAO()

    def gestionar_citas(self):
        return self.cita_dao.obtener_todas_citas()

    def asignar_cita(self, cita_id, medico_id):
        return self.cita_dao.asignar_medico(cita_id, medico_id)