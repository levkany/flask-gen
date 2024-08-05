import logging
import sys
from . config import LOG_LEVEL


logger = logging.getLogger('flask_gen')
logger.setLevel(LOG_LEVEL)
handler = logging.StreamHandler(sys.stderr)
handler.setLevel(LOG_LEVEL)
logger.addHandler(handler)
