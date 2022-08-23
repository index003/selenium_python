import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)

fm = "%(asctime)s %(levelname)s [%(name)s][%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
logging.basicConfig(level=logging.INFO, filename="../log/log01.log", format=fm)

logging.debug("this is a debug ...")
logging.info("this is a info ...")
logging.warning("this is a warning ...")
logging.error("this is a error 中文...")
logging.critical("this is a critical ...")

