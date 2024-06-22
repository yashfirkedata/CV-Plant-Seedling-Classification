import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import smart_resize
from PIL import Image
from numpy import expand_dims, argmax

# Define colors
primaryColor = "#3366FF"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F0F0"
textColor = "#333333"

# Load the trained model
MODEL_PATH = 'Model/model-00092-0.16305-0.07721-.h5'  # Update with your model path
model = load_model(MODEL_PATH)

# Class labels for plant seedlings
class_labels = ['Black-grass', 'Charlock', 'Cleavers', 'Common Chickweed', 'Common wheat', 
                'Fat Hen', 'Loose Silky-bent', 'Maize', 'Scentless Mayweed', 'Shepherd’s Purse', 
                'Small-flowered Cranesbill', 'Sugar beet']

# Streamlit layout and styling
st.set_page_config(page_title="Plant Seedlings Classification", page_icon=":herb:")
st.title("Plant Seedlings Classification")

# Upload file and make predictions
file = st.file_uploader("Please upload an image file (JPEG/PNG)", type=["jpg", "png"])

if file is not None:
    # Display uploaded image
    img = Image.open(file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image
    image_data = image.img_to_array(img)
    image_data = smart_resize(image_data, (120, 120), interpolation='bilinear')
    
    # Make prediction
    prediction = model.predict(expand_dims(image_data, axis=0))
    predicted_class_index = argmax(prediction)
    predicted_class_label = class_labels[predicted_class_index]

    # Display prediction
    st.write("")
    st.subheader("Prediction:")
    st.write(f"Class label: **{predicted_class_label}**")
    st.write(f"Confidence: {prediction[0][predicted_class_index]:.2%}")

# Footer and styling
st.markdown(
    """
    <style>
    .st-bq {
        background-color: #f0f0f0;
        padding: 10px;
        border-radius: 5px;
        margin-top: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .st-bq a {
        color: #3366FF;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="st-bq">
        <p style="color: #333333;">Created with ❤️ by Yash Vijay Firke</p>
        <p style="color: #333333;">Check out the code on <a href="https://github.com/yashfirkedata/CV-Plant-Seedling-Classification" style="color: #3366FF;">GitHub</a></p>
    </div>
    """,
    unsafe_allow_html=True,
)
