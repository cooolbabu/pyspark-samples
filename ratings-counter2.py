from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

lines = sc.textFile("ml-latest-small\\ratings.csv")

# lines.foreach(print)

ratings = lines.map(lambda x: x.split(',')[2])
result = ratings.countByValue()

sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print("%s %i" % (key, value))

print("ratings datatype: ", type(ratings))
print("results datatype: ", type(result))
print("sortedResults datatype: ", type(sortedResults))
