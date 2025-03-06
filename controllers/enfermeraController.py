from model.DAO.citaDAO import AddCitaDAO
from model.DAO.signosVitalesDAO import SignosVitalesDAO

class EnfermeraController:
    def __init__(self):
        self.cita_dao = AddCitaDAO()
        self.signos_dao = SignosVitalesDAO()
    
    def registrar_signos(self, paciente_id, signos):
        return self.signos_dao.agregar_signos(paciente_id, signos)

    def actualizar_estado_cita(self, cita_id, estado):
        return self.cita_dao.actualizar_estado(cita_id, estado)