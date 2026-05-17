import random
import deepl
import sounddevice as sd 
import numpy as np
import scipy.io.wavfile as wav 
import speech_recognition as sr 
import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
duration = 5
sample_rate = 44100
Idioma = int(input("Hola, en que idioma quieres jugar: Inglés: 1 Alemán: 2 Italiano: 3 o Francés: 4 "))

if Idioma == 1:
    Dificultad = int(input("En que dificultad quieres jugar? Facíl: 1 Medio: 2 Difícil: 3 o INSANO: 4 (Advertencia! Insano es oraciones enteras.) "))
    niveles = {
        "Facíl": ["Perro", "Coche", "Gato", "Pizza", "Hamburguesa", "Diez", "Mesa", "Movíl", "Avión", "Lapíz"],
        "Medio": ["Leer", "Cortar", "Volar", "Saltar", "Dormir", "Vivir", "Escribir", "Comer", "Beber", "Descubrir"],
        "Difícil": ["Guapo", "Bonita", "Colorido", "Gigante", "Lento", "Rapido", "Inteligente", "Feliz", "Paciente"],
        "Insano": [
            "Tengo un perro bonito",
            "Tengo 3 camisetas bonitas",
            "El es muy lento",
            "Corte un gato de papel",
            "Mi movil es un nokia",
            "Soy muy paciente, no como mi amigo",
            "Mi madre esta feliz",
            "Yo leo muchos libros y me gusta",
            "Amo los aviones, son muy cool",
            "Me gusta jugar con el movil",
        ],
    }

    if Dificultad == 1:
        palabra = niveles["Facíl"]
    elif Dificultad == 2:
        palabra = niveles["Medio"]
    elif Dificultad == 3:
        palabra = niveles["Difícil"]
    elif Dificultad == 4:
        palabra = niveles["Insano"]

    puntos = 0
    Test = random.choice(palabra)

    for i in palabra:
        speak(f"¿Como se dice '{i}' en Inglés? ")
        auth_key = "35870bce-545f-4ac7-9aca-258b24149803:fx"  # Replace with your key
        deepl_client = deepl.DeepLClient(auth_key)
        traduccion = deepl_client.translate_text(i, target_lang="EN-US").text
        pregunta= input(f"¿Como se dice {i} en Inglés")
        if pregunta.capitalize() == traduccion:
            speak("¡Felicidades! Ganaste 1 punto")
            puntos += 1
            speak(f"Tus puntos: {puntos}")
        else:
            print("Oh no... la traducción correcta es:", traduccion)
elif Idioma == 2:
    Dificultad = int(input("En que dificultad quieres jugar? Facíl: 1 Medio: 2 Difícil: 3 o INSANO: 4 (Advertencia! Insano es oraciones enteras.) "))
    Dificultad = int(input("En que dificultad quieres jugar? Facíl: 1 Medio: 2 Difícil: 3 o INSANO: 4 (Advertencia! Insano es oraciones enteras.) "))
    niveles = {
        "Facíl": ["Perro", "Coche", "Gato", "Pizza", "Hamburguesa", "Diez", "Mesa", "Movíl", "Avión", "Lapíz"],
        "Medio": ["Leer", "Cortar", "Volar", "Saltar", "Dormir", "Vivir", "Escribir", "Comer", "Beber", "Descubrir"],
        "Difícil": ["Guapo", "Bonita", "Colorido", "Gigante", "Lento", "Rapido", "Inteligente", "Feliz", "Paciente"],
        "Insano": [
            "Tengo un perro bonito",
            "Tengo 3 camisetas bonitas",
            "El es muy lento",
            "Corte un gato de papel",
            "Mi movil es un nokia",
            "Soy muy paciente, no como mi amigo",
            "Mi madre esta feliz",
            "Yo leo muchos libros y me gusta",
            "Amo los aviones, son muy cool",
            "Me gusta jugar con el movil",
        ],
    }

    if Dificultad == 1:
        palabra = niveles["Facíl"]
    elif Dificultad == 2:
        palabra = niveles["Medio"]
    elif Dificultad == 3:
        palabra = niveles["Difícil"]
    elif Dificultad == 4:
        palabra = niveles["Insano"]

    puntos = 0
    Test = random.choice(palabra)

    for i in palabra:
        speak(f"¿Como se dice '{i}' en Inglés? ")
        auth_key = "35870bce-545f-4ac7-9aca-258b24149803:fx"  # Replace with your key
        deepl_client = deepl.DeepLClient(auth_key)
        traduccion = deepl_client.translate_text(i, target_lang="EN-US").text
        pregunta= input(f"¿Como se dice {i} en Aléman?")
        if pregunta.capitalize() == traduccion:
            speak("¡Felicidades! Ganaste 1 punto")
            puntos += 1
            speak(f"Tus puntos: {puntos}")
        else:
            print("Oh no... la traducción correcta es:", traduccion)
