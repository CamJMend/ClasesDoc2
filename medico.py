from usuario import usuario  

class doctor(usuario):
    def __init__(self, id, role, birth_date,name, age, especialidad,horario_de_trabajo):
        usuario.__init__(self, id, role, birth_date,name, age)
        self.especialidad = especialidad
        self.horario_de_trabajo = horario_de_trabajo
        self.citas=[]
    def actualizarCita(self,cita):
        for i in range(len(self.citas)):
            if self.citas[i].id == cita.id:
                self.citas[i] = cita
    def agendarCita(self,cita):
        self.citas.append(cita)
    def verCitas(self):
        return self.citas
    def cancelarCita(self,cita):
        self.citas.remove(cita)
    