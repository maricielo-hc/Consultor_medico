from pyswip import Prolog
import os, sys

class MotorExperto:
    def __init__(self):
        self.prolog = Prolog()

        # Detectar si corre como .exe (PyInstaller) o normal
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS  # Carpeta temporal donde PyInstaller descomprime
        else:
            base_path = os.path.dirname(__file__)  # Carpeta del script Python

        ruta = os.path.join(base_path, "prolog", "base_conocimiento.pl")
        self.prolog.consult(ruta)

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
