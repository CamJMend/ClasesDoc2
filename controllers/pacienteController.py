from model.Objects.cita import Cita
from model.Objects.paciente import Paciente
from model.DAO.pacienteDAO import PacienteDAO

class PacienteController:
    def __init__(self):
        self.paciente_dao = PacienteDAO()

    def agendar_cita(self, fecha, hora, motivo, medico, paciente):
        nueva_cita = Cita(fecha, hora, motivo, "pendiente", f"cita_{fecha}_{hora}", medico, paciente)
        self.paciente_dao.agendar_cita(nueva_cita)

    def cancelar_cita(self, cita_id):
        self.paciente_dao.cancelar_cita(cita_id)
    
    def add_paciente(self, paciente: Paciente):
        self.paciente_dao.add_paciente(paciente)
