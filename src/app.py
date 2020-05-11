# app.py
# Backend to server using Flask

from flask import Flask, render_template, request, json
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home() :
    return render_template("index.html")

@app.route("/generate")
def generate() :

    _name = request.form['selectName']
    _class = request.form['selectClass']
    _race = request.form['selectRace']
    _bkground = request.form['selectBackground']

    return ("Character: " + _name)

if __name__ == "__main__" :
    app.run(debug=True) #TODO: set debug to false for deployment