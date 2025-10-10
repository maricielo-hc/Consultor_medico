# 🩺 Sistema Experto – Consultor Médico

Este proyecto es un **sistema experto en Prolog**, con una **interfaz gráfica en Python**. Su objetivo es ayudar a detectar síntomas básicos y sugerir posibles diagnósticos de manera interactiva.

## 📂 Estructura del Proyecto

```
Consultor_medico/
│
├── prolog/                   # Base de conocimiento
│   └── base_conocimiento.pl
│
├── python/                   # Código en Python
│   ├── gui.py                # Interfaz gráfica
│   ├── motor.py              # Conexión Python ↔ Prolog
│
├── data/                     # (opcional) Archivos de soporte
│
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Este archivo
```

## 🚀 Cómo usarlo

### 🔹 Opción 1: Descargar el ejecutable (recomendado)

No necesitas instalar nada, simplemente:

1. Descarga el archivo `.zip` desde la última release:
   👉 [Descargar aquí](https://github.com/maricielo-hc/Consultor_medico/releases/download/v1.0.0/Consultor_medico_v1.0.zip)
2. Extrae el `.zip`.
3. Abre el archivo `Consultor_medico.exe` y ejecutar.

¡Listo! Se abrirá la ventanilla donde puedes realizar tus consultas.

### 🔹 Opción 2: Ejecutar desde el código fuente

Si prefieres correrlo con Python y Prolog:

1. Clona el repositorio:

   ```bash
   git clone https://github.com/<TU_USUARIO>/<TU_REPO>.git
   cd Consultor_medico
   ```
2. Activa el entorno virtual e instala dependencias:

   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el sistema:

   ```bash
   python python/gui.py
   ```

## 🧠 Tecnologías usadas

* **Prolog (SWI-Prolog)** → motor lógico y base de conocimiento.
* **Python + Tkinter** → interfaz gráfica.
* **PySwip** → puente entre Python y Prolog.
* **PyInstaller** → creación del ejecutable.

## 📌 Estado del proyecto

Versión `v1.0.0` – primera release funcional.

## ✨ Futuras mejoras

* Ampliar la base de síntomas y diagnósticos.
* Mejorar la interfaz gráfica.
* Publicar versión multiplataforma (Linux/Mac).
