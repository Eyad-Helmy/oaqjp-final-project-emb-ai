import requests
def emotion_detector(text_to_analyse):
    
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL, headers=header, json=payload)
    response = response.json()
    confidence_scores = response["emotionPredictions"][0]["emotion"]

    max_key = ""
    max_value = 0
    for key, emotion_score in confidence_scores.items():
        if emotion_score > max_value:
            max_key = key
            max_value = emotion_score

    return max_key


# print(emotion_detector("i really like you"))
#response["emotionPredictions"][0]