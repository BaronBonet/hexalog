import sys

from logger.ports import Logger


class DummyLogger(Logger):
    """
    Useful for testing
    """

    def debug(self, msg: str, **kwargs):
        pass

    def info(self, msg: str, **kwargs):
        pass

    def warning(self, msg: str, **kwargs):
        pass

    def error(self, msg: str, **kwargs):
        pass

    def fatal(self, msg: str, **kwargs):
        pass
        sys.exit(msg)
