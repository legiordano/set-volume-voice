import speech_recognition as sr
import osascript

def set_system_volume(volume):
    osascript.osascript(f'set volume output volume {volume}')

def main():
    recognizer = sr.Recognizer()

    print("Di 'subir volumen' o 'bajar volumen' para controlar el volumen con la voz.")
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                print("Escuchando...")
                audio = recognizer.listen(source, timeout=3)
                command = recognizer.recognize_google(audio, language="es-ES").lower()

                if "subir volumen" in command:
                    set_system_volume(50)
                    print("Volumen aumentado al 50%.")
                elif "bajar volumen" in command:
                    set_system_volume(10)
                    print("Volumen reducido al 10%.")
                elif "terminar" in command:
                    break
                else:
                    print("Comando no reconocido.")

            except sr.WaitTimeoutError:
                print("Tiempo de espera agotado. Vuelve a intentarlo.")
            except sr.UnknownValueError:
                print("No se pudo entender el comando de voz.")
            except sr.RequestError:
                print("Error al solicitar el servicio de reconocimiento de voz.")

if __name__ == "__main__":
    main()
