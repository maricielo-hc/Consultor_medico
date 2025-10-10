from pyswip import Prolog
import os
import sys
from datetime import datetime

class MotorExperto:
    def __init__(self):
        self.prolog = Prolog()

        # base_path: carpeta donde está este motor.py
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))

        # Solo cargamos el archivo esencial: reglas_enfermedades.pl
        ruta_reglas = os.path.join(base_path,"..", "prolog", "reglas_enfermedades.pl")

        if os.path.exists(ruta_reglas):
            self.prolog.consult(ruta_reglas)
        else:
            raise FileNotFoundError(f"No se encontró {ruta_reglas} — por favor coloca tu reglas_enfermedades.pl en prolog/")

        # Archivo general para guardar todos los casos
        self.data_path = os.path.join(base_path, "data", "casos.txt")
        os.makedirs(os.path.dirname(self.data_path), exist_ok=True)

    def _sanitize_user(self, nombre, apellido, edad):
        """Crea un identificador de usuario adecuado para Prolog (atom entre comillas)."""
        nombre_atom = (nombre.strip() + "_" + apellido.strip() + "_" + str(edad)).lower().replace(" ", "_")
        return f"'{nombre_atom}'", nombre_atom

    def agregar_sintomas(self, nombre, apellido, edad, sintomas, dias):
        """Registra en Prolog los hechos registro_sintoma(User, sintoma, dias)."""
        user_quoted, _ = self._sanitize_user(nombre, apellido, edad)
        for s in sintomas:
            query = f"assertz(registro_sintoma({user_quoted}, {s}, {int(dias)}))."
            list(self.prolog.query(query))

    def diagnosticar(self, nombre, apellido, edad):
        """Consulta posible_enfermedad(User, E)."""
        user_quoted, _ = self._sanitize_user(nombre, apellido, edad)
        consulta = f"posible_enfermedad({user_quoted}, E)."
        resultados = list(self.prolog.query(consulta))
        if resultados:
            return [str(r['E']) for r in resultados]
        return []

    def guardar_paciente(self, nombre, apellido, edad, sintomas, dias, diagnosticos):
        """Guarda en data/casos.txt el registro legible del paciente."""
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.data_path, "a", encoding="utf-8") as f:
            f.write("=== NUEVO PACIENTE ===\n")
            f.write(f"Fecha: {fecha}\n")
            f.write(f"Nombre: {nombre}\n")
            f.write(f"Apellido: {apellido}\n")
            f.write(f"Edad: {edad}\n")
            f.write("Síntomas:\n")
            for s in sintomas:
                f.write(f"  - {s.replace('_', ' ')} (duración: {dias} días)\n")
            f.write("Diagnóstico:\n")
            if diagnosticos:
                for d in diagnosticos:
                    f.write(f"  - {d}\n")
            else:
                f.write("  - No determinado\n")
            f.write("=========================\n\n")
        return self.data_path
