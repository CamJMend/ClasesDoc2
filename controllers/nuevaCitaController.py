from model.Objects.cita import Cita
from dbConnection.FirebaseConnection import FirebaseConnection

class NuevaCitaController:
    def __init__():
        pass
    def addCita(self, fecha, hora, motivo, medico, paciente):
        nueva_cita = Cita(fecha, hora, motivo, "pendiente", medico, paciente)
        #self.cita_dao.nueva_cita(cita)
        pass