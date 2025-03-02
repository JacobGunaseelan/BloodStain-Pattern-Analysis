from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
import cv2
import os

app = Flask(__name__)  # Fixed typo
model = tf.keras.models.load_model("./models/bloodstain_model.keras")

# Define bloodstain classifications
bloodstain_classes = {
    "Drop": {"Weapon": "Sharp object/stabbing", "Impact": "Ground", "Movement": "Likely stationary"},
    "Flow": {"Weapon": "Blunt force", "Impact": "Torso/Head", "Movement": "Victim moved after injury"},
    "Swipe": {"Weapon": "Blunt force", "Impact": "Wall/Surface", "Movement": "Movement after impact"},
    "Pool": {"Weapon": "Heavy trauma", "Impact": "Ground", "Movement": "Stationary after impact"},
    "Pattern": {"Weapon": "Gunshot", "Impact": "Torso/Head", "Movement": "Likely stationary"},
    "HighSpatter": {"Weapon": "Gunshot", "Impact": "Wall/Surface", "Movement": "Minimal"},
    "LowSpatter": {"Weapon": "Blunt force", "Impact": "Ground", "Movement": "Limited movement"},
    "MediumSpatter": {"Weapon": "Blunt force", "Impact": "Torso/Head", "Movement": "Likely moved"}
}

# Function to preprocess image for model prediction
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))  # Resize to match model input
    image = image / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["file"]
    filename = file.filename
    filepath = os.path.join("static", filename)
    file.save(filepath)

    # Preprocess the image and predict
    image = preprocess_image(filepath)
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction)

    # Get corresponding bloodstain type
    class_labels = list(bloodstain_classes.keys())
    predicted_label = class_labels[predicted_class]
    result = bloodstain_classes[predicted_label]
    result["Bloodstain Type"] = predicted_label

    return render_template("index.html", result=result, image_path=filepath)

if __name__ == "__main__":  # Fixed typo
    app.run(debug=True)
