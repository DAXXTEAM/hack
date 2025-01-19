from env import MONGO_URL
from logger import LOGGER
from Hack.database.mongo import Mongo

DB = None
if MONGO_URL:
    LOGGER(__name__).info('Database Initialised')
    DB = Mongo(MONGO_URL)
