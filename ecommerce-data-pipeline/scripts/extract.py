import os
import requests
import pandas as pd
from datetime import datetime

# Detectar carpeta raíz del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Crear carpeta data si no existe
os.makedirs(DATA_DIR, exist_ok=True)

def extract_products():
    """
    Extrae productos de la API DummyJSON y retorna un DataFrame.
    """
    url = "https://dummyjson.com/products?limit=100"
    response = requests.get(url)
    response.raise_for_status()  # lanza error si la API falla
    data = response.json()

    df = pd.DataFrame(data["products"])
    df["extracted_at"] = datetime.now()

    return df

if __name__ == "__main__":
    df = extract_products()
    csv_path = os.path.join(DATA_DIR, "products_raw.csv")
    df.to_csv(csv_path, index=False)
    print("✔ Archivo guardado en:", csv_path)