elif Idioma == 3:    
    Dificultad = int(input("En que dificultad quieres jugar? Facíl: 1 Medio: 2 Difícil: 3 o INSANO: 4 (Advertencia! Insano es oraciones enteras.) "))
    niveles = {
        "Facíl": ["Perro", "Coche", "Gato", "Pizza", "Hamburguesa", "Diez", "Mesa", "Movíl", "Avión", "Lapíz"],
        "Medio": ["Leer", "Cortar", "Volar", "Saltar", "Dormir", "Vivir", "Escribir", "Comer", "Beber", "Descubrir"],
        "Difícil": ["Guapo", "Bonita", "Colorido", "Gigante", "Lento", "Rapido", "Inteligente", "Feliz", "Paciente"],
        "Insano": [
            "Tengo un perro bonito",
            "Tengo 3 camisetas bonitas",
            "El es muy lento",
            "Corte un gato de papel",
            "Mi movil es un nokia",
            "Soy muy paciente, no como mi amigo",
            "Mi madre esta feliz",
            "Yo leo muchos libros y me gusta",
            "Amo los aviones, son muy cool",
            "Me gusta jugar con el movil",
        ],
    }

    if Dificultad == 1:
        palabra = niveles["Facíl"]
    elif Dificultad == 2:
        palabra = niveles["Medio"]
    elif Dificultad == 3:
        palabra = niveles["Difícil"]
    elif Dificultad == 4:
        palabra = niveles["Insano"]

    puntos = 0
    Test = random.choice(palabra)

    for i in palabra:
        speak(f"¿Como se dice '{i}' en Inglés? ")
        auth_key = "35870bce-545f-4ac7-9aca-258b24149803:fx"  # Replace with your key
        deepl_client = deepl.DeepLClient(auth_key)
        traduccion = deepl_client.translate_text(i, target_lang="EN-US").text
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate,channels=1,dtype="int16")
        sd.wait()
        wav.write("resultado.wav", sample_rate, recording)
        pregunta= input(f"¿Como se dice {i} en Inglés")
        if pregunta.capitalize() == traduccion:
            speak("¡Felicidades! Ganaste 1 punto")
            puntos += 1
            speak(f"Tus puntos: {puntos}")
        else:
            print("Oh no... la traducción correcta es:", traduccion)
elif Idioma == 4:
    Dificultad = int(input("En que dificultad quieres jugar? Facíl: 1 Medio: 2 Difícil: 3 o INSANO: 4 (Advertencia! Insano es oraciones enteras.) "))
    niveles = {
        "Facíl": ["Perro", "Coche", "Gato", "Pizza", "Hamburguesa", "Diez", "Mesa", "Movíl", "Avión", "Lapíz"],
        "Medio": ["Leer", "Cortar", "Volar", "Saltar", "Dormir", "Vivir", "Escribir", "Comer", "Beber", "Descubrir"],
        "Difícil": ["Guapo", "Bonita", "Colorido", "Gigante", "Lento", "Rapido", "Inteligente", "Feliz", "Paciente"],
        "Insano": [
            "Tengo un perro bonito",
            "Tengo 3 camisetas bonitas",
            "El es muy lento",
            "Corte un gato de papel",
            "Mi movil es un nokia",
            "Soy muy paciente, no como mi amigo",
            "Mi madre esta feliz",
            "Yo leo muchos libros y me gusta",
            "Amo los aviones, son muy cool",
            "Me gusta jugar con el movil",
        ],
    }

    if Dificultad == 1:
        palabra = niveles["Facíl"]
    elif Dificultad == 2:
        palabra = niveles["Medio"]
    elif Dificultad == 3:
        palabra = niveles["Difícil"]
    elif Dificultad == 4:
        palabra = niveles["Insano"]

    puntos = 0
    Test = random.choice(palabra)

    for i in palabra:
        speak(f"¿Como se dice '{i}' en Inglés? ")
        auth_key = "35870bce-545f-4ac7-9aca-258b24149803:fx"  # Replace with your key
        deepl_client = deepl.DeepLClient(auth_key)
        traduccion = deepl_client.translate_text(i, target_lang="EN-US").text
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate,channels=1,dtype="int16")
        sd.wait()
        wav.write("resultado.wav", sample_rate, recording)
        pregunta= input(f"¿Como se dice {i} en Inglés")
        if pregunta.capitalize() == traduccion:
            speak("¡Felicidades! Ganaste 1 punto")
            puntos += 1
            speak(f"Tus puntos: {puntos}")
        else:
            print("Oh no... la traducción correcta es:", traduccion)
