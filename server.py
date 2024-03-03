"""Module handling the Flask HTTP server."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/emotionDetector")
def emot_detector():
    """Function handling emotion detection request."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    emotion_values = ""
    for emotion in response:
        if emotion == 'dominant_emotion':
            continue
        val = response[emotion]
        emotion_values += f"'{emotion}': {val}, "
    return f"""For the given statement, the system response is {emotion_values[:-2]}.
                The dominant emotion is {dominant_emotion}."""

@app.route("/")
def render_index_page():
    """Function handling root GET requests."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
