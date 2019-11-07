#import knjiznice 2 nacina
#request lahko uporabljamo samo za POST methodo
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def prva_stran():
    return render_template ("prva_stran.html")

@app.route("/kontakt")
def kontakt ():
    emaili = ["super.svizec@gmail.com", "avto.svizec@email.com", "cars.svizec@email.com"]
    return render_template ("kontakt.html", emaili=emaili)

#dodaj metodo....
@app.route("/poslji-sporocilo", methods=["POST"])
def poslji_sporocilo():
    zadeva = request.form.get("zadeva")
    sporocilo = request.form.get("sporocilo")

    #tukaj bi shranili te spremenljivki v bazo

    print ("Zadeva je: " + zadeva)
    print ("Sporocilo je: " + sporocilo)
    return "Hvala za poslano zadevo: " + zadeva + " " + sporocilo

@app.route("/omeni")
def omeni ():
    return render_template ("omeni.html")

if __name__ == '__main__':
    app.run()
