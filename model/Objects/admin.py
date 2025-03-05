from model.usuario import Usuario

class Admin(Usuario):
    def __init__(self, id, nombre, fecha_nacimiento):
        super().__init__(id, nombre, fecha_nacimiento, "admin")
    
    #def actualizar_cita(self, idc):
    #def actualizar_usuario(self, idc):
    #def ver_horarios_trabajo(self, id):