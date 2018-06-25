from pyspark.ml import PipelineModel
from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.sql.functions import col

model = PipelineModel.load("logreg.model")

sc =SparkContext()
sqlContext = SQLContext(sc)
data = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load('/home/ubuntu/dirwithcsv/t.csv')

data = data.select([column for column in data.columns])
data.show(5)

prediction = model.transform(test)
prediction.select("text","sentiment","probability","label","prediction")\
	.orderBy("probability", ascending = False)\
	.show(n = 10, truncate = 30)


