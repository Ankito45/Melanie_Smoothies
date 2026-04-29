# Melanie’s Smoothie Shop: Snowflake Data Warehousing (DABW) Implementation

This repository contains the technical implementation of **Melanie’s Smoothie Shop**, a hands-on project completed as part of the **Snowflake Hands-on Essentials: Data Warehousing (DABW)** certification workshop.

## 🎯 Project Objective
To build and manage a cloud data warehouse for a fictional smoothie business. This project demonstrates the ability to architect data pipelines in Snowflake, moving from raw data ingestion to structured, queryable analytical layers.

## 🏗️ Technical Workflow

### 1. Environment Configuration
Established a dedicated hierarchy including the `SMOOTHIES` database and specific schemas to ensure data isolation and organized object management.

### 2. Data Ingestion & Staging
* **Stages:** Created and managed stages to point to fruit ingredient data files.
* **File Formats:** Defined custom `FILE FORMAT` objects to handle various data delimiters, header skipping, and error handling.
* **Loading:** Executed bulk data loads using the `COPY INTO` command, ensuring high-performance ingestion.

### 3. Handling Semi-Structured Data
A key component involved processing nutritional facts stored in **JSON** format.
* Utilized the `VARIANT` data type to store raw JSON.
* Applied **Colon Notation** (e.g., `data:calories`) to extract nested values.
* Demonstrated data flattening techniques to transform JSON into relational tables.

### 4. Data Modeling & Reliability
* **Sequences:** Implemented automatic primary key generation for the `FRUIT_STOCK` table.
* **Views:** Built user-facing views to simplify the join logic between inventory data and nutritional facts.

## 📁 Repository Structure
```text
├── py_scripts/
├── streamlit_app.py        # Main config file   
├── README.md               # Project documentation
└── .gitignore              # requiremenst file for the app.py to run
