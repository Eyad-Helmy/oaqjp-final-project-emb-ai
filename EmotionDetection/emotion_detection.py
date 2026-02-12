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
    output = confidence_scores
    '''{"anger": 0.006274985, 
        "disgust": 0.0025598293, 
        "fear": 0.009251528, 
        "joy": 0.9680386, 
        sadness": 0.049744144, 
        "dominant_emotion":"joy"}
    '''

    for key, emotion_score in confidence_scores.items():
        if emotion_score > max_value:
            max_key = key
            max_value = emotion_score

    output["dominant_emotion"] = max_key

    return output

# print(emotion_detector("i really like you"))