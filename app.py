from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and encoders
model, le_device, le_ref = pickle.load(open("model.pkl", "rb"))

@app.route('/', methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        time_on_site = float(request.form['time_on_site'])
        page_views = int(request.form['page_views'])
        bounce_rate = float(request.form['bounce_rate'])
        device = le_device.transform([request.form['device']])[0]
        referral = le_ref.transform([request.form['referral']])[0]

        features = np.array([[time_on_site, page_views, bounce_rate, device, referral]])
        prediction = model.predict(features)[0]
    return render_template("index.html", prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
