import speech_recognition as sr

def audio_file_to_text(audio_file_path):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load audio file
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)  # Read the entire audio file

        try:
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Sorry, could not understand the audio."
        except sr.RequestError as e:
            return f"Error occurred: {e}"

if __name__ == "__main__":
    audio_file_path = "recorded_audio.wav"  # Replace with your audio file path
    converted_text = audio_file_to_text(audio_file_path)
    print(f"Transcribed text: {converted_text}")
