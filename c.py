import sounddevice as sd
import speech_recognition as sr

def speech_recognition_microphone(language="es-ES"):
    recognizer = sr.Recognizer()

    print("Di algo...")

    # Record audio using sounddevice with a single channel (mono)
    audio = sd.rec(int(10 * 44100), samplerate=44100, channels=1)
    sd.wait()

    try:
        text = recognizer.recognize_google(audio, language=language)
        return text
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print(f"Error al solicitar resultados de la API de reconocimiento de voz de Google: {e}")

def main():
    text = speech_recognition_microphone(language="es-ES")
    print("Texto reconocido:", text)

if __name__ == "__main__":
    main()

