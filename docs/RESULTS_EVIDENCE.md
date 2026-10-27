# Results Evidence and Reproduction Notes

This document maps the README to artifacts inspected during the documentation review. Cell numbers are **1-based positions in the saved notebook**, including markdown cells. Results were checked against saved outputs, not independently rerun.

| Claim | Source | Saved evidence |
|---|---|---|
| Titanic logistic regression | [HW3](../04_Spark_MLlib/HW3_Spark_MLlib.ipynb), cell 49 | AUC 0.7970404984; accuracy 0.7386759582; weighted F1 0.7373399632 |
| Titanic random forest | HW3, cells 54 and 56 | Both display AUC 0.8311266874; accuracy 0.8188153310; weighted F1 0.8136523189 |
| Census baseline | [HW4](../06_MLflow/HW4_MLflow_with_Spark_MLlib.ipynb), cell 27 | AUC 0.9035865108; accuracy 0.8539325843 |
| Census cross-validation | HW4, cells 32 and 37 | 3 folds; 3 regularization values × 3 elastic-net values; AUC 0.9035843368; accuracy 0.8539325843 |
| Wikipedia scale | [HW2](../03_Spark_DataFrames_and_SQL/HW2_Spark_SQL_Yelp.ipynb), cells 36 and 39 | Read count 22,509,898; seeded 10% sample count 2,252,530 |
| Streaming implementation | [Streaming lab](../05_Structured_Streaming/Lab10-2_IoT_Streaming.ipynb), cell 19 | One-hour windows; 30-minute slides; `availableNow=True`; checkpointed table output |
| Wine-quality experiment comparison | [Tracking lab](../06_MLflow/Lab13-2_MLflow_Tracking.ipynb), cells 21 and 25 | Test AUC 0.8834115358 and 0.8912222477 |
| Chatbot integration | [chatbot.py](../07_GenAI_Chatbot/chatbot.py) | Environment-based endpoint settings and Streamlit session history |

## Interpretation boundaries

- The saved Wikipedia header is `prev_id, curr_id, n, prev_title, curr_title, type`, while the loading schema places `n` after the title fields and sets `header=false`. This shifts the click count and titles and includes the header as a row. The saved output shows null or misassigned values; traffic rankings and page-flow sums need correction and a fresh run. The read count establishes scale only.
- Subsequent Wikipedia queries use the 10% sample rather than all source rows. No cluster speed, latency, or scaling benchmark is recorded.
- The Titanic and census tuned runs show no improvement over the corresponding untuned results. A systematic search alone does not prove greater reliability.
- Spark's `MulticlassClassificationEvaluator(metricName="f1")` is reported as weighted F1.
- The streaming exercise processes available files using an available-now trigger. The code uses 30-minute slides despite an instruction referring to five minutes.
- H2O is discussed in HW3; no H2O-versus-Spark performance benchmark is presented.
- The chatbot's missing-configuration checks reference `st` before its import. Configure all three environment variables before launching; improving that error path would require a separate code change.
- Dataset paths, Databricks permissions, and runtime compatibility must be reviewed before rerunning. Some historical warnings remain, and interactive outputs were not fully exported.

This documentation update leaves executable files and saved results unchanged.
