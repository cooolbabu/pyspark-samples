**pyspark.SparkConf()**
Cofiguration for a Spark application. Used to set various spark parameters as key-value pairs

**pyspark.SparkContext()**
Main entry point for Spark functionality. A SparkContext represents the connection to a spark cluster and can be used to create RDD and broadcast variables on that Cluster

```
    conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
    sc = SparkContext(conf = conf)
```

```
    lines = sc.textFile("file:///SparkCourse/ml-100k/u.data")
```
- Read text file from HDFS file system or any Hadoop supported file system URI and return it as RDD of Strings


```
    ratings = lines.map(lambda x: x.split(',')[2])
    result = ratings.countByValue()
```
- Split RDD by ',', select the third column. countbyvalue => group and count unique values