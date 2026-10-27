# Big Data Analytics with Spark & Databricks: Hive, Spark SQL, MLlib, Streaming & MLflow

This repository collects my hands-on work from **MSBA 6331 — Big Data Analytics** (Carlson, University of Minnesota). It covers the full big data workflow on **Databricks**:
- querying with **Hive** and **Spark SQL** on multi-gigabyte datasets (including **22 million rows** of Wikipedia clickstream data)
- building distributed **Spark MLlib** pipelines
- processing **streaming** IoT data
- tracking experiments with **MLflow**
- wiring a hosted LLM into a **Streamlit chatbot**

The best models reached **AUC 0.831** (Titanic survival) and **AUC 0.904** (census income).

## 🔍 Project Goals

- Learn to store, query and transform data that's too big for a single machine, using Hive, Spark DataFrames and Spark SQL on Unity Catalog.
- Build, tune and evaluate machine learning pipelines that scale, with Spark MLlib.
- Put models and data flows into production with Structured Streaming, MLflow experiment tracking and an LLM-powered app.

## 📄 Files Included

| Folder | Notebook | What it covers |
|---|---|---|
| `01_Databricks_and_Spark_Basics/` | `Lab1-1`, `Lab1-2` | Linux shell and file operations on the Databricks driver |
| | `Lab5-1_Using_Spark` | Spark fundamentals: Unity Catalog volumes, loading CSVs into DataFrames, lineage and `explain()` execution plans, and feature computation |
| `02_Hive/` | `Lab3-1_Hive_Intro` | Creating Hive databases and tables and querying a retail (`dualcore`) dataset |
| | **`HW1_Big_Data_and_Hive`** | Big data architecture (shared-nothing design, managed vs. external tables) and Hive analysis |
| `03_Spark_DataFrames_and_SQL/` | `Lab6-1_Create_DataFrames` | Creating and saving DataFrames from different sources and formats |
| | `Lab6-2_LendingClub_Analysis` | Sampling, cleaning and analyzing LendingClub loan data |
| | **`HW2_Spark_SQL_Yelp`** | Yelp academic dataset (346 MB, ~500K rows) and Wikipedia clickstream data (1.2 GB, 22M rows) |
| `04_Spark_MLlib/` | `Lab8-1_Feature_APIs` | OneHotEncoder, StringIndexer, VectorAssembler and scalers |
| | `Lab8-2_Concrete_Strength_Regression` | Feature pipeline with standardization for a regression target |
| | `Lab8-3_Used_Car_Value_Prediction` | Decision tree classifier inside an ML Pipeline |
| | `Lab8-4_ML_Pipeline` | Bike-share demand: GBTRegressor plus CrossValidator hyperparameter tuning |
| | **`HW3_Spark_MLlib`** | Spark MLlib vs. scikit-learn and H2O comparison; Titanic survival with logistic regression vs. random forest |
| `05_Structured_Streaming/` | `Lab10-2_IoT_Streaming` | Windowed aggregations on streaming IoT events |
| `06_MLflow/` | `Lab13-2_MLflow_Tracking` | Logging parameters, metrics and models to MLflow |
| | **`HW4_MLflow_with_Spark_MLlib`** | Census income prediction: tracking a baseline model vs. a cross-validated one |
| `07_GenAI_Chatbot/` | `chatbot.py` | Streamlit chatbot calling a Databricks-hosted LLM (`.env.example` shows the configuration) |

> The notebooks were developed on Databricks and converted to `.ipynb` from Databricks exports. Results are shown as text outputs, and interactive charts aren't kept. Most data comes from `databricks-datasets` or public sources, so no large data files are stored here.

## 🧪 Methods Used

- **Distributed storage and querying:** Hive DDL and managed vs. external tables on Unity Catalog, Spark SQL joins and aggregations, and a medallion-style raw (bronze) → cleaned table flow.
- **Data engineering with Spark DataFrames:** schema inspection, sampling large datasets, type casting, splitting and joining, and saving managed tables.
- **Machine learning with Spark MLlib:**
  - feature transformers and VectorAssembler inside end-to-end ML Pipelines
  - logistic regression, decision tree, random forest and gradient-boosted tree models
  - **CrossValidator + ParamGridBuilder** hyperparameter tuning
  - evaluation with AUC, accuracy, F1 and RMSE
- **Structured Streaming:** turning batch logic into a streaming job, windowed counts, and writing streams to tables.
- **MLOps:** MLflow experiment tracking, comparing runs and selecting a model, and saving trained pipeline models.
- **GenAI integration:** an OpenAI-compatible client pointed at a Databricks AI Gateway, with Streamlit session state for chat history.

## 📈 Key Findings

- **Titanic survival (HW3):** a tuned **random forest** beat logistic regression, with **AUC 0.831 vs. 0.797**, accuracy **81.9% vs. 73.9%**, and F1 **0.814 vs. 0.737**.
- **Census income (HW4):** logistic regression reached **AUC 0.904** and **85.4% accuracy**. A version with 3-fold cross-validation over 9 hyperparameter combinations matched that performance, and I chose it in MLflow because its tuning is systematic and therefore more reliable.
- **Framework choice (HW3):** Spark MLlib is the right tool when data can't fit on one machine or has to plug into streaming pipelines (e.g., churn across millions of records, real-time fraud detection). scikit-learn is better for fast prototyping on smaller data, and H2O's AutoML suits cases where automatically comparing many models adds value.
- **Scale:** queries over **22 million** Wikipedia clickstream rows (for example, the top referrers driving traffic to Wikipedia) ran interactively on a Spark cluster.

## 🛠 Technologies

- **Databricks** (Unity Catalog, volumes, clusters)
- **Apache Spark / PySpark:** DataFrames, Spark SQL, MLlib, Structured Streaming
- **Hive** (HiveQL)
- **MLflow**
- Streamlit, OpenAI-compatible SDK, Databricks AI Gateway
- Python, SQL, Linux shell

## ✅ Outcome

The repository shows end-to-end big data skills, from ingesting and querying multi-gigabyte datasets to building, tuning, tracking and deploying scalable ML models and an LLM-powered application. These are the same tools used in production data platforms.

---

By **Parul Chaudhary** · [LinkedIn](https://www.linkedin.com/in/parulchaud) · [Email](mailto:parul.jaswant@gmail.com)
