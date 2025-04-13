import logging
import re
from logging.handlers import RotatingFileHandler

class EmojiSafeFormatter(logging.Formatter):
    def format(self, record):
        # Replace emojis and non-ASCII characters
        record.msg = re.sub(r'[^\x00-\x7F]+', '[emoji]', str(record.msg))
        return super().format(record)

def setup_logger(enable_logging=True, log_level=logging.INFO):
    logger = logging.getLogger("project_risk_manager")
    logger.setLevel(log_level)

    if logger.hasHandlers():
        logger.handlers.clear()

    if not enable_logging:
        # Disable all logging by attaching NullHandler
        logger.addHandler(logging.NullHandler())
        return logger

    # ✅ File handler
    file_handler = RotatingFileHandler(
        "logs/project_risk_manager.log",
        maxBytes=1_000_000,
        backupCount=5,
        encoding="utf-8-sig"
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(EmojiSafeFormatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    ))

    # ✅ Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    ))

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Default logger (logging enabled)
logger = setup_logger()
