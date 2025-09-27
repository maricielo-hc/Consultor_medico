from pyswip import Prolog
import os

class MotorExperto:
    def __init__(self):
        self.prolog = Prolog()
        # Construir ruta absoluta a base_conocimiento.pl
        ruta = os.path.join(os.path.dirname(__file__), "..", "prolog", "base_conocimiento.pl")
        self.prolog.consult(os.path.abspath(ruta))

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
