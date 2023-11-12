"""
This is an example of how to use the TestsLogger class to test logging.

During tests eject the Test logger to the service, adapters, or handlers that you want to test.
You can either ignore the logs and your tests will run as normal,
or you can use the contains_log method to check if a log was called.
"""
import pytest

from examples.service import Service
from hexalog.adapters.logger_for_tests import LoggerForTests


def test_logging():
    logger = LoggerForTests()
    service = Service(logger)

    # If you expect a fatal log to be raised during the tests be sure to wrap it in a pytest.raises
    with pytest.raises(Exception) as e:
        service.do_something()

    assert logger.contains_log(level="ERROR")
    assert logger.contains_log(message="Doing something")
    assert logger.contains_log(level="INFO", message="Doing something meaningful")
    assert str(e.value) == "Something is very wrong, exiting"
