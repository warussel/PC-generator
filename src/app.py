# app.py
# Backend to server using Flask

from flask import Flask, render_template, request, json, send_from_directory
from character import Character
app = Flask(__name__)

# Home page to fill in character info
@app.route("/")
@app.route("/home")
def home() :
    print("Render home page")
    return render_template("home.html")

# Info about the application
@app.route("/about")
def about() :
    print("Render About page")
    return render_template("about.html")

# Results page, generate a character
@app.route("/generate", methods=['POST'])
def generate() :
    print("Received Character: ")
    _name = request.form['selectName']
    PC = Character(_name)
    PC.generate()
    returnDict = vars(PC)
    print("Sending Character: ", vars(PC))
    _class = request.form['selectClass']
    _race = request.form['selectRace']
    _bkground = request.form['selectBackground']

    return render_template("results.html", character=returnDict)

@app.route("/print")
def servePDF() :
    print("Printing PDF")
    filename = f"CharacterSheet.pdf"

    return render_template("print.html")
#    try:
#        return send_from_directory("./static",filename=filename)
#    except Exception as e :
#        return str(e)

if __name__ == "__main__" :
    app.run(debug=True) #TODO: set debug to false for deployment