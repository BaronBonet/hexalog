from abc import ABC, abstractmethod


class Logger(ABC):
    """Driven port defining the interface for logging"""

    @abstractmethod
    def debug(self, message: str, **kwargs):
        pass

    @abstractmethod
    def info(self, message: str, **kwargs):
        pass

    @abstractmethod
    def warning(self, message: str, **kwargs):
        pass

    @abstractmethod
    def error(self, message: str, **kwargs):
        pass

    @abstractmethod
    def fatal(self, message: str, **kwargs):
        pass
