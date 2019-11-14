import random
#import knjiznice 2 nacina
#request lahko uporabljamo samo za POST methodo
from flask import Flask, render_template, request, redirect, make_response
#import komentarja iz druge datoteke...
from modeli import Komentar, db

app = Flask(__name__)
#db.create naredimo da se naredi struktura baze...
db.create_all()

@app.route("/")
def prva_stran():
    ime = request.cookies.get("ime")

    #preberemo vse komentarje
    komentarji = db.query(Komentar).all()

    #dodajanje spremnljivk v html ime=ime z jinjo poklicemo nato znotraj html-ja
    return render_template ("prva_stran.html", ime=ime, komentarji=komentarji)

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
    return render_template ("prikaz_sporocila.html", zadeva=zadeva)

@app.route("/prijava", methods=["POST"])
def prijava ():
    ime = request.form.get("ime")

    odgovor = make_response(redirect("/"))
    odgovor.set_cookie("ime", ime)
    return odgovor

@app.route("/komentar", methods=["POST"])
def poslji_komentar():
    vsebina_komentarja = request.form.get("vsebina")


    #tukaj se bo komentar shranil v podatkovno bazo
    komentar = Komentar (
        avtor=request.cookies.get("ime"),
        vsebina=vsebina_komentarja
    )

    #dodajanje komentarja v bazo
    db.add(komentar)

    #shranjevanje komentarja
    db.commit()

    return redirect("/")

@app.route("/skrito-stevilo")
def skrito_stevilo():
    odgovor = make_response(render_template("skrito_stevilo.html"))

    if not request.cookies.get("SkritoStevilo"):
        stevilo = str(random.randint(1, 20))
        odgovor.set_cookie("SkritoStevilo", stevilo)

    return odgovor

@app.route("/poslji-skrito-stevilo", methods=["POST"])
def poslji_skrito_stevilo():
    skrito_stevilo = request.cookies.get("SkritoStevilo")
    vpisano_stevilo = request.form.get("stevilo")

    if skrito_stevilo == vpisano_stevilo:
        return "PRAVILNO"
    else:
        return "NI PRAVILNO"

if __name__ == '__main__':
    app.run(debug=True)
