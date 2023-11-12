import pytest

from hexalog.adapters.logger_for_tests import LoggerForTests

_KWARGS = {"foo": "bar"}


@pytest.mark.parametrize(
    "method,level,msg,kwargs",
    [
        ("debug", "DEBUG", "test debug message", _KWARGS),
        ("info", "INFO", "test info message", _KWARGS),
        ("warning", "WARNING", "test warning message", _KWARGS),
        ("error", "ERROR", "test error message", _KWARGS),
    ],
)
def test_logger_methods(method, level, msg, kwargs):
    logger = LoggerForTests()

    log_method = getattr(logger, method)
    log_method(msg, **kwargs)

    assert logger.contains_log(level=level, message=msg)


def test_fatal_raises_exception():
    logger = LoggerForTests()
    with pytest.raises(Exception) as exc_info:
        logger.fatal("Fatal error occurred")

    assert str(exc_info.value) == "Fatal error occurred"
