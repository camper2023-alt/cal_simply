from flask import Flask, render_template, request
app = Flask(__name__)
import math

@app.route("/")
def damage_quickly(at=100,dif=100,po=100):
    x = math.floor(22 * at * po / dif)
    y = math.floor(x / 50 + 2)
    damage = [math.floor(y * (0.85 + (i / 100))) for i in range(16)]
    return render_template("cal_simply.html", damage = damage)

@app.route("/result", methods=["POST"])
def result():
    if request.form["at"] == "":
        at = 100
    else:
        at = int(request.form["at"])
    if request.form["dif"] == "":
        dif = 100
    else:
        dif = int(request.form["dif"])
    if request.form["po"] == "":
        po = 100
    else:
        po = int(request.form["po"])
    x = math.floor(22 * at * po / dif)
    y = math.floor(x / 50 + 2)
    damage = [math.floor(y * (0.85 + (i / 100))) for i in range(16)]
    return render_template("result.html", damage = damage, at=at, dif=dif, po=po)