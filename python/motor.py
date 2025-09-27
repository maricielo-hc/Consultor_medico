from pyswip import Prolog

class MotorExperto:
    def __init__(self):
        self.prolog = Prolog()
        # Cargar base de conocimiento
        self.prolog.consult("../prolog/base_conocimiento.pl")

    def agregar_sintoma(self, sintoma):
        """Agrega un síntoma a Prolog"""
        query = f"assert({sintoma})."
        list(self.prolog.query(query))

    def diagnosticar(self):
        """Obtiene diagnóstico desde Prolog"""
        resultados = list(self.prolog.query("enfermedad(E)."))
        if resultados:
            return [r["E"] for r in resultados]
        return []
