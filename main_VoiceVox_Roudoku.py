# Roudoku with VoiceVox, "main_VoiceVox_Roudoku.py" by F. Fujita on 2023/01/10

import random
from flask import Flask, render_template, request
import json
import requests
import wave

app = Flask(__name__, static_url_path='/static')
answer_data = []
Speaker_No = 0
voice_count = 0
filepath = './VoiceVox_Roudoku-main/static/audio/audio'     # Please set the PATH according to your environment.

@app.route("/")
# Display by the HTML
def home():
    return render_template("index_VoiceVox_Roudoku_R.html")

@app.route("/get_Voice")
# Get the Voice No from HTML
def get_Voice_No():
    global Speaker_No
    Speaker_No = int(request.args.get('Voice_No'))
    return (str('OK'))

@app.route("/get")
# Communicate with HTML
def get_bot_response():
    userText = request.args.get('msg')
    answer = make_answer(userText)
    return answer

# Create an answer
def make_answer(tempText):
    global voice_count
    voice_count = voice_count + 1
    if (voice_count >= 30000):
        voice_count = 0
    voice_count_text = ('0000' + str(voice_count))[-4:]

    if (tempText == ""):
        tempText = "　"
    temp_Answer = tempText
    generate_wav(temp_Answer, Speaker_No, filepath, voice_count_text)      
    return str(voice_count_text + ':' + temp_Answer)

# Create a wave file
def generate_wav(text, speaker, filepath, voice_count_text):
    filepath = filepath + voice_count_text + '.wav'
    host = 'localhost'
    port = 50021
    params = (
        ('text', text),
        ('speaker', speaker),
        ('prePhonemeLength', 0),
    )
    response1 = requests.post(
        f'http://{host}:{port}/audio_query',
        params=params
    )
    headers = {'Content-Type': 'application/json',}
    response2 = requests.post(
        f'http://{host}:{port}/synthesis',
        headers=headers,
        params=params,
        data=json.dumps(response1.json())
    )
    wf = wave.open(filepath, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(24000)
    wf.writeframes(response2.content)
    wf.close()

if __name__ == "__main__":
    random.seed(None)
    app.run(host='127.0.0.1', port=5000, debug=True)
