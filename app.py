from flask import Flask, render_template, request
from MachineLearningCode import MachineLearningCode

# apps initializations
app = Flask(__name__)

MLC = MachineLearningCode()


# routes definitions

@app.route('/')
@app.route('/home')
def hello_world():
    MLC.train()
    return render_template("index.html", Predicted_flower_name="Predicted flower name",
                           Accuracy_of_prediction="Accuracy of prediction")


@app.route('/predict', methods=['POST'])
def predictandoutput():
    sl = request.form["slengthin"]
    sw = request.form["swidthin"]
    pl = request.form["plengthin"]
    pw = request.form["pwidthin"]
    Result = MLC.predict(sl, sw, pl, pw)
    return render_template("index.html", Predicted_flower_name=Result[0][0], Accuracy_of_prediction=Result[1])


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/about')
def about():
    return render_template("about.html")


# app run

if __name__ == '__main__':
    app.run(debug=True, port=5001)
