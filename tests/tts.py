import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
engine.say("Olá, me chamo Memphis, sua Assistente pessoal!")
engine.runAndWait()
