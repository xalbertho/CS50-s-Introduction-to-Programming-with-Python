
import os
from elevenlabs.client import ElevenLabs
from elevenlabs import save # Usamos save en lugar de play para evitar errores de librerías
from dotenv import load_dotenv

load_dotenv()

client = ElevenLabs(
    # Es mejor usar variables de entorno, pero si pones el string directo también sirve
    api_key="sk_d029f7cbfba74ce9a730e7a612e105ffdb69846d852eb2b7" 
)

# Generar el audio (Tu código estaba bien aquí)
audio = client.text_to_speech.convert(
    text="The first move is what sets everything in motion.",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

# --- AQUÍ ESTÁ EL TRUCO PARA ARCH LINUX ---

# 1. Guardamos el generador de audio en un archivo
print("Guardando audio...")
save(audio, "hackathon_audio.mp3")

# 2. Lo reproducimos usando el sistema operativo
# Esto es mucho más estable que intentar que python maneje el stream de audio en vivo
print("Reproduciendo...")
os.system("mpv hackathon_audio.mp3")
