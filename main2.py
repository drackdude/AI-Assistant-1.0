import speech_recognition as sr

def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_file_path) as source:
        
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.record(source)
        
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
    
    return None


audio_file_path = "path/to/your/audio/file.wav"
transcribed_text = transcribe_audio(audio_file_path)

if transcribed_text:
    print("Transcribed Text:")
    print(transcribed_text)
else:
    print("Failed to transcribe the audio.")
