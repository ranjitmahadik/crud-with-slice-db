from dotenv import load_dotenv
import os
import logging

from config.huey_configs import HueyConfigs
from config.kv_config import KvConfigs
from logger.logger import set_up_logger

def load_config():
    load_dotenv()
    set_up_logger()
    
    #task queue configs
    HueyConfigs().host = os.getenv("HUEY_REDIS", "localhost")
    HueyConfigs().port = os.getenv("HUEY_REDIS_PORT", 6379)
    
    # main store configs.
    KvConfigs().host = os.getenv("KV_HOST", "localhost")
    KvConfigs().port = os.getenv("KV_PORT", 6380)
    
    logging.getLogger("configuration").info(f"All Configurations are loaded. {KvConfigs()}")
    
    
    
    