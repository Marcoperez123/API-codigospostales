from flask import Flask, jsonify
import pandas as pd

# Cargar el archivo Excel
file_catalogo_colonia = "Copia de CatalogoColonia.xlsx"
df_catalogo = pd.read_excel(file_catalogo_colonia, sheet_name='Copia_de_CatalogoColonia')

# Normalizar datos
df_catalogo['SECCION'] = df_catalogo['SECCION'].astype(str).str.strip()
df_catalogo['CP'] = df_catalogo['CP'].astype(str).str.strip()

# Crear la aplicación Flask
app = Flask(__name__)

# Función para buscar por sección electoral
def buscar_por_seccion(df, seccion):
    seccion = str(seccion).strip()
    resultado = df[df['SECCION'] == seccion][['CP', 'NOMBRE', 'MUNICIPIO_NOMBRE', 'ENTIDAD', 'DISTRITO']]
    if resultado.empty:
        return {"error": f"Sección electoral '{seccion}' no encontrada."}
    return resultado.to_dict(orient='records')

# Función para buscar por código postal
def buscar_por_cp(df, cp):
    cp = str(cp).strip()
    resultado = df[df['CP'] == cp][['SECCION', 'NOMBRE', 'MUNICIPIO_NOMBRE', 'ENTIDAD', 'DISTRITO']]
    if resultado.empty:
        return {"error": f"Código postal '{cp}' no encontrado."}
    return resultado.to_dict(orient='records')

# Endpoint para buscar por sección electoral
@app.route('/seccion/<seccion>', methods=['GET'])
def api_seccion(seccion):
    return jsonify(buscar_por_seccion(df_catalogo, seccion))

# Endpoint para buscar por código postal
@app.route('/cp/<cp>', methods=['GET'])
def api_cp(cp):
    return jsonify(buscar_por_cp(df_catalogo, cp))

# Ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)
