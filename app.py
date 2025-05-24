from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model/boosting_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    inputs = [float(request.form[k]) for k in request.form]
    prediction = model.predict([inputs])
    return render_template('index.html', result=round(prediction[0], 2))

if __name__ == '__main__':
    app.run(debug=True)
