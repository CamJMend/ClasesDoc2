class Cita:
    def __init__(self, id, fecha, hora, motivo, estado='Pendiente'):
        self.id = id
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.estado = estado

    def __repr__(self):
        return f"Cita(id={self.id}, fecha={self.fecha}, hora={self.hora}, motivo={self.motivo}, estado={self.estado})"