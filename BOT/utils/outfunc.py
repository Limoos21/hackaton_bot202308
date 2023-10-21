import speech_recognition as speech_r
import pyaudio
import wave
import requests
import json
import os


async def voice_chat(sample):
    r = speech_r.Recognizer()

    with sample as audio:
        content = r.record(audio)
        r.adjust_for_ambient_noise(audio)

        voice_text = r.recognize_google(content, language="ru_RU")

        return voice_text

async def openai(voice_text):

    api_key = 'chad-0cb1fb922ef94cf7a72823d1efbc0b65fv2f7umj'

    url = 'https://ask.chadgpt.ru/api/public/gpt-3.5'

    data = {
        "message": voice_text,   #Допиши  промт
        "api_key": api_key
    }

    json_data = json.dumps(data)

    response = requests.post(url, json_data)

    return response.json()