from model.usuario import Usuario

class Enfermera(Usuario):
    def __init__(self, id, nombre, fecha_nacimiento, horario_trabajo):
        super().__init__(id, nombre, fecha_nacimiento, "enfermera")
        self.horario_trabajo = horario_trabajo
    
    #def actualizar_cita(self):
    #def registrar_signos_vitales(self, id):
    #def actualizar_consulta(self, idc):