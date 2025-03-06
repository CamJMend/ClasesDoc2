from model.Objects.usuario import Usuario

class Paciente(Usuario):
    def __init__(self, id, nombre, fecha_nacimiento, signos_vitales, fecha_ingreso, fecha_egreso):
        super().__init__(id, nombre, fecha_nacimiento, "paciente")
        self.signos_vitales = signos_vitales
        self.fecha_ingreso = fecha_ingreso
        self.fecha_egreso = fecha_egreso
    
    #Getters
    def get_signos_vitales(self):
        return self.signos_vitales
    
    def get_fecha_ingreso(self):
        return self.fecha_ingreso

    def get_fecha_egreso(self):
        return self.fecha_egreso

    #Setters
    def set_signos_vitales(self, _signos_vitales):
        self.signos_vitales = _signos_vitales
    
    def set_fecha_ingreso(self, _fecha_ingreso):
        self.fecha_ingreso = _fecha_ingreso

    def set_fecha_egreso(self, _fecha_egreso):
        self.fecha_egreso = _fecha_egreso

    #Dictionary
    def create_dictionary(self):
        data = super().create_dictionary()
        data.update({
            "signos_vitales": self.signos_vitales,
            "fecha_ingreso": self.fecha_ingreso,
            "fecha_egreso": self.fecha_egreso
        })
        return data
    


    
 