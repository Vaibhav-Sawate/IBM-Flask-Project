from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Emotion Detection API! Use the /emotionDetector endpoint to analyze emotions."

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    text_to_analyze = request.json.get('text', '')
    response = emotion_detector(text_to_analyze)

    # Prepare the output format
    output = {
        "anger": response['anger'],
        "disgust": response['disgust'],
        "fear": response['fear'],
        "joy": response['joy'],
        "sadness": response['sadness'],
        "dominant_emotion": response['dominant_emotion']
    }

    # Prepare the response message
    dominant_emotion = response['dominant_emotion']
    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {output['anger']}, 'disgust': {output['disgust']}, "
        f"'fear': {output['fear']}, 'joy': {output['joy']} "
        f"and 'sadness': {output['sadness']}. The dominant emotion is {dominant_emotion}."
    )

    return jsonify(output), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
