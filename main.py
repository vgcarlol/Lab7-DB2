import pandas as pd
import pymongo
from sqlalchemy import create_engine

# SQL
engine = create_engine("postgresql://postgres:1234@localhost:5432/demografia_mundial")
df_poblacion = pd.read_sql("SELECT * FROM pais_poblacion", engine)

# MongoDB
cliente = pymongo.MongoClient("mongodb+srv://221164:123456abc@cluster0.xkjndsz.mongodb.net/")
db = cliente["turismo_mundial"]
coleccion = db["costos_turisticos"]
data_turismo = list(coleccion.find())
df_turismo = pd.DataFrame(data_turismo)
