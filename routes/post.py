from fastapi import APIRouter

from service.post_service import PostService
from dto.request import CrudCreate, CrudUpdate
from models.post import Post
from exceptions import ApiException, ResourceNotFound


# import interaces and their impls for task queue
from dal.itask_queue import ITaskQueue
from dal.task_queue import TaskQueue

# import interaces and their impls for redis kv
from dal.ikv_repository import IKVRepository
from dal.redis_repositoryimpl import RedisRepositoryImpl



# perform di.
dal: IKVRepository = RedisRepositoryImpl()
task_queue: ITaskQueue = TaskQueue()
post_service = PostService(dal=dal, task_queue=task_queue)


router = APIRouter()


@router.post("/api/v1/post")
async def create_post(data: CrudCreate):
    try:
        post = Post(data.key, data.value, data.ttl)
        response = post_service.create_post(post)
        return response
    except Exception as err:
        raise ApiException(error_code=500, message="Server side error")


@router.get("/api/v1/post/{key}")
async def get_post(key: str):
    try:
        response = post_service.get_post(key)
        return response
    except ResourceNotFound as err:
        raise err
    except Exception as err:
        raise ApiException(error_code=500, message="Server side error")


@router.put("/api/v1/post")
async def update_post(data: CrudUpdate):
    try:
        post = Post(data.key, data.value, data.ttl)
        response = post_service.update_post(post)
        return response
    except Exception as err:
        raise ApiException(error_code=500, message="Server side error")


@router.delete("/api/v1/post/{key}")
async def delete_post(key: str):
    try:
        response = post_service.delete_post(key)
        return response
    except Exception as err:
        raise ApiException(error_code=500, message="Server side error")


@router.post("/api/v1/post-if-not-exists/")
async def add_post_if_not_exists(data: CrudCreate):
    try:
        post = Post(data.key, data.value, data.ttl)
        response = post_service.add_post_if_not_exists(post)
        return response
    except Exception as err:
        raise ApiException(error_code=500, message="Server side error")
