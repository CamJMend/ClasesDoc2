from model.DAO.citaDAO import AddCitaDAO

class MedicoController:
    def __init__(self):
        self.cita_dao = AddCitaDAO()

    def revisar_citas(self, medico_id):
        return self.cita_dao.obtener_citas_por_medico(medico_id)

    # def aceptar_cita(self, cita_id):
    #     return self.cita_dao.actualizar_estado(cita_id, "Aceptada")