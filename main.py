import tkinter as tk
import sys
import os

# Agregar la ruta de Python al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'python'))

from python.app import ConsultorMedicoApp

def main():
    root = tk.Tk()
    app = ConsultorMedicoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()