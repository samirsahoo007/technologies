PySpark Tutorial
================
PySpark is the Spark Python API.  

Start PySpark
=============
First make sure that you have started the Spark cluster. To start Spark, you execute:

````
cd $SPARK_HOME
./sbin/start-all.sh
````

To start PySpark, execute the following:

````
cd $SPRAK_HOME
./bin/pyspark
````

Successful execution will give you the PySpark prompt:

````
./bin/pyspark
Python 2.7.10 (default, Aug 22 2015, 20:33:39) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
16/01/20 10:26:28 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 1.6.0
      /_/

Using Python version 2.7.10 (default, Aug 22 2015 20:33:39)
SparkContext available as sc, HiveContext available as sqlContext.
>>> 
````

Note that the shell already have created a SparkContext (````sc````) object and you may use it to create RDDs.

Creating RDDs
=============
You may create RDDs by reading files from data structures, local file system, HDFS, and other data sources.

Create RDD from a Data Structure (or Collection)
------------------------------------------------
* Example-1

````
>>> data = [1, 2, 3, 4, 5, 8, 9]
>>> data
[1, 2, 3, 4, 5, 8, 9]
>>> myRDD = sc.parallelize(data)
>>> myRDD.collect()
[1, 2, 3, 4, 5, 8, 9]
>>> myRDD.count()
7
>>> 
````

* Example-2

````
>>> kv = [('a',7), ('a', 2), ('b', 2), ('b',4), ('c',1), ('c',2), ('c',3), ('c',4)]
>>> kv
[('a', 7), ('a', 2), ('b', 2), ('b', 4), ('c', 1), ('c', 2), ('c', 3), ('c', 4)]
>>> rdd2 = sc.parallelize(kv)
>>> rdd2.collect()
[('a', 7), ('a', 2), ('b', 2), ('b', 4), ('c', 1), ('c', 2), ('c', 3), ('c', 4)]
>>>
>>> rdd3 = rdd2.reduceByKey(lambda x, y : x+y)
>>> rdd3.collect()
[('a', 9), ('c', 10), ('b', 6)]
>>> 
````

* Example-3

````
# ./bin/pyspark 
Python 2.7.10 (default, Aug 22 2015, 20:33:39) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
16/01/21 16:46:08 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 1.6.0
      /_/

Using Python version 2.7.10 (default, Aug 22 2015 20:33:39)
SparkContext available as sc, HiveContext available as sqlContext.
>>> kv = [('a',7), ('a', 2), ('b', 2), ('b',4), ('c',1), ('c',2), ('c',3), ('c',4)]

>>> kv
[('a', 7), ('a', 2), ('b', 2), ('b', 4), ('c', 1), ('c', 2), ('c', 3), ('c', 4)]
>>> rdd2 = sc.parallelize(kv)
>>> rdd2.collect()
[('a', 7), ('a', 2), ('b', 2), ('b', 4), ('c', 1), ('c', 2), ('c', 3), ('c', 4)]

>>> rdd3 = rdd2.groupByKey()
>>> rdd3.collect()
[
 ('a', <pyspark.resultiterable.ResultIterable object at 0x104ec4c50>), 
 ('c', <pyspark.resultiterable.ResultIterable object at 0x104ec4cd0>), 
 ('b', <pyspark.resultiterable.ResultIterable object at 0x104ce7290>)
]

>>> rdd3.map(lambda x : (x[0], list(x[1]))).collect()
[
 ('a', [7, 2]), 
 ('c', [1, 2, 3, 4]), 
 ('b', [2, 4])
]
>>> 
````

# How can I do this in PySpark?

More concrete example, I want to transform this DF (visualized in JSON)

```
{
    "order": "c-331",
    "travel": [
        {
            "place": {
                "name": "A place",
                "address": "The address",
                "latitude": 0.0,
                "longitude": 0.0
            },
            "distance_in_kms": 1.0,
            "estimated_time": {
                "seconds": 988,
                "nanos": 102
            }
        }
    ]
}
```

into

```
{
    "order": "c-331",
    "travel": [
        {
            "place": {
                "name": "A place",
                "address": "The address",
                "latitude": 0.0,
                "longitude": 0.0
            },
            "distance_in_kms": 1.0,
            "estimated_time": "988s"
        }
    ]
}
```

You can do this with the following pyspark functions:

      withColumn lets you create a new column. We will use this to extract "estimated_time"

      concat concatenates string columns

      lit creates a column of a given string

      Please have a look at the following example:

```
from pyspark.sql import functions as F
j = '{"order":"c-331","travel":[{"place":{"name":"A place","address":"The address","latitude":0.0,"longitude":0.0},"distance_in_kms":1.0,"estimated_time":{"seconds":988,"nanos":102}}]}'
df = spark.read.json(sc.parallelize([j]))

#the following command creates a new column called estimated_time2 which contains the values of travel.estimated_time.seconds concatenated with a 's' 
bla = df.withColumn('estimated_time2', F.concat(df.travel.estimated_time.seconds[0].cast("string"), F.lit("s")))

#unfortunately it is currently not possible to use withColumn to add a new member to a struct. Therefore the following command replaces 'travel.estimated_time' with the before created column estimated_time2
bla = bla.select("order"
                , F.array(
                    F.struct(
                        bla.travel.distance_in_kms[0].alias("distance_in_kms")
                        ,bla.travel.place[0].alias("place")
                        , bla.estimated_time2.alias('estimated_time')
                        )).alias("travel"))

bla.show(truncate=False)
bla.printSchema()
```

And that is the output:

```
+-----+------------------------------------------+ 
|order|travel                                    | 
+-----+------------------------------------------+ 
|c-331|[[1.0,[The address,0.0,0.0,A place],988s]]| 
+-----+------------------------------------------+


root 
|-- order: string (nullable = true) 
|-- travel: array (nullable = false) 
| |-- element: struct (containsNull = false) 
| | |-- distance_in_kms: double (nullable = true)
| | |-- place: struct (nullable = true) 
| | | |-- address: string (nullable = true) 
| | | |-- latitude: double (nullable = true) 
| | | |-- longitude: double (nullable = true) 
| | | |-- name: string (nullable = true) 
| | |-- estimated_time: string (nullable = true)
```


Create RDD from a Local File System
-----------------------------------
````
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
...
JavaSparkContext context = new JavaSparkContext();
...
final String inputPath ="file:///dir1/dir2/myinputfile.txt";
JavaRDD<String> rdd = context.textFile(inputPath);
...
````


Create RDD from HDFS
--------------------
* Example-1:

````
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
...
JavaSparkContext context = new JavaSparkContext();
...
final String inputPath ="hdfs://myhadoopserver:9000/dir1/dir2/myinputfile.txt";
JavaRDD<String> rdd = context.textFile(inputPath);
...
````

* Example-2:

````
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
...
JavaSparkContext context = new JavaSparkContext();
...
final String inputPath ="/dir1/dir2/myinputfile.txt";
JavaRDD<String> rdd = context.textFile(inputPath);
...
````

Questions/Comments
==================
* [View Mahmoud Parsian's profile on LinkedIn](http://www.linkedin.com/in/mahmoudparsian)
* Please send me an email: mahmoud.parsian@yahoo.com
* [Twitter: @mahmoudparsian](http://twitter.com/mahmoudparsian) 

Thank you!

````
best regards,
Mahmoud Parsian
````

[![Data Algorithms Book](https://github.com/mahmoudparsian/data-algorithms-book/blob/master/misc/data_algorithms_image.jpg)](http://shop.oreilly.com/product/0636920033950.do) 
