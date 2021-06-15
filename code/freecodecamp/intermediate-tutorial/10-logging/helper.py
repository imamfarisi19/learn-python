import logging 
logger = logging.getLogger(__name__) 
logger.propagate = False 
logger.into('hello from helper') 

