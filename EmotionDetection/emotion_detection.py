import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=input_json, headers=headers)
    if response.status_code == 200:
        response_json = json.loads(response.text)
        emotions = response_json['emotionPredictions'][0]['emotion']
        dominant_emotion = ""
        dominant_score = 0
        for emotion in emotions:
            if emotions[emotion] > dominant_score:
                dominant_score = emotions[emotion]
                dominant_emotion = emotion
        emotions['dominant_emotion'] = dominant_emotion
        return emotions
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'sadness': None,
            'joy': None,
            'fear': None,
            'dominant_emotion': None
        }
    elif response.status_code == 500:
        return {
            'anger': None,
            'disgust': None,
            'sadness': None,
            'joy': None,
            'fear': None,
            'dominant_emotion': None
        }
    else:
        return {
            'anger': None,
            'disgust': None,
            'sadness': None,
            'joy': None,
            'fear': None,
            'dominant_emotion': None
        }