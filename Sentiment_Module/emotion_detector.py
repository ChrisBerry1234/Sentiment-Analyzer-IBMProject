import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myjson = {"raw_document": {"text": text_to_analyze }}

    response = requests.post(url, json = myjson, headers = headers)
    formatted_response = json.loads(response.text)
    scores = {}
    max = -1
    Dominant_emotion = None

    for x in formatted_response['emotionPredictions']:
        for emotion, score in x['emotion'].items():
            scores[emotion] = score
            print({f'"{emotion}": {score}'})

    for emotion, score in scores.items():
        if score > max:
            max = score
            Dominant_emotion = emotion
    print({f'"Dominant emotion": {Dominant_emotion}: {max}'})    
         
