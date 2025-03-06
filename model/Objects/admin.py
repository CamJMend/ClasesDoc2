from model.Objects.usuario import Usuario

class Admin(Usuario):
    def __init__(self, id, nombre, fecha_nacimiento):
        super().__init__(id, nombre, fecha_nacimiento, "admin")

    