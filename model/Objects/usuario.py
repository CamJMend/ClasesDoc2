class Usuario():
    def __init__(self, id, nombre, fecha_nacimiento, role):
        self.id = id
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.role = role
    
    #Getters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre
    
    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento
    
    def get_role(self):
        return self.role

    #Setters
    def set_id(self, _id):
        self.id = _id
    
    def set_nombre(self, _nombre):
        self.nombre = _nombre

    def set_fecha_nacimiento(self, _fecha_nacimiento):
        self.fecha_nacimiento = _fecha_nacimiento

    def set_role(self, _role):
        self.role = _role

    def create_dictionary(self):
        return {
                "id": self.id,
                "nombre": self.nombre,
                "fecha_nacimiento": self.fecha_nacimiento,
                "role": self.role,
            }
    