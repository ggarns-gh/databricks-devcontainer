import sys
import importlib_metadata


def test_python_version_is_310():
    assert (
        sys.version_info.major == 3
        and sys.version_info.minor == 10
        and sys.version_info.micro >= 12
    )


def test_delta_version_is_310():
    assert importlib_metadata.version("delta_spark") == "3.1.0"
