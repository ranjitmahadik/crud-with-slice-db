from app import app
from fastapi.responses import JSONResponse
from exceptions import ApiException, ResourceNotFound, OperationFailed


@app.exception_handler(ApiException)
async def internal_server_error_handler(_, exc: ApiException):
    return JSONResponse(status_code=exc.error_code, content={"message": str(exc)})


@app.exception_handler(ResourceNotFound)
async def internal_server_error_handler(_, exc: ResourceNotFound):
    return JSONResponse(status_code=404, content={"message": str(exc)})


@app.exception_handler(OperationFailed)
async def internal_server_error_handler(_, exc: OperationFailed):
    return JSONResponse(status_code=500, content={"message": str(exc)})
