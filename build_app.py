import os
import shutil
import subprocess
import sys
import stat

def eliminar_carpeta_segura(ruta):
    """Elimina carpeta de forma segura, manejando permisos"""
    if not os.path.exists(ruta):
        return
    
    # Función para cambiar permisos de archivos
    def cambiar_permisos(func, path, exc_info):
        try:
            os.chmod(path, stat.S_IWRITE)
            func(path)
        except Exception as e:
            print(f"⚠️  No se pudo eliminar {path}: {e}")
    
    try:
        shutil.rmtree(ruta, onerror=cambiar_permisos)
        print(f"✅ Carpeta {ruta} eliminada")
    except Exception as e:
        print(f"⚠️  No se pudo eliminar {ruta}: {e}")

def instalar_dependencias():
    """Instala todas las dependencias necesarias"""
    print("📦 Instalando dependencias...")
    
    dependencias = ['pyswip']
    
    for dep in dependencias:
        try:
            __import__(dep)
            print(f"✅ {dep} ya instalado")
        except ImportError:
            print(f"📥 Instalando {dep}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])

def verificar_archivos():
    """Verifica que todos los archivos necesarios existan"""
    print("🔍 Verificando archivos...")
    
    archivos_necesarios = [
        'main.py',
        'python/motor.py',
        'python/app.py', 
        'prolog/reglas_enfermedades.pl',
        'prolog/sistema_principal.pl'
    ]
    
    for archivo in archivos_necesarios:
        if not os.path.exists(archivo):
            print(f"❌ FALTANTE: {archivo}")
            return False
        print(f"✅ {archivo}")
    
    # Verificar SWI-Prolog
    swi_dir = "swi-prolog"
    if os.path.exists(swi_dir):
        for archivo in os.listdir(swi_dir):
            if archivo.lower().startswith('swipl') and archivo.lower().endswith('.exe'):
                print(f"✅ SWI-Prolog encontrado: {archivo}")
                return True
    
    print("❌ SWI-Prolog no encontrado")
    return False

def construir_ejecutable():
    """Construye el ejecutable con todas las dependencias"""
    
    # Instalar dependencias primero
    instalar_dependencias()
    
    if not verificar_archivos():
        print("❌ No se puede continuar - Faltan archivos")
        return
    
    # Verificar PyInstaller
    try:
        import PyInstaller
        print("✅ PyInstaller listo")
    except ImportError:
        print("📦 Instalando PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    print("🔨 Construyendo ConsultorMedico.exe...")
    
    # Limpiar build anterior (de forma segura)
    print("🧹 Limpiando builds anteriores...")
    eliminar_carpeta_segura("build")
    eliminar_carpeta_segura("dist")
    
    # Comando con todas las dependencias incluidas
    try:
        subprocess.check_call([
            sys.executable, "-m", "PyInstaller",
            "--onefile",
            "--windowed",
            "--name=ConsultorMedico",
            "--add-data=prolog/reglas_enfermedades.pl;prolog",
            "--add-data=prolog/sistema_principal.pl;prolog",
            "--add-data=python/motor.py;python",
            "--add-data=python/app.py;python",
            "--add-data=swi-prolog;swi-prolog",
            "--hidden-import=pyswip",
            "main.py"
        ])
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en PyInstaller: {e}")
        return
    
    # Verificar resultado
    if os.path.exists("dist/ConsultorMedico.exe"):
        print("✅ ¡ÉXITO! Ejecutable creado: dist/ConsultorMedico.exe")
        
        # Crear ZIP
        shutil.make_archive("ConsultorMedico-Portable", 'zip', 'dist')
        print("📦 ZIP creado: ConsultorMedico-Portable.zip")
        
        print("\n" + "="*50)
        print("🎉 ¡NUEVO EJECUTABLE LISTO!")
        print("✅ pyswip incluido")
        print("✅ SWI-Prolog incluido") 
        print("✅ Listo para distribuir")
        print("="*50)
    else:
        print("❌ Error: No se creó el ejecutable")

if __name__ == "__main__":
    construir_ejecutable()