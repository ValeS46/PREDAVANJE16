import os
from sqla_wrapper import SQLAlchemy

#get envoriment value
#sqlite/// kjer se bodo podatki shranjevali lokalno
db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///podatkova-baza.sqlite"))