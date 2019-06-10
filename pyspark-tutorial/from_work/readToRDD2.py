import sys, json
from pyspark import SparkContext

# Run the following command on bash before running this python script
# export PYTHONIOENCODING=utf8
 
if __name__ == "__main__":
 
  # create Spark context with Spark configuration
  sc = SparkContext()
  sc.setLogLevel("ERROR")
  #sc.setLogLevel("OFF")
 
  # read input text files present in the directory to RDD
  lines = sc.textFile("/tmp/batchx-tool/reactorx-apps-1.223.1.33.nwf/data/khRepo")
  lCount = lines.count()
  linesWithString = lines.filter(lambda line: "DRIVEWAY" in line)
  llist = linesWithString.collect()
  for l in llist:
    json_line = json.loads(l)
    print json_line['FeatureProto']['road_segment']['form_of_way']
  
