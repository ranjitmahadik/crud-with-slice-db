from dal.ikv_repository import IKVRepository
from dal.itask_queue import ITaskQueue
from models.post import Post
from exceptions import OperationFailed


class PostService:
    def __init__(self, dal: IKVRepository, task_queue: ITaskQueue):
        self.dal = dal
        self.task_queue = task_queue

    def create_post(self, post: Post):
        taskId = self.task_queue.create_post(post)
        if taskId:
            return {"status": "post creation enqued", "taskId": taskId}
        raise OperationFailed("post created failed, please try again")

    def get_post(self, key):
        return self.dal.get_post(key)

    def update_post(self, post: Post):
        taskId = self.task_queue.create_post(post)
        if taskId:
            return {"status": "post updation enqued", "taskId": taskId}
        raise OperationFailed("post created failed, please try again")

    def delete_post(self, key):
        taskId = self.task_queue.delete_post(key)
        if taskId:
            return {"status": "post deletion enqued", "taskId": taskId}
        raise OperationFailed("post updation failed, please try again")

    def add_post_if_not_exists(self, post: Post):
        taskId = self.task_queue.add_post_if_not_exists(post)
        if taskId:
            return {"status": "post creation enqued", "taskId": taskId}
        raise OperationFailed("post created failed, please try again")

