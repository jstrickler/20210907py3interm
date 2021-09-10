#!/usr/bin/env python

import logging

logging.basicConfig(
    format='%(levelname)s\t%(asctime)s\ts%(name)s\t%(message)s\t%(filename)s', # <1>
    filename='../TEMP/formatted.log',
    level=logging.INFO,
)

logging.info("this is information")
logging.warning("this is a warning")
logging.info("this is information")
logging.critical("this is critical")
