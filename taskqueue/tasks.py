from taskqueue import huey
from dal.redis_repositoryimpl import RedisRepositoryImpl
from dal.ikv_repository import IKVRepository
import logging

redis: IKVRepository = RedisRepositoryImpl()
logger = logging.getLogger("worker")


@huey.task(retries=10, retry_delay=1000)
def create_post(post):
    logger.info(f"create post called with {post}")
    return redis.create_post(post)


@huey.task(retries=10, retry_delay=1000)
def delete_post(key: str):
    logger.info(f"delete_post called with {key}")
    return redis.delete_post(key)


@huey.task(retries=10, retry_delay=1000)
def add_post_if_not_exists(post):
    logger.info("add_post_if_not_exists called with {post}")
    return redis.add_post_if_not_exists(post)
