from flask import Flask, render_template

app = Flask("Emotion Detection")

@app.route('/')
def render_index():
    return render_template("index.html")

@app.route('/emotionDetector')
def call_emotion_detector():
    pass