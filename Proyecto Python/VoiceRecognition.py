# Paquete que reconoce el audio y lo pasa a texto 
import speech_recognition as sr
#Paquete que convierte el texto a audio
import pyttsx3
#Paquete que redirige a youtube ,wikipedia o manda mensajes a whatssap
import pywhatkit
#Paquete para obtener el dia o la fecha
import datetime
#Paquete para buscar en wikipedia
import wikipedia
#Paquete de chistes
import pyjokes 
#Paquete Time para delays
import time
#importa paquete para reproducir sonidos
import winsound
#importa la clase respuestas
from Responses import Responses
#import random
import random
#import webBrowser 
import webbrowser

wikipedia.set_lang('es')
global Mensaje
test=False

#Creación del listener
listener = sr.Recognizer()

#
engine = pyttsx3.init()

#Sets the voice to a female voice 0=SystemDefault 1=female
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

greeting="Hola humano"



response=""



def talk(text):
    engine.say(text)
    engine.runAndWait()

#Descomenta para recuperar la funcionalidad original
def wakeword():
    
    try:
        with sr.Microphone() as source: 
          voice = listener.listen(source,phrase_time_limit=5)
          command =listener.recognize_google(voice,language='es-US')
          command = command.lower()
          if 'alexa' in command:
              talk('Que puedo hacer por ti?')
              ready=True
          else:
                
                ready=False
    except:
        ready=False
        pass
    return ready 



#Metodo para acatar un comando
def take_command():
    try: 
        with sr.Microphone() as source: 
          winsound.PlaySound("listening",winsound.SND_FILENAME)
# Reconocimiento de voz 
          voice = listener.listen(source,phrase_time_limit=5)
          command =listener.recognize_google(voice,language='es-MX')
          command = command.lower()
        
        if 'alexa' in command:
            # removes siri from command
            command=command.replace('alexa','')
            
        
    except:
        command=""
        pass
    return command

# Metodo para correr comando
#El original no le pasas el mensaje
def run_ai():
    #Se usa el microfono de la computadora
    command = take_command()
    command = command.lower()
    print(command)
    if command!= "":
        if 'abre' in command:
            pagina=command.replace('abre','',1)
            Responses.openPage(Responses,pagina)

        if 'reproduce' in command:
            song=command.replace('reproduce','',1)
            Responses.playSong(Responses,song)
        
        

        elif 'hora' in command:
            Responses.getTime(Responses)

        elif 'quién es' in command:
            person=command.replace('quién es','',1)
            Responses.searchPerson(Responses,person)


        elif 'busca' in command:
            search=command.replace('busca','',1)
            Responses.generalSearch(Responses,search)

        elif 'chiste' in command:
           Responses.getJoke(Responses)

        elif 'qué es' in command:
            info=command.replace('qué es','',1)
            Responses.getInfo(Responses,info)

        elif 'qué pasó en' in command:
            info=command.replace('qué pasó en','',1)
            Responses.getInfo(Responses,info)

        elif 'llámame' in command:
            newName=command.replace('llámame','',1)
            Responses.setName(Responses,newName)

        elif 'dime mi nombre' in command:
            Responses.getName(Responses)

        elif 'cómo estás' in command:
            Responses.howAmI(Responses)
        
        elif 'apágate'in command or 'apaga te' in command or 'ciérrate' in command:
            Responses.poweroff(Responses)
        

    else:
        talk("Lo siento,no pude escucharte")

  

def run():
    #Run  Default Greeting
    talk(greeting)

    while True:  
    #WakeWord
     #Wake word Validation
        startListening=wakeword()
     #Funcion que me permita siempre estar escuchando
        if startListening == True:
        # Pide un comando
            run_ai()
            startListening = False


#El original no le pasas el mensaje
def run_ai_Command(command):
    #Se usa el microfono de la computadora
    command = command.lower()
    print(command)
    if command!= "":
        if 'abre' in command:
            pagina=command.replace('abre','',1)
            Responses.openPage(Responses,pagina)

        if 'reproduce' in command:
            song=command.replace('reproduce','',1)
            Responses.playSong(Responses,song)
        
        

        elif 'hora' in command:
            Responses.getTime(Responses)

        elif 'quién es' in command or 'quien es' in command :
            person=command.replace('quién es','',1)
            person=command.replace('quien es','',1)
            Responses.searchPerson(Responses,person)


        elif 'busca' in command:
            search=command.replace('busca','',1)
            Responses.generalSearch(Responses,search)

        elif 'chiste' in command:
           Responses.getJoke(Responses)

        elif 'qué es' in command or 'que es' in command :
            info=command.replace('qué es','',1)
            info=command.replace('que es','',1)
            Responses.getInfo(Responses,info)

        elif 'qué pasó en' in command:
            info=command.replace('qué pasó en','',1)
            Responses.getInfo(Responses,info)

        elif 'llámame' in command or 'llamame' in command:
            newName=command.replace('llámame','',1)
            newName=command.replace('llamame','',1)
            Responses.setName(Responses,newName)

        elif 'dime mi nombre' in command:
            Responses.getName(Responses)

        elif 'cómo estás' in command or 'cómo estas' in command or 'como estas' in command or 'como estás' in command:
            Responses.howAmI(Responses)
        
        elif 'apágate'in command or 'apaga te' in command or 'ciérrate' in command or 'apagate' in command:
            Responses.poweroff(Responses)
        

    else:
        talk("Lo siento,no pude escucharte")
        
