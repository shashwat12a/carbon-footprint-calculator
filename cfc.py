from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('./index.html', emissions=0)

@app.post("/calculate")
def calculate():
    if request.form["electricity"] != '':
        electricity = float(request.form["electricity"])
    else:
        electricity = 0.0
    if request.form["lpg"] != '':
        lpg = float(request.form["lpg"])
    else:
        lpg = 0.0
    if request.form["coal"] != '':
        coal = float(request.form["coal"])
    else:
        coal = 0.0
    if request.form["petrol"] != '':
        petrol = float(request.form["petrol"])
    else:
        petrol = 0.0
    if request.form["cng"] != '':
        cng = float(request.form["cng"])
    else:
        cng = 0.0
    if request.form["diesel"] != '':
        diesel = float(request.form["diesel"])
    else:
        diesel = 0.0

    emissions = (lpg*1.51*33) + (coal*2.42) + (electricity*0.82) + (petrol*2.3) + (diesel*2.7) + (cng*2.6)
    print(emissions)
    return render_template('./index.html', emissions=round(emissions))

@app.route("/about")
def about():
    return render_template("./about.html")

@app.route("/credits")
def credits():
    return render_template("./credits.html")

@app.route("/vehicle")
def vehicle():
    return render_template("./vehicle.html")

@app.post("/v-calculate")
def vcalculate():
    if request.form["type"] != "":
        type = int(request.form["type"])
    else:
        type = 0
    if request.form["kms"] != "":
        kms = int(request.form["kms"])
    else:
        kms = 0
    if type == 0:
        val = 0
    elif type == 1:
        val = 0.0334
    elif type == 2:
        val == 0.0351
    elif type == 3:
        val = 0.325
    elif type == 4:
        val = 0.1135
    elif type == 5:
        val = 0.1322
    elif type == 6:
        val = 0.10768
    elif type == 7:
        val = 0.103
    elif type == 8:
        val = 0.063
    elif type == 9:
        val = 0.138
    elif type == 10:
        val = 0.130
    elif type == 11:
        val = 0.117
    elif type == 12:
        val = 0.142
    elif type == 13:
        val = 0.131
    elif type == 14:
        val = 0.153
    elif type == 15:
        val = 0.189
    elif type == 16:
        val = 0.197
    elif type == 17:
        val = 0.203
    elif type == 18:
        val = 0.267
    elif type == 19:
        val = 0.230
    
    emissions = round(val * kms)
    if emissions < 1:
        emissions = val * kms
    return render_template("./vehicle.html", emissions=emissions)