from pyspark.sql import SparkSession 
from pyspark.sql.functions import col

spark=SparkSession.builder.appName("PartitionApp").getOrCreate()
numFrame=spark.range(0,5000000).withColumn("Values",col("id")%1000)
numFrame.take(5)

#Original partitions
print("Initial Number of partitions:",numFrame.rdd.getNumPartitions())

#Increasing partitions to 12
newNumFrame=numFrame.repartition(12)
print("Current Number of partitions:",newNumFrame.rdd.getNumPartitions())

#Reducing partitions to 3
finalNumFrame=newNumFrame.coalesce(3)
print("Final Number of partitions:",finalNumFrame.rdd.getNumPartitions())

spark.stop()