import logging
from redis import Redis, StrictRedis
from models import Post
from exceptions import ResourceNotFound,ResourceAlreadyExists,OperationFailed
from config import KvConfigs

from dal.ikv_repository import IKVRepository


class RedisRepositoryImpl(IKVRepository):
    def __init__(self, host: str = KvConfigs().host, port=KvConfigs().port, db=0):
        self.client = Redis(host=host, port=port)
        logging.getLogger("dal").info(f"redis kv configured on {host}:{port}")
    def create_post(self, post: Post):
        if post.ttl:
            result = self.client.set(post.key, post.value, ex=post.ttl)
        else:
            result = self.client.set(post.key, post.value)
        if not result:
            raise OperationFailed(f"unable to create the post")
        return result

    def get_post(self, key: str):
        value = self.client.get(key)
        if value is None:
            raise ResourceNotFound(f"Key '{key}' deosn't exists!")
        return value

    def update_post(self, post: Post):
        result = self.client.set(post.key, post.value)
        if not result:
            raise OperationFailed(f"unable to update the post")
        return result

    def delete_post(self, key):
        deleted = self.client.getdel(key)
        if deleted is None:
            raise ResourceNotFound(f"Key '{key}' doesn't exists to delete.")
        return deleted

    def add_post_if_not_exists(self, post: Post):
        result = self.client.setnx(post.key, post.value)
        if result is None or result == False:
            raise ResourceAlreadyExists(f"post with {post.key} already exists")
        return result

    def get_post_expiration(self, key):
        ttl_in_milliseconds = self.client.ttl(key)
        if ttl_in_milliseconds == -1:
            raise ResourceNotFound(f"Key '{key}' has no expiration.")
        elif ttl_in_milliseconds == -2:
            raise ResourceNotFound(f"Key '{key}' deosn't exists!")
        else:
            return ttl_in_milliseconds / 1000