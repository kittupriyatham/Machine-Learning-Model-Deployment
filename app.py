from flask import Flask,render_template,request
from MachineLearningCode import MachineLearningCode

app = Flask(__name__)

MLC=MachineLearningCode()
@app.route('/')
def hello_world():
    MLC.train()
    return render_template("index.html",Predicted_flower_name="Predicted flower name", Accuracy_of_prediction="Accuracy of prediction")
@app.route('/',methods=['POST'])
def predictandoutput():
    sl=request.form["slengthin"]
    sw=request.form["swidthin"]
    pl=request.form["plengthin"]
    pw=request.form["pwidthin"]
    Result=MLC.predict(sl,sw,pl,pw)
    return render_template("index.html",Predicted_flower_name=Result[0][0],Accuracy_of_prediction=Result[1])
# <<<<<<< HEAD

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

# =======
# >>>>>>> 43265125815ec693d752ffe1c262f76aa06c1f34
if __name__ == '__main__':
    app.run(debug=True)
