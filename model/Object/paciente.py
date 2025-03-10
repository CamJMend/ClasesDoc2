from model.Objects.usuario import Usuario

class Paciente(Usuario):
    def __init__(self, id, nombre, fecha_nacimiento):
        self.id = id
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    
 