from pyswip import Prolog
import os
import sys
from datetime import datetime

class MotorExperto:
    def __init__(self, ruta_reglas=None):
        self.prolog = Prolog()

        # === CONFIGURAR RUTAS PARA TU ESTRUCTURA ===
        if getattr(sys, 'frozen', False):
            # Modo ejecutable
            base_path = sys._MEIPASS
            swi_path = os.path.join(base_path, "swi-prolog", "swipl.exe")
        else:
            # Modo desarrollo  
            base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            swi_path = os.path.join(base_path, "swi-prolog", "swipl.exe")

        # CONFIGURAR pyswip para usar TU SWI-Prolog
        if os.path.exists(swi_path):
            os.environ['SWI_PROLOG_BINARY'] = swi_path
            print(f"✅ SWI-Prolog configurado: {swi_path}")
        else:
            print(f"⚠️  SWI-Prolog no encontrado en: {swi_path}")

        # === CARGAR REGLAS PROLOG ===
        if ruta_reglas is None:
            ruta_reglas = os.path.join(base_path, "prolog", "reglas_enfermedades.pl")

        if os.path.exists(ruta_reglas):
            self.prolog.consult(ruta_reglas)
            print("✅ Reglas de enfermedades cargadas")
        else:
            raise FileNotFoundError(f"No se encontraron reglas en: {ruta_reglas}")

        # === CONFIGURAR CARPETA DE DATOS ===
        if getattr(sys, 'frozen', False):
            data_dir = os.path.join(os.path.expanduser("~"), "ConsultorMedico_data")
        else:
            data_dir = os.path.join(base_path, "data")

        os.makedirs(data_dir, exist_ok=True)
        self.data_path = os.path.join(data_dir, "casos.txt")
        print(f"📁 Datos guardados en: {self.data_path}")

    def _sanitize_user(self, nombre, apellido, edad):
        """Crea identificador para Prolog"""
        nombre_atom = (nombre.strip() + "_" + apellido.strip() + "_" + str(edad)).lower().replace(" ", "_")
        return f"'{nombre_atom}'", nombre_atom

    def agregar_sintomas(self, nombre, apellido, edad, sintomas, dias):
        """Registra síntomas en Prolog"""
        user_quoted, _ = self._sanitize_user(nombre, apellido, edad)
        for s in sintomas:
            query = f"assertz(registro_sintoma({user_quoted}, {s}, {int(dias)}))."
            list(self.prolog.query(query))
        print(f"✅ {len(sintomas)} síntomas registrados para {nombre}")

    def diagnosticar(self, nombre, apellido, edad):
        """Realiza diagnóstico"""
        user_quoted, _ = self._sanitize_user(nombre, apellido, edad)
        consulta = f"posible_enfermedad({user_quoted}, E)."
        resultados = list(self.prolog.query(consulta))
        
        if resultados:
            enfermedades = [str(r['E']) for r in resultados]
            print(f"🎯 Diagnóstico: {enfermedades}")
            return enfermedades
        else:
            print("🔍 No se encontró diagnóstico")
            return []

    def guardar_paciente(self, nombre, apellido, edad, sintomas, dias, diagnosticos):
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
    
    # === NUEVO: MOSTRAR UBICACIÓN CLARA PARA USUARIOS ===
        if getattr(sys, 'frozen', False):
            # Para usuarios con .exe
            import tkinter.messagebox as msg
            import subprocess
        
            # Mensaje MEJORADO
            msg.showinfo(
                "💾 Datos Guardados", 
                f"✅ Información del paciente guardada exitosamente\n\n"
                f"📂 Ubicación:\n"
                f"{self.data_path}\n\n"
                f"🔍 Para ver los datos:\n"
                f"1. Abre el Explorador de Windows\n"
                f"2. Ve a: C:\\Users\\[TuUsuario]\\\n"  
                f"3. Busca la carpeta 'ConsultorMedico_data'"
            )
        
            # Intentar abrir la carpeta automáticamente
            try:
                carpeta = os.path.dirname(self.data_path)
                subprocess.Popen(f'explorer "{carpeta}"')
            except:
                pass  # Si falla, no hay problema
    
        print(f"💾 Paciente guardado: {self.data_path}")
        return self.data_path