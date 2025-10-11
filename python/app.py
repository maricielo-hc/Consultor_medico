import tkinter as tk
from tkinter import messagebox
import sys
import os
from motor import MotorExperto
from datetime import datetime

import sys, os

def ruta_recurso(ruta_relativa):
    """Devuelve la ruta absoluta del recurso, compatible con PyInstaller"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath("."), ruta_relativa)


def resource_path(relative_path):
    """Obtiene la ruta absoluta para PyInstaller y desarrollo."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return os.path.join(base_path, relative_path)





# Lista de síntomas (tomados de tus reglas, con underscore)
SINTOMAS = [
    "fiebre", "tos", "dolor_cabeza", "dolor_muscular", "dificultad_respiratoria", "anosmia",
    "dolor_abdominal", "vomito", "dolor_hipocondrio_derecho", "rigidez_cuello",
    "dolor_pecho", "diarrea", "dolor_articulaciones", "erupcion_cutanea",
    "estornudos", "picazon_nasal", "congestion", "dolor_garganta", "inflamacion_amigdalas",
    "dolor_facial", "ardor_orinar", "dolor_lumbar", "ictericia", "fatiga", "nausea", "sensibilidad_luz"
]

class ConsultorMedicoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Consultor Médico — Versión Amigable 🩺🐻")
        self.root.geometry("520x640")
        self.root.configure(bg="#E8F7FF")

        # ----------- INICIALIZAR MOTOR -----------
        ruta_reglas = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "prolog", "reglas_enfermedades.pl")
        self.motor = MotorExperto(ruta_reglas)
        # -----------------------------------------

        # Frames (tres pantallas)
        self.frame1 = tk.Frame(root, bg="#E8F7FF")
        self.frame2 = tk.Frame(root, bg="#E8F7FF")
        self.frame3 = tk.Frame(root, bg="#E8F7FF")

        self._build_frame1()
        self._build_frame2()
        self._build_frame3()

        self.frame1.pack(fill="both", expand=True)
        # estado temporal
        self.selected_sintomas = []
        self.dias = 1


    # ---------------- Frame 1: Datos personales ----------------
    def _build_frame1(self):
        f = self.frame1
        tk.Label(f, text="¡Hola! 😊", font=("Segoe UI", 20, "bold"), bg="#E8F7FF").pack(pady=10)
        tk.Label(f, text="Vamos a registrar al paciente", font=("Segoe UI", 12), bg="#E8F7FF").pack(pady=5)

        tk.Label(f, text="Nombre:", bg="#E8F7FF").pack(pady=(20,5))
        self.entry_nombre = tk.Entry(f, font=("Segoe UI", 12))
        self.entry_nombre.pack()

        tk.Label(f, text="Apellido:", bg="#E8F7FF").pack(pady=(10,5))
        self.entry_apellido = tk.Entry(f, font=("Segoe UI", 12))
        self.entry_apellido.pack()

        tk.Label(f, text="Edad:", bg="#E8F7FF").pack(pady=(10,5))
        self.entry_edad = tk.Entry(f, font=("Segoe UI", 12), width=6)
        self.entry_edad.pack()

        tk.Button(f, text="👉 Continuar", bg="#6ECF9A", font=("Segoe UI", 12, "bold"),
                  command=self._to_frame2).pack(pady=25)

    # ---------------- Frame 2: Selección de síntomas ----------------
    def _build_frame2(self):
        f = self.frame2
        header = tk.Frame(f, bg="#E8F7FF")
        header.pack(fill="x")
        tk.Button(header, text="← Volver", bg="#FFB6C1", command=self._to_frame1).pack(side="left", padx=10, pady=10)
        tk.Label(header, text="Selecciona los síntomas", font=("Segoe UI", 14, "bold"), bg="#E8F7FF").pack(pady=10)

        # caja de checkboxes con scrollbar
        box = tk.Frame(f, bg="#E8F7FF")
        box.pack(fill="both", expand=True, padx=15)

        canvas = tk.Canvas(box, bg="#E8F7FF", highlightthickness=0)
        scrollbar = tk.Scrollbar(box, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#E8F7FF")

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0,0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.check_vars = {}
        for s in SINTOMAS:
            var = tk.IntVar()
            cb = tk.Checkbutton(scroll_frame, text=s.replace("_", " "), variable=var, bg="#E8F7FF", anchor="w")
            cb.pack(fill="x", padx=5, pady=2)
            self.check_vars[s] = var

        # duración
        tk.Label(f, text="Duración de los síntomas (días):", bg="#E8F7FF").pack(pady=(5,0))
        self.entry_dias = tk.Entry(f, width=6, font=("Segoe UI", 12))
        self.entry_dias.insert(0, "1")
        self.entry_dias.pack(pady=5)

        tk.Button(f, text="📋 Diagnosticar", bg="#4FC3F7", font=("Segoe UI", 12, "bold"),
                  command=self._on_diagnosticar).pack(pady=15)

    # ---------------- Frame 3: Resultado ----------------
    def _build_frame3(self):
        f = self.frame3
        header = tk.Frame(f, bg="#E8F7FF")
        header.pack(fill="x")
        tk.Label(header, text="Resultado", font=("Segoe UI", 16, "bold"), bg="#E8F7FF").pack(pady=10)

        self.result_text = tk.Label(f, text="", font=("Segoe UI", 12), bg="#E8F7FF", justify="left")
        self.result_text.pack(pady=10, padx=10)

        btns = tk.Frame(f, bg="#E8F7FF")
        btns.pack(pady=15)
        tk.Button(btns, text="💾 Guardar paciente", bg="#F7C46C", command=self._on_guardar).pack(side="left", padx=8)
        tk.Button(btns, text="🏠 Inicio", bg="#B3E5FC", command=self._to_frame1).pack(side="left", padx=8)
        # En el frame de botones, agrega:
        tk.Button(btns, text="📂 Abrir Carpeta Datos", 
                  command=self._abrir_carpeta_datos, 
                  bg="#A5D6A7").pack(side=tk.LEFT, padx=8)
    # ---------------- Navegación entre frames ----------------
    def _clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def _to_frame1(self):
        # limpiar inputs
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        # limpiar síntomas seleccionados
        for var in self.check_vars.values():
            var.set(0) 
        self.entry_dias.delete(0, tk.END)
        self.entry_dias.insert(0, "1")
        self.result_text.config(text="")
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame1.pack(fill="both", expand=True)

    def _to_frame2(self):
        nombre = self.entry_nombre.get().strip()
        apellido = self.entry_apellido.get().strip()
        edad = self.entry_edad.get().strip()

        if not nombre or not apellido or not edad:
            messagebox.showwarning("Faltan datos", "Por favor completa nombre, apellido y edad.")
            return
        try:
            int(edad)
        except ValueError:
            messagebox.showerror("Edad inválida", "La edad debe ser un número entero.")
            return

        self.frame1.pack_forget()
        self.frame3.pack_forget()
        self.frame2.pack(fill="both", expand=True)

    # ---------------- Acciones ----------------
    def _on_diagnosticar(self):
        nombre = self.entry_nombre.get().strip()
        apellido = self.entry_apellido.get().strip()
        edad = self.entry_edad.get().strip()
        dias = self.entry_dias.get().strip()
        try:
            dias = int(dias)
            if dias < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Duración inválida", "Ingresa un número válido de días.")
            return

        seleccion = [s for s, var in self.check_vars.items() if var.get() == 1]
        if not seleccion:
            messagebox.showwarning("Selecciona síntomas", "Por favor selecciona al menos un síntoma.")
            return

        # registrar en Prolog
        self.motor.agregar_sintomas(nombre, apellido, edad, seleccion, dias)

        # diagnosticar
        resultados = self.motor.diagnosticar(nombre, apellido, edad)
        if resultados:
            texto = "Parece que podría ser:\n" + "\n".join([f"• {r}" for r in resultados])
        else:
            texto = "No se encontró un diagnóstico exacto. Considera revisar los síntomas o consultar a un profesional."

        self.result_text.config(text=texto)
        self.selected_sintomas = seleccion
        self.dias = dias

        # mostrar pantalla de resultados
        self.frame2.pack_forget()
        self.frame3.pack(fill="both", expand=True)

    def _on_guardar(self):
        nombre = self.entry_nombre.get().strip()
        apellido = self.entry_apellido.get().strip()
        edad = self.entry_edad.get().strip()
        diagnosticos = []
        # extraer lista de diagnósticos desde result_text
        raw = self.result_text.cget("text")
        if "•" in raw:
            diagnosticos = [line.replace("• ", "").strip() for line in raw.splitlines() if line.strip().startswith("•")]
        else:
            if "No se encontró" not in raw:
                diagnosticos = [raw.strip()]

    def _abrir_carpeta_datos(self):
        """Abre la carpeta donde se guardan los datos"""
        import subprocess
        import os
        
        if getattr(sys, 'frozen', False):
            # Para .exe - misma lógica que motor.py
            data_dir = os.path.join(os.path.expanduser("~"), "ConsultorMedico_data")
        else:
            # Para desarrollo
            data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    
        if os.path.exists(data_dir):
            try:
                subprocess.Popen(f'explorer "{data_dir}"')
            except Exception as e:
                messagebox.showinfo(
                    "📂 Carpeta de Datos", 
                    f"Ubicación:\n{data_dir}\n\n"
                    f"Puedes copiar esta ruta en el Explorador de Windows"
                )
        else:
            messagebox.showinfo(
                "📂 Carpeta de Datos", 
                f"La carpeta se creará al guardar el primer paciente:\n{data_dir}"
            )


        # Guardar un archivo por paciente
        ruta_dir = os.path.join("data", "pacientes")
        os.makedirs(ruta_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_arch = f"{nombre}_{apellido}_{timestamp}.txt"
        ruta_archivo = os.path.join(ruta_dir, nombre_arch)

        with open(ruta_archivo, "w", encoding="utf-8") as f:
            f.write("👩‍⚕️ CONSULTA MÉDICA\n")
            f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Nombre: {nombre}\n")
            f.write(f"Apellido: {apellido}\n")
            f.write(f"Edad: {edad}\n")
            f.write("\nSíntomas:\n")
            for s in self.selected_sintomas:
                f.write(f" - {s.replace('_',' ')} (duración: {self.dias} días)\n")
            f.write("\nDiagnóstico:\n")
            if diagnosticos:
                for d in diagnosticos:
                    f.write(f" - {d}\n")
            else:
                f.write(" - No determinado\n")

        # También guardar en el registro general mediante el motor
        self.motor.guardar_paciente(nombre, apellido, edad, self.selected_sintomas, self.dias, diagnosticos)

        messagebox.showinfo("Paciente guardado", f"Datos guardados en:\n{ruta_archivo}")
        self._to_frame1()

if __name__ == "__main__":
    root = tk.Tk()
    app = ConsultorMedicoApp(root)
    root.mainloop()
