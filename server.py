from flask import Flask, request, make_response, render_template, jsonify
from Sentiment_Module.emotion_detector import emotion_detector

app = Flask("My Emotion Detector")

@app.route('/')
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotions_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_scores, dominant_emotion = emotion_detector(text_to_analyze)

    message = (
                f"For the given statement: '{text_to_analyze}',"+
                f" the system response is {emotion_scores},"+ 
                f" the dominant emotion is {dominant_emotion}")

    return message
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)