import sys, os
batchx_path='/tmp/batchx-tool/reactorx-apps-1.230.5.88.nwf'
SPARK_HOME = os.path.join(batchx_path, 'app/spark-2.1.1-bin-hadoop2.6/')
print 'SPARK_HOME=',SPARK_HOME

# Add the PySpark directories to the Python path:
sys.path.insert(1, os.path.join(SPARK_HOME, 'python'))
sys.path.insert(1, os.path.join(SPARK_HOME, 'python', 'pyspark'))
sys.path.insert(1, os.path.join(SPARK_HOME, 'python', 'build'))

# This is to put a check if the version of py4j changes in future
py4j_src_path = os.path.join(SPARK_HOME, 'python', 'lib/py4j-0.10.4-src.zip')



from pyspark.conf import SparkConf
from pyspark.sql import SparkSession, SQLContext, Row
from pyspark.sql.types import StringType, IntegerType, StructType, StructField

"""Create a single node Spark application."""
sc_conf = SparkConf()
sc_conf.setAppName("batchx_tests")
sc_conf.setMaster('local[2]')
sc_conf.set('spark.executor.memory', '2g')
sc_conf.set('spark.executor.cores', '4')
sc_conf.set('spark.cores.max', '40')
sc_conf.set('spark.logConf', True)
# print sc_conf.getAll()
print 'sc_conf=',sc_conf

SparkSession._instantiatedContext = None

spark = SparkSession.builder.config(conf=sc_conf).getOrCreate()
sparkSession = SparkSession

def get_dataframe(khRepo='data/khRepo/', table_name='khRepo_table'):
        '''
        Read data/khRepo and return dataframe
        :param khRepo:
        :param table_name:
        :return:
        '''
        dataFrame = spark.read.json(khRepo)  # time taken =  10.959002018
        dataFrame.createOrReplaceTempView(table_name)  # Create a temporary view using the DataFrame
        return dataFrame

df_building_footprints = get_dataframe('/tmp/batchx-tool/reactorx-apps-1.230.5.88.nwf/data/buildingFiles/building-footprints/building-footprints.json')
df_building_footprints.show()
print df_building_footprints.count()

df_tool_output = get_dataframe('/tmp/batchx-tool/reactorx-apps-1.230.5.88.nwf/data/output/tool_output.featureproto')
df_tool_output.show()
print df_tool_output.count()

df_actual_features = df_building_footprints.join(
    df_tool_output
).select(
    df_tool_output.metadata.source_attribution.sub_path_source[0].process_info.build_id,
    df_tool_output.FeatureProto.is_active, # is_active is not in buildin_footprints
    df_tool_output.FeatureProto.protocol_version,
    df_building_footprints.FeatureProto.protocol_version, 
    df_tool_output.FeatureProto.version,
    df_building_footprints.FeatureProto.version,
    df_tool_output.FeatureProto.representative_point,
    df_building_footprints.FeatureProto.representative_point
).withColumnRenamed('metadata.source_attribution.sub_path_source[0].process_info.build_id', 'build_id'
).where(
    (df_tool_output.FeatureProto.feature_type[0] == 'BUILDING') & 
    (df_tool_output.FeatureProto.feature_id ==  df_building_footprints.FeatureProto.feature_id) & 
    (df_tool_output.FeatureProto.building.roof_type ==  df_building_footprints.FeatureProto.building.roof_type) &
    (df_tool_output.FeatureProto.building.base_height ==  df_building_footprints.FeatureProto.building.base_height) &
    (df_tool_output.FeatureProto.building.top_height ==  df_building_footprints.FeatureProto.building.top_height) & 
    (df_tool_output.FeatureProto.iso_country_code ==  df_building_footprints.FeatureProto.iso_country_code) &
    (df_tool_output.FeatureProto.iso_subdivision_code ==  df_building_footprints.FeatureProto.iso_subdivision_code) &
    (df_tool_output.FeatureProto.history[0].edit_type ==  df_building_footprints.FeatureProto.history[0].edit_type) &
    (df_tool_output.FeatureProto.history[0].source ==  df_building_footprints.FeatureProto.history[0].source ) &
    (df_tool_output.FeatureProto.history[0].source_id ==  df_building_footprints.FeatureProto.history[0].source_id) &
    (df_tool_output.FeatureProto.history[0].timestamp ==  df_building_footprints.FeatureProto.history[0].timestamp) &
    (df_tool_output.FeatureProto.history[0].vendor_id ==  df_building_footprints.FeatureProto.history[0].vendor_id)
).where("build_id like '%NeutronBatchX /  reactorx-apps-%'")
df_actual_features.show()
print df_actual_features.count()
