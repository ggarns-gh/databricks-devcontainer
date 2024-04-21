import pytest
from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession


@pytest.fixture(autouse=True, scope="session")
def spark():

    builder = (
        SparkSession.builder.master("local[1]")
        .appName("databricks-dev-container-pytest")
        .config("spark.databricks.delta.snapshotPartitions", 2)
        .config("spark.default.parallelism", 1)
        .config(
            "spark.driver.extraJavaOptions",
            "-Ddelta.log.cacheSize=3 -XX:+CMSClassUnloadingEnabled -XX:+UseCompressedOops",
        )
        .config("spark.driver.memory", "2g")
        .config("spark.dynamicAllocation.enabled", False)
        .config("spark.executor.cores", 1)
        .config("spark.executor.instances", 1)
        .config("spark.io.compression.codec", "lz4")
        .config("spark.rdd.compress", False)
        .config("spark.shuffle.compress", False)
        .config("spark.sql.catalogImplementation", "hive")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.ui.retainedExecutions", 1)
        .config("spark.sql.shuffle.partitions", 1)
        .config("spark.sql.sources.parallelPartitionDiscovery.parallelism", 1)
        .config("spark.ui.dagGraph.retainedRootRDDs", 1)
        .config("spark.ui.enabled", False)
        .config("spark.ui.retainedJobs", 1)
        .config("spark.ui.retainedStages", 1)
        .config("spark.ui.retainedTasks", 1)
        .config("spark.ui.showConsoleProgress", False)
        .config("spark.worker.ui.retainedExecutors", 1)
        .config("spark.worker.ui.retainedDrivers", 1)
    )

    spark_session = configure_spark_with_delta_pip(builder).getOrCreate()

    logger = spark_session.sparkContext._jvm.org.apache.log4j
    logger.LogManager.getLogger("org").setLevel(logger.Level.OFF)
    logger.LogManager.getLogger("akka").setLevel(logger.Level.OFF)

    yield spark_session
    spark_session.stop()
