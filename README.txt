E-commerce Data Pipeline (API → Python → BigQuery → Looker Studio)

Overview
This project implements an end-to-end data pipeline that:

- Extracts real product data from a public e-commerce API
- Cleans and transforms the dataset using Python and Pandas
- Loads the processed data into BigQuery
- Visualizes business metrics through a Looker Studio dashboard

The project simulates the workflow used by modern Data Engineering and Analytics Engineering teams.

Pipeline Architecture
The pipeline follows a simple and scalable architecture:
https://raw.githubusercontent.com/astonmartin32/ecommerce-data-pipeline/main/dashboard/architecture.png


E-commerce API
        ↓
extract.py
        ↓
products_raw.json
        ↓
transform.py
        ↓
products_clean.csv
        ↓
load_bigquery.py
        ↓
BigQuery dataset: ecommerce.products
        ↓
Looker Studio Dashboard

Features

Data Extraction
- Automated request to a public API
- Extracts product-level details such as:
  price, brand, category, rating, stock, description, thumbnails

Data Transformation
- Cleaning missing or inconsistent values
- Filtering required fields
- Creating engineered columns:
  estimated_revenue = price * stock
  extracted_at timestamp
- Export to CSV for downstream processing

Data Loading (BigQuery)
- Uses BigQuery Python Client
- Automatically detects schema
- Overwrites table on each load using WRITE_TRUNCATE
- Final table stored at:
  ecommerce.products

Looker Studio Dashboard
Includes:
- Total product count
- Average price
- Average rating
- Total estimated revenue
- Revenue by brand
- Revenue by category
- Top 10 most expensive products
- Clean and minimal layout suitable for analytics

Project Structure

ecommerce-data-pipeline/
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load_bigquery.py
│
├── data/
│   ├── products_raw.json
│   ├── products_clean.csv
│
├── dashboard/
│   ├── looker_screenshots/
│
├── .gitignore
└── README.md

Technologies Used
- Python
- Pandas
- BigQuery
- Google Cloud IAM
- Looker Studio
- REST API Integration
- Git and GitHub

How to Run
Recommended setup:

pip install -r requirements.txt
python scripts/extract.py
python scripts/transform.py
python scripts/load_bigquery.py
