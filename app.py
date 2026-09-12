from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("diabetes_model.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    age = float(request.form["age"])
    blood_pressure = float(request.form["blood_pressure"])
    blood_sugar = float(request.form["blood_sugar"])
    bmi = float(request.form["bmi"])

    # Same order used while training
    features = [[
        age,
        blood_pressure,
        blood_sugar,
        bmi
    ]]

    prediction = model.predict(features)

    result = prediction[0]

    return render_template(
        "index.html",
        prediction="Diabetes: " + result
    )


if __name__ == "__main__":
    app.run(debug=True)