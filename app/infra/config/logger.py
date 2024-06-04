import logging

class Logger:
    def __init__(self) -> None:
      logging.basicConfig(level=logging.INFO)
      self.logger = logging.getLogger(__name__)

    def critical(self, message, **kwargs):
        self.logger.critical(message, **kwargs)

    def error(self, message, **kwargs):
        self.logger.error(message, **kwargs)

    def warn(self, message, **kwargs):
        self.logger.warn(message, **kwargs)

    def info(self, message, **kwargs):
        self.logger.info(message, **kwargs)

    def debug(self, message, **kwargs):
        self.logger.debug(message, **kwargs)