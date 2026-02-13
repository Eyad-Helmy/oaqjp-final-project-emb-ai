from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/')
def render_index():
    return render_template("index.html")

@app.route('/emotionDetector')
def call_emotion_detector():
    text = request.args.get("textToAnalyze")

    result = emotion_detector(text)

    if result["dominant_emotion"] == None:
        return "Invalid text! Please try again!"
        
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text