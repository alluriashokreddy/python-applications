from core_lib.logger import other
import logging
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger.info('Main function')
    other.doSomething()