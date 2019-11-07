#import knjiznice 2 nacina
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def prva_stran():
    return render_template ("prva_stran.html")

@app.route("/kontakt")
def kontakt ():
    emaili = ["super.svizec@gmail.com", "avto.svizec@email.com", "cars.svizec@email.com"]
    return render_template ("kontakt.html", emaili=emaili)

@app.route("/omeni")
def omeni ():
    return render_template ("omeni.html")



if __name__ == '__main__':
    app.run()
