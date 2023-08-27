import sounddevice as sd
import numpy as np
import speech_recognition as sr

def speech_recognition_microphone(language="es-ES"):
    recognizer = sr.Recognizer()

    print("Di algo...")

    # Record audio using sounddevice
    audio = sd.rec(int(10 * 44100), samplerate=44100, channels=2)
    sd.wait()

    try:
        # Convert audio data to a single channel (mono)
        audio_mono = np.mean(audio, axis=1)

        text = recognizer.recognize_google(audio_mono, language=language)
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

