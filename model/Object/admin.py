from model.Objects.usuario import Usuario
from abc import ABC, abstractmethod

class Admin(Usuario):
    def __init__(self, id, nombre, fecha_nacimiento):
        super().__init__(id, nombre, fecha_nacimiento, "admin")
    
    
    
    @abstractmethod
    def actualizar_cita(self, idc):
        pass
    @abstractmethod
    def actualizar_usuario(self, idc):
        pass
    @abstractmethod
    def ver_horarios_trabajo(self, id):
        pass