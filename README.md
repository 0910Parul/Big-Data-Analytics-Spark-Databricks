# Scalable Data Analytics and Machine Learning with Apache Spark & Databricks

## Project Overview

This repository explores distributed data processing, predictive analytics, streaming, and AI integration using Apache Spark and Databricks. Seven modules cover data ingestion and SQL analysis, reusable machine learning pipelines, experiment tracking, and a Streamlit chatbot connected to a hosted LLM.

The analytical objective is to turn large or continuously arriving datasets into structured information and evaluated models. Separate use cases include retail data, Yelp reviews, Wikipedia clickstream data, Titanic survival, and census income.

## Key Highlights

- **Data scale:** loaded a Wikipedia clickstream source with **22M+ rows** and created a seeded 10% sample for SQL exercises.
- **Predictive modeling:** recorded test ROC-AUC of **0.831** for Titanic survival and **0.904** for census income classification.
- **Model comparison:** evaluated logistic regression and random forest pipelines using ROC-AUC, accuracy, and weighted F1.
- **Streaming:** implemented event aggregations with one-hour windows, 30-minute slides, and checkpointed table output.
- **Experiment tracking and AI integration:** logged model parameters and metrics with MLflow and built a Streamlit interface using a Databricks-hosted endpoint.

Start with the [model comparison](04_Spark_MLlib/HW3_Spark_MLlib.ipynb), [MLflow experiment](06_MLflow/HW4_MLflow_with_Spark_MLlib.ipynb), or [results evidence and limitations](docs/RESULTS_EVIDENCE.md).

## Technical Implementation

| Module | Implementation |
|---|---|
| Databricks and Spark basics | Linux file operations, Unity Catalog volumes, CSV loading, DataFrame transformations, and execution plans |
| Hive | Database and table creation, managed and external table concepts, and retail queries |
| DataFrames and SQL | LendingClub exploration; Yelp schema inspection, table separation, and joins; Wikipedia source loading, sampling, and aggregation exercises |
| Spark MLlib | Feature encoding and assembly, missing-value handling, classification and regression workflows, model persistence, and cross-validation |
| Structured Streaming | Explicit event schema, windowed counts, incremental file ingestion, checkpoints, and table output using an available-now trigger |
| MLflow | Parameter and metric logging, run comparisons, saved-model loading, and baseline versus tuned census-income models |
| GenAI chatbot | OpenAI-compatible client, Databricks endpoint configuration, conversation history, and a Streamlit interface |

HW3 also discusses scikit-learn and H2O alongside Spark MLlib as a qualitative framework comparison.

## Methods & Technologies

- **Data platform:** Databricks, Unity Catalog, Hive/HiveQL, Apache Spark, PySpark DataFrames, and Spark SQL.
- **Feature preparation:** SQLTransformer, Imputer, StringIndexer, OneHotEncoder, VectorAssembler, and scaling examples.
- **Modeling and evaluation:** logistic regression, decision tree, random forest, gradient-boosted regression trees, CrossValidator, ParamGridBuilder, ROC-AUC, accuracy, weighted F1, and RMSE.
- **Tracking and applications:** MLflow, scikit-learn in the wine-quality lab, Streamlit, python-dotenv, and the OpenAI-compatible SDK.
- **Languages and analysis:** Python, SQL, Linux shell, pandas, NumPy, and Matplotlib.

## Results & Insights

These values come from saved notebook outputs; they have not been independently rerun for this documentation update.

| Use case | Model / run | Test ROC-AUC | Test accuracy | Test weighted F1 |
|---|---|---:|---:|---:|
| Titanic survival | Logistic regression | 0.797 | 73.9% | 0.737 |
| Titanic survival | Random forest, including the cross-validated run | **0.831** | **81.9%** | **0.814** |
| Census income | Logistic regression baseline | 0.904 | 85.4% | — |
| Census income | Logistic regression, 3-fold CV over 9 combinations | 0.904 | 85.4% | — |

