import speech_recognition as sr
import os

# Listen and recognize speech
def listen_microphone():
    microphone = sr.Recognizer()
    
    with sr.Microphone() as source:
        microphone.adjust_for_ambient_noise(source)
        print("Diga algo!")
        audio = microphone.listen(source)
            
    try:
        text = microphone.recognize_google(audio, language = "pt-BR")
        
        if "navegador" in text: 
            os.system("firefox")
            
        elif "calculadora" in text:
            os.system("gnome-calculator")
            
        elif "editor" in text:
            os.system("code")
        
        elif "reprodutor" in text:
            os.system("vlc")
            
        elif "bloco de notas" in text:
            os.system("gedit")
            
        elif "música" in text:
            os.system("spotify")
            
        elif "desligar" in text:
            os.system("poweroff")
        
        elif "reiniciar" in text:
            os.system("reboot")
            
        print("Você disse: {}".format(text))
    except sr.UnknownValueError:
        print("Desculpe, não entendi!")
        
    return text

while(True):
    listen_microphone()