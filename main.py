import speech_recognition as sr
import osascript  # Solo para macOS

def set_system_volume(volume):
    # Ajustar el volumen del sistema utilizando osascript (para macOS)
    osascript.osascript(f'set volume output volume {volume}')

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Di 'subir volumen' o 'bajar volumen' para controlar el volumen con la voz.")
        while True:
            try:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

                # Reconocer el comando de voz
                command = recognizer.recognize_google(audio).lower()

                if "subir volumen" in command:
                    set_system_volume(50)  # Ajusta el volumen deseado aquí (por ejemplo, 50).
                elif "bajar volumen" in command:
                    set_system_volume(10)  # Ajusta el volumen deseado aquí (por ejemplo, 10).
                elif "terminar" in command:
                    break
                else:
                    print("Comando no reconocido.")

            except sr.UnknownValueError:
                print("No se pudo entender el comando de voz.")
            except sr.RequestError:
                print("Error al solicitar el servicio de reconocimiento de voz.")

if __name__ == "__main__":
    main()
