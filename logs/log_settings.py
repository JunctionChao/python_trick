#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging


basedir = os.path.abspath(os.path.dirname(__file__))

def configure_logging():
    ''' format default:
    %(asctime)s - %(name)s - %(levelname)s - %(message)s
    '''
    _format = '[%(asctime)s] %(message)s'
    level = logging.WARNING
    logfile = os.path.join(basedir, 'logs', 'debug')

    logging_settings = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': logging._levelToName[level],
                'formatter': 'file',
                'stream': 'ext://sys.stdout',
            },
            'file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': 'DEBUG',
                'formatter': 'file',
                'filename': logfile,
                'mode': 'a',
                'maxBytes': 10485760, # 10M
                'backupCount': 5,
            },
        },
        'formatters': {
            'file': {
                'format': _format
            }
        },
        'loggers': {
            'sampleLogger': {
                'level': 'DEBUG',
                'handlers': ['console', 'file'],
                "propagate": "no"
            }
        }
    }

    # Set default logging settings.
    logging.config.dictConfig(logging_settings)

    # Redirect warnings to log so can be debugged.
    logging.captureWarnings(True)

# logging._nameToLevel
# logging._levelToName
configure_logging()



"""
在其余模块中使用
logger = logging.getLogger(__name__)
"""