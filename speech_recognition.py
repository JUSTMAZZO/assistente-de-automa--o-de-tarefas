import speech_recognition as sr

def recognize_speech(entry_widget):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        entry_widget.insert(0, text)  # Insere o texto reconhecido na entrada
    except sr.UnknownValueError:
        print("Não foi possível reconhecer o áudio.")
    except sr.RequestError:
        print("Erro na API de reconhecimento de fala.")
