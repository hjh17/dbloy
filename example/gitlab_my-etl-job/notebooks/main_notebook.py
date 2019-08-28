# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC # My ETL Pipeline

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Access Parameters

# COMMAND ----------

DB_URL = dbutils.widgets.get("DB_URL")
DB_PASSWORD = dbutils.widgets.get("DB_PASSWORD")

NOTEBOOK_1_PATH = dbutils.widgets.get("NOTEBOOK_1_NAME")
NOTEBOOK_2_PATH = dbutils.widgets.get("NOTEBOOK_2_NAME")

print("DB_URL : ", DB_URL)
print("DB_PASSWORD : ", DB_PASSWORD)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Import and interact with the main library

# COMMAND ----------

from my_python_lib import _version
from my_python_lib import main_function


print("Using my_python_lib version ", _version.__version__)

# COMMAND ----------

five = main_function.add(2,3)

assert five == 5

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Run sibling notebooks

# COMMAND ----------

dbutils.notebook.run(
  NOTEBOOK_1_PATH,
  timeout_seconds=500)

# COMMAND ----------

dbutils.notebook.run(
  NOTEBOOK_2_PATH,
  timeout_seconds=500)
