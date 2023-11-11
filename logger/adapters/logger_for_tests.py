from logger.ports import Logger


class LoggerForTests(Logger):
    def __init__(self):
        self.logs = []

    def _log(self, level, msg, **kwargs):
        self.logs.append((level, msg, kwargs))

    def debug(self, msg: str, **kwargs):
        self._log("DEBUG", msg, **kwargs)

    def info(self, msg: str, **kwargs):
        self._log("INFO", msg, **kwargs)

    def warning(self, msg: str, **kwargs):
        self._log("WARNING", msg, **kwargs)

    def error(self, msg: str, **kwargs):
        self._log("ERROR", msg, **kwargs)

    def fatal(self, msg: str, **kwargs):
        self._log("FATAL", msg, **kwargs)
        # So we don't actually exit the tests raise an exception instead
        raise Exception(msg)

    def contains_log(self, level=None, message=None):
        return any(
            log
            for log in self.logs
            if (level is None or log[0] == level)
            and (message is None or log[1] == message)
        )
