# CV-Plant-Seedling-Classification 🌿🌾
```🏥Recognize, identify, and classify plant images using CNN and image recognition algorithms. The goal of the project is to create a classifier capable of determining a plant's species from a photo.```

## Classes 🌱
- Black-grass
- Charlock
- Cleavers
- Common Chickweed
- Common wheat
- Fat Hen
- Loose Silky-bent
- Maize
- Scentless Mayweed
- Shepherd’s Purse
- Small-flowered Cranesbill
- Sugar beet

## Dataset 📊
Cropped Plants V2

[Dataset Link](https://vision.eng.au.dk/plant-seedlings-dataset/#:~:text=The%20Plant%20Seedlings%20Dataset%20contains,roughly%2010%20pixels%20per%20mm.)

### Sample Data
![Sample Data](https://github.com/yashfirkedata/CV-Plant-Seedling-Classification/blob/2876fc20d56b56876332f0444238369c47b81a93/model_images/sample_data.png)

# Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/yashfirkedata/CV-Plant-Seedling-Classification.git
cd CV-Plant-Seedling-Classification
```

### Step 2: Download the Model
Download the model file from `Model/model.txt` and place it in the `Model/` directory.

### Step 3: Create a Virtual Environment

#### For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### For Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Requirements
```bash
pip install -r requirements.txt
```

### Step 5: Run the Streamlit App
```bash
streamlit run app.py
```

# Tasks Performed ✔️
1. Data Exploration
2. Model 1: Baseline (mini VGG like structure)
3. Model 2: Tuning Baseline Addressing Overfitting
4. Model 3: Data Augmentation
5. Model 4: Creating Synthetic Data
6. Extensive Model Testing and Visualizing predictions

# Main Model 🧠
### Model Architecture
![Model Architecture](https://github.com/yashfirkedata/CV-Plant-Seedling-Classification/blob/c55656869b69ffb5f0d45a5fbbe83f5a7192ba37/model_images/model_summary.png)

### Model Loss and Accuracy
![Model Loss and Accuracy](https://github.com/yashfirkedata/CV-Plant-Seedling-Classification/blob/2876fc20d56b56876332f0444238369c47b81a93/model_images/Acc%20and%20loss.png)

### Confusion Matrix
![Confusion Matrix](https://github.com/yashfirkedata/CV-Plant-Seedling-Classification/blob/2876fc20d56b56876332f0444238369c47b81a93/model_images/confusion_matrix.png)

### Classification Report
![Classification Report](https://github.com/yashfirkedata/CV-Plant-Seedling-Classification/blob/2876fc20d56b56876332f0444238369c47b81a93/model_images/Classification%20report.png)

### Predictions
![Predictions](https://github.com/yashfirkedata/CV-Plant-Seedling-Classification/blob/2876fc20d56b56876332f0444238369c47b81a93/model_images/predictions.png)

# Web Application 🌐

### App Interface

![Web App Image 2](https://github.com/yashfirkedata/CV-Plant-Seedling-Classification/blob/2876fc20d56b56876332f0444238369c47b81a93/web_app_images/img2.jpg)
![Web App Image 1](https://github.com/yashfirkedata/CV-Plant-Seedling-Classification/blob/2876fc20d56b56876332f0444238369c47b81a93/web_app_images/img1.jpg)
![Web App Image 3](https://github.com/yashfirkedata/CV-Plant-Seedling-Classification/blob/2876fc20d56b56876332f0444238369c47b81a93/web_app_images/img3.jpg)


# Suggestions and Feedback Appreciated 🙏

If you have any suggestions or feedback regarding this project, please feel free to share them with us. Your input is valuable and helps us improve our work. Thank you for your support!


