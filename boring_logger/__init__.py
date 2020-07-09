import logging
import os

DEBUG = "true" in os.getenv("DEBUG", "false").lower()


def get_logger(name, debug=DEBUG):
    """
    Returns logger object.

    arguments:
        name (str): logger name
        debug (bool): if True logging level is set to DEBUG
                            otherwise level INFO is used
    returns:
        logger
    """
    logger = logging.getLogger(name)

    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    if not logger.hasHandlers():
        sh = logging.StreamHandler()
        sh.setFormatter(
            logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        )
        logger.addHandler(sh)

    return logger
