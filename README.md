# 🧠 Student Score Predictor (Capstone Project)

A simple Flask web app that predicts a student's future score based on:

- 📘 Study hours  
- 😴 Sleep hours  
- 🧠 Previous score  

The prediction is powered by a trained **Gradient Boosting** model (`boosting_model.pkl`).

---

## 🚀 How to Run Locally

1. Clone the repository  
2. Install requirements:  
   `pip install -r requirements.txt`  
3. Run the app:  
   `python app.py`  
4. Open browser at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💡 Sample Inputs

| Study Hours | Sleep Hours | Previous Score | Output  |
|-------------|-------------|----------------|---------|
| 60          | 6           | 80             | 87.67   |

---

## 🖥️ How It Works

1. User enters values in the form  
2. Data is sent to the ML model  
3. Model returns a prediction  
4. Result is displayed with basic styling

---

## 🧪 Input Validation & Error Handling

- Ensures only numeric input is accepted  
- Graceful error messages if input is missing/invalid

---

## 🖼️ Screenshots

### Before Styling  
![Before Screenshot](screenshot_before.png)

### After Styling  
![After Screenshot](screenshot.png)

---

## 📁 Project Structure

```
student_score_app/
├── model/
│   └── boosting_model.pkl
├── templates/
│   └── index.html
├── static/ (optional for CSS)
├── app.py
├── README.md
├── LICENSE
├── requirements.txt
```

---

## 📜 License

This project is licensed under the MIT License.  
Feel free to use, modify, and share with attribution.

