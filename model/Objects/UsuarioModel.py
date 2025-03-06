class UsuarioModel:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_usuario_por_id(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                return usuario
        return None

    def autenticar_usuario(self, nombre, contrasena):
        for usuario in self.usuarios:
            if usuario.nombre == nombre and usuario.login(contrasena):
                return usuario
        return None