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
#Paquete numero random
import random
#Importa el usuario
from User import User
#import webBrowser 
import webbrowser
#import sys
import sys
#so the next import can work
sys.path.append('C:/Users/jeffr/OneDrive/Documentos/UV/7mo semestre/INTERFACES DE USUARIO AVANZADAS/Proyecto Python/Gui')

wikipedia.set_lang('es')
#Creación del listener
listener = sr.Recognizer()

#
engine = pyttsx3.init()

#Sets the voice to a female voice 0=SystemDefault 1=female
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#---------------MQTT------------







#---------------MQTT------------

def talk(text):
    engine.say(text)
    engine.runAndWait()



class Responses:
    def __init__(self):
        self.response=""
    
    def response_set(self,response):
        self.response=response
    def response_get(self):
        return self.response
    
    #Metodos con todas las respuestas
    def playSong(self,song):
         if song!="":
                response='Reproduciendo:'+song
                self.response_set(self,response)
                talk('Reproduciendo:'+song)
                pywhatkit.playonyt (song)
         else:
                response="Lo siento, no te pude escuchar, puedes repetirlo?"
                self.response_set(self,response)
                talk("Lo siento,no te pude escuchar,puedes repetirlo?")

    def openPage(self,pagina):
         if pagina!="":
             if 'facebook' in pagina:
                response='Abriendo:'+pagina
                self.response_set(self,response)
                talk('Abriendo:'+pagina)
                webbrowser.open("https://facebook.com")
             if 'cuevana' in pagina:
                response='Abriendo:'+pagina
                self.response_set(self,response)
                talk('Abriendo:'+pagina)
                webbrowser.open("https://cuevana3.io/")
             if 'twitter' in pagina:
                response='Abriendo:'+pagina
                self.response_set(self,response)
                talk('Abriendo:'+pagina)
                webbrowser.open("https://twitter.com/home")
             if 'reddit' in pagina:
                response='Abriendo:'+pagina
                self.response_set(self,response)
                talk('Abriendo:'+pagina)
                webbrowser.open("https://reddit.com")
             if 'google' in pagina:
                response='Abriendo:'+pagina
                self.response_set(self,response)
                talk('Abriendo:'+pagina)
                webbrowser.open("https://google.com")
         else:
                response="Lo siento, no te pude escuchar, puedes repetirlo?"
                self.response_set(self,response)
                talk("Lo siento, no te pude escuchar, puedes repetirlo?")

    def getTime(self):
            time= datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            response='La hora es: '+time
            self.response_set(self,response)
            talk('La hora es: '+time)

    def searchPerson(self,person):
        if person!="":
            try:
                info=wikipedia.summary(person,1,auto_suggest=False)
                print(info)
                response=info
                self.response_set(self,response)
                talk(info)
                #in case it finds more than 1 definition ,takes a random one
            except wikipedia.DisambiguationError as e:
                s = random.choice(e.options)
                p=wikipedia.summary(s,1,auto_suggest=False)
                talk(p)
            except wikipedia.exceptions.PageError as e:
                response="Lo siento, no pude encontrar la pagina"
                self.response_set(self,response)
                talk("Lo siento, no pude encontrar la pagina")    
        else:
                response="Lo siento, no te pude escuchar, puedes repetirlo?"
                self.response_set(self,response)
                talk("Lo siento, no te pude escuchar, puedes repetirlo?")

    def generalSearch(self,search):
        if search!="":
                response='Buscando '+search
                self.response_set(self,response)
                talk('Buscando '+search)
                pywhatkit.search(search)
        else:
            
                talk("Lo siento,no te pude escuchar,puedes repetirlo?")

    def getJoke(self):
            joke=pyjokes.get_joke('es')
            print(joke)
            response=joke
            self.response_set(self,response)
            talk(joke)

    def getInfo(self,info):
        if info!="":
            try:
                summary=wikipedia.summary(info,1,auto_suggest=False)
                print(summary)
                response=summary
                self.response_set(self,response)
                talk(summary)
                #in case it finds more than 1 definition ,takes a random one
            except wikipedia.DisambiguationError as e:
                s = random.choice(e.options)
                p=wikipedia.summary(s,1,auto_suggest=False)
                talk(p)
            except wikipedia.exceptions.PageError as e:
                response="Lo siento, no pude encontrar la pagina"
                self.response_set(self,response)
                talk("Lo siento, no pude encontrar la pagina")   
        else:
                response="Lo siento, no te pude escuchar,puedes repetirlo?"
                self.response_set(self,response)
                talk("Lo siento, no te pude escuchar,puedes repetirlo?")

    def setName(self,newName):
        if newName!="":
            response="OK,Ahora te llamare "+str(newName)
            self.response_set(self,response)
            talk("OK,Ahora te llamare "+str(newName))
            User.setName(User,newName)
        else:
                response="Lo siento, no te pude escuchar,puedes repetirlo?"
                self.response_set(self,response)
                talk("Lo siento, no te pude escuchar,puedes repetirlo?")
                

    def getName(self):
           name= User.getName(User)
           response="Tu nombre es "+str(name)
           self.response_set(self,response)
           talk("Tu nombre es "+str(name))

    def howAmI(self):
         name= User.getName(User)
         feelings = random.randint(1, 2)
         if feelings== 1:
             response="Estoy bien"+str(name)+", Gracias por preguntar"
             self.response_set(self,response)
             talk("Estoy bien"+str(name)+", Gracias por preguntar")
         if feelings== 2:
             response="De maravila"+str(name)
             self.response_set(self,response)
             talk("De maravila"+str(name))
             
    def poweroff(self):
        response="Apágando..."
        self.response_set(self,response)
        talk("Apágando...")
        quit()
        
    
        
        
        
    

            

    
         
            