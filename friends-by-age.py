from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("FriendsByAge")
sc = SparkContext(conf=conf)

# Fake friends data set
# ID, Name, Age, # of Friends


def parseLine(line):
    fields = line.split(',')
    age = int(fields[2])
    numFriends = int(fields[3])
    return (age, numFriends)


lines = sc.textFile("./data/fakefriends.csv")
rdd = lines.map(parseLine)

totalsByAge = rdd.mapValues(lambda x: (x, 1)).reduceByKey(
    lambda x, y: (x[0] + y[0], x[1] + y[1]))

# Collect and print
dataCollect = totalsByAge.collect()
for row in dataCollect:
    print(str(row[0]) + " :: " + str(row[1]))

averagesByAge = totalsByAge.mapValues(lambda x: x[0] / x[1])
results = averagesByAge.sortByKey(True).collect()
for result in results:
    print(result)

