import logging
from pyspark.sql import SparkSession
def suppress_py4j_logging():
 logger = logging.getLogger('py4j')
 logger.setLevel(logging.WARN)
def create_testing_pyspark_session():
 return (SparkSession.builder
 .master('local[2]')
 .appName('my-local-testing-pyspark-context')
 .enableHiveSupport()
 .getOrCreate())

suppress_py4j_logging()
create_testing_pyspark_session()
