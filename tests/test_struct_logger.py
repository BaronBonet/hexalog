import pytest

from hexalog.adapters.struct_logger import StructLogger

_PATH_TO_STRUCT_LOGGER = "hexalog.adapters.struct_logger.get_logger"

_KWARGS = {"foo": "bar"}


@pytest.mark.parametrize(
    "method,level,msg,kwargs",
    [
        ("debug", "debug", "test debug message", _KWARGS),
        ("info", "info", "test info message", _KWARGS),
        ("warning", "warning", "test warning message", _KWARGS),
        ("error", "error", "test error message", _KWARGS),
    ],
)
def test_logger_methods(mocker, method, level, msg, kwargs):
    mock_logger = mocker.patch(_PATH_TO_STRUCT_LOGGER)

    logger = StructLogger()

    log_method = getattr(logger, method)

    log_method(msg, **kwargs)

    getattr(mock_logger(), level).assert_called_once_with(msg, **kwargs)


def test_fatal_exits(mocker):
    mock_logger = mocker.patch(_PATH_TO_STRUCT_LOGGER)
    logger = StructLogger()

    msg = "test fatal"
    level = "fatal"

    log_method = getattr(logger, level)

    with pytest.raises(SystemExit) as e:
        log_method(msg, **_KWARGS)

    getattr(mock_logger(), level).assert_called_once_with(msg, **_KWARGS)

    assert e.type == SystemExit
    assert e.value.code == msg
