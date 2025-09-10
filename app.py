from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bmi", methods=["POST"])
def bmi():
    weight = float(request.form["weight"])
    height = float(request.form["height"])
    bmi = round(weight / (height * height), 2)

    # Classify BMI result
    if bmi < 18.5:
        category = "Underweight 😕"
        color = "info"
    elif 18.5 <= bmi < 24.9:
        category = "Normal ✅"
        color = "success"
    elif 25 <= bmi < 29.9:
        category = "Overweight ⚠️"
        color = "warning"
    else:
        category = "Obese ❌"
        color = "danger"

    return render_template("result.html", bmi=bmi, category=category, color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

