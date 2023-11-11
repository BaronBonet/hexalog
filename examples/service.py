from logger.ports import Logger


class Service:
    def __init__(self, logger: Logger):
        self.logger = logger

    def do_something(self):
        self.logger.debug("Doing something", foo="bar")
        self.logger.info("Doing something meaningful", foo="bar")
        self.logger.warning("Something might be wrong", foo="bar")
        self.logger.error("Something is wrong", foo="bar")
        self.logger.fatal("Something is very wrong, exiting", foo="bar")
