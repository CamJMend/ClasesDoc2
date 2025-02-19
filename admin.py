from usuario import usuario


class admin(usuario):
    def __init__(self, id, role, birth_date,name, age):
        usuario.__init__(self, id, role, birth_date,name, age)
    def actualizarCita(self,cita):
        for i in range(len(self.citas)):
            if self.citas[i].id == cita.id:
                self.citas[i] = cita
    def actualizarUsuario(self,usuario):
        for i in range(len(self.usuarios)):
            if self.usuarios[i].id == usuario.id:
                self.usuarios[i] = usuario
    def verHorariosDeTrabajo(self):
        pass