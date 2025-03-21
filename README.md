﻿# SITnovate Project
 # 🔎 Spam Email Classifier using Flask, Firebase, and Machine Learning

This project is an AI-based web application designed to classify emails as **Spam** or **Not Spam**. It uses **Flask** for the backend API, **Firebase Firestore** for storing classification data, and a **Machine Learning model** trained on natural language processing techniques (like TF-IDF and Naive Bayes).

---

## 📊 Features
- ✨ Classifies emails as **Spam** or **Not Spam** using a trained ML model.
- 🔒 Stores classified email data in **Firebase Firestore**.
- 🔄 Provides an API endpoint for predictions.
- 📚 Built with **Flask** and **Firebase Admin SDK**.
- 🔧 Cross-Origin Resource Sharing (CORS) enabled for smooth frontend-backend integration.

---

## 🎓 Tech Stack
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn (Naive Bayes, TF-IDF Vectorizer)
- **Database**: Firebase Firestore
- **Deployment**: Render (or any platform supporting Flask)

---

## 🎓 Prerequisites
- Python >= 3.8
- Firebase Project with Firestore enabled
- Render (or any deployment platform)

---

## 📚 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate    # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Prepare Firebase Credentials
- Download the **`serviceAccountKey.json`** from Firebase Console.
- Convert it to base64:
```bash
base64 serviceAccountKey.json
```
- Create a `.env` file in the backend folder:
```env
FIREBASE_CRED_JSON=PASTE_YOUR_BASE64_STRING_HERE
```

### 5. Run the Application Locally
```bash
python backend/app.py
```

The Flask server should start on `http://127.0.0.1:5000/`

---

## 🔠 API Endpoints

### 1. Test API
**URL**: `/`
**Method**: `GET`

```json
{
  "message": "Spam Email Classifier API is running!"
}
```

### 2. Classify an Email
**URL**: `/predict`
**Method**: `POST`

**Request Body:**
```json
{
  "email": "Congratulations! You've won a free lottery."
}
```

**Response:**
```json
{
  "prediction": "Spam",
  "spam_probability": 0.89
}
```

### 3. Retrieve All Stored Emails
**URL**: `/get_emails`
**Method**: `GET`

**Response:**
```json
{
  "emails": [
    {
      "email_text": "Congratulations! You've won a free lottery.",
      "prediction": "Spam",
      "spam_probability": 0.89
    }
  ]
}
```

---

## 🌐 Deployment (Render)
1. Upload your project to a GitHub repository.
2. Create a **Web Service** on Render and connect the repo.
3. Set the following environment variables on Render:
   - `FIREBASE_CRED_JSON` = _(Base64 encoded string)_
4. Set the **Start Command** to:
```bash
gunicorn backend.app:app
```
5. Deploy and access your API via the provided Render URL.

---

## 🌀 Project Structure
```
├── backend
│   ├── app.py                # Flask Application
│   ├── .env                  # Environment Variables
│   ├── requirements.txt      # Python Dependencies
├── model
│   ├── spam_model.pkl        # Trained ML Model
│   └── vectorizer.pkl        # TF-IDF Vectorizer
├── frontend
│   ├── index.html            # Frontend HTML File
│   ├── styles.css            # CSS Styles
│   └── script.js             # Frontend Logic
└── README.md                 # Project Documentation
```

---

## 🚨 Troubleshooting
- **Firebase Credentials Error**:
   - Ensure the base64 string in `.env` is correct.
   - Verify the environment variable `FIREBASE_CRED_JSON` is set in Render.
- **Model Not Found**:
   - Verify `spam_model.pkl` and `vectorizer.pkl` are correctly placed in the `/model` directory.
- **CORS Error**:
   - Ensure CORS is enabled in Flask using:
     ```python
     from flask_cors import CORS
     CORS(app)
     ```

---

## 🌟 Contributions
Feel free to fork this repo and contribute by submitting a pull request.

---

## 📢 License
This project is open-source and available under the [MIT License](LICENSE).

---

## 🚀 Acknowledgments
- [Firebase](https://firebase.google.com/)
- [Render](https://render.com/)
- [Scikit-learn](https://scikit-learn.org/)

---

> ✨ **Made with Python, Flask, and Firebase**


