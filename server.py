"""serves website"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_getter():
    """
    emotion getter
    """
    text_to_analyze = request.args.get('textToAnalyze')
    my_json = emotion_detector(text_to_analyze)
    if my_json['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    output = f"For the given statement, the system response is \
    'anger': {my_json['anger']}, \
    'disgust': {my_json['disgust']} \
    , 'fear': {my_json['fear']}, 'joy': {my_json['joy']} \
    and 'sadness': {my_json['sadness']}. The dominant emotion is \
    {my_json['dominant_emotion']}."
    print(output)
    return output

@app.route("/")
def render_index_page():
    """
    website getter
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
