from model.Objects.usuario import Usuario

class Medico(Usuario):
    def __init__(self, id, nombre, fecha_nacimiento, especialidad, horario_trabajo):
        super().__init__(id, nombre, fecha_nacimiento, "medico")
        self.especialidad = especialidad
        self.horario_trabajo = horario_trabajo
    
    #Getters
    def get_especialidad(self):
        return especialidad
    
    def get_horario_trabajo(self):
        return horario_trabajo

    #Setters
    def set_especialidad(self, _especialidad):
        self.especialidad = _especialidad
    
    def set_horario_trabajo(self, _horario_trabajo):
        self.horario_trabajo = _horario_trabajo

    #Dictionary
    def create_dictionary(self):
        data = super().create_dictionary()
        data.update({
            "especialidad": self.especialidad,
            "horario_trabajo": self.horario_trabajo
        })
        return data
        
    