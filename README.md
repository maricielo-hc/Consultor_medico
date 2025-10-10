
## 🩺 Consultor Médico — Versión 2

**Consultor Médico** es una aplicación con interfaz gráfica desarrollada en **Python** y **Prolog**, diseñada para ayudar a diagnosticar posibles enfermedades en función de los síntomas ingresados por el usuario.
Esta segunda versión trae mejoras en el motor experto, una interfaz más fluida y un conjunto ampliado de reglas médicas.

---

### 🚀 Novedades de la versión 2

* 🔧 Integración mejorada con **Prolog** (ahora más estable y eficiente).
* 🧠 Nuevas reglas de diagnóstico (más enfermedades y síntomas reconocidos).
* 💾 Corrección en la carga de archivos de reglas.
* 🎨 Interfaz optimizada para una mejor experiencia de usuario.
* ⚙️ Soporte completo para entornos virtuales (`.venv`).

---

### 🖥️ Requisitos del sistema

* **Python 3.11+**
* **SWI-Prolog** instalado y agregado al PATH
* Librerías necesarias (instalables desde `requirements.txt`)

Instálalas con:

```bash
pip install -r requirements.txt
```

---

### ▶️ Ejecución desde código fuente

1. Clona el repositorio o descárgalo en formato ZIP.
2. Asegúrate de tener el entorno virtual activado:

   ```bash
   .venv\Scripts\activate
   ```
3. Ejecuta la aplicación:

   ```bash
   python python/app.py
   ```

---

### 📦 Descargar aplicación compilada

Puedes descargar la versión ejecutable (`.exe`) directamente desde el siguiente enlace:

👉 **[Descargar Consultor Médico v2 (.zip)](https://github.com/MaricieloHuaman/Consultor_medico/releases/download/v2.0/Consultor_medico_v2.zip)**

*(No es necesario tener Python o Prolog instalados para usar esta versión.)*

---

### 🧬 Estructura del proyecto

```
Consultor_medico/
│
├── python/
│   ├── app.py               # Interfaz gráfica principal
│   ├── motor.py             # Motor de conexión Python–Prolog
│   ├── data/                # Archivos de datos (síntomas, registros, etc.)
├── prolog/              # Carpeta de archivos .pl
│   └── reglas_enfermedades.pl
│
├── requirements.txt
└── README.md
```

---

### ❤️ Créditos

Proyecto académico integrador de **Python + Prolog**, aplicado al diagnóstico médico básico.
Inspirado en sistemas expertos de IA tradicionales, adaptado con una interfaz moderna.



