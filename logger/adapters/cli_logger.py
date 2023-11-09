import logging
import sys

from logger.ports import Logger


class ColorfulCLIHandler(logging.StreamHandler):
    """Custom logging handler that adds colors for CLI"""

    COLORS = {
        "DEBUG": "\033[36m",  # Cyan
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "FATAL": "\033[41m",  # Background Red
        "ENDC": "\033[0m",  # Reset
    }

    def format(self, record):
        colored_record = super().format(record)
        return f"{self.COLORS.get(record.levelname, self.COLORS['ENDC'])}{colored_record}{self.COLORS['ENDC']}"


class ColorfulCLILogger(Logger):
    def __init__(self, log_level: int = logging.DEBUG):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        handler = ColorfulCLIHandler()
        handler.setFormatter(formatter)

        self.logger.handlers.clear()
        self.logger.addHandler(handler)

    def _log(self, level, msg, **kwargs):
        extra_info = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
        formatted_msg = f"{msg} - {extra_info}"
        self.logger.log(level, formatted_msg)

    def debug(self, msg: str, **kwargs):
        self._log(logging.DEBUG, msg, **kwargs)

    def info(self, msg: str, **kwargs):
        self._log(logging.INFO, msg, **kwargs)

    def warning(self, msg: str, **kwargs):
        self._log(logging.WARNING, msg, **kwargs)

    def error(self, msg: str, **kwargs):
        self._log(logging.ERROR, msg, **kwargs)

    def fatal(self, msg: str, **kwargs):
        self._log(logging.CRITICAL, msg, **kwargs)
        sys.exit(msg)
