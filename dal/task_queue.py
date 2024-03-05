from models.post import Post
from taskqueue.tasks import create_post, delete_post, add_post_if_not_exists
from dal.itask_queue import ITaskQueue

class TaskQueue(ITaskQueue):
    def create_post(self, post: Post):
        taskID = create_post(post)
        return taskID.id if taskID is not None else None

    def delete_post(self, key: str):
        taskID = delete_post(key)
        return taskID.id if taskID is not None else None

        

    def add_post_if_not_exists(self, post: Post):
        taskID = add_post_if_not_exists(post)
        return taskID.id if taskID is not None else None
