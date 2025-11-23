from flask import Flask, request, make_response, render_template, url_for
from Sentiment_Module.emotion_detector import emotion_detector

app = Flask("My Emotion Detector")

@app.route('/')
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotionsdetector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    res = make_response({"message": f"Your emotion was {response}"})
    res.status_code = 200

    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)