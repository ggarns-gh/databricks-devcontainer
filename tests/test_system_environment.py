import sys
import importlib_metadata
import platform
from pyspark.sql.session import SparkSession


def test_spark_version(spark: SparkSession):
    assert spark.version == "3.5.0"


def test_os_release():
    os_release = platform.freedesktop_os_release()
    assert os_release["ID"] == "ubuntu" and os_release["VERSION_ID"] == "22.04"


def test_java_version(spark: SparkSession):
    java_version = spark.sparkContext._gateway.jvm.scala.util.Properties.javaSpecVersion()
    assert java_version == "1.8"


def test_scala_version(spark: SparkSession):

    scala_version_parts = spark.sparkContext._gateway.jvm.scala.util.Properties.versionNumberString().split(".")
    scala_version_major = int(scala_version_parts[0]) if len(scala_version_parts) > 0 else 0
    scala_version_minor = int(scala_version_parts[1]) if len(scala_version_parts) > 1 else 0
    scala_version_micro = int(scala_version_parts[2]) if len(scala_version_parts) > 2 else 0

    assert (
        scala_version_major == 2
        and scala_version_minor == 12
        and scala_version_micro >= 15
    )


def test_python_version():
    assert (
        sys.version_info.major == 3
        and sys.version_info.minor == 10
        and sys.version_info.micro >= 12
    )


def test_delta_version():
    assert importlib_metadata.version("delta_spark") == "3.1.0"
