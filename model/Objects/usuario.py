class Usuario:
    def __init__(self, id, nombre, rol, contrasena):
        self.id = id
        self.nombre = nombre
        self.rol = rol
        self.contrasena = contrasena  # Store hashed password in a real application

    def login(self, contrasena):
        # Check if the password matches
        if self.contraseña == contrasena:
            print(f"Usuario {self.nombre} ha iniciado sesión.")
            return True
        return False

    def logout(self):
        print(f"Usuario {self.nombre} ha cerrado sesión.")
        return True