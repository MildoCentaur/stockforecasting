import logging
import logging.config


def main():
    # Configure the logging system
    logging.config.fileConfig('logconfig.ini')
