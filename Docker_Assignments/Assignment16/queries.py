from pyspark.sql import SparkSession
from pyspark.sql.functions import col,sum,avg,desc

spark = SparkSession.builder.appName("DemoSparkApp").getOrCreate()
df=spark.read\
    .option("header",True) \
    .option("inferSchema",True) \
    .csv("employees.csv")
df.show()

print("Employees ordered by Salary:")
df.orderBy(col("salary").desc()).show()

print("Department wise salary")
df.groupBy("department").sum("salary").show()

print("Saving top 3 highest paid employees:")
top3=df.orderBy(col("salary").desc()).limit(3)
top3.show()
top3.write.csv("ans/highestSalary",header=True)

spark.stop()