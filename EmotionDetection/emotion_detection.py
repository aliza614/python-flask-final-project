import requests, json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = input_json, headers = headers)
    print("response is", response)
    if response.status_code == 400:
        output_json = \
        {
            'anger':None, 
            'disgust':None, 
            'fear':None, 
            'joy':None, 
            'sadness': None, 
            'dominant_emotion': None
        }
        return output_json
    output_json = json.loads(response.text)['emotionPredictions'][0]['emotion']
    dominant_emotion = ''
    dominant_emotion_score= -1
    emotions = ['anger','disgust', 'fear', 'joy','sadness']
    for emotion in emotions:
        if dominant_emotion == '':
            dominant_emotion = emotion
            dominant_emotion_score = output_json[emotion]
        elif dominant_emotion_score < output_json[emotion]:
            dominant_emotion = emotion
            dominant_emotion_score = output_json[emotion]

    output_json['dominant_emotion'] = dominant_emotion
    return output_json