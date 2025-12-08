import numpy as np
from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.inception_v3 import preprocess_input

import os

app = Flask(__name__)


model = load_model('model/currency_model.h5')

labels=['INDIA100NEW', 'INDIA100OLD', 'INDIA10NEW', 'INDIA10OLD', 'INDIA20', 'INDIA200', 'INDIA2000', 'INDIA500', 'INDIA50NEW', 'INDIA50OLD']

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    top_5 = None
    img_path=""
    img=None
    try:
        if request.method == "POST" :
            
            img = request.files['image']
            if not img.filename.endswith(('png', 'jpg', 'jpeg')):
                return "Please upload a valid image (PNG, JPG, JPEG).", 400
            
            img_path = os.path.join('static', img.filename)
            img.save(img_path)
            
            img = image.load_img(img_path, target_size=(224, 224)) 
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)
            
           
            preds = model.predict(img_array)
            top_5_preds = np.argsort(preds[0])[-5:][::-1] 
            top_5_probs = np.sort(preds[0])[-5:][::-1]
            
            prediction = labels[top_5_preds[0]] 
            top_5 = [(labels[i], top_5_probs[idx]) for idx, i in enumerate(top_5_preds)]  
            
            return render_template("index.html", prediction=prediction, top_5=top_5)
    except Exception as e:
            
            return f"Error processing the image: {str(e)}", 500
        
    return render_template("index.html", prediction=prediction, top_5=top_5)

if __name__ == "__main__":
    app.run(debug=True)
