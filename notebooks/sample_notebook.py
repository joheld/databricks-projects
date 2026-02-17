# Databricks notebook source
# MAGIC %md
# MAGIC # Sample Databricks Notebook
# MAGIC This is a sample notebook for CI/CD pipeline testing.

# COMMAND ----------

import pandas as pd
from pyspark.sql import SparkSession

# COMMAND ----------

# Create sample data
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['San Jose', 'San Francisco', 'Oakland']
}

df = pd.DataFrame(data)
print(df)

# COMMAND ----------

# Convert to Spark DataFrame
spark_df = spark.createDataFrame(df)
spark_df.show()
