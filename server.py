from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask("Emotion Detection")

@app.route('/')
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_getter():
    text_to_analyze = request.args.get('textToAnalyze')
    my_json = json.loads(emotion_detector(text_to_analyze))
    output = f"For the given statement, the system response is 'anger': {my_json['anger']}, 'disgust': {my_json['disgust']} \
    , 'fear': {my_json['fear']}, 'joy': {my_json['joy']} and 'sadness': {my_json['sadness']}. The dominant emotion is \
    {my_json['dominant_emotion']}."
    print(output)
    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)