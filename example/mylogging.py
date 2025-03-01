"""
Setup logging configuration from JSON file.
"""

import json
import logging
from logging.config import dictConfig


def setup_logging(log_level: str) -> logging.Logger:
    """Configure logging with the specified level.

    Args:
        log_level: String representation of logging level (e.g., "INFO", "DEBUG")

    Returns:
        Configured logger instance
    """
    # Load config from JSON file
    try:
        with open("logging_config.json", "r", encoding="UTF-8") as f:
            config = json.load(f)
        # do not use level in config file, get from command line
        config["handlers"]["console"]["level"] = log_level
        dictConfig(config)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        # Fallback to default config if file not found or invalid
        logging.basicConfig(
            format="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%dT%H:%M:%SZ",
        )
        logging.warning("Failed to load logging config from file {e}", e)
    # set logger to not propagate to root logger and set default level
    logger = logging.getLogger()
    logger.propagate = False
    logger.setLevel(getattr(logging, log_level))
    return logger
