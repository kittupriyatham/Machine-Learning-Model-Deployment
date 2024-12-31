"""
docstring
"""

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
    """
    docstring
    """
    # print("Hello World!")
    return render_template("home.html")


@app.route('/predict', methods=['GET','POST'])
def predictandoutput():
    """
    docstring
    """
    print("Inside predictandoutput function")
    MLC.train()
    sepal_length = request.form["slengthin"]
    sepal_width = request.form["swidthin"]
    petal_length = request.form["plengthin"]
    petal_width = request.form["pwidthin"]
    sepal_length, sepal_width, petal_length, petal_width = ( float(sepal_length),
    float(sepal_width), float(petal_length), float(petal_width))
    result = MLC.predict(sepal_length, sepal_width, petal_length, petal_width)
    return render_template("result.html", Predicted_flower_name=result[0][0],
                           Accuracy_of_prediction=int(result[1]*100))


@app.route('/dashboard')
def dashboard():
    """
    docstring
    """
    return render_template("dashboard.html")


@app.route('/about')
def about():
    """
    docstring
    """
    return render_template("about.html")

@app.route('/prediction')
def prediction():
    """
    docstring
    """
    return render_template("index.html")


# app run

if __name__ == '__main__':
    app.run(debug=True)