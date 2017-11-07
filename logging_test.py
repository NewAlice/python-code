import logging
logging.basicConfig(level=logging.INFO, filename='mylog.log')
logging.info('Starting program')
logging.info('Trying to divid 1 by 0')
print 1/0
logging.info('The division succeeded')
logging.info('Ending program')