import os
import sys
import unittest
 
SPARK_HOME = os.environ["SPARK_HOME"]
os.path.join(SPARK_HOME)
print SPARK_HOME
 
# Add the PySpark directories to the Python path:
sys.path.insert(1, os.path.join(SPARK_HOME, 'python'))
sys.path.insert(1, os.path.join(SPARK_HOME, 'python', 'pyspark'))
sys.path.insert(1, os.path.join(SPARK_HOME, 'python', 'build'))
sys.path.insert(1, os.path.join(SPARK_HOME, 'python', 'lib/py4j-0.8.2.1-src.zip'))

# If PySpark isn't specified, use currently running Python binary:
pyspark_python =  sys.executable
os.environ['PYSPARK_PYTHON'] = pyspark_python
 
from pyspark.conf import SparkConf
from pyspark.context import SparkContext
 
sc_values = {}
 
class PySparkTestCase(unittest.TestCase):
 
    def setUp(self):
        self._old_sys_path = list(sys.path)
        conf = SparkConf().setMaster("local[2]") \
            .setAppName(self.__class__.__name__) \
            .set("spark.authenticate.secret", "111111")
        self.sc = SparkContext(conf=conf)
 
    def tearDown(self):
        self.sc.stop()
        sys.path = self._old_sys_path
 
class TestResusedScA(PySparkTestCase):
 
    def testA_1(self):
        rdd = self.sc.parallelize([1,2,3])
        self.assertEqual(rdd.collect(), [1,2,3])
        sc_values['testA_1'] = self.sc
 
    def testA_2(self):
        sc_values['testA_2'] = self.sc
 
        self.assertEquals(self.sc, sc_values['testA_1'])
 
 
class TestResusedScB(unittest.TestCase):
    def testB_1(self):
        pass
 
 
if __name__ == '__main_':
    unittest.main()
