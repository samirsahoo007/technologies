Download, Install, and Run PySpark

0. For macbook users: Enable "Remote Login"

````
System Preferences --> Sharing --> enable "Remote Login" service
````

1. Make Sure Java is Installed Properly
=======================================
````
java -version
java version "1.8.0_72"
Java(TM) SE Runtime Environment (build 1.8.0_72-b15)
Java HotSpot(TM) 64-Bit Server VM (build 25.72-b15, mixed mode)
````

2. Download the latest binary Spark from https://downloads.apache.org/spark/ 
    OR
    just download the following URL.
```
https://www.apache.org/dyn/closer.lua/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.7.tgz
```

3. Setup SPARK_HOME
===================
Go to the official Apache Spark download page(https://www.apache.org/dyn/closer.lua/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.7.tgz) and download the latest version of Apache Spark available there. 

````
# tar -xvf downloaded_directory/spark-2.4.3-bin-hadoop2.7.tgz

Save the following lines to ~/.bash_profile
export SPARK_HOME=downloaded_directory/spark-2.4.3-bin-hadoop2.7
export PATH=$PATH:downloaded_directory/spark-2.4.3-bin-hadoop2.7/bin
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH
export PATH=$SPARK_HOME/python:$PATH

# source ~/.bash_profile
# ./bin/pyspark

````

4. Start the Spark Cluster
==========================
````
cd /Users/samirsahoo/spark-2.4.3-bin-hadoop2.7/

ls -l
total 2736
-rw-r--r--@  1 samirsahoo  897801646  1343562 Feb 26 21:02 CHANGES.txt
-rw-r--r--@  1 samirsahoo  897801646    17352 Feb 26 21:02 LICENSE
-rw-r--r--@  1 samirsahoo  897801646    23529 Feb 26 21:02 NOTICE
drwxr-xr-x@  3 samirsahoo  897801646      102 Feb 26 21:02 R
-rw-r--r--@  1 samirsahoo  897801646     3359 Feb 26 21:02 README.md
-rw-r--r--@  1 samirsahoo  897801646      120 Feb 26 21:02 RELEASE
drwxr-xr-x@ 25 samirsahoo  897801646      850 Feb 26 21:02 bin
drwxr-xr-x@  9 samirsahoo  897801646      306 Feb 26 21:02 conf
drwxr-xr-x@  3 samirsahoo  897801646      102 Feb 26 21:02 data
drwxr-xr-x@  6 samirsahoo  897801646      204 Feb 26 21:02 ec2
drwxr-xr-x@  3 samirsahoo  897801646      102 Feb 26 21:02 examples
drwxr-xr-x@  8 samirsahoo  897801646      272 Feb 26 21:02 lib
drwxr-xr-x@ 37 samirsahoo  897801646     1258 Feb 26 21:02 licenses
drwxr-xr-x@  9 samirsahoo  897801646      306 Feb 26 21:02 python
drwxr-xr-x@ 24 samirsahoo  897801646      816 Feb 26 21:02 sbin


./sbin/start-all.sh
````

5. Check Master and Worker
==========================
Make sure that Master and Worker processes are running:

````
jps
1347 Master
1390 Worker
````

6. Check The Spark URL
======================

````
http://localhost:8080
````

*Issues*:
**What if you get the following error?**

1. (venv363) Samirs-XYZ $ ./sbin/start-all.sh
    WARNING: Attempting to start all Apache Hadoop daemons as samirsahoo in 10 seconds.
    WARNING: This is not a recommended production deployment configuration.
    WARNING: Use CTRL-C to abort.
    Starting namenodes on [localhost]
    localhost: sameer_sahoo@localhost: Permission denied (publickey,password,keyboard-interactive).
    Starting datanodes
    localhost: sameer_sahoo@localhost: Permission denied (publickey,password,keyboard-interactive).
    Starting secondary namenodes [Samirs-XYZ]
    Samirs-XYZ: sameer_sahoo@samirs-mbp: Permission denied (publickey,password,keyboard-interactive).
    2021-05-16 21:20:29,168 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
    Starting resourcemanager
    resourcemanager is running as process 81524.  Stop it first.
    Starting nodemanagers
    localhost: sameer_sahoo@localhost: Permission denied (publickey,password,keyboard-interactive).


*Solution*: Here the username sameer_sahoo may not have passwordless access that you've set above. If the passwordless setup is correct, then check the user... e.g. in my case if you'd see, the username for which passwordless access was set is samirsahoo not sameer_sahoo

```
 $ users
   samirsahoo
```

So from where this username "sameer_sahoo" is coming from??? Check ~/.ssh/config ...; the username in "User" Change User line from "User sameer_sahoo" to "User samirsahoo" and run ./start-all.sh again.

*# Follow the steps below if you want to make your system passwordless*

```
$ ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
$ chmod 0600 ~/.ssh/authorized_keys
```

7. Define 2 Very Basic Python Programs
======================================

* Python program: ````test.py````

````
cat /Users/samirsahoo/spark-2.4.3-bin-hadoop2.7/test.py
#!/usr/bin/python

import sys

for line in sys.stdin:
	print "hello " + line
````

* Python program: ````test2.py````
	
````	
cat /Users/samirsahoo/spark-2.4.3-bin-hadoop2.7/test2.py
#!/usr/bin/python

def fun2(str):
	str2 = str + " zaza"
	return str2
````

8. Start and Run pyspark
========================
````
cd /Users/samirsahoo/spark-2.4.3-bin-hadoop2.7/
./bin/pyspark
Python 2.7.10 (default, Oct 23 2015, 19:19:21)
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
16/04/04 11:18:01 INFO spark.SparkContext: Running Spark version 1.6.1
...
...
...
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 1.6.1
      /_/

Using Python version 2.7.10 (default, Oct 23 2015 19:19:21)
SparkContext available as sc, HiveContext available as sqlContext.

>>> data = ["john","paul","george","ringo"]
>>> data
['john', 'paul', 'george', 'ringo']

>>> rdd = sc.parallelize(data)
>>> rdd.collect()
['john', 'paul', 'george', 'ringo']


>>> test = "/Users/samirsahoo/spark-2.4.3-bin-hadoop2.7/test.py"
>>> test2 = "/Users/samirsahoo/spark-2.4.3-bin-hadoop2.7/test2.py"
>>> import test
>>> import test2


>>> pipeRDD =  rdd.pipe(test)
>>> pipeRDD.collect()
[u'hello john', u'', u'hello paul', u'', u'hello george', u'', u'hello ringo', u'']


>>> rdd.collect()
['john', 'paul', 'george', 'ringo']


>>> rdd2 = rdd.map(lambda x : test2.fun2(x))
>>> rdd2.collect()
['john zaza', 'paul zaza', 'george zaza', 'ringo zaza']
>>>
````
