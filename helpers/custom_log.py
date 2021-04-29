import sys
from logging import DEBUG
import logging
import logging.handlers


class CustomLog:
    def __init__(self, format="%(asctime)s | %(levelname)s | %(message)s", level=DEBUG):
        self.format = format
        self.level = level
        self.console_formatter = logging.Formatter(self.format)
        self.console_logger = logging.StreamHandler(sys.stdout)
        self.console_logger.setFormatter(self.console_formatter)
        self.logger = logging.getLogger("my log")
        self.logger.setLevel(self.level)

    def info(self, msg, extra=None):
        self.logger.info(msg, extra=extra)

    def error(self, msg, extra=None):
        self.logger.error(msg, extra=extra)

    def debug(self, msg, extra=None):
        self.logger.debug(msg, extra=extra)

    def warning(self, msg, extra=None):
        self.logger.warning(msg, extra=extra)

    def critical(self, msg, extra=None):
        self.logger.critical(msg, extra=extra)

    @staticmethod
    def close_log():
        logging.shutdown()
