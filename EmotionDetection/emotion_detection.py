"""Module providing a function for Emotion Detection of provided text."""

import requests
import json

def emotion_detector(text_to_analyse):
    """Function accepting text data and sending it to the Watson API for emotion detection."""
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    response = requests.post(url, json = myobj, headers=header)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    formatted_response = json.loads(response.text)
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_scores, key=lambda e: emotion_scores[e])
    emotion_scores['dominant_emotion'] = dominant_emotion
    return emotion_scores
