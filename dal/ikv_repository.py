from abc import ABC, abstractmethod
from models import Post


class IKVRepository(ABC):

    @abstractmethod
    def create_post(self, post: Post):
        pass

    @abstractmethod
    def get_post(self, key: str):
        pass

    @abstractmethod
    def update_post(self, post: Post):
        pass

    @abstractmethod
    def delete_post(self, key):
        pass

    @abstractmethod
    def add_post_if_not_exists(self, post: Post):
        pass

    @abstractmethod
    def get_post_expiration(self, key):
        pass
