from flask import Flask, render_template, request
from MachineLearningCode import MachineLearningCode

# apps initializations
app = Flask(__name__)
print("Flask app initialized")
MLC = MachineLearningCode()


# routes definitions

@app.route('/')
@app.route('/home')
def hello_world():
    print("Hello World!")
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predictandoutput():
    print("Inside predictandoutput function")
    MLC.train()
    sl = request.form["slengthin"]
    sw = request.form["swidthin"]
    pl = request.form["plengthin"]
    pw = request.form["pwidthin"]
    print(sl, sw, pl, pw, type(eval(sl)), type(eval(sw)), type(eval(pl)), type(eval(pw)))
    sl, sw, pl, pw = eval(sl), eval(sw), eval(pl), eval(pw)
    result = MLC.predict(sl, sw, pl, pw)
    print(result)
    return render_template("result.html", Predicted_flower_name=result[0][0], Accuracy_of_prediction=result[1])


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/about')
def about():
    return render_template("about.html")


# app run

if __name__ == '__main__':
    app.run(debug=True, port=5001)
