import os
from sqla_wrapper import SQLAlchemy

#get envoriment value
#sqlite/// kjer se bodo podatki shranjevali lokalno
#os.getenv
db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///podatkova-baza.sqlite"))

#gre za podatkovne baze in je treba eksplicitno nastaviti tip polja
#primary key nastavimo samo tistemu ki je ključ
class Komentar (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    avtor = db.Column(db.String)
    vsebina = db.Column(db.String)