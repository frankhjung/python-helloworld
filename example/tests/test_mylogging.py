import logging
import json
from unittest.mock import patch, mock_open

from example.mylogging import setup_logging


def test_setup_logging_default():
    """Test logging setup with default configuration."""
    logger = setup_logging("DEBUG")
    assert logger.level == logging.DEBUG
    assert logger.propagate is False


def test_setup_logging_from_json():
    """Test logging setup from JSON configuration file."""
    mock_config = {
        "version": 1,
        "formatters": {
            "standard": {
                "format": "%(asctime)s %(levelname)s %(message)s",
                "datefmt": "%Y-%m-%dT%H:%M:%SZ",
            }
        },
        "handlers": {
            "console": {"class": "logging.StreamHandler", "formatter": "standard"}
        },
        "loggers": {"": {"handlers": ["console"], "propagate": "False"}},
    }
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_config))):
        logger = setup_logging(logging.getLevelName(logging.WARNING))
        assert logger.level == logging.WARNING
        assert logger.propagate is False


def test_setup_logging_json_not_found():
    """Test logging setup when JSON file is not found."""
    with (
        patch("builtins.open", side_effect=FileNotFoundError),
        patch("logging.warning") as mock_warning,
    ):
        logger = setup_logging(logging.getLevelName(logging.INFO))
        assert logger.level == logging.INFO
        assert logger.propagate is False
        assert logger.hasHandlers()  # Check if default handler was added
        mock_warning.assert_called_once()


def test_setup_logging_invalid_json():
    """Test logging setup with invalid JSON file."""
    with (
        patch("builtins.open", mock_open(read_data="invalid json")),
        patch("logging.warning") as mock_warning,
    ):
        logger = setup_logging(logging.getLevelName(logging.DEBUG))
        assert logger.level == logging.DEBUG
        assert logger.propagate is False
        assert logger.hasHandlers()  # Check if default handler was added
        mock_warning.assert_called_once()
