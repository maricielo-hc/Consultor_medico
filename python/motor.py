from pyswip import Prolog
import os
import sys
from datetime import datetime

class MotorExperto:
    def __init__(self):
        self.prolog = Prolog()

        # Detectar si corre como .exe (PyInstaller) o normal
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS  # Carpeta temporal donde PyInstaller descomprime
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))  # Carpeta actual del script

        # Ruta del archivo base de conocimiento en Prolog
        ruta = os.path.join(base_path, "..", "prolog", "base_conocimiento.pl")
        self.prolog.consult(ruta)

        # Ruta para guardar datos de pacientes
        self.data_path = os.path.join(base_path, "..", "data", "casos.txt")
        if not os.path.exists(os.path.dirname(self.data_path)):
            os.makedirs(os.path.dirname(self.data_path))

    def agregar_sintoma(self, sintoma):
        """Agrega un síntoma dinámicamente en Prolog."""
        query = f"assert({sintoma})."
        list(self.prolog.query(query))

    def diagnosticar(self):
        """Ejecuta el diagnóstico consultando Prolog."""
        resultados = list(self.prolog.query("enfermedad(E)."))
        if resultados:
            return [r["E"] for r in resultados]
        return []

    def guardar_paciente(self, nombre, sintomas, diagnostico):
        """Guarda los datos del paciente en un archivo .txt"""
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.data_path, "a", encoding="utf-8") as f:
            f.write("=== NUEVO PACIENTE ===\n")
            f.write(f"Fecha: {fecha}\n")
            f.write(f"Nombre: {nombre}\n")
            f.write(f"Síntomas: {', '.join(sintomas)}\n")
            f.write(f"Diagnóstico: {', '.join(diagnostico) if diagnostico else 'No determinado'}\n")
            f.write("=========================\n\n")

        print(f"✅ Datos de {nombre} guardados correctamente en {self.data_path}")
