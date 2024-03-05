import logging
import os


def set_up_logger(logging_level_str="DEBUG"):
    logging_level = getattr(
        logging, os.getenv("LOGGING_LEVEL", logging_level_str.upper())
    )

    # Configure loggers from an array
    logger_config = {
        "dal": os.getenv("LOG_DAL", "true").lower() == "true",
        "service": os.getenv("LOG_SERVICE", "true").lower() == "true",
        "worker": os.getenv("LOG_WORKER", "true").lower() == "true",
        "configuration": os.getenv("LOG_CONFIGURATION", "true").lower() == "true",
        "huey": os.getenv("LOG_HUEY", "true").lower() == "true",
    }
    for name, enabled in logger_config.items():
        if enabled:
            logger = logging.getLogger(name)
            logger.setLevel(logging_level)
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)