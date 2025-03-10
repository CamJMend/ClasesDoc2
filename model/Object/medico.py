from model.Objects.usuario import Usuario

class Medico(Usuario):
    def __init__(self, id, nombre, fecha_nacimiento, especialidad, horario_trabajo):
        super().__init__(id, nombre, fecha_nacimiento, "medico")
        self.especialidad = especialidad
        self.horario_trabajo = horario_trabajo
    
    #def actualizar_consulta(self, idc):
    #def aceptar_cita(self):
    #def ver_citas_agendadas(self, idc):
    #def cancelar_cita(self, idc):
    