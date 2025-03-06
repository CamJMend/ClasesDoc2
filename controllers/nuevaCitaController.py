from model.DAO.citaDAO import AddCitaDAO
from model.Objects.cita import Cita

class NuevaCitaController:
    def __init__(self):
        self.dao = AddCitaDAO()

    def crear_cita(self, fecha, hora, motivo, estado, id_cita, id_medico, id_paciente):
        nueva_cita = Cita(fecha, hora, motivo, estado, id_cita, id_medico, id_paciente)
        self.dao.add_cita(nueva_cita)