- **Model choice:** the Titanic random forest performed better than logistic regression on the saved test split. Its tuned run matched the untuned forest's displayed metrics.
- **Tuning:** the census runs achieved nearly identical test performance. Cross-validation documents a systematic search; these outputs do not establish improved generalization.
- **Scale and data quality:** the Wikipedia read returned **22,509,898 rows**, including the header read as data, and the sample contained **2,252,530 rows**. The saved schema places the click count and title columns in the wrong order, affecting downstream sums and rankings. Those rankings need correction and a fresh run before interpretation. See [the evidence notes](docs/RESULTS_EVIDENCE.md).
- **Experiment traceability:** the MLflow lab records wine-quality gradient-boosting test AUC of 0.8834 for the baseline and 0.8912 with 200 estimators.

These are educational implementations and saved experiments. Production deployment, latency, throughput, and business impact have not been measured here.

## Repository Structure

| Folder | Files and purpose |
|---|---|
| [01_Databricks_and_Spark_Basics](01_Databricks_and_Spark_Basics/) | Linux shell and file operations; `Lab5-1_Using_Spark.ipynb` |
| [02_Hive](02_Hive/) | `Lab3-1_Hive_Intro.ipynb`, `HW1_Big_Data_and_Hive.ipynb` |
| [03_Spark_DataFrames_and_SQL](03_Spark_DataFrames_and_SQL/) | DataFrame creation, LendingClub analysis, and `HW2_Spark_SQL_Yelp.ipynb` |
| [04_Spark_MLlib](04_Spark_MLlib/) | Feature APIs, concrete features, used-car classification, bike-share regression, and `HW3_Spark_MLlib.ipynb` |
| [05_Structured_Streaming](05_Structured_Streaming/) | `Lab10-2_IoT_Streaming.ipynb` |
| [06_MLflow](06_MLflow/) | `Lab13-2_MLflow_Tracking.ipynb`, `HW4_MLflow_with_Spark_MLlib.ipynb` |
| [07_GenAI_Chatbot](07_GenAI_Chatbot/) | `chatbot.py`, application dependencies, and `.env.example` |
| [docs](docs/) | Metric provenance and reproduction notes |

## Getting Started

### Databricks notebooks

1. Import the desired `.ipynb` files into a Databricks workspace and attach compatible compute. The notebooks use a provided `spark` session, `dbutils`, and Databricks SQL/display features.
2. Review input, catalog, schema, volume, model, and checkpoint paths. The examples include table overwrites and cleanup cells that drop resources.
3. Obtain the referenced datasets from `databricks-datasets`, public sources, or course-hosted downloads. Large datasets are not included; original paths may no longer be available.
4. Run setup and preparation cells before the analytical cells. Review the clickstream column-order and header issue before interpreting aggregations.
5. Open the experiment view for the MLflow modules to inspect parameters, metrics, and model artifacts.

The root [requirements.txt](requirements.txt) lists supporting Python packages; installing it alone does not recreate the Databricks environment. Notebook exports retain text outputs, while some interactive charts are absent.

### Streamlit chatbot

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r 07_GenAI_Chatbot/requirements.txt
cd 07_GenAI_Chatbot
cp .env.example .env
```

Set all three variables in `.env`: `DATABRICKS_TOKEN`, `DATABRICKS_BASE_URL`, and `DATABRICKS_LLM_MODEL`, using a reachable, authorized endpoint. Then launch:

```bash
streamlit run chatbot.py
```

Keep credentials in the local environment. The application calls a hosted model and requires network access.

## Applications & Takeaways

- **Analytical reporting:** schema checks, joins, and aggregation patterns can support repeatable reporting on customer, lending, review, or event data.
- **Decision support:** comparing models with multiple metrics makes trade-offs visible before selecting a predictive approach.
- **Operational monitoring:** streaming windows and checkpoints illustrate how event summaries can feed monitoring workflows.
- **Reproducibility:** experiment logs make model choices reviewable, while source-schema validation is essential before turning query outputs into recommendations.

These are potential applications of the techniques; revenue gains and operational deployment have not been evaluated.

## Project Context

Developed for **MSBA 6331 — Big Data Analytics**, Carlson School of Management, University of Minnesota. Original module names, notebooks, and saved outputs are retained.

---

By **Parul Chaudhary** · [LinkedIn](https://www.linkedin.com/in/parulchaud) · [Email](mailto:parul.jaswant@gmail.com)
