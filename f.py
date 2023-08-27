import sounddevice as sd
import speech_recognition as sr

def speech_recognition_microphone(language="en-US"):
    recognizer = sr.Recognizer()

    with sd.InputStream(callback=callback):
        print("Say something...")

        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=10)  # Listen for up to 10 seconds
                text = recognizer.recognize_google(audio, language=language)
                return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error requesting results from Google Web Speech API: {e}")

def callback(indata, frames, time, status):
    pass  # Callback function, not used in this example

def main():
    text = speech_recognition_microphone(language="en-US")
    print("Recognized text:", text)

if __name__ == "__main__":
    main()

