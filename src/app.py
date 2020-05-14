# app.py
# Backend to server using Flask

from flask import Flask, render_template, request, json, send_from_directory
from character import Character, parse_input
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
    # Create a character
    _name = request.form['selectName']
    PC = Character(_name)
    _class = parse_input(request.form['selectClass'])
    _race = parse_input(request.form['selectRace'])
    _bkground = parse_input(request.form['selectBackground'])
    # Generate PC stats
    PC.generate(_class,_race,_bkground)
    returnDict = PC.output()
    print("Sending Character: ", returnDict)

    # Post character info
    return render_template("results.html", character=returnDict)

# Display Character PDF
# TODO: Fill in PDF
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