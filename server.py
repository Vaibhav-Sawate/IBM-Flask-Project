"""
This module implements an API for detecting emotions from a given text using Flask.
It has two endpoints: 
1. A home endpoint ('/') which returns a welcome message.
2. An '/emotionDetector' endpoint to analyze emotions in a text via a POST request.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Home route to welcome users to the Emotion Detection API.
    """
    return "Welcome to the Emotion Detection API! Use /emotionDetector"

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Route to detect emotions from a given text.
    Accepts a JSON body with a 'text' field.
    Returns a JSON response with emotion scores or an error message if the input is invalid.
    """
    # Get the text to analyze from the JSON request body
    text_to_analyze = request.json.get('text', '').strip()

    # Call the emotion detector function and get the response
    response = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None
    if response['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400

    # Prepare the output format
    output = {
        "anger": response['anger'],
        "disgust": response['disgust'],
        "fear": response['fear'],
        "joy": response['joy'],
        "sadness": response['sadness'],
        "dominant_emotion": response['dominant_emotion']
    }

    # Return the JSON output
    return jsonify(output), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
