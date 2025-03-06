from model.usuario import Usuario

class Enfermera(Usuario):
    def __init__(self, id, nombre, fecha_nacimiento, horario_trabajo):
        super().__init__(id, nombre, fecha_nacimiento, "enfermera")
        self.horario_trabajo = horario_trabajo

        #Getters
        def get_horario_trabajo(self):
            return horario_trabajo

        #Setters
        def set_horario_trabajo(self, _horario_trabajo)
            self.horario_trabajo = _horario_trabajo

        #Dictionary        
        def create_dictionary(self):
            data = super().create_dictionary()
            data.update({
                "horario_trabajo": self.horario_trabajo
            })
            return data
