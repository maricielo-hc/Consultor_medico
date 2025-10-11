# 🩺 Consultor Médico — Versión 2.0

**Consultor Médico** es una aplicación **portable** con interfaz gráfica desarrollada en **Python** y **Prolog**, diseñada para ayudar a diagnosticar posibles enfermedades en función de los síntomas ingresados por el usuario.  
Esta versión incluye una **aplicación ejecutable independiente** que no requiere instalación de Python o Prolog.

---

### 🚀 Novedades de la versión 2.0

* 🎯 **Aplicación portable** - Ejecutable .exe independiente
* 🔧 Integración mejorada con **Prolog** (ahora más estable y eficiente)
* 🧠 Nuevas reglas de diagnóstico (más enfermedades y síntomas reconocidos)
* 💾 Guardado automático de datos en carpeta del usuario
* 🎨 Interfaz optimizada para una mejor experiencia de usuario
* 📦 **SWI-Prolog incluido** - No requiere instalación externa

---

### 🖥️ Para Desarrolladores

* **Python 3.11+**
* **SWI-Prolog** (incluido en la versión portable)
* Librerías necesarias (instalables desde `requirements.txt`)

Instálalas con:
```bash
pip install -r requirements.txt
```

#### ▶️ Ejecución desde código fuente
1. Clona el repositorio
2. Activa el entorno virtual:
   ```bash
   .venv\Scripts\activate
   ```
3. Ejecuta la aplicación:
   ```bash
   python python/app.py
   ```

---

### 📥 **PARA USUARIOS FINALES**

#### ⭐ **Descargar aplicación portable**
**[📥 Descargar ConsultorMedico-Portable.zip](https://github.com/maricielo-hc/Consultor_medico/releases/download/v2.0/ConsultorMedico-Portable.zip)**

#### 🎯 **Instalación (solo 3 pasos):**
1. **Descarga** el archivo ZIP
2. **Extrae** en cualquier carpeta
3. **Ejecuta** `ConsultorMedico.exe`

**¡Listo! No requiere instalación de Python o Prolog.**

---

### 💾 **Datos Guardados**
La aplicación guarda automáticamente los registros en:
```
C:\Users\[TuUsuario]\ConsultorMedico_data\casos.txt
```

Para acceder fácilmente, usa el botón **"📂 Abrir Carpeta Datos"** en la aplicación.

---

### 🧬 Estructura del proyecto

```
Consultor_medico/
├── swi-prolog/               # SWI-Prolog portable (incluido)
├── prolog/                   # Base de conocimiento
│   ├── reglas_enfermedades.pl
│   └── sistema_principal.pl
├── python/                   # Lógica principal
│   ├── app.py               # Interfaz gráfica
│   └── motor.py             # Conexión Python-Prolog
├── main.py                  # Punto de entrada unificado
├── build_app.py             # Script para construir .exe
├── ConsultorMedico-Portable.zip # Versión portable
├── requirements.txt
└── README.md
```

---

### 🛠️ Compilar desde código fuente
Para generar tu propio ejecutable:
```bash
python build_app.py
```

---

### ❤️ Créditos
Proyecto académico integrador de **Python + Prolog**, aplicado al diagnóstico médico básico.  
Inspirado en sistemas expertos de IA tradicionales, adaptado con una interfaz moderna.

**¡Ahora con versión portable lista para distribuir!** 🎉

---

### 📞 Soporte
Si encuentras algún problema con la aplicación portable, abre un **issue** en el repositorio.

