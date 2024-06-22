import sys
import subprocess
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'streamlit', 'pillow', 'numpy', 'tensorflow'])
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import smart_resize
from PIL import Image
from numpy import expand_dims
from numpy import argmax
from tensorflow.nn import softmax

primaryColor = "#0000FF" 
backgroundColor = "#FFFFFF" 
secondaryBackgroundColor = "#FFFFFF" 
textColor = "#000000"

MODEL_PATH = 'model-00092-0.16305-0.07721-.h5'  # Update with your model path
model = load_model(MODEL_PATH)

class_labels = ['Black-grass', 'Charlock', 'Cleavers', 'Common Chickweed', 'Common wheat', 'Fat Hen', 'Loose Silky-bent', 'Maize', 'Scentless Mayweed', 'Shepherd’s Purse', 'Small-flowered Cranesbill', 'Sugar beet']

st.write("""
         # Plant Seedlings Classification
         """
         )

file = st.file_uploader("Please upload an image file", type=["jpg", "png"])

def import_and_predict(image_data, model):
    
    x = expand_dims(image_data, axis=0) 
    predictions = model.predict(x)
    predicted_class_index = argmax(predictions)
    predicted_class_label = class_labels[predicted_class_index]
        
    return predicted_class_label

if file is None:
    st.text("Please upload an image file")
else:
    img = Image.open(file)
    st.image(img, use_column_width=False)
    image_data = image.img_to_array(img)
    image_data = smart_resize(image_data, (120, 120), interpolation='bilinear')
        
    prediction = import_and_predict(image_data, model)

    st.text("\n\nPrediction:")
    st.write(prediction)
