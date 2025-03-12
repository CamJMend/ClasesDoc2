from model.Objects.enfermera import Enfermera
from model.DAO.enfermeraDAO import EnfermeraDAO

class EnfermeraController:
    def __init__(self):
        self.enfermera_dao = EnfermeraDAO()

    def actualizar_cita(self, cita_id, nuevos_datos):
        self.enfermera_dao.actualizar_cita(cita_id, nuevos_datos)

    def registrar_signos_vitales(self, paciente_id, signos):
        self.enfermera_dao.registrar_signos_vitales(paciente_id, signos)

    def actualizar_consulta(self, cita_id, nuevos_datos):
        self.enfermera_dao.actualizar_consulta(cita_id, nuevos_datos)
    
    def add_enfermera(self, enfermera: Enfermera):
        self.enfermera_dao.add_enfermera(enfermera)