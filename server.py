''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']

    # Check if the label is None, indicating an error or invalid input
    if anger is None:
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the sentiment label and score
        output = "For the given statement, the system response is "
        output += f"'anger': {anger}, "
        output += f"'disgust': {disgust}, "
        output += f"'fear': {fear}, "
        output += f"'joy': {joy} and "
        output += f"'sadness': {sadness}. "
        output += f"The dominant emotion is <strong>{dominant}<strong>."
        return output

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)
