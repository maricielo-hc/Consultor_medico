import tkinter as tk
from motor import MotorExperto

# Inicializar motor experto
motor = MotorExperto()

def diagnosticar():
    # Reiniciar síntomas para nueva consulta
    motor = MotorExperto()

    if fiebre_var.get():
        motor.agregar_sintoma("fiebre")
    if tos_var.get():
        motor.agregar_sintoma("tos")
    if difres_var.get():
        motor.agregar_sintoma("dificultad_respiratoria")
    if dolor_muscular_var.get():
        motor.agregar_sintoma("dolor_muscular")
    if anosmia_var.get():
        motor.agregar_sintoma("anosmia")

    resultados = motor.diagnosticar()
    if resultados:
        salida.set(f"Posible diagnóstico: {', '.join(resultados)}")
    else:
        salida.set("No se encontró diagnóstico.")

# GUI
root = tk.Tk()
root.title("Sistema Experto de Síntomas")

tk.Label(root, text="Seleccione síntomas:").pack()

fiebre_var = tk.BooleanVar()
tk.Checkbutton(root, text="Fiebre", variable=fiebre_var).pack()

tos_var = tk.BooleanVar()
tk.Checkbutton(root, text="Tos", variable=tos_var).pack()

difres_var = tk.BooleanVar()
tk.Checkbutton(root, text="Dificultad Respiratoria", variable=difres_var).pack()

dolor_muscular_var = tk.BooleanVar()
tk.Checkbutton(root, text="Dolor Muscular", variable=dolor_muscular_var).pack()

anosmia_var = tk.BooleanVar()
tk.Checkbutton(root, text="Anosmia", variable=anosmia_var).pack()

tk.Button(root, text="Diagnosticar", command=diagnosticar).pack()

salida = tk.StringVar()
tk.Label(root, textvariable=salida, fg="blue").pack()

root.mainloop()
