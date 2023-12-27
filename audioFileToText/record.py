import pyaudio
import wave

def record_audio(output_filename, record_seconds):
    CHUNK = 1024  # Number of frames per buffer
    FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
    CHANNELS = 1  # Number of audio channels (1 for mono, 2 for stereo)
    RATE = 44100  # Sample rate (samples per second)

    audio = pyaudio.PyAudio()

    # Create an audio stream
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    # Record audio for the specified duration
    for i in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a WAV file
    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

if __name__ == "__main__":
    output_filename = "recorded_audio.wav"  # Set the output filename
    record_seconds = 10  # Set the duration of recording in seconds

    print(f"Recording audio for {record_seconds} seconds...")
    record_audio(output_filename, record_seconds)
    print(f"Audio recorded and saved as '{output_filename}'")
