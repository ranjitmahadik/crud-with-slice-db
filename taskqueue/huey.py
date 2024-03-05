import logging
from huey import RedisHuey
from config.huey_configs import HueyConfigs


huey = RedisHuey("post", host=HueyConfigs().host, port=HueyConfigs().port, blocking=False)

logger = logging.getLogger("huey")
logger.info(f"configured with {HueyConfigs().host}:{HueyConfigs().port}")

logger.info(f"{HueyConfigs()}")