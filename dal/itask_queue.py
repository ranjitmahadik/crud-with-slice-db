from abc import ABC, abstractmethod
from models import Post


class ITaskQueue(ABC):
    @abstractmethod
    def create_post(self, post: Post):
        pass

    @abstractmethod
    def delete_post(self, key: str):
        pass

    @abstractmethod
    def add_post_if_not_exists(self, post: Post):
        pass
