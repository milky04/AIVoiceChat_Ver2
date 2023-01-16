import json
import requests

# スピーカーIDを指定(0:つくよみちゃん)
speaker_id = 0

# 引数にセリフを指定
def speech_synthesis(text):
    # 音声合成のクエリの作成
    response = requests.post(
        "http://localhost:50031/audio_query",
        params={
            'text': text,
            'speaker': speaker_id,
            'core_version': '0.0.0'
        })
    query = response.json()

    # 音声合成のwavの生成
    response = requests.post(
        'http://localhost:50031/synthesis',
        params={
            'speaker': speaker_id,
            'core_version': "0.0.0",
            'enable_interrogative_upspeak': 'true'
        },
        data=json.dumps(query))

    return response.content
