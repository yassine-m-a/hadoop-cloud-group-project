from pyspark import SparkContext, SparkConf

# Config Spark
conf = SparkConf().setAppName("SearchJeanmougin")
sc = SparkContext(conf=conf)

# RDD
rdd = sc.textFile("hdfs:///user/ubuntu/frwiki.xml.bz2")

# Filtre
results = rdd.filter(lambda line: "jeanmougin" in line.lower())
count = results.count()
print(f"Occurrences du mot 'jeanmougin' : {count}")

# Arrêter Spark
sc.stop()