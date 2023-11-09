import logging

import pytest

from logger.adapters.cli_logger import ColorfulCLILogger

_PATH_TO_COLORFUL_CLI_LOGGER = "logger.adapters.cli_logger.ColorfulCLILogger._log"

_KWARGS = {"foo": "bar"}


@pytest.mark.parametrize(
    "method,level,msg,kwargs",
    [
        ("debug", logging.DEBUG, "test debug message", _KWARGS),
        ("info", logging.INFO, "test info message", _KWARGS),
        ("warning", logging.WARNING, "test warning message", _KWARGS),
        ("error", logging.ERROR, "test error message", _KWARGS),
    ],
)
def test_cli_logger_methods(mocker, method, level, msg, kwargs):
    mock_log = mocker.patch(_PATH_TO_COLORFUL_CLI_LOGGER)

    logger = ColorfulCLILogger()

    log_method = getattr(logger, method)

    log_method(msg, **kwargs)

    mock_log.assert_called_once_with(level, msg, **kwargs)


def test_cli_logger_fatal_exits(mocker):
    mock_log = mocker.patch(_PATH_TO_COLORFUL_CLI_LOGGER)
    logger = ColorfulCLILogger()

    msg = "test fatal"

    with pytest.raises(SystemExit) as e:
        logger.fatal(msg, **_KWARGS)

    mock_log.assert_called_once_with(logging.CRITICAL, msg, **_KWARGS)

    assert e.type == SystemExit
    assert e.value.code == msg
