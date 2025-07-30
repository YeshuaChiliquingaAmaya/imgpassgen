# run_test.py
import os
from imgpassgen import generate_password, verify_password, VerificationError

# --- CONFIGURACIÓN ---
# Coloca una imagen tuya en la carpeta y pon su nombre aquí
MI_FOTO = "pennywise.jpeg" 
MI_FRASE = "esta-vez-si-funciona"

# --- VERIFICACIÓN INICIAL ---
if not os.path.exists(MI_FOTO):
    print(f"❌ ERROR: No se encontró la imagen de prueba '{MI_FOTO}'.")
    print("   Asegúrate de tener una imagen con ese nombre en esta carpeta.")
    exit()

print("✅ Imagen encontrada. Probando la librería con el nuevo algoritmo (PBKDF2)...")
print("-" * 40)

try:
    # 1. Generar contraseña
    print("1. Generando contraseña...")
    password = generate_password(MI_FOTO, MI_FRASE)
    print(f"   => Contraseña generada: {password}\n")

    # 2. Verificar con datos correctos
    print("2. Verificando con datos CORRECTOS...")
    assert verify_password(password, MI_FOTO, MI_FRASE) is True
    print("   => ✅ ¡ÉXITO! La verificación es correcta.\n")

    # 3. Verificar con datos incorrectos
    print("3. Verificando con frase INCORRECTA...")
    try:
        verify_password(password, MI_FOTO, "frase-mala")
    except VerificationError:
        print("   => ✅ ¡ÉXITO! La verificación falló como se esperaba.\n")

    print("🎉🎉🎉 ¡LO LOGRAMOS! ¡Tu librería funciona! 🎉🎉🎉")

except Exception as e:
    print(f"\n❌ Ocurrió un error inesperado: {e}")
    print("   Asegúrate de tener el último código con PBKDF2 en 'src/imgpassgen/core.py'.")