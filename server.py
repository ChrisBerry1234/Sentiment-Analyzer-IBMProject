from flask import Flask, request, make_response, render_template, jsonify
from Sentiment_Module.emotion_detector import emotion_detector

app = Flask("My Emotion Detector")

@app.route('/')
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotions_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze.strip() == "":
        return ("Please Enter Text"), 400
    if text_to_analyze.isdigit():
        return ("Please Only enter text"), 400

    emotion_scores, dominant_emotion = emotion_detector(text_to_analyze)

    #create object to send 
    message = {
                "input": text_to_analyze,
                "scores": emotion_scores,
                "dominant_emotion": dominant_emotion
            }

    return jsonify(message), 200

#error handles
@app.errorhandler(404)
def api_not_found():
    return {"message": "API not found"}, 404

@app.errorhandler(Exception)
def handle_exception(e):
    return {"message": str(e)}, 500
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)