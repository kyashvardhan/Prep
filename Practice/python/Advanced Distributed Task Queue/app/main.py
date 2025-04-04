# app/main.py

from fastapi import FastAPI, HTTPException
from app.tasks import long_running_task
from celery.result import AsyncResult

app = FastAPI(title="Advanced Distributed Task Queue")

@app.post("/tasks/")
def create_task(duration: int):
    """
    Enqueue a long running task with a specified duration.
    """
    task = long_running_task.delay(duration)
    return {"task_id": task.id}

@app.get("/tasks/{task_id}")
def get_task_status(task_id: str):
    """
    Retrieve the status and result of a task by task_id.
    """
    result = AsyncResult(task_id, app=long_running_task.app)
    if result.state == "PENDING":
        return {"task_id": task_id, "status": result.state}
    elif result.state != "FAILURE":
        return {"task_id": task_id, "status": result.state, "result": result.result}
    else:
        raise HTTPException(status_code=500, detail=str(result.info))
