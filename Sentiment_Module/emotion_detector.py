""" Emotion Detection Module
    Sends text to the IBM Watson Emotion API and returns 
    object"""

import json
import requests


def emotion_detector(text_to_analyze):
    """ Sends a  request to the IBM Watson Emotion API and return 
    a dictionary of emotion scores and the dominant emotion string."""

    url = 'https://sn-watson-emotion.labs.skills.network/v1/"watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myjson = {"raw_document": {"text": text_to_analyze }}

    response = requests.post(url, json = myjson, headers = headers, timeout = 5)
    formatted_response = json.loads(response.text)
    scores = {}
    max = -1
    dominant_emotion = None

    for x in formatted_response['emotionPredictions']:
        for emotion, score in x['emotion'].items():
            scores[emotion] = score
            print({f"{emotion}": {score}})

    for emotion, score in scores.items():
        if score > max:
            max = score
            dominant_emotion = emotion

    #print({f'"Dominant emotion": {dominant_emotion}: {max}'})    
    #return dominant_emotion
    return scores, dominant_emotion
