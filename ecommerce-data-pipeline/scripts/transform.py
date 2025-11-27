import os
import pandas as pd

# Detectar carpeta raíz y data
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def transform_products():
    """
    Lee el CSV crudo, limpia columnas y crea KPIs.
    """
    raw_path = os.path.join(DATA_DIR, "products_raw.csv")
    df = pd.read_csv(raw_path)

    # Columnas importantes
    df = df[[
        "id", "title", "description", "price", "discountPercentage",
        "rating", "stock", "brand", "category", "thumbnail", "extracted_at"
    ]]

    # KPI simple: revenue estimado
    df["estimated_revenue"] = df["price"] * df["stock"]

    return df

if __name__ == "__main__":
    df = transform_products()
    clean_path = os.path.join(DATA_DIR, "products_clean.csv")
    df.to_csv(clean_path, index=False)
    print("✔ Transformación completa →", clean_path)
