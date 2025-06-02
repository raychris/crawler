'''Set up logging'''

import datetime
import logging
import logging.config
import os.path

from crawler.crawler_logging.logging_config import logging_config

def enableLogging():
    '''Return a log object after setting up a logger'''
    nowUtc = datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%S')
    if 'LOGDIR' in os.environ.keys():
        logDir = os.environ['LOGDIR']
    else:
        logDir = os.environ['HOME']
    logging_config['handlers']['file']['filename'] = os.path.join(logDir,''.join(['crawler','_',nowUtc,'.log']))
    logging.config.dictConfig(logging_config)
    log = logging.getLogger()
    return log