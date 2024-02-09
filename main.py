from flask import Flask, render_template, request, redirect, url_for
from __init__ import Krontos
from os import remove

app = Flask(__name__)
instance0 = Krontos()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        inputFile = request.files['file']
        inputFile.save(f"inputFiles/{inputFile.filename}")
        
        instance0.getDataset(f"inputFiles/{inputFile.filename}")
        instance0.createTable()
        instance0.updateTable()
        
        remove(f"inputFiles/{inputFile.filename}")
        return redirect(url_for("status"))

    return render_template("index.html")

@app.route("/stat", methods=["GET", "POST"])
def status():
    if request.method == "POST":
        merchant = request.form["merchant"]
        pincode = request.form["pincode"]

        stat = [None, None, merchant, pincode] #existance, availability
        try:
            stat[0] = 1
            stat[1] = instance0.pincodeStat(merchant, int(pincode))
        
        except ValueError:
            stat[0] = 0

        print(stat)
        return render_template("status.html", status=stat)

    return render_template("status.html")

if __name__ == "__main__":
    app.run(debug=True)
