from fastapi import FastAPI
import pandas as pd

# Cargar datos desde el archivo CSV
df = pd.read_csv("modified_codigos_postales.csv")

# Inicializar FastAPI
app = FastAPI()

@app.get("/colonias/{codigo_postal}")
def obtener_colonias(codigo_postal: int):
    # Filtrar datos por código postal
    colonias = df[df["d_codigo"] == codigo_postal]
    
    if colonias.empty:
        return {"mensaje": "Código postal no encontrado"}
    
    # Convertir resultados a lista de diccionarios
    resultado = colonias[["d_asenta", "d_tipo_asenta", "d_mnpio", "d_estado", "d_zona"]].to_dict(orient="records")
    return {"codigo_postal": codigo_postal, "colonias": resultado}

# Para ejecutar la API:
# uvicorn geonames_api:app --reload
