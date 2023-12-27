import speech_recognition as sr

def audio_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone with a timeout of 10 seconds
    with sr.Microphone() as source:
        print("Speak something...")
        try:
            audio_data = recognizer.listen(source, timeout=10)
        except sr.WaitTimeoutError:
            return "Timeout. No speech detected within 10 seconds."

        try:
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Sorry, could not understand the audio."
        except sr.RequestError as e:
            return f"Error occurred: {e}"

if __name__ == "__main__":
    converted_text = audio_to_text()
    print(f"You said: {converted_text}")
