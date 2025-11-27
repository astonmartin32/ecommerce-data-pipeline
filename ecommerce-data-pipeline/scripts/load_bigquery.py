

import os
import pandas as pd
from google.cloud import bigquery

# Ruta ABSOLUTA al credentials.json
CREDS_PATH = r"C:\Users\gilbe\OneDrive\Desktop\ecommerce-data-pipeline\credentials.json"

print("Usando credenciales en:", CREDS_PATH)
print("Existe el archivo?", os.path.exists(CREDS_PATH))

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDS_PATH

# Detectar carpeta raíz
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")



def load_to_bigquery():
    # Cliente de BigQuery
    client = bigquery.Client()

    # ⚠️ Cambia YOUR_PROJECT_ID por tu project ID real
    table_id = "data-pipeline-project-479414.ecommerce.products"


    # Leer el CSV limpio
    csv_path = os.path.join(DATA_DIR, "products_clean.csv")
    print("Leyendo datos desde:", csv_path)
    df = pd.read_csv(csv_path)

    # Config del job: autodetecta esquema y sobreescribe tabla
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",
        autodetect=True
    )

    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()

    table = client.get_table(table_id)
    print(f"✔ Carga completada. Filas: {table.num_rows}, Columnas: {len(table.schema)}")

if __name__ == "__main__":
    load_to_bigquery()